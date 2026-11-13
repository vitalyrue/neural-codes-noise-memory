"""Shared style and export for the approved scientific-figure plan.

Plot positions are mathematical coordinates; schematic positions follow the
scientific objects, not generic card templates. SVG remains editable source.
"""
from pathlib import Path
import hashlib
import json
import inspect
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import yaml

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'candidate-content/visuals/candidates/20261023'
INK = '#17365D'
TEXT = '#19202C'
MUTED = '#5D6876'
TEAL = '#0F6B78'
FLOW = '#0B7F95'
ORANGE = '#C4580B'
LINE = '#9AA7B5'
PALE = '#EAF2F8'
PALE_TEAL = '#E4F2F0'
PALE_ORANGE = '#FCEEE3'
PAPER = '#FFFFFF'
WARM = '#FFFDF7'
COLORS = [INK,TEXT,MUTED,TEAL,FLOW,ORANGE,LINE,PALE,PALE_TEAL,PALE_ORANGE,PAPER,WARM,'#F1F3F6']

plt.rcParams.update({
    'font.family': 'DejaVu Sans', 'font.size': 11.5,
    'axes.labelsize': 11.5, 'axes.titlesize': 12.5,
    'axes.labelcolor': TEXT, 'text.color': TEXT,
    'xtick.color': MUTED, 'ytick.color': MUTED,
    'axes.edgecolor': LINE, 'axes.spines.top': False,
    'axes.spines.right': False, 'axes.facecolor': PAPER,
    'figure.facecolor': WARM, 'savefig.facecolor': WARM,
    'svg.fonttype': 'none', 'svg.hashsalt': 'burak-illustrations-20261023',
    'mathtext.fontset': 'dejavusans', 'lines.linewidth': 2.1,
})

def setup(ax, xlabel=None, ylabel=None):
    if xlabel: ax.set_xlabel(xlabel)
    if ylabel: ax.set_ylabel(ylabel)
    ax.grid(False)
    ax.tick_params(labelsize=10.5)
    return ax

def save(fig, asset_id, checks, details=None):
    """Export immutable versioned candidates and record only actual checks.

    A QA report is a calculated-figure check, not the generic template gate or
    independent semantic acceptance. Reviewers inspect both PNG sizes.
    """
    folder = OUT / asset_id
    folder.mkdir(parents=True, exist_ok=True)
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    canvas = fig.bbox
    clipped=[]
    visible=[]
    for artist in fig.findobj(matplotlib.text.Text):
        if not artist.get_visible() or not artist.get_text(): continue
        box=artist.get_window_extent(renderer)
        if box.width==0 or box.height==0: continue
        txt=artist.get_text()
        visible.append(txt)
        if box.x0 < canvas.x0-1 or box.y0 < canvas.y0-1 or box.x1 > canvas.x1+1 or box.y1 > canvas.y1+1:
            clipped.append(txt)
    fig.savefig(folder/'figure.svg', metadata={'Date':None}, bbox_inches=None)
    fig.savefig(folder/'figure.png', dpi=210, metadata={'Software':'Matplotlib scientific figure'})
    with Image.open(folder/'figure.png') as im:
        w,h=im.size
        im.resize((700, round(h*700/w)),Image.Resampling.LANCZOS).save(folder/'book-width.png')
    profile_path=Path('C:/Users/vital/.codex/skills/course-diagram-builder/references/house-graphic-v1.yaml')
    profile=yaml.safe_load(profile_path.read_text(encoding='utf-8'))
    allowed={v.lower() for v in profile['color'].values()}
    svg=(folder/'figure.svg').read_text(encoding='utf-8')
    used=set(re.findall(r'(?:fill|stroke):\s*(#[0-9a-fA-F]{6})',svg))
    outside=sorted(c for c in used if c.lower() not in allowed)
    checks['svg_color_tokens_in_profile']=not outside
    spec=Path(inspect.stack()[1].filename).resolve()
    issues=[{'rule':'canvas-text','label':s} for s in clipped]
    issues += [{'rule':'palette-token','color':s} for s in outside]
    issues += [{'rule':'calculated-check','check':k} for k,v in checks.items() if not v]
    data={
        'asset_id':asset_id,'route':'deterministic-scientific-vector',
        'status':'pass' if all(checks.values()) and not clipped else 'fail',
        'checks':checks,'text_outside_canvas':clipped,
        'visible_labels':visible,'insertion_width_px':700,
        'svg_sha256':hashlib.sha256((folder/'figure.svg').read_bytes()).hexdigest(),
        'png_sha256':hashlib.sha256((folder/'figure.png').read_bytes()).hexdigest(),
        'spec_sha256':hashlib.sha256(spec.read_bytes()).hexdigest(),
        'profile':profile['profile']['id'],'profile_version':profile['profile']['version'],
        'automatic_gates':'pass' if not issues else 'fail',
        'issues':issues,'warnings':[],
        'palette_token_check':{'used':sorted(used),'outside_profile':outside},
        'palette_family':'technical-editorial-blueprint',
        'palette_profile':'house-graphic-v1',
        'limits':'Computed checks and canvas bounds only; independent image/meaning/readability review required.',
        'details':details or {},
    }
    (folder/'qa.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
    plt.close(fig)
    return data
