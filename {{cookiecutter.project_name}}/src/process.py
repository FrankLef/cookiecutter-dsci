import hydra
from omegaconf import DictConfig
import process.etl as etl


@hydra.main(version_base=None, config_path="../config/etl", config_name="db")
def proc_etl(cfg: DictConfig) -> dict:
    data = etl.main(cfg)
    return data
