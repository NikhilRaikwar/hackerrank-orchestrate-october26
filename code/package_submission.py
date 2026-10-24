"""Build code.zip from an explicit submission whitelist, never the whole repo."""
import argparse
import hashlib
from pathlib import Path
import zipfile


def package(root, destination):
    required = ['README.md','code/main.py','code/requirements.txt','code/evaluation/main.py',
                'code/evaluation/evaluation_report.md','code/evaluation/usage_report.md']
    for name in required:
        if not (root/name).is_file():
            raise ValueError('Missing required submission file: '+name)
    files = [root/'README.md',root/'.env.example']
    files += [p for p in (root/'code').rglob('*') if p.is_file()
              and p.suffix in {'.py','.md','.txt'} and '__pycache__' not in p.parts]
    with zipfile.ZipFile(destination,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
        for path in sorted(files):
            name = path.relative_to(root).as_posix()
            info = zipfile.ZipInfo(name,date_time=(2026,1,1,0,0,0))
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info,path.read_bytes())
    with zipfile.ZipFile(destination) as archive:
        names = archive.namelist()
        assert archive.testzip() is None
        assert set(required) <= set(names)
        assert all(name in {'README.md','.env.example'} or name.startswith('code/') for name in names)
        assert not any('/__pycache__/' in name or name.endswith(('.zip','.gz','.tgz','.7z','.rar')) for name in names)
        print(f'{destination}: {len(names)} files, {destination.stat().st_size:,} bytes; no corpus, plans, transcripts, caches or nested archives')
        print('SHA-256:',hashlib.sha256(destination.read_bytes()).hexdigest())


if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=root/'code.zip')
    args = parser.parse_args()
    package(root,args.output)
