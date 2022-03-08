# Function-basic
반복적인 기능들을 한 곳으로 모아놓고 사용하는 기능을 `함수`라고 한다. 함수의 정의를 통해, 반복적인 코드 작성을 피할 수 있어 코드의 이해도를 높일 수 있는 것이 장점이다.

## `parameter` and `argument`
`parameter` : 함수를 선언할 때, 호출하는 부분에서 보내주는 데이터를 받는 변수  
- `default parameter`  : `argument`를 받지 못하는 상황에서 디폴트 값을 넣어주어, 오류상황을 배제함  

`arguemnt` : 함수를 호출할 때, 함수에 보내주는 데이터
- `keyword argument` : 원하는 parameter에 값을 보내고 싶을 때, 지정해서 사용

### code
```python
def plus(num1, num2): # parameter
    print(num1, + num2)

plus(1, 2) # argument
```
### code output
```python
1 2
```

## `return`
함수 실행한 결과를 저장하고 싶을 때, 사용합니다.

## `*args`, `**kwargs`
- 함수를 호출할 때, 아규먼트와 키워드 아규먼트의 갯수를 특정지을 수 없을 때 사용
- 파라미터로 사용

함수를 호출할 때도, `*`를 사용할 수 있다. 이 경우 호출한 변수를 `argument` 형태로 함수로 보내주게 된다. 자세한 예제는 아래 예제를 참고하자.
### Code1 (*args, **kwargs)
```python
def plus(*args, **kwargs):
    print(type(args), args)
    return sum(args)

plus(1, 2, 3, 4, 5, num1=6, num2=7)
```
### Code output
```
<class 'tuple'> (1, 2, 3, 4, 5)
<class 'dict'> {'num1': 6, 'num2': 7}
15
```
### Code2 *
```python
def func(num1, num2, num3):
    return num1 + num2 + num3

data = [1,2,3]
func(*data)
```
### Code2 output
```python
6
```

## `Docstring`
함수의 설명을 작성하는 부분을 `docstring`이라고 한다. 함수 사용시 `shift`+`tab`키를 통해 확인을 할 수 있다.  
`docstring`에는 크게 아래의 내용이 포함된다.  

**1) 어떤 파라미터를 어떤 데이터 값으로 받는가**,  
**2) 어떤 결과를 리턴하는지**  
**3) 함수가 어떤 기능을 동작하는지** 

`docstring` 작성은 함수 바로 아래에, `"docstring"` (여러줄 작성시에는 `"""docstring"""`) 형태로 작성하면 된다.