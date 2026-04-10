# What would the code in Figure 3.4 do if the statement x = 25 were replaced
# by x = -25?
#
# 그림 3.4의 코드에서 x = 25를 x = -25로 바꾸면 어떻게 될까요?
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

# [답]
# 무한루프에 빠진다.
# x = -25이면 high = max(1.0, -25) = 1.0, 탐색 범위는 0.0 ~ 1.0
# abs(ans**2 - (-25)) = abs(ans**2 + 25) → 항상 25 이상이므로
# while 조건이 절대 False가 되지 않아 루프가 끝나지 않는다.
# 근본적으로 -25의 제곱근은 실수에서 존재하지 않는다.
