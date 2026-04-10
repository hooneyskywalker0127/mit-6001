# 사용자로부터 10개의 int형을 입력 받은 후, 그 중 가장 큰 홀수를 출력하는 프로그램을 작성해봅시다. 
# 만약 입력 값들 중에서 홀수가 없다면 그에 관련한 메시지를 출력하도록 합니다.


list = []
odd_list = []
for i in range(10):
    j = int(input(f"{i+1}번째 숫자를 입력해주세요"))
    list.append(j)
for j in list:
    if j%2 !=0:
        odd_list.append(j)
if len(odd_list) == 0:
    print("입력 값들 중 홀수가 없습니다.")
else:
    print(f"{max(odd_list)}가 가장 큰 홀수입니다.")


