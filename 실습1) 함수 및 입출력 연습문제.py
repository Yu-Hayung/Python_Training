# 함수 및 입출력 연습문제

# 1) 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성
# 2) 람다와 조건부표현식을 사용하여 is_odd함수를 작성
# 3) is_odd함수를 이용하여 숫자를 입력하여 홀수와 짝수 여부 확인

num = int(input("홀,짝을 알고싶은 숫자를 입력하세요.>"))

# def is_odd(num):
#     if num % 2 ==0:
#         return "짝수입니다"
#     else:
#         return "홀수입니다"
# print(is_odd(num))

def is_odd(num):
    i = lambda num : "짝수입니다." if num %2 == 0 else "홀수입니다."
    return i(num)

print(num,is_odd(num))


# 2. 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수 작성
# - 입력으로 들어오는 수의 개수는 정해져 있지 않다.
# - 평균 값을 구할 때 len 함수를 사용

list = []

def avg(a) :
    return sum(a)  / len(a)

while True:
    ask = int(input("평균을 구하려는 수를 입력하세요.(종료:'0')>"))
    if ask == 0:
        break
    else:
        list.append(ask)
        f = avg(list)
        print("평균값 :",f)


# 3. 사용자의 입력을 파일(test   .txt)에 저장하는 프로그램을 작성해 보자.
# (프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가.)

s = '추가된 내용이다.\n'
f = open('test.txt', 'a')
f.write(s)
f.close( )


# 4. 다음 내용을 지닌 파일 test1.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장.
# (replace 함수 사용)
# Life is too short
# you need java

s = " Life is too short \n you need java "
f = open('test1.txt', 'w')                  # 파일 생성 하여 문자열을 입력한다.
f.write(s)                                  # 쓰기 함수 실행
f.close( )                                  # 파일 닫는다.

f = open('test1.txt', 'r')                  # 파일을 열어 읽기모드를 실행한다.
data = f.read()                             # 열어 놓은 파일을 읽는다.
print(data)                                 # "문자열 확인을 위한 출력"
f.close( )                                  # 파일 닫기

f = open('test1.txt', 'r')                  # r 로 오픈하여 읽기 모드
r = f.read().replace("java","python")       # 변경 사항
f.close( )                                  # 파일 닫기

f = open('test1.txt', 'w')                  # 변경 하고자 하는 값 입력을 위해 w
f.write(r)                                  # r 을 적용한다. 읽기 모드에서 수정 불가능
f.close( )                                  # 파일 닫기

f = open('test1.txt', 'r')                  # 파일을 열어 읽기를 실행한다.
data = f.read()                             # 변경 확인을 위한 읽기 실행입니다.
print(data)                                 # 변경 사항을 확인한다.
f.close( )                                  # 파일 닫기


