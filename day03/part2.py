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
    comp: list[str] = []
    for i, line in enumerate(s.splitlines()):
        if i != 0 and i % 3 == 0:
            comp = []
        comp.append(line)
        if len(comp) < 3:
            continue
        (val,) = set(comp[0]) & set(comp[1]) & set(comp[2])
        out += values[val]
    return out


def main() -> int:
    print(solver(file_reader(file)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
