#!/usr/bin/env python3
def safe_print_integer(value):
    """Imprime value si es un entero y devuelve true; si no, devuelve false."""
    try:
        print(f"{value}"))
        return True
    except (TypeError, ValueError):
        return False
