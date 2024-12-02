from pathlib import Path

from sbmlutils.factory import *
from sbmlutils.metadata import *


_m = Model(

)

if __name__ == "__main__":
    create_model(
        _m,
        output_dir=Path(__file__).parent / "results"
    )


