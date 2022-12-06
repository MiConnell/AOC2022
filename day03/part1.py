from __future__ import annotations

import os
import string

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> str:
    with open(file) as f:
        return f.read()


def solver(s: str) -> int:
    values = {
        letter: i
        for i, letter in enumerate(
            string.ascii_letters,
            start=1,
        )
    }
    out = 0
    for line in s.splitlines():
        mid = len(line) // 2
        first, second = line[:mid], line[mid:]
        (priority_item,) = set(first) & set(second)
        out += values[priority_item]
    return out


def main() -> int:
    print(solver(file_reader(file)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
