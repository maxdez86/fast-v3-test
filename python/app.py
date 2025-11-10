"""Simple test script for version check and scan hooks."""

import jmespath

print("jmespath version:", jmespath.__version__)

# Duplicated check
print("jmespath version:", jmespath.__version__)

def get_complexity_result():
    """Placeholder for external complexity tools like lizard."""
    pass

def line_warning():
    """
    Simple example of a line-level warning.
    Intentionally includes an unused variable to trigger pylint (W0612).
    """
    unused_variable = 42  # <- Pylint: W0612 (unused-variable)
    print("⚠️ Line-level warning: placeholder example")

if __name__ == "__main__":
    get_complexity_result()
    line_warning()
