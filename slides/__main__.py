import argparse
from typing import Optional, List
from . import app


def __main__(args: Optional[List] = None) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", "-p", type=int, default=5000, help="port of the web server")
    parser.add_argument("--no-debug", "-n", action="store_true", help="disable debug mode")
    args = parser.parse_args(args)

    app.run(debug=not args.no_debug, port=args.port)


if __name__ == "__main__":
    __main__()
