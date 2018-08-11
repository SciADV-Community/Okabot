from systemd.journal import JournaldLogHandler
import logging

logger = logging.getLogger(__name__)
journal_handler = JournaldLogHandler()
journal_handler.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))
logger.addHandler(journal_handler)
logger.setLevel(logging.INFO)

logging.debug("Logging enabled")