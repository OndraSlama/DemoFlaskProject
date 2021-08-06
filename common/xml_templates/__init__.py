import json
from pathlib import Path


for file in Path(__file__).parent.glob("*.tmpl"):
    with file.open() as f:
        data = json.load(f)
        globals()[file.stem] = data
