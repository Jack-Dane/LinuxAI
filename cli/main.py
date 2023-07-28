import argparse
import subprocess

import requests


def main(message: str, model: str, run: bool):
    response = requests.post(
        "http://localhost:8000/query",
        json={
            "statement": message,
            "open_ai_model": model
        }
    )

    command = response.json()["command"]

    print(f"Command: {command}")
    if run:
        subprocess.run(command, shell=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "LinuxAI CLI"
    )

    parser.add_argument(
        "--message", required=True,
        help="The message that defines the query you want to run"
    )
    parser.add_argument(
        "--model", default="gpt-3.5-turbo",
        help="The OpenAI model used to query your data"
    )
    parser.add_argument(
        "--run", action=argparse.BooleanOptionalAction,
        help="Will run the returning command on your machine"
    )

    args = parser.parse_args()
    main(args.message, args.model, args.run)
