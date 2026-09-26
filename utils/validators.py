def check_name(name: str) -> bool:
    if not isinstance(name, str):
        return False

    if not (2 <= len(name) <= 50) or name.isdigit():
        return False

    return True
