"""Read every tracked challenge file and summarize the participant corpus.

This is a repository inspection tool, not a deletion solver. It never produces
predictions or reads organizer-only material. Sample labels are summarized only.
"""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import json
import sqlite3
import subprocess
from pypdf import PdfReader
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'tmp' / 'inspection'
DEST.mkdir(parents=True, exist_ok=True)
tracked = subprocess.check_output(['git', 'ls-files'], cwd=ROOT, text=True).splitlines()
report = ['# Complete source-file inspection', '', 'Generated from local tracked files; sample answers are validation data only.', '']
shapes = Counter()

def shape(value, prefix='$'):
    if isinstance(value, dict):
        shapes[prefix + ': ' + ', '.join(sorted(value))] += 1
        for key, item in value.items():
            if isinstance(item, (dict, list)):
                shape(item, prefix + '.' + key)
    elif isinstance(value, list):
        for item in value:
            shape(item, prefix + '[]')

for name in tracked:
    path = ROOT / name
    raw = path.read_bytes()
    report += ['## ' + name, '', f'Bytes: {len(raw)}; SHA-256: {hashlib.sha256(raw).hexdigest()}', '']
    ext = path.suffix.lower()
    if ext == '.csv':
        with path.open(encoding='utf-8-sig', newline='') as stream:
            reader = csv.DictReader(stream)
            rows = list(reader)
            report += [f'Rows: {len(rows)}', '', 'Fields: ' + ', '.join(reader.fieldnames or []), '']
        if name.endswith('sample_output.csv'):
            counts = Counter(row['deletion_status'] for row in rows)
            ops = Counter(step['operation'] for row in rows for step in json.loads(row['steps_json']))
            report += ['Sample statuses: ' + str(dict(counts)), '', 'Sample operations: ' + str(dict(ops)), '']
        elif name.endswith('deletion_requests.csv'):
            report += ['Audit range: ' + min(row['audit_at'] for row in rows) + ' to ' + max(row['audit_at'] for row in rows), '']
        elif name.endswith('system_activity.csv'):
            for field in ('operation', 'activity_type', 'event_type', 'system_id', 'reported_result'):
                if field in rows[0]:
                    report += [field + ': ' + str(dict(Counter(row[field] for row in rows))), '']
    elif ext == '.json':
        data = json.loads(raw)
        report += ['Top-level: ' + (', '.join(data) if isinstance(data, dict) else f'array[{len(data)}]'), '']
        shape(data)
        (DEST / (path.stem + '.excerpt.txt')).write_text(json.dumps(data, ensure_ascii=False, indent=2)[:16000], encoding='utf-8')
    elif ext == '.sql':
        connection = sqlite3.connect(':memory:')
        connection.executescript(raw.decode('utf-8-sig'))
        for (table,) in connection.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"):
            quoted = '"' + table.replace('"', '""') + '"'
            columns = [row[1] for row in connection.execute('PRAGMA table_info(' + quoted + ')')]
            count = connection.execute('SELECT COUNT(*) FROM ' + quoted).fetchone()[0]
            report += [f'Table {table}: {count} rows; fields: ' + ', '.join(columns), '']
        connection.close()
    elif ext == '.pdf':
        reader = PdfReader(path)
        text = '\n\n'.join(page.extract_text() or '' for page in reader.pages)
        report += [f'Pages: {len(reader.pages)}; extracted characters: {len(text)}', '']
        (DEST / (path.stem + '.txt')).write_text(text, encoding='utf-8')
    elif ext == '.png':
        with Image.open(path) as picture:
            picture.load()
            report += [f'Image: {picture.size[0]} x {picture.size[1]}; {picture.mode}', '']
    else:
        text = raw.decode('utf-8-sig')
        lines = text.splitlines()
        report += [f'Lines: {len(lines)}', '']
        if ext == '.log':
            (DEST / (path.stem + '.excerpt.txt')).write_text('\n'.join(lines[:8] + ['...'] + lines[-3:]), encoding='utf-8')

report += ['# All observed JSON structures', '']
for key, count in sorted(shapes.items()):
    report += [f'- {count}: {key}']
(DEST / 'file_inventory.md').write_text('\n'.join(report) + '\n', encoding='utf-8', newline='\n')
print(f'Read {len(tracked)} tracked files. Inventory: {DEST / "file_inventory.md"}')
print('\n'.join(report[-min(40, len(shapes)):]))
