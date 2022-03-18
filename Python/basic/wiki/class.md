# class
변수와 함수가 모두 모아놓은 개념  
코드 작성시에 코드의 효율을 높여주는 방법 중 하나로, 변수와 함수가 모두 모여있는 개념이라고 할 수 있다. 하지만 그 개념들을 완전히 이해하고 있지 않다면, 혼란을 일으킬 수 있

사용방법
- 변수와 함수가 들어있는 클래스를 선언
- 클래스를 객체로 만들어서 클래스 안에 선언되 변수와 함수를 사용

## 클래스의 선언
## 객체 지향
- 실제 세계를 코드에 반영해서 개발하는 방법  
- 여러명의 개발자가 코드를 효율적으로 작성해서 프로젝틀 완성시키기 위한 방법  

## Inheritance
```python

```

## Method Over-riding
```python

```

## Super
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