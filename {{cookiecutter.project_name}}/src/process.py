import process.etl as etl
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.absolute()))
from config import settings  # noqa


cfg = settings.msaccess
print(cfg.path)


# out = etl.build_engine(cfg.path)
# print(type(out))
