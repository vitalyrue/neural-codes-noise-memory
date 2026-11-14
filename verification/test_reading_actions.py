"""Focused checks for attaching reader actions to built pages."""
from pathlib import Path
from tempfile import TemporaryDirectory
import importlib.util
import unittest

spec = importlib.util.spec_from_file_location('reading_actions', Path(__file__).with_name('attach_reading_actions.py'))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class ReadingActionsTest(unittest.TestCase):
    def test_nested_pages_and_repeat_are_stable(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            nested = root / 'chapters' / 'chapter.html'
            nested.parent.mkdir()
            nested.write_text('<html><body><main>Passage</main></body></html>', encoding='utf-8')
            redirect = root / 'redirect.html'
            redirect.write_text('<html><body>Redirect</body></html>', encoding='utf-8')
            self.assertEqual(module.attach_reading_actions(root), 1)
            result = nested.read_text(encoding='utf-8')
            self.assertIn('../ask-ai-assets/ask-ai.js?v=', result)
            self.assertIn('../ask-ai-assets/ask-ai.css?v=', result)
            self.assertIn('neural-codes-noise-memory', result)
            self.assertEqual(result.count(module.START), 1)
            self.assertNotIn(module.START, redirect.read_text(encoding='utf-8'))
            self.assertEqual(module.attach_reading_actions(root), 1)
            self.assertEqual(nested.read_text(encoding='utf-8'), result)
            self.assertTrue((root / 'ask-ai-assets' / 'ask-ai.js').is_file())

if __name__ == '__main__':
    unittest.main()
