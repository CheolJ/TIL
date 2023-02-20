# Class
`변수와 함수가 모두 모아놓은 개념`.  
코드 작성시에 코드의 효율을 높여주는 방법 중 하나로, 변수와 함수가 모두 모여있는 개념이라고 할 수 있다. 특히 클래스는 코드의 복잡도나 중복된 부분들을 획기적으로 줄일 수 있는 기법들을 포함하고 있기 때문에, `clean-code` 와 `object oriented programming`에 있어서는 매우 중요한 개념이다. 각 개념들을 잘 인지하고 코딩에 임한다면, 많은 사람들의 이해를 이끌어낼 수 있는 코드를 만들어 낼 수 있을 것이다.  


## class 개념
클래스는 `객체를 정의하는 틀`이라고 정의할 수 있다. 객체지향프로그래밍에서 얘기하는 그 `객체(Object)`를 만들어내는 틀이다. 다시말해, __클래스는 객체를 생성할 수 있도록 객체 내부 기능들을 정의해준다.__ 객체 내부의 기능들은 `메서드(method)`라고 정의한다. 클래스로부터 만들어진 객체는 그 클래스의 `인스턴스(instance)`라고 정의한다.

## Constructor & Initializer
Object를 생성하기 위해 Class를 아래와 같이 정의 후에 객체를 생성하였다. 그 과정은 다음과 같다.  
`example` class를 정의 한 후에 `test = example()` 로 `객체 생성(Construct)`을 호출하게 되면, class 내부의 `__new__`에서 객체 생성을 `할당(Allocate)`하고, `__init__`만 `오버라이딩`하여 `객체를 초기화(Initialize)` 시킵니다. 일반적으로 파이썬에서는 클래시 생성시 `__init__`메소드만 오버라이딩하여 사용합니다.(일반적으로 `__new__` 메서드 생략)  
메소드 오버라이딩(Method overriding)은 `상속(Inheritance)`에 대해 얘기한 후 아래에 더 자세히 기술하였다.
### 클래스 정의
```python
class example:
    def __init__(self): # Initializer; 초기화
        super().__init__()


    def __new__(self): # Allocator; 할당자
        return super().__new__(cls)


    def number(self):
        return 'Object generated!'


test = example() # Constructor; 생성자
print(test.number())
```
### 결과 출력
```
Object Generated!
```
---

## Inheritance
상속(Inheritance)은 기존의 클래스의 기능(속성, 메서드)들을 물려받는 개념이다. 클래스는 상속해주는 클래스를 부모 클래스(Parent class/Super class), 상속 받는 클래스를 자녀 클래스(Child class/Sub class) 라고 정의한다. 사용법은 간다하다. 자식클래스를 선언할때, 소괄호로 부모클래스를 포함시키면, 상속은 완료되어 부모 클래스의 속성과 메서드를 모두 따로 표기하지 않고도 사용이 가능하다.

### 클래스 상속 예제
```python
class Country:
    """Super class"""
    name = '국가명'
    population = '인구'
    capital = '수도'
    
    def show(self):
        print('국가 클래스의 메소드입니다.')


class Korea(Country):
    """Sub class"""
    
    def __init__(self, name):
        self.name = name
    

    def show_name(self):
        print('국가 이름은 : ', self.name)


a = Korea('대한민국')
a.show()
a.show_name()
print(a.capital)
print(a.name)
```
### 실행 결과
```python
국가 클래스의 메소드입니다.
국가 이름은 :  대한민국
'수도'
'대한민국'
```

## Method Over-riding
클래스를 상속 받은 후에 동일 명의 메소드를 자식 클래스에서 재선언할 수 있다. 이를 `메소드-오버라이딩(method-overriding)`이라고 얘기한다. 이 경우, 상속받은 메서드는 사라지고, **재선언한 매소드를 사용하게 된다.**
### 메서드 오버라이딩 예제
```python
class Country:
    """Super class"""
    name = '국가명'
    population = '인구'
    capital = '수도'
    
    def show(self):
        print('국가 클래스의 메소드입니다.')

class Korea(Country):
    """Sub Class"""

    def __init__(self, name,population, capital):
        self.name = name
        self.population = population
        self.capital = capital

    def show(self):
        print(
            """
            국가의 이름은 {} 입니다.
            국가의 인구는 {} 입니다.
            국가의 수도는 {} 입니다.
            """.format(self.name, self.population, self.capital)
        )


a = Korea('대한민국', '500000000', '서울')
a.show()
```

### 실행 결과
```python
국가의 이름은 대한민국 입니다.
국가의 인구는 50000000 입니다.
국가의 수도는 서울 입니다.
```