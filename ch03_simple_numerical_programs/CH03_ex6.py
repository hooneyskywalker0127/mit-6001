# Add some code to the implementation of Newton-Raphson that keeps track of the
# number of iterations used to find the root. Use that code as part of a program
# that compares the efficiency of Newton-Raphson and bisection search.
# (You should discover that Newton-Raphson is more efficient.)
#
# 뉴턴-랩슨 구현에 반복 횟수를 추적하는 코드를 추가하세요.
# 그 코드를 사용하여 뉴턴-랩슨과 이분 검색의 효율성을 비교하는 프로그램을 작성하세요.
# (뉴턴-랩슨이 더 효율적임을 알 수 있어야 합니다.)
#
# 참고 (그림 3.5):
# epsilon = 0.01
# k = 24.0
# guess = k/2.0
# while abs(guess*guess - k) >= epsilon:
#     guess = guess - (((guess**2) - k)/(2*guess))
# print('Square root of', k, 'is about', guess)

x = 24.0
epsilon = 0.01

# 뉴턴-랩슨
nr_guess = x / 2.0
nr_iters = 0
while abs(nr_guess**2 - x) >= epsilon:
    nr_guess = nr_guess - ((nr_guess**2 - x) / (2 * nr_guess))
    nr_iters += 1
print(f'Newton-Raphson: {nr_iters}번 반복, 결과 = {nr_guess}')

# 이분 탐색
low = 0.0
high = max(1.0, x)
bs_ans = (high + low) / 2.0
bs_iters = 0
while abs(bs_ans**2 - x) >= epsilon:
    if bs_ans**2 < x:
        low = bs_ans
    else:
        high = bs_ans
    bs_ans = (high + low) / 2.0
    bs_iters += 1
print(f'이분 탐색: {bs_iters}번 반복, 결과 = {bs_ans}')
