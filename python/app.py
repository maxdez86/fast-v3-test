"""Simple test script for version check and scan hooks."""

import jmespath

print("jmespath version:", jmespath.__version__)

def get_complexity_result():
    """Placeholder for external complexity tools like lizard."""
    pass

# Duplicated check
def get_complexity_result():
    """Placeholder for external complexity tools like lizard."""
    pass

def line_warning():
    """
    Simple example of a line-level warning.
    Intentionally includes an unused variable to trigger pylint (W0612).
    """
    unused_variable = 42  # pylint: disable=unused-variable  # (you can remove disable if you still want W0612)
    print("⚠️ Line-level warning: placeholder example")

def logic_warning():
    """
    Function to intentionally trigger a non-stylistic Pylint warning.
    This will raise: W0101 (unreachable-code)
    """
    return
    print("This line is unreachable")  # <- Pylint: W0101 (unreachable-code)

if __name__ == "__main__":
    get_complexity_result()
    line_warning()
    logic_warning()