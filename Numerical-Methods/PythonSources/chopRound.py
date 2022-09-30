import math
def Round(n, roundVal):
    return round(n, roundVal)

def Chop(n, chopVal):
    decimals = len(str(n).split('.')[1])
    if decimals <= chopVal:
        return n
    step = 10.0 ** chopVal
    return math.trunc(step * n) / step
