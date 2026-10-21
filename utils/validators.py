def check_name(name: str) -> bool:
    if not isinstance(name, str):
        return False

    if not (2 <= len(name) <= 50) or name.isdigit():
        return False

    return True


def parse_phone(phone: str):
    confirmed_sym = "0123456789+-() "
    nums = "0123456789"
    parsed = ""

    for dig in phone:
        if dig not in confirmed_sym:
            return None
        if dig in nums:
            parsed += dig

    return parsed


def validate_phone(phone: str):
    if not (phone is not None and
            isinstance(phone, str) and
            phone.isdigit() and
            10 <= len(phone) <= 15):
        return False
    return True
