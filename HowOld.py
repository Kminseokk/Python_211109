from datetime import datetime as dt

a = dt.today().year #a는 현재년도
print('이번 년도는 :',a,'년 입니다.')

print('몇년도생 이세요? 1900 이상, 현재 년도 미만 만 가능해요')

b = int(input("입력해주세요.")) #b는 사용자 생년

if b > 1899 and b < a:
    c = a - b + 1 #c는 나이 계산 
    if c >= 17 and c <20:
        print('고등학생 이시네요')
    elif c >= 20 and c < 27:
        print('대학생이시네요')
    else:
        print('학생은 아니실 것 같네요')
else:
    print('잘못 입력했나봐요')
