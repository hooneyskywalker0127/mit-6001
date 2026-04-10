# Let s be a string that contains a sequence of decimal numbers separated by
# commas, e.g., s = '1.23,2.4,3.123'. Write a program that prints the sum of
# the numbers in s.
#
# s를 소수점 숫자들이 쉼표로 구분된 문자열이라고 할 때, 예를 들어 s = '1.23,2.4,3.123'
# s에 있는 숫자들의 합을 출력하는 프로그램을 작성하세요.

s = '1.23,2.4,3.123'
total = 0
for num in s.split(','):
    total += float(num)

print(total)