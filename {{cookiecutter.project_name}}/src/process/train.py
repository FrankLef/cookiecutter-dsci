import hydra
from hydra.core.hydra_config import HydraConfig
from omegaconf import DictConfig


@hydra.main(version_base=None, config_path="../../config/etl", config_name="db")
def show_config(cfg: DictConfig) -> None:
    """Function to process the data"""
    print(f"Process data using {cfg.acc.path}")
    print(f"tables used: {cfg.acc.tables}")


@hydra.main(version_base=None, config_path="../../config/etl", config_name="db")
def show_hydra(cfg: HydraConfig) -> None:
    cfg = HydraConfig.get()
    print(f"{cfg.job.name=}")


def main() -> None:
    show_config()
    show_hydra()


if __name__ == "__main__":
    main()
