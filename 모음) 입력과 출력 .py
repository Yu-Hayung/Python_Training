
# 사용자가 입력한 값을 어던 변수에 대입 하고 싶을 때 'intput()' 으로 받는다.
# 프롬프트를 띄워서 가용자 입력을 받을 수 있다.

number = input("숫자를 입력하세요: ")
# 숫자를 입력하세요: 3
print(number)
# 3

for i in range(10):            # 한줄의 결괏값 출력하기
    print(i, end=' ')          # end = '' 는 끝 날때 마닥 무엇을 출력하라 라는 의미
# 0 1 2 3 4 5 6 7 8 9



# 파일을 생성할 수 있다.
# open 함수   open(file,mode,encoding, newline)
# 모드는 r(읽기), w(쓰기), rb(바이너리 읽기), wb(바이너리 쓰기)
# encoding 은 문자열 인코딩 설정하며 기본값은 None 객체 이다.
# newline 옵션은 텍스트 파일의 끝에 줄 넘김의 설정을 하며 기본값은 None 이다.

f = open("새파일.txt", 'w')    # 쓰기 파일 생성
f.close()


# write : 쓰기 함수
f = open("새파일1.txt", 'w')             # 쓰기 파일을 생성한다
for i in range(1, 11):                  # 쓰는 내용을 반복문을 이용해 작성한다
    data = "%d 번째 줄입니다.\n" % i      # 쓰여지는 문구는 "i 번째 줄 입니다."
    f.write(data)                       # 명령어 써라
f.close()                               # 생성한 파일은 닫아 메모리 유실을 막는다.

# resadline : 읽기 함수
f = open("새파일1.txt", 'r')
line = f.readline()                     # 파일에 쓰인 글을 읽어라
print(line)
f.close()

f = open("새파일1.txt", 'r')
while True:                             # 반복해서 읽도록 반복문 사용
    line = f.readline()                 # line 라인별로 하나씩 읽도록 원함
    if not line: break                  # 무한반복을 멈추기 위한 break
    print(line)
f.close()

# readlines
f = open("새파일1.txt", 'r')
lines = f.readlines()                  # resadline 에 s 를 붙혔다.
for line in lines:                     # 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트를 돌려준다.
 print(line)
f.close()

# read
f = open("새파일.txt", 'r')             # read 파일의 내용 전체를 문자열로 돌려준다.
data = f.read()
print(data)
f.close()

# 'a' 파일에 새로운 내용을 추가하기
# w 모드로 파일을 열면 기존 내용이 모두 사라진다.
# 유지 하면서 새로운 값을 추가 하고 싶으면 a를 사용한다.
f = open("새파일1.txt",'a')
for i in range(11, 20):
    data = "%d 번째 줄입니다.\n" % i
    f.write(data)
f.close()

# write 메소드 - 내용을 파일에 쓰고 출력된 문자들의 개수를 반환한다.
# write(self, AnyStr) self : 인자로 설정한다. / AnyStr: 문자열을 설정한다.
s = '문자열 파일 쓰기 확인'
f = open('test.txt', 'w')
f.write(s)
f.close( )

s = ['1234', '4567', '89']        # 리스트로 작성하여 쓰기
f = open('test.txt', 'w')         # 쓰기 기능 파일 생성
f.write(''.join(s))               # join 함수
f.close( )                        # 출력 결과 : 1234456789

s = ('1234', '4567', '89')
f = open('test2.txt', 'w')
f.write(''.join(s))               # 튜플의 내용을 파일에 쓰기 위해서는 join 메소드와 같이 사용한다
f.close( )                        # 출력 결과 : 1234456789

s = {'1234':1, '567':2, '89':3}
f = open('test3.txt', 'w')
f.write(''.join(s))
f.close( )

s = '추가된 내용이다.\n'            # 내용 추가하기 \n - 줄바꿈
f = open('test2.txt', 'a')       # 파일 선택
f.write(s)
f.close( )

# writelines 메소드는 내용을 파일의 행 리스트로 쓴다.
# writelines(self, List) 메소드 / self 매개변수 : self 인자를 설정 / List[AnyStr] 매개변수 : 리스트를 설정

s = '문자열 파일 쓰기 확인'
f = open('test4.txt', 'w')
f.writelines(s)
f.close( )

s = ['1234', '4567', '89']
f = open('test5.txt', 'w')
f.writelines(s)
f.close( )

s = ['1234\n', '567\n', '89\n']       # \n 으로 줄 바꿈을 한다.
f = open('test6.txt', 'w')
f.writelines(s)
f.close( )

# split 메소드로 문자열을 리스트로 반환한다.
# split 메소드로 객체에 저장된 문자열을 공백 기준으로 문자열을 분리한다.
# split 메소드는 모든 공백을 제거하고 문자열 내의 단어 리스트를 얻을 수 있다.


s2 = ['1234\n', '567\n', '89\n']
f = open('test_split.txt', 'w')
f.writelines(s2)
f.close()

f = open("test_split.txt",'a')
for i in range(11, 20):
    data = "반복문 테스트 입니다. \n %d 번째 줄입니다.\n" % i
    f.write(data)
f.close()

s1 = 'test_split 테스트 문구 입니다. \n 문자열 파일 쓰기 확인 '
f = open("test_split.txt",'a')
f.write(s1)
f.close()


f = open('test_split.txt')
s = f.read( )
f.close( )
print('파일 내용:', s.split( ))

# readline 메소드를 이용하여 한 라인씩 문자열로 반환한다.
# readline 메소드는 현재 읽는 위치인 파일 포인터에서 개행 문자인 \n까지 읽는다.
# readline 메소드가 아무 값도 할당받지 않은 상태의 빈 객체인 빈 문자열을 반환한다.
# readline 메소드로 읽은 내용이 파일의 끝에 도달하면 빈 줄은 하나의 개행 문자인
# \n만을 포함하는 문자열로 표현된다

f = open('test5.txt', mode='r', encoding='utf-8')
s = f.read( )
f.close( )
print(s)

# split 메소드로 문자열을 리스트로 반환한다.
# split 메소드로 객체에 저장된 문자열을 공백 기준으로 문자열을 분리한다.
# split 메소드는 모든 공백을 제거하고 문자열 내의 단어 리스트를 얻을 수 있다.

f = open('test4.txt')
s = f.read( )
f.close( )
print('파일 내용:', s.split( ))     # 리스트로 반환 된다.

# 파일 반복자

f = open("새파일2.txt", 'w')             # 테스트용 : 문자열이 있는 파일
for i in range(1, 5+1):
    data = "%d 번째 학생입니다." % i
    f.write(data)
f.close()

f = open('새파일2.txt')
for i in f:               # for 문으로 파일의 반복자를 반복하여 파일을 읽어온다.
    print(i)
f.close( )

# seek 메소드는 가장 첫 번째 위치에서 n 번째 바이트로 포인트를 이동한다.
# seek(offset, whence) 메소드
# offset 매개변수 : 첫 번째 위치를 설정한다. / whence 매개변수 : 최종 위치를 설정한다.
# tell 메소드는 파일 내 현재 포인트 위치를 반환한다.

# Python의 파일 개체에는 작업 위치를 변경하는 seek 메서드와 위치를 확인하는 tell 메서드를 제공하고 있어요.
# 다음은 파일의 내용이 회문(앞 뒤가 똑같은 문장)인지 판별하는 예제 코드입니다.
f1 = open('새파일3.txt', 'w')
f1.write('abc abc aaa')
f1.seek(5)
print('첫 번째 현재 위치 반환:', f1.tell( ))
f2 = open('새파일3.txt')
print('한 문자 읽기:', f2.read(1))
print('두 번째 현재 위치 반환:', f2.tell( ))

 # https://ehpub.co.kr/26-python-%ED%8C%8C%EC%9D%BC-%EC%9E%85%EC%B6%9C%EB%A0%A5%EC%97%90%EC%84%9C-%EC%9E%91%EC%97%85-%EC%9C%84%EC%B9%98-%EB%B3%80%EA%B2%BD-seek-%EC%9C%84%EC%B9%98-%ED%99%95%EC%9D%B8-tell/
fname = input("파일명:")
try:
    fs = open(fname, "rb")
    data = fs.read()
    print("파일 데이터:", data)
    fs.seek(0, 2)  # 파일 끝에서 0바이트 이동(파일 끝으로 이동)
    fsize = fs.tell()
    print("파일 크기:", fsize, "bytes")
    pflag = True
    for i in range(0, fsize):
        fs.seek(i)  # 파일 시작에서 i바이트 이동
        bd = fs.read(1)
        fs.seek(-(i + 1), 2)  # 파일 끝에서 (i+1)바이트 이전으로 이동
        ad = fs.read(1)
        if (bd != ad):
            pflag = False
            break
    fs.close()

    if pflag:
        print("회문입니다.")
    else:
        print("회문이 아닙니다.")
except:
    print("예외가 발생하였습니다.")


# with 문과 함께 사용하기
# with 컨텍스트 [as 별칭]:  // with 문은 컨텍스트를 자원 해제한다.
# close 메소드를 마지막에 호출하지 않으면 해당 객체가 다른 값으로 치환되거나 프로그램이 종료될 때에 자동으로 close 메소드를 실행
# 명시적으로 close 메소드를 호출하는 것을 권장한다.

with open("test7.txt", "w") as f:
 f.write("Life is too short, you need python")

# with 문을 사용하면 with 블록을 벗어나는 순간 열린 파일 객체 f 가 자동으로 close 되어 편리하다

file = open('test8.txt', 'w')
with file:
    file.write('with 문에서 별칭을 사용하지 않는다.')


