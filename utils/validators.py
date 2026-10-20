def check_name(name: str) -> bool:
    if not isinstance(name, str):
        return False

    if not (2 <= len(name) <= 50) or name.isdigit():
        return False

    return True


def parse_phone(phone: str):
    confirmed_sym = "0123456789+-() "
    parsed = ""

    for dig in phone:
        if dig not in confirmed_sym:
            return None
        parsed += dig

    return parsed


def validate_phone(phone: str):
    flag = True
    if not (isinstance(phone, str) or
            phone.isdigit() or
            phone is not None or
            10 <= len(phone) <= 15):
        flag = False

    return flag
