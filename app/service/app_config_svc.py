import json
import os

APP_CFG_FILE_NAME = "app_cfg.json"


def load_config() -> dict:
    with open(os.path.join("app", APP_CFG_FILE_NAME), "r") as cfg_file:
        return json.loads(cfg_file.read())


def save_config(cfg: dict):
    with open(os.path.join("app", APP_CFG_FILE_NAME), "w") as cfg_file:
        cfg_file.write(json.dumps(cfg))


def edit_config(cfg_key: str, cfg_new_value: str):
    cfg = load_config()
    cfg[cfg_key] = cfg_new_value
    save_config(cfg)
