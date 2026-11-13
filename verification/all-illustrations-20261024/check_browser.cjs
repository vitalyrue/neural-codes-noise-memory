/* Scoped post-build check. Run only after the root agent has rebuilt the guide.
   Use bundled Node with NODE_PATH pointing at bundled node_modules.
   Only three context screenshots are written; no PDF navigation or full-book audit.
*/
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const args = process.argv.slice(2);
const argValue = (key, fallback) => {
  const index = args.indexOf(key);
  return index < 0 ? fallback : args[index + 1];
};
const baseUrl = argValue('--base-url', 'http://127.0.0.1:8765/guide/site/').replace(/\/?$/, '/');
const rootStart = '2026-10-24T18:31:14.999410+03:00';
const expectedCounts = {
  'ch:FOUNDATIONS': 4,
  'ch:MEMORY-INFORMATION': 4,
  'ch:EYE-DRIFT': 4,
  'ch:PLACE-FIELDS': 5,
  'ch:SYNTHESIS': 1,
};
const screenshotTargets = {
  'A01:878': 'context-foundations-A01-878.png',
  'A05:390': 'context-eye-A05-390.png',
  'A07:878': 'context-place-A07-878.png',
};
const rows = JSON.parse(fs.readFileSync(path.join(__dirname, 'integration.json'), 'utf8'));
if (rows.length !== 9 || new Set(rows.map(r => r.id)).size !== 9) {
  throw new Error('Expected nine distinct figure rows in the current integration packet.');
}
const groups = [...new Set(rows.map(r => r.chapter))].map(chapter => rows.filter(r => r.chapter === chapter));
if (groups.length !== 5) throw new Error('Expected exactly five changed chapters.');
const expectedFor = row => {
  // Do not guess page names from prose titles. Chapter IDs are fixed in the packet.
  const key = row.chapter_id || row.review_contract?.source_scope_id;
  const filename = (key || '').replace(':', '-').toLowerCase() + '.html';
  const count = expectedCounts[key];
  if (count === undefined) throw new Error(`Unknown chapter ID: ${key}`);
  return { key, filename, count };
};

(async () => {
  const startedAt = new Date().toISOString();
  const browser = await chromium.launch({ channel: 'msedge', headless: true });
  const page = await browser.newPage();
  const records = [], pageRecords = [], screenshots = [], runtimeErrors = [];
  page.on('pageerror', error => runtimeErrors.push({ url: page.url(), message: error.message }));
  try {
    for (const width of [878, 390]) {
      await page.setViewportSize({ width, height: 816 });
      for (const group of groups) {
        const expected = expectedFor(group[0]);
        const url = new URL('chapters/' + expected.filename, baseUrl).href;
        await page.goto(url + '?allFigures=20261024', { waitUntil: 'networkidle' });
        await page.evaluate(async () => {
          if (window.MathJax?.startup?.promise) await window.MathJax.startup.promise;
          if (document.fonts?.ready) await document.fonts.ready;
          await Promise.all([...document.querySelectorAll('main figure img')].map(img =>
            img.complete ? Promise.resolve() : new Promise(resolve => {
              img.addEventListener('load', resolve, { once: true });
              img.addEventListener('error', resolve, { once: true });
            })));
        });
        const chapterResult = await page.evaluate(() => {
          const main = document.querySelector('main');
          return {
            viewportWidth: innerWidth,
            pageWidth: Math.max(document.documentElement.scrollWidth, document.body.scrollWidth),
            mainFigures: document.querySelectorAll('main figure img').length,
            mathErrors: document.querySelectorAll('main mjx-merror, main .MathJax_Error').length,
            mathSpans: document.querySelectorAll('main .math').length,
            mathContainers: document.querySelectorAll('main mjx-container').length,
            unresolvedBlock: !!main?.textContent.includes('{{block:'),
            literalMarkdownImage: !!main?.textContent.includes('!['),
          };
        });
        chapterResult.chapter = group[0].chapter;
        chapterResult.chapterId = expected.key;
        chapterResult.width = width;
        chapterResult.expectedFigures = expected.count;
        chapterResult.status = chapterResult.pageWidth <= width + 1 &&
          chapterResult.mainFigures === expected.count && chapterResult.mathErrors === 0 &&
          (!chapterResult.mathSpans || chapterResult.mathContainers > 0) &&
          !chapterResult.unresolvedBlock && !chapterResult.literalMarkdownImage ? 'pass' : 'fail';
        pageRecords.push(chapterResult);

        for (const row of group) {
          const stem = path.basename(row.asset, path.extname(row.asset));
          const result = await page.evaluate(({ stem, expectedAlt }) => {
            const hits = [...document.querySelectorAll('main figure img')].filter(img => {
              const file = decodeURIComponent(new URL(img.src).pathname).split('/').pop();
              return file === stem + '.png' || file === 'fig-' + stem + '.png';
            });
            const img = hits[0];
            const figure = img?.closest('figure');
            const scroller = figure?.querySelector(':scope > div[aria-describedby]');
            const caption = figure?.querySelector('figcaption');
            let scrolling = null;
            if (scroller) {
              const overflow = scroller.scrollWidth > scroller.clientWidth + 1;
              const style = getComputedStyle(scroller);
              scroller.scrollLeft = 0;
              scroller.scrollLeft = 150;
              scrolling = {
                selector: 'figure > div[aria-describedby]',
                clientWidth: scroller.clientWidth,
                scrollWidth: scroller.scrollWidth,
                overflowX: style.overflowX,
                overflow,
                moved: scroller.scrollLeft > 0,
                trialScrollLeft: scroller.scrollLeft,
              };
              scroller.scrollLeft = 0;
            }
            return {
              matchedImages: hits.length,
              loaded: !!img && img.complete && img.naturalWidth > 0,
              width: img?.getBoundingClientRect().width ?? null,
              naturalWidth: img?.naturalWidth ?? null,
              alt: img?.alt ?? null,
              altMatches: img?.alt === expectedAlt,
              caption: caption?.textContent.trim() ?? null,
              captionLinked: !!scroller && scroller.getAttribute('aria-describedby') === caption?.id,
              outerFigureScrollPresent: !!img?.closest('.figure-scroll'),
              horizontalScroll: scrolling,
            };
          }, { stem, expectedAlt: row.alt });
          result.id = row.id;
          result.visualId = row.visual_id;
          result.chapter = row.chapter;
          result.viewportWidth = width;
          const scroll = result.horizontalScroll;
          result.status = result.matchedImages === 1 && result.loaded &&
            Math.abs(result.width - 700) < 2 && result.altMatches && !!result.caption &&
            result.captionLinked && result.outerFigureScrollPresent && !!scroll &&
            (!scroll.overflow || (scroll.moved && ['auto', 'scroll'].includes(scroll.overflowX))) &&
            (width !== 390 || (scroll.overflow && scroll.moved)) &&
            chapterResult.status === 'pass' ? 'pass' : 'fail';
          records.push(result);

          const screenshotFile = screenshotTargets[row.id + ':' + width];
          if (screenshotFile) {
            const img = page.locator(`main figure img[src$="${stem}.png"]`);
            await img.scrollIntoViewIfNeeded();
            await img.evaluate(el => {
              const inner = el.closest('figure')?.querySelector(':scope > div[aria-describedby]');
              if (inner) inner.scrollLeft = 0;
            });
            await page.evaluate(() => window.scrollBy(0, -70));
            await page.screenshot({ path: path.join(__dirname, screenshotFile), fullPage: false });
            screenshots.push({ id: row.id, width, file: screenshotFile, scrollLeft: 0 });
          }
        }
      }
    }
    const data = {
      startedAt, finishedAt: new Date().toISOString(), rootStart,
      rootWallElapsedSeconds: (Date.now() - Date.parse(rootStart)) / 1000,
      awakeExecutionTime: 'unverified', baseUrl, records, pageRecords, screenshots, runtimeErrors,
      status: records.length === 18 && pageRecords.length === 10 && screenshots.length === 3 &&
        [...records, ...pageRecords].every(r => r.status === 'pass') && !runtimeErrors.length ? 'pass' : 'fail',
      scope: 'Nine inserted figures at 878 and 390 px; five changed chapters; three context screenshots. No semantic acceptance or full-book audit.',
      screenshotReview: 'pending separate pixel inspection',
    };
    fs.writeFileSync(path.join(__dirname, 'browser-check.json'), JSON.stringify(data, null, 2));
    console.log(JSON.stringify({ status: data.status, figureChecks: records.length, pages: pageRecords.length,
      screenshots: screenshots.map(s => s.file), failures: records.filter(r => r.status !== 'pass').map(r => [r.id, r.viewportWidth]),
      pageFailures: pageRecords.filter(r => r.status !== 'pass'), runtimeErrors }, null, 2));
    if (data.status !== 'pass') process.exitCode = 1;
  } finally { await browser.close(); }
})().catch(error => { console.error(error); process.exit(1); });
