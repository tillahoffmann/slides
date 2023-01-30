import argparse
import os
from pathlib import Path
from typing import Optional, List
from . import app


def __main__(args: Optional[List] = None) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", "-p", type=int, default=5000, help="port of the web server")
    parser.add_argument("--no-debug", "-n", action="store_true", help="disable debug mode")
    parser.add_argument("--demo", action="store_true", help="launch the demo slides")
    args = parser.parse_args(args)

    # Change to the demo directory.
    if args.demo:
        demo_path = Path(__file__).parent / "demo"
        os.chdir(demo_path)
        print(f"open http://127.0.0.1:{args.port}/?document=README.md to view the demo slides")
    app.run(debug=not args.no_debug, port=args.port)


if __name__ == "__main__":
    __main__()
