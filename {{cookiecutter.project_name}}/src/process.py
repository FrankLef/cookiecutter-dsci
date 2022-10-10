import process.etl as etl
from pathlib import Path
import sys

sys.path.append(str(Path.cwd()))

import config.etl.db as cfg  # noqa


out = etl.build_engine(cfg.PATH)
print(type(out))
