#  Preprocessing Module

import re


def preprocess_message(message: str) -> str:
    """
    Clean and normalize incoming message text.
    """

    if not message or not message.strip():
        raise ValueError("Input message is empty.")

    # Remove extra whitespace
    message = message.strip()

    # Replace multiple newlines with single newline
    message = re.sub(r'\n+', '\n', message)

    # Replace multiple spaces with single space
    message = re.sub(r'\s+', ' ', message)

    return message
