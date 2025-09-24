#ch05.py (ch05 모듈) 자동완성: ctrl+space
# ctrl + shift + P --> select interpreter --> interpreter(base) 선택
# 실행 : cmd 터미널(ctrl+j)
def my_hello(cnt): #cnt번 반복
    print(__name__)
    for i in range(cnt):
        print('hello Python', end = "\t")
        print('Hello World')

if __name__ == '__main__':
    my_hello(2)