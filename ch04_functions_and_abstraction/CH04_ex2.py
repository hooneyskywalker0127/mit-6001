# Finger exercise (4.3.1)
# When the implementation of fib in Figure 4.7 is used to compute fib(5),
# how many times does it compute the value fib(2)?
#
# 아래 Figure 4.7의 fib 구현으로 fib(5)를 계산할 때,
# fib(2)는 몇 번 계산될까요?
#
# [Figure 4.7]
# def fib(n):
#     """Assumes n an int >= 0
#        Returns Fibonacci of n"""
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
# def testFib(n):
#     for i in range(n+1):
#         print 'fib of', i, '=', fib(i)

