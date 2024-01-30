import logging
logging.basicConfig(level=logging.INFO)

handler = logging.StreamHandler()
formatter = logging.Formatter('\t%(levelname)s\t%(pathname)s\t%(message)s')
handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(handler)