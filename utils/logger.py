import logging

_FMT = "%(asctime)s [%(levelname)s] %(message)s"


def configure_logging() -> None:
    logging.basicConfig(level=logging.INFO, format=_FMT)


configure_logging()
// update 2022-03-03 17:22:32
