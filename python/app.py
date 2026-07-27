"""Simple test script for version check and scan hooks"""

# Replace jmespath with jupyter-core version check
import jupyter_core

print("jupyter-core version:", jupyter_core.__version__)

def long_repeated_function():
    """
    A long, intentionally duplicated function exceeding ~100 tokens
    to trigger PMD CPD.

    The function does nothing meaningful; it just performs many small
    operations so that token count is high enough for detection.
    """
    total = 0
    total += 1
    total += 2
    total += 3
    total += 4
    total += 5
    total += 6
    total += 7
    total += 8
    total += 9
    total += 10
    total += 11
    total += 12
    total += 13
    total += 14
    total += 15
    total += 16
    total += 17
    total += 18
    total += 19
    total += 20
    total += 21
    total += 22
    total += 23
    total += 24
    total += 25
    total += 26
    total += 27
    total += 28
    total += 29
    total += 30
    total += 31
    total += 32
    total += 33
    total += 34
    total += 35
    total += 36
    total += 37
    total += 38
    total += 39
    total += 40
    total += 41
    total += 42
    total += 43
    total += 44
    total += 45
    total += 46
    total += 47
    total += 48
    total += 49
    total += 50
    return total


def get_complexity_result() -> int:
    """Placeholder for external complexity tools like lizard."""
    a = 1 + 2
    return a


def line_warning():
    """
    Simple example of a line-level warning.
    Intentionally includes an unused variable to trigger pylint (W0612).
    """
    unused_variable = 42  # pylint: disable=unused-variable
    print("Line-level warning: placeholder example")


def logic_warning():
    """
    Function to intentionally trigger a non-stylistic Pylint warning.
    This will raise: W0101 (unreachable-code)
    """
    return
    print("This line is unreachable")  # Pylint: W0101 (unreachable-code)


if __name__ == "__main__":
    print(long_repeated_function)    
    get_complexity_result()
    line_warning()
    logic_warning()
