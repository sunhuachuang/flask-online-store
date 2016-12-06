def check(v, regex):
    if not regex.match(v):
        raise ValueError
    return v
