def validate_positive_number(value):
    """Reusable function to validate numeric input."""
    try:
        num = float(value)
        if num < 0:
            return False
        return True
    except ValueError:
        return False

def print_header(title):
    """Reusable UI header."""
    print("\n" + "="*30)
    print(f"{title.center(30)}")
    print("="*30)
