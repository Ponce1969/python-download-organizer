from __future__ import annotations

import logging
import tomllib
from pathlib import Path
from typing import Final


# ==================================================
# PATHS
# ==================================================

BASE_DIR: Final[Path] = Path(__file__).parent
CONFIG_FILE: Final[Path] = BASE_DIR / "config.toml"
LOG_FILE: Final[Path] = BASE_DIR / "ordenar_descargas.log"


# ==================================================
# CONFIG
# ==================================================

class Config:
    def __init__(self, data: dict) -> None:

        general = data["general"]
        folders = data["folders"]
        others = data["others"]

        self.dry_run: bool = bool(general["dry_run"])
        self.downloads_folder: str = str(general["downloads_folder"])

        self.extension_map: dict[str, str] = {
            f".{k.lower()}": v
            for k, v in folders.items()
        }

        self.others_folder: str = str(others["folder"])


def load_config() -> Config:

    if not CONFIG_FILE.exists():
        raise FileNotFoundError(f"No existe {CONFIG_FILE}")

    with CONFIG_FILE.open("rb") as f:
        data = tomllib.load(f)

    return Config(data)


# ==================================================
# LOGGING
# ==================================================

def setup_logging() -> None:

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE, encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )


# ==================================================
# FILESYSTEM
# ==================================================

def ensure_folders(base: Path, names: set[str]) -> dict[str, Path]:

    folders: dict[str, Path] = {}

    for name in names:
        path = base / name
        path.mkdir(parents=True, exist_ok=True)

        folders[name] = path

    return folders


def generate_unique_path(path: Path) -> Path:

    if not path.exists():
        return path

    stem = path.stem
    suffix = path.suffix
    parent = path.parent

    counter = 1

    while True:

        candidate = parent / f"{stem}_{counter}{suffix}"

        if not candidate.exists():
            return candidate

        counter += 1


# ==================================================
# CORE
# ==================================================

def move_file(
    source: Path,
    target_dir: Path,
    dry_run: bool,
) -> bool:

    target = generate_unique_path(target_dir / source.name)

    if dry_run:
        logging.info("[DRY-RUN] %s → %s", source.name, target_dir.name)
        return False

    try:
        source.rename(target)

        logging.info("%s → %s", source.name, target_dir.name)
        return True

    except PermissionError:
        logging.error("Permiso denegado: %s", source)

    except FileNotFoundError:
        logging.error("No encontrado: %s", source)

    except OSError as exc:
        logging.error("Error OS: %s (%s)", source, exc)

    except Exception:
        logging.exception("Error inesperado: %s", source)

    return False


def organize(cfg: Config) -> None:

    downloads = Path.home() / cfg.downloads_folder

    if not downloads.exists():
        logging.critical("No existe: %s", downloads)
        return

    logging.info("Organizando: %s", downloads)

    folder_names = set(cfg.extension_map.values())
    folder_names.add(cfg.others_folder)

    folders = ensure_folders(downloads, folder_names)

    moved = 0
    skipped = 0

    for item in downloads.iterdir():

        if not item.is_file():
            continue

        ext = item.suffix.lower()

        folder_name = cfg.extension_map.get(ext, cfg.others_folder)

        target_dir = folders[folder_name]

        if item.parent == target_dir:
            skipped += 1
            continue

        if move_file(item, target_dir, cfg.dry_run):
            moved += 1
        else:
            skipped += 1

    logging.info(
        "Finalizado | Movidos: %s | Omitidos: %s",
        moved,
        skipped,
    )


# ==================================================
# ENTRYPOINT
# ==================================================

def main() -> None:

    setup_logging()

    try:
        config = load_config()

    except Exception as exc:
        logging.critical("Error cargando config: %s", exc)
        return

    organize(config)


if __name__ == "__main__":
    main()
