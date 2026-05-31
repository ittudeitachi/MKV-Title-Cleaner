import subprocess
import logging
from dataclasses import dataclass
from pathlib import Path


# =========================
# Configuration
# =========================

@dataclass(frozen=True)
class AppSettings:
    mkvpropedit_path: Path
    working_dir: Path = Path.cwd()
    file_extension: str = ".mkv"
    dry_run: bool = False


settings = AppSettings(
    mkvpropedit_path=Path(r"C:\Program Files\MKVToolNix\mkvpropedit.exe"),
    dry_run=False
)


# =========================
# Logging
# =========================

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

logger = logging.getLogger(__name__)


# =========================
# Validation
# =========================

def validate_settings(config: AppSettings):

    if not config.mkvpropedit_path.exists():
        raise FileNotFoundError(
            f"mkvpropedit.exe not found: {config.mkvpropedit_path}"
        )


# =========================
# File Scanner
# =========================

def find_mkv_files(config: AppSettings):
    return config.working_dir.rglob(f"*{config.file_extension}")


# =========================
# Remove MKV Title Metadata
# =========================

def remove_title(
    file_path: Path,
    tool_path: Path,
    dry_run: bool = False
) -> bool:

    command = [
        str(tool_path),
        str(file_path),
        "--delete",
        "title"
    ]

    if dry_run:
        logger.info(f"[DRY RUN] Would process:")
        logger.info(file_path)
        return True

    try:
        subprocess.run(
            command,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        logger.info(f"Removed title: {file_path}")
        return True

    except subprocess.CalledProcessError:
        logger.error(f"Failed: {file_path}")
        return False


# =========================
# Main Logic
# =========================

def run(config: AppSettings):

    validate_settings(config)

    total = 0
    success = 0
    failed = 0

    logger.info(f"Scanning directory:")
    logger.info(config.working_dir)

    for file_path in find_mkv_files(config):

        total += 1

        if remove_title(
            file_path=file_path,
            tool_path=config.mkvpropedit_path,
            dry_run=config.dry_run
        ):
            success += 1
        else:
            failed += 1

    logger.info("========== COMPLETE ==========")
    logger.info(f"Total Files: {total}")
    logger.info(f"Successful: {success}")
    logger.info(f"Failed: {failed}")


# =========================
# Entry Point
# =========================

if __name__ == "__main__":
    run(settings)