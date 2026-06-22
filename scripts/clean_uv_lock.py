import shutil
from pathlib import Path
p = Path('uv.lock')
if not p.exists():
    print('uv.lock not found')
    raise SystemExit(1)
shutil.copy2(p, p.with_suffix('.lock.bak'))
lines = p.read_text(encoding='utf-8').splitlines()
cleaned = []
for line in lines:
    if line.strip() in ('<<<<<<< HEAD', '======='):
        continue
    if line.strip().startswith('>>>>>>>'):
        continue
    cleaned.append(line)
p.write_text('\n'.join(cleaned) + '\n', encoding='utf-8')
print('Cleaned uv.lock and backed up to uv.lock.bak')
