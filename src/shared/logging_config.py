import logging
from rich.logging import RichHandler
from src.shared.config import settings

def setup_logging(name: str | None = None) -> logging.Logger:
    """
    Configures and returns a logger with RichHandler.
    """
    log_level = getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO)
    
    logging.basicConfig(
        level=log_level,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True, markup=True)]
    )
    
    logger = logging.getLogger(name if name else "klipper_sdk")
    return logger

logger = setup_logging()
