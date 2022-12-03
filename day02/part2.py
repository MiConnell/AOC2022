import os

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def solver(s: str) -> int:
    out = sorted(
        sum(int(line) for line in part.splitlines()) for part in s.split("\n\n")
    )
    return sum(out[:-3])


if __name__ == "__main__":
    print(solver(file_reader(file)))
