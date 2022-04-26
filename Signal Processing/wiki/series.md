# Series(mathmatics)
신호처리는 복잡한 신호들을 분석하여 원하는 신호를 잘 수집하는 것에 그 목적이 있다. 신호를 단순화 하기 위해서는 식을 단순화 시키는 과정이 필요한데, 그 기반이 되는 것이 `급수(Series)`이다. 본 wiki에서는 신호처리에 기본적으로 쓰이는 수학 이론들을 정리하고 할 수 있는 한 증명까지 진행해보았다. `Latex`으로 공식을 정리해놨기 떄문에, 언제가는 긁어서 쓸 날이 올거라고 믿어보자. (github에서는 latex을 인식하지 못하는 사고가 발생했다..전부 잘 인시가고서 latex만 인식안하는 넌 정말 편식하는 나쁜아이로구나...!)

## Taylor series
테일러 시리즈는 미지의 함수를 무한한 다항식의 합으로 나타내 식을 근사하는 기법이다. 복잡한 함수를 다항식으로 나타낼 수 있기 때문에, 함수의 경향성이나 계산을 보다 용이하게 할 수 있는 장점이 있다.
### Definition
함수 $f(x)$가 $a \in R$에서 미분이 가능할 때, 다항함수로 근사한 식을 `테일러 급수(Taylor seires)`라고 부른다.

$T_f(x) = \displaystyle\sum_{n=0}^{\infty}{(x-a)^n}=f(a) + f'(a)(x-a) + {1\over2!}f''(a)(x-a)^2 + {1\over3!}f'''(a)(x-a)^3 + \cdots + {1\over n!}f^{(n)}(x-a)^n$  

### `MacLaurin series`
간단한 삼각함수는 MacLaurin Series를 통해 표현할 수 있고, 원래 식과 매우 유사하다는 것을 계산과 여러 증명을 통해 알 수 있다. 
#### Definition
$a=0$일 때의 테일러 급수를 매클로린급수라고 부른다.  
$M_f(x) = \displaystyle\sum_{n!}^{\infty}{f(0)+f'(0)x + {1 \over 2!}f''(0)x^2 + {1 \over 3!}f'''(0)x^3 + \cdots + {1 \over n!}f^{(n)}x^n}$

### `Analytic Function`
#### Definition
함수 f가 한 점 $x=a$에서 해석적이라는 것은, 그 점 근방에서 테일러 급수가 수렴하는 것이고, 정의역 D의 모든 점에서 해석적인 함수를 해석함수라고 한다. 다시말해, 어떤

### `Laurant series`
#### Definition
테일러 급수(Talyor series)의 범위를 실수 범위에서 복소수 범위까지 확장시킨 함수를 로랑급수(Laurant series)라고 한다.  
$f_z(x) = \displaystyle\sum_{n=0}^{\infty}{c_z(z-z_0)^n}$

#### holomorphic function
복소 범위에서 미분가능(정칙), 해석가능한 함수를 정칙함수로 정의한다. 다시말해, `일반적으로 복소함수가 미분가능(정칙)하면, 반드시 로랑급수가 원래 함수와 같아진다` 라고 얘기할 수 있다

## Euler equation

## Fourier series

### prove

## Reference