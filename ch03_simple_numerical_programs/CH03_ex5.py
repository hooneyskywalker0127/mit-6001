# What is the decimal equivalent of the binary number 10011?
#
# 이진수 10011의 십진수 값은 무엇인가요?

num = '10011'
result = 0

for bit in num:
    result = result * 2 + int(bit)

print(result)
