import re


def checkLen(data):
    return len(data)


def checkUpper(data):
    upper = re.compile('[A-Z]+')
    match = upper.findall(data)
    if match:
        return True
    else:
        return False


def checkLower(data):
    lower = re.compile('[a-z]+')
    match = lower.findall(data)
    if match:
        return True
    else:
        return False


def checkNum(data):
    num = re.compile('[0-9]+')
    match = num.findall(data)
    if match:
        return True
    else:
        return False


def checkSymbol(data):
    symbol = re.compile('([^a-zA-Z0-9])+')
    match = symbol.findall(data)
    if match:
        return True
    else:
        return False


def check_password_safety(passwd):
    if not checkLen(passwd) >= 8:
        return False
    elif not checkLower(passwd):
        return False
    elif not checkUpper(passwd):
        return False

    return True
