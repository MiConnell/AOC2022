import collections
import os

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def solver(s: str) -> int:
    target = 4
    check = collections.deque(maxlen=target)
    for i, letter in enumerate(s.strip(), start=1):
        check.append(letter)
        if len(set(check)) == target:
            return i
    raise NotImplementedError("Not Found")


def main() -> int:
    print(solver(file_reader(file)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
