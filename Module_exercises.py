# 带参有返回值函数
def test01(a):
    result = a + 1
    return result


# 无参有返回值函数
def test02():
    a = 1
    result = a + 1
    return result


# 带参无返回值函数
def test03(a):
    a = 1
    result = a + 1
    return None


# 无参无返回值函数
def test04():
    a = 1
    result = a + 1
    return None


print(test01(1))
print(test02())
print(test03(1))
print(test04())
