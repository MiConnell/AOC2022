from __future__ import annotations

import os

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> str:
    with open(file) as f:
        return f.read()


def solver(s: str) -> int:
    return max(sum(int(line) for line in part.splitlines()) for part in s.split("\n\n"))


def main() -> int:
    print(solver(file_reader(file)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
