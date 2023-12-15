"""infini 日志。

infini 使用 [loguru](https://github.com/Delgan/loguru) 来记录日志信息。
自定义 logger 请参考 [loguru](https://github.com/Delgan/loguru) 文档。
"""
from datetime import datetime
from multilogging import multilogger
from pathlib import Path
from .settings import DEBUG


__all__ = ["logger", "error_or_exception"]

logger = multilogger(
    name="HydroRoll", payload="Core", level="DEBUG" if DEBUG else "INFO"
)
current_path = Path(__file__).resolve().parent
LOG_PATH = current_path / "logs"
if not LOG_PATH.exists():
    LOG_PATH.mkdir(parents=True, exist_ok=True)
logger.add(
    sink=LOG_PATH / (datetime.now().strftime("%Y-%m-%d") + ".log"),
    level="INFO",
    rotation="10 MB",
)  # 每个日志文件最大为 10MB


def error_or_exception(message: str, exception: Exception, verbose: bool = True):
    # 弃用的方法
    # logger.remove()
    # logger.add(
    #     sys.stderr,
    #     format="<magenta>{time:YYYY-MM-DD HH:mm:ss.SSS}</magenta> <level>[{level}]</level> > <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    # )

    if verbose:
        logger.exception(exception)
        logger.critical(message)
    else:
        logger.critical(f"{message} {exception!r}")
