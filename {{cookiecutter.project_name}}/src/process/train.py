import hydra
from hydra.core.hydra_config import HydraConfig
from omegaconf import DictConfig

cfg_path = "../../config"


@hydra.main(version_base=None, config_path=cfg_path, config_name="config")
def show_config(cfg: DictConfig) -> None:
    """Function to process the data"""

    # raw_path = abspath(cfg.acc.path)
    raw_path = cfg.acc.path
    print(f"Process data using {raw_path}")
    print(f"tables used: {cfg.acc.tables}")


@hydra.main(version_base=None, config_path=cfg_path, config_name="config")
def show_hydra(cfg: HydraConfig) -> None:
    cfg = HydraConfig.get()
    print(cfg.job.name)
    print(cfg.output_subdir)


def main() -> None:
    show_config()
    show_hydra()


if __name__ == "__main__":
    main()
