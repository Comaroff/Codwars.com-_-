# Некоторые числа обладают забавными свойствами. Например:
#
# 89 --> 8¹ + 9² = 89 * 1
#
# 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
#
# 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
#
# Дано положительное целое число n, записанное как abcd... (a, b, c, d... будучи цифрами) и положительное целое число p
#
# мы хотим найти положительное целое число k, если оно существует, такое, что сумма цифр n, взятых в последовательных степенях p, равна k * n.
# Другими словами:
#
# Существует ли целое число k, например : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
#
# Если это так, мы вернем k, если нет -1.
#
# Примечание: n и p всегда будут даны как строго положительные целые числа.
#
# dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
# dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
# dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
# dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ +


def dig_pow(a, b):
    digit = a
    res = [int(i) for i in str(digit)]
    s = 0
    for i in range(len(res)):
        s += res[i] ** b
        b += 1
    if (s % a) == 0:
        return s / a
    else:
        return -1

print(dig_pow(46289, 3))