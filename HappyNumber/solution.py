def isHappy(self, n: int) -> bool:
    while n != 1:
        if 1 < n < 10:
            return False

    return True