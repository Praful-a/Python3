# r = a % n
# r = a - (n * floor(a/n))

# -2 - (11 * (-2/11))
# -2 - (11 * 1)
# -2 - 11
# 9

import math
# a = -2 % -11

print(math.fmod(-2, 11))
# print(2 % -11)
# print(-9 // 4)
print(10 % -3)
print(math.fmod(10, -3))
print(-3 // 10)
print(-3 % 10)
