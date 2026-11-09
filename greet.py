"""Print a friendly greeting."""

import sys


def greet(name: str) -> str:
    """Return a greeting for name."""
    return f"Hello, {name}!"


def main() -> int:
    """Greet the first command-line argument, or the world."""
    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(greet(name))
    return 0


def test_greet() -> None:
    assert greet("Hee") == "Hello, Hee!"


if __name__ == "__main__":
    raise SystemExit(main())
