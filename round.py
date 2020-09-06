#精确四舍五入

from decimal import Decimal,ROUND_HALF_UP

def my_round(a):
    a = abs(a)
    a = str(a)
    a_r = Decimal(a).quantize(Decimal("0.0"), rounding = "ROUND_HALF_UP")
    return a_r

print(my_round(20.25),round(20.25,1))
