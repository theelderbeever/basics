import dvc.api
import pandas as pd

with dvc.api.open(
    "data/data.xml", repo="https://github.com/theelderbeever/basics"
) as fd:
    print(pd.read_csv(fd))
