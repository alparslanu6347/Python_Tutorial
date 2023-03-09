#dunder methods (magic methods)
# dunder = double under (__) score methods
#dunder methods:
# + object.__add__(self, other)
# - object.__sub__(self, other)
# * object.__mul__(self, other)
# / object.__truediv__(self, other)
# // object.__floordiv__(self, other)
# % object.__mod__(self, other)
# ** object.__pow__(self, other)
# << object.__lshift__(self, other)
# >> object.__rshift__(self, other)
# & object.__and__(self, other)
# ^ object.__xor__(self, other)
# | object.__or__(self, other)

# += object.__iadd__(self, other)
# -= object.__isub__(self, other)
# *= object.__imul__(self, other)
# /= object.__idiv__(self, other)
# //= object.__ifloordiv__(self, other)
# %= object.__imod__(self, other)      vb.

# print(3 + 5)
# print(int.__add__(3,5)) # aslında int toplama bu şekilde
#
# print("Ali" + "Veli")
# print(str.__add__("Ali", "Veli"))# aslında str toplama bu şekilde
#
# print([1,2,3] + [4,5,6])
# print(list.__add__([1,2,3], [4,5,6]))# aslında list toplama bu şekilde

class Mylist(list):
    def __add__(self, other):
        if len(self) != len(other):
            return "Bu elemanlar toplanamaz"
        else:
            result = Mylist()
            for i in range(len(self)):
                result.append(self[i] + other[i])
        return result

    def __sub__(self, other):
        if len(self) != len(other):
            return "Bu elemanlar çıkarılamaz"
        else:
            result = Mylist()
            for i in range(len(self)):
                result.append(self[i] - other[i])
        return result

    def __eq__(self, other):
        if sum(self) == sum(other):
            return True
        return False
    def __abs__(self):  # abs = mutlak değer
        result = Mylist()
        for i in self:
            if i >= 0:
                result.append(i)
            else:
                result.append(-1 * i)
        return result


liste1 = Mylist([1,2,-3])
liste2 = Mylist([-4,5,-6])

print(liste1 + liste2)
print(liste1 - liste2)
print(liste1 == liste2)
print(abs(liste1))
print(abs(liste2))


