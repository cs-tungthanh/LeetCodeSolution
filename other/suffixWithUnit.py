# Given a number, convert it to prefix style
# For example: 1000 -> 1k
import math

def suffixWithUnit(input):
    powerOf1000 = int(math.floor(math.log10(abs(input))) // 3)
    exponent = 3 * powerOf1000
    result = input * 10 ** (-exponent)
    UNITS = [' ', ' k', ' M', ' G']
    if (powerOf1000 > len(UNITS)):
        prefix = 'x10^{}'.format(powerOf1000)
    else:
        prefix = UNITS[powerOf1000]
    print('input',input,'result', '{} {}'.format(result, prefix))
    print('---')
    return result

if __name__ == '__main__':
    suffixWithUnit(123)
    suffixWithUnit(1234)
    suffixWithUnit(12345)
    suffixWithUnit(12345678)
