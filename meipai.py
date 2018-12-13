# -*- coding: utf-8 -*-
import base64

a = "e1f1aHR0cDosoJMIDBBWvL212dmlkZW8xMC5tZWl0dWRhdGEuY29tLzViNTgxNWE3OWIyM2I3ODY3X0gyNjRfMV8xOTdjMTIxM2E0ZDE2NC5tcDQ/az03ZWI2Y2IyNzZjMjZlYmRkMmY0ZDY1ZWZhMzlhMDcyNCZ0PTVjMTZX0GecYxOWFl"

def getHex(a):
    hex_1 = a[:4][::-1]
    str_1 = a[4:]
    return str_1, hex_1


def getDec(a):
    b = str(int(a, 16))
    c = list(b[:2])
    d = list(b[2:])
    return c, d


def substr(a, b):
    k = int(b[0])
    c = a[:k]
    d = a[k:k+int(b[1])]
    temp = a[int(b[0]):].replace(d, "")
    result = c + temp
    return result


def getPos(a, b):
        b[0] = len(a) - int(b[0]) - int(b[1])
        return b


str1, hex1 = getHex(a)
pre, tail = getDec(hex1)
d = substr(str1, pre)
kk = substr(d, getPos(d, tail))
a = base64.b64decode(kk)
print(a)


