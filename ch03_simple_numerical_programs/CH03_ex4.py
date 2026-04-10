# What would have to be changed to make the code in Figure 3.4 work for finding
# an approximation to the cube root of both negative and positive numbers?
# (Hint: think about changing low to ensure that the answer lies within the
# region being searched.)
#
# 그림 3.4의 코드가 음수와 양수 모두의 세제곱근을 구할 수 있으려면 무엇을 바꿔야 할까요?
# (힌트: 탐색 범위 안에 답이 포함되도록 low 값을 바꾸는 것을 생각해보세요.)
#
# [Figure 3.4]
# x = 25
# epsilon = 0.01
# numGuesses = 0
# low = 0.0
# high = max(1.0, x)
# ans = (high + low)/2.0
# while abs(ans**2 - x) >= epsilon:
#     numGuesses += 1
#     if ans**2 < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low)/2.0
# print('numGuesses =', numGuesses)
# print(ans, 'is close to square root of', x)

x = -27
epsilon = 0.01
numGuesses = 0

if x < 0:
    low = min(-1.0, x)
    high = 0.0
else:
    low = 0.0
    high = max(1.0, x)

ans = (high + low) / 2.0
while abs(ans**3 - x) >= epsilon:
    numGuesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0

print('numGuesses =', numGuesses)
print(ans, 'is close to cube root of', x)
