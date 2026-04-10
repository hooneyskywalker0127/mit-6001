# 변수 x,y,z,를 테스트하여 셋 중 가장 큰 홀수 숫자를 저장하고 있는 변수를 출력하고, 
# 세 변수 모두 짝수라면 이를 알리는 메시지를 출력하는 프로그램을 작성해봅시다.

import random

x = int(random.uniform(1,10))
y = int(random.uniform(1,10))
z = int(random.uniform(1,10))
odd_list =[]


if x%2 ==0 and y%2 ==0 and z%2 ==0:
    print("x,y,z 세 숫자 모두 짝수입니다.")
else:
    if x%2 !=0:
        list.append(x)
    if y%2 !=0:    
        list.append(y)
    if z%2 !=0:
        list.append(z)
    print(f"{max(list)}가 가장 큰 홀수 숫자입니다.")