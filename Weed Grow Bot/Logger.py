import logging
import os

log_file = os.path.join(os.getcwd(), "bot.log")
logging.basicConfig(
    filename=log_file,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)
