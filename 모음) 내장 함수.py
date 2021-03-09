# 내장 함수 : 파이썬에서 자주 사용되는 많은 함수들로 편리하게 코드를 짤 수 있다.

# 1. 숫자 함수
print(bin(10))  # bin() 2진법 binary의 약자  은 2진수 문자열로 변환하여 반환한다.
print(oct(10))  # 8진수 문자열로 변환하여 반환한다.
print(hex(10))  # 16진수 문자열로 변환하여 반환한다.
print(float(5))  # float() 정수 또는 문자열을 부동 소수로 반환한다.
print(float('5'))
print(divmod(7, 3))  # divmod 함수는 a를 b로 나눈 몫과 나머지를 튜플 자료형으로 반환한다
print(int('11', 2))  # 문자열 숫자를 정수 형태로 반환한다.
                     # 2진수, 8진수, 16진수로 표현된 문자열 숫자를 10진수로 변환
print(round(1.5))    # 소수점 뒤에 오는 숫자를 반올림하여 반환한다.

#  2. 인스턴스 함수

string = 'a'            # hash 함수는 객체의 해시값을 반환한다.
print(hash(string))     # 해시값은 컴퓨터에서 부여한 주소의 값이라고 생각하면 된다.

string = 'a'            # id 함수는 인자인 객체를 입력받아 객체의 레퍼런스인 고유 주소값을 반환한다.
print(id(string))       # 지리 좌표계인 위도와 경도의 역할은 해시값 ,주소의 역할은 고유 주소값이 한다고 보면 된다.

print(dir([1, 2, 3]))   # dir 함수는 객체가 가지고 있는 모든 속성의 이름들을 리스트로 반환한다.

print(type((1, 2)), end='')        # type 함수는 객체를 입력받아 객체가 지닌 요소의 자료형을 반환한다
print(type({'id' : 1}), end='')    # type 함수로 반환하는 자료형은 int, str, list, tuple, dict, set 등을 반환한다.
print(type({1, 2}), end='')


class Person:                    # isinstance 객체가 클래스의 객체인지를 판단하여 참이면 True로 거짓이면 False를 반환한다.
    pass
a = Person( )
print(isinstance(a, Person))     # isinstance (object 매개변수:객체를 설정 , classinfo 매개변수: 클래스의 정보를 설정 )

# 3. 자료형 함수
                               # bytes 함수는 정수나 문자열을 새로운 바이너리 객체로 반환한다. 반환한 바이너리는 불변 시퀀스 이다.
data = 3                       # bytes([source[, encoding]]) 함수
print(bytes(data))             # source 매개변수 : 정수나 문자열을 설정한다.
                               # encoding 매개변수 : 문자열 인코딩을 설정한다.

data = 5                       # bytearray 함수는 정수를 새로운 바이너리 배열 객체로 반환한다.
print(bytearray(data))

print(list('python'))         # list 함수는 반복 가능한 자료형을 입력받아 리스트로 만들어 반환한다.
print(list((1, 2, 3)))

print(tuple('abc'))          # tuple 함수는 반복 가능한 자료형을 입력받아 튜플로 만들어 반환한다
print(tuple([1, 2, 3]))

# print(dict([(1, 'one'), ('two', 2)])   # dict 함수는 반복 가능한 자료형을 입력받아 딕셔너리로 만들어 반환한다.
                                       # dict 함수의 딕셔너리 안에 있는 아이템끼리는 순서가 없으므로 임의의 순서로 저장한다.

# print(set([1, 2, 3, 4, 5, 5, 5]))           # set 함수는 반복 가능한 자료형을 입력받아 세트로 만들어 반환한다.
# print(set({1:2, 2:3, 3:4, 1:5, 2:5, 3:5})

print(bool(1))                       # bool 함수는 논리값인 True 또는 False 중의 하나를 반환한다.
print(list(zip([1, 2, 3], [4, 5])))  # zip 함수는 자료형을 같은 개수로 묶어서 튜플로 반환한다.

c = [1, 2, 3, 4, 5]                  # slice(start, stop[, step]) 함수
d = slice(1, 4)
print(c[d])

print(len('python'))                 # len 함수는 자료형의 길이를 구하고 요소의 전체 개수를 반환한다.
print(len([1, 2, 3]))

print(list(range(10)))               # range(start, stop[, step]) 함수
print(list(range(3, 10)))
print(list(range(4, 10, 2)))

print(eval('1+2'))                   # eval(expression, globals=None, locals=None) 함수
print(eval(" '홍'+'길'+'동' "))       # expression : 표현식으로 실행 가능한 표현식이다.
print(eval('divmod(4, 3)'))          # globals 옵션 : 전역적 객체로 객체는 딕셔너리이며 기본값은 None.
                                     # locals 옵션 : 지역적 객체로 모든 매핑 객체가 될 수 있으며 기본값은 None.

print(all([1, 2, 3, 0]))             # any 함수는 인자인 반복 가능한 자료형에 하나라도 참이면 True를 반환한다.

def postive_number(x):               # filter 함수는 반복 가능한 자료형을 수행해서 필터를 통하여 연속열의 요소를 걸러내어서 반환한다.
    return x>0
print(list(filter(postive_number, [1, 2, 3, -4, -5, -6])))

def two_times(x):                    #  map(function, iterable) 함수
    return x*2                       # function 매개변수 : 함수로 참을 반환하는 요소들을 구축한다.
                                     # iterable 매개변수 : 반복 가능한 자료형을 설정한다
print(list(map(two_times, [1, 2, 3, 4])))

for name in enumerate(['홍길동', '전우치', '임꺽정']): # enumerate(iterable, start=0) 함수
    print(name)

f = [1, 6, 3, 8, 6, 2, 9]      # reversed 함수는 연속열의 역순인 사본을 생성하여 반환한다.
print(list(reversed(f)))

print(max([1, 2, 3]))          # max 함수는 반복 가능한 자료형을 입력받아 최대값을 반환한다.
print(max('python'))

print(min([1, 2, 3]))          # min 함수는 반복 가능한 자료형을 입력받아 최소값을 반환한다
print(min('python'))

a = [1, 2, 3, 4, 5]            # sum 함수는 반복 가능한 자료형의 입력값을 받아 서로 더한 값을 반환한다.
print(sum(a))
print(sum(a, 10))

# 4. 문자열 함수

print(chr(65))      # chr 함수는 아스키코드에 해당하는 문자로 반환한다.
print(ord('A'))     # ord 함수는 유니코드 문자에 해당하는 아스키코드를 반환한다.
print(str('0.3'))   # str 함수는 객체를 표현하는 문자열을 반환한다
print(repr('0.3'))  # repr 함수는 주어진 객체의 표현 문구를 구하고 객체의 인쇄 가능한 표현을 포함하는 문자열을 반환한다

# 5. 입출력 함수

a = input('입력: ')      # print 함수는 객체를 출력하고 옵션으로 출력 형태를 지정할 수 있다.
print(a)

# 6. 오브젝트 함수
# 오브젝트를 확인하거나 오브젝트의 정보를 알려주는 함수이다.

# ascii 함수는 repr 함수처럼 객체의 인쇄 가능한 표현을 포함하는 문자열과 문자열에 포함된 아스키코드도 반환한다.

# callable 함수는 객체가 실행 가능한지 확인하고 반환한다.

# classmethod 함수는 메소드를 클래스 메소드로 변환한다.
# 클래스 메소드는 클래스 내부에서 직접 접근이 가능한 메소드이다.

# compile 함수는 코드를 컴파일한다.
# compile(source, filename, mode, optimize=-1) 함수
# source 매개변수 : 코드를 설정한다.
# filename 매개변수 : 코드를 읽은 파일명을 설정한다.
# mode 매개변수 : 컴파일해야 하는 코드 종류를 설정한다.
# optimize 옵션 : 컴파일러의 최적화 수준을 설정하며 기본값은 –1이다.
# ➀ -1 ⇢ 최적화 수준 선택 ➁ 0 ⇢ 최적화 없음
# ➂ 1 ⇢ 최적화 확인 제거 ➃ 2 ⇢ 함수에 대한 설명인 독스트링 제거

# complex 함수는 문자열이나 숫자를 복소수로 변환하여 반환한다.
# 복소수는 실수와 허수 합으로 이루어지는 실수를 확장한 수이다.
# 파이썬에서는 실수+허수에서 허수에 소문자 j이나 대문자 J를 붙이면 복소수가 된다.
# 복소수는 전기의 교류를 표현하고 계산하는 데 유용하게 사용된다.
# complex([real[, imag]]) 함수
# real 매개변수 : 실수부를 설정한다.
# imag 매개변수 : 허수부를 설정한다.

# exec 함수는 파이썬 코드의 동적 실행을 지원한다.

# delattr 함수는 객체에 주어진 문자열로 된 이름의 속성이 있으면 그 속성을 제거한다.
# delattr(object, name) 함수
# object 매개변수 : 객체를 설정한다.
# name 매개변수 : 속성명을 설정한다.

# getattr 함수는 객체에 주어진 문자열로 된 이름의 속성값을 반환한다.

# globals 함수는 현재 전역 테이블을 나타내는 딕셔너리를 반환한다.
# globals 함수는 실행 위치에서 현재 모듈의 전역 객체 이름 공간의 사본을 구한다.

# hasattr 함수는 객체가 주어진 문자열로 된 이름의 속성이 있는지를 파악하고 반환한다.
# hasattr(object, name) 함수
# object 매개변수 : 객체를 설정한다.
# name 매개변수 : 속성명을 설정한다.

# help 함수는 객체의 내장 도움말 시스템을 호출하여 표시한다.

# issubclass 함수는 클래스가 특정 클래스의 자식 클래스인지 확인하고 반환한다.
# issubclass(class, classinfo) 함수
# class 매개변수 : 클래스를 설정한다.
# classinfo 매개변수 : 클래스의 정보를 설정한다.

# iter 함수는 연속열에 대해서 반복자를 생성하고 for 문에서 내부적으로 사용한다.

# locals 함수는 현재 지역 테이블을 나타내는 딕셔너리를 반환한다.
# locals 함수는 실행 위치의 지역 객체 이름 공간의 사본을 구한다.

# memoryview 함수는 지정된 객체로부터 만들어진 메모리 뷰 객체를 반환한다.

# next 함수는 반복자를 입력받아 반복자와 생성자 사이에서 다음 요소를 요청한다.

# object 함수는 새로운 기능의 객체를 반환한다.

# setattr 함수는 객체에 주어진 문자열로 된 이름의 속성값을 저장한다.
# setattr(object, name) 함수
# object 매개변수 : 객체를 설정한다.
# name 매개변수 : 속성명을 설정한다.

# open 함수는 파일을 열고 파일 객체를 반환한다.
# open(file, mode='r', encoding=None, newline=None) 함수
# file 매개변수 : 파일의 경로를 설정한다.
# mode 옵션 : 파일이 열리는 모드를 설정하며 기본값은 r 모드이다.
# ➀ r ⇢ 읽기 ➁ w ⇢ 쓰기 ➂ rb ⇢ 바이너리 읽기 ➃ wb ⇢ 바이너리 쓰기
# encoding 옵션 : 문자열 인코딩을 설정하며 기본값은 None.
# newline 옵션 : 텍스트 파일의 끝에 줄 넘김의 설정을 하며 기본값은 None.

# property 함수는 등록 정보 속성을 반환한다.
# property(fget=None, fset=None, fdel=None, doc=None) 함수
# fget 옵션 : 속성값을 얻는 함수를 설정하며 기본값은 None.
# fset 옵션 : 속성값을 설정하는 함수를 설정하며 기본값은 None.
# fdel 옵션 : 속성값을 삭제하는 함수를 설정하며 기본값은 None.
# doc 옵션 : 속성의 독스트링을 만들며 기본값은 None.

# staticmethod 함수는 메소드를 정적 메소드로 변환한다.
# 정적 메소드는 클래스 외부에서 직접 접근이 가능한 메소드이다.

# super 함수는 클래스 내부에서 해당 클래스의 부모 클래스를 찾을 때 사용한다.

# vars 함수는 객체에 주어진 모듈의 최상위 속성들을 반환한다.

# ˍ ˍ importˍ ˍ 함수는 모듈을 임포트 한다.

