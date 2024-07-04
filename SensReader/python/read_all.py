from pathlib import Path
from reader import main

scannet_folder = Path(f"../../../scannet-data/scans")

for i in range(106, 199):
    main(
        [
            "--filename",
            str(scannet_folder / f"scene{i:0>4}_00/scene{i:0>4}_00.sens"),
            "--output_path",
            str(scannet_folder / f"scene{i:0>4}_00/scene{i:0>4}_00.sens.out"),
        ]
    )
