

import zipfile
from glob import glob
from pathlib import Path

scene_list = glob("./scene????_??")
scene_list.sort()

for scene in scene_list:
    scene_path = Path(scene)
    print(f"{scene_path = }")
    suffix_list = [
        "instance-filt",
        "instance",
        "label-filt",
        "label",
    ]
    for suffix in suffix_list:
        zip_path = scene_path / f"{scene}_2d-{suffix}.zip"
        print(f"extracting {zip_path} to {scene_path}")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(scene_path)
