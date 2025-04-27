import argparse
import logging
import os
import sys

LOG_LEVEL = os.environ.get("LOG_LEVEL", "DEBUG").upper()
logging.basicConfig(
    stream=sys.stdout,
    level=LOG_LEVEL,
    format="%(message)s",
)
logging.getLogger("gpt.completion").setLevel(LOG_LEVEL)
LOGGER = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="OpenAI GPT-3 text completion")
    parser.add_argument(
        "file",
        type=argparse.FileType("r"),
        nargs="?",
        default=sys.stdin,
        help="File to read text from",
    )
    parser.add_argument(
        "--instructions",
        "-i",
        type=str,
        help="GPT system instruction",
    )
    parser.add_argument("--message", "-m", type=str, help="Send message")
    args = parser.parse_args()

    if not args.file.isatty():
        LOGGER.debug("Reading from: %s", args.file.name)
        with args.file as f:
            data = f.read()
            LOGGER.debug("Data: %s", data)
            # print(chat.send(f.read(), echo=True))
            return
