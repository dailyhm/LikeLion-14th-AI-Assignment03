import numpy as np #numpy를 np로 축약

arr = np.zeros([7,7] , dtype= int) #7*7의 모두 0으로 채워지게 만듬

arr[::2,1::2] = 1   
arr[1::2,::2] = 1

for row in range(7): #7번 반복
    for col in range(7):
        print(arr[row,col],end = " ")
    print()