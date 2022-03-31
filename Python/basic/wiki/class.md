# class
`변수와 함수가 모두 모아놓은 개념`.  
코드 작성시에 코드의 효율을 높여주는 방법 중 하나로, 변수와 함수가 모두 모여있는 개념이라고 할 수 있다. 특히 클래스는 코드의 복잡도나 중복된 부분들을 획기적으로 줄일 수 있는 기법들을 포함하고 있기 때문에, `clean-code` 와 `object oriented programming`에 있어서는 매우 중요한 개념이다. 각 개념들을 잘 인지하고 코딩에 임한다면, 많은 사람들의 이해를 이끌어낼 수 있는 코드를 만들어 낼 수 있을 것이다.  


## class 개념
클래스를 설명해 놓은 글들을 보면, 붕어빵을 찍어내는 틀, 자동차 바디를 찍어내는 틀 등으로 무언가를 찍어내는 틀이라고 설명이 많이 되어있다.~~(필자에게는 큰 틀에서는 이해가 갔지만, 예시가 와닿지는 않았다.)~~ 필자의 경우, league of legend의 미니언 예시가 가장 인상깊었다. league of legend에서는 일정한 시간 간격으로 미니언들이 생성되고 각 미니언들은 일정한 체력을 가지고 있다. 또한, 시간이 지남에 따라 미니언의 방어력들이 올라가고, 특정 조건에 따라서는 미니언들이 강해지기도 한다. 이를 코드로 나타내려면 어떻게 해야할까? 변수로 일일히 지정하고 만들기에는 너무 어려운 길이라고 생각된다. 이때 미니언의 정보들을 가지고 있는 어떤 변수형이 존재한다면, 그 변수형을 여러개 만

## Initializer
`생성자(Initialzier)`는
```python
class a:
    def __init__(self):
        
```

## Inheritance
클래스의 기능을 가져다가 기능을 수정하거나 추가할 때 사용하는 방법

```python

```

## Method Over-riding
클래스의 기존의 있었던 기능을 수정하는 기능
```python

```

## Super
부모 클래스에서 사용된 함수의 코드를 가져다가 자식 클래스의 함수에서 재사용할 때 사용
```python
class Marine:
    def __init__(self, h, a_p):
        self.health = h
        self.attack_power = a_p
        pass
    
    def attack(self, unit):
        unit.health -= self.attack_power
        if unit.health <= 0:
            unit.health = 0
            print("유닛이 사망하였습니다.")
```

## getter, setter
객체 내부 변수에 접근할 때 특정 로직을 거쳐서 접근시키는 방법
제한 조건을 적용시켜, 내부 변수에 접근시에 필터 역할을 함.