import argparse
import logging
import os
import sys

from . import openai
from .models import ChatRequest, Message, SystemMessage, UserMessage

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
        help="Instructions to be included in the prompt",
    )
    parser.add_argument(
        "--message",
        "-m",
        type=str,
        help="Message to be included in the request",
    )
    args = parser.parse_args()

    if not args.file.isatty():
        LOGGER.debug("Reading from: %s", args.file.name)
        with args.file as f:
            data = f.read()
            LOGGER.debug("Data: %s", data)
            response = openai.chat_completion(
                ChatRequest(
                    model="gpt-4",
                    messages=[
                        SystemMessage(
                            content="You are a helpful assistant.",
                        ),
                        UserMessage(
                            content=data,
                        ),
                    ],
                    temperature=0,
                )
            )
            print(response.choices[0].message.content)
            # print(chat.send(f.read(), echo=True))
            return
