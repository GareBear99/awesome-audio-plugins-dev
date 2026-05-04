#!/usr/bin/env python3
from pathlib import Path
import json, re, sys
root = Path(__file__).resolve().parents[1]
required = [
    'README.md',
    'CONTRIBUTING.md',
    'LICENSE',
    'LINK_PAGES/freevox8.md',
    'docs/START_HERE_ECOSYSTEM.md',
    'docs/SEO_START_HERE_PLAYBOOK.md',
    'data/start_here_network.json',
]
missing = [p for p in required if not (root / p).exists()]
if missing:
    print('Missing required files:', missing)
    sys.exit(1)
for jf in ['data/start_here_network.json','data/seo_keywords.json']:
    json.loads((root/jf).read_text())
readme = (root/'README.md').read_text(encoding='utf-8')
markers = [
    'Start Here — GareBear99 Audio Plugin Dev Map',
    'awesome-music-platforms',
    'awesome-python-audio-science',
    'FreeVox8',
    'TizWildinEntertainmentHUB public .io router',
]
missing_markers = [m for m in markers if m not in readme]
if missing_markers:
    print('Missing README markers:', missing_markers)
    sys.exit(1)
# local markdown links
broken=[]
for p in root.rglob('*.md'):
    text=p.read_text(encoding='utf-8', errors='ignore')
    for m in re.finditer(r'\[[^\]]+\]\(([^)]+)\)', text):
        target=m.group(1).split('#')[0]
        if not target or '://' in target or target.startswith('mailto:') or target.startswith('#'):
            continue
        target=target.replace('%20',' ')
        if not (p.parent/target).exists() and not (root/target).exists():
            broken.append(f'{p.relative_to(root)} -> {target}')
if broken:
    print('Broken local markdown links:')
    print('\n'.join(broken[:50]))
    sys.exit(1)
print('Repository validation passed.')
