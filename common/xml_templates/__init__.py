""" This module autoamtically load all .tmpl files from xml_templates folder and saves them to module variables """
import json
from pathlib import Path

for file in Path(__file__).parent.glob("*.tmpl"):
    with file.open() as f:
        data = json.load(f)
        globals()[file.stem] = data
