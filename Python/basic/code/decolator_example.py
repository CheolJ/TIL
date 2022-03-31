"""
Decolator 함수의 기본 형식

def c(func):
    def wrapper(*args, **kwargs):
        code_1
        result = func(*args, **kwargs)
        code_3
        return result
    
    return wrapper

"""

user_datas = [{"user":"test", "pw":1234, 'count':0},
              {"user":"python", "pw":5678, 'count':0}]


def need_login(func):
    def wrapper(*args, **kwargs):
        # user pw 화인
        user, pw = tuple(input("insert user pw : ").split(" "))
        
        # 존재하는 id 인지 확인
        for idx, user_data in enumerate(user_datas):
            if (user_data["useer"]) == user and (user_data["pw"]==pw):
                user_datas[idx]['count'] += 1
                #함수 실행
                return func(*args, **kwargs)
            
        return "wrong login data"

    return wrapper

@need_login
def plus(num1, num2):
    return num1+num2 

print(plus(1,2))