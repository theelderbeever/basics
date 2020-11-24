import dvc.api

with dvc.api.open(
    "data/data.xml",
    repo="https://github.com/theelderbeever/basics"
) as fd:
    print(fd)