## Figure and Axes - subplots
이전에 `matplotlib.pyplot.figure`와 `fig.subplot`을 통해 그래프를 세팅했었는데, `matplotlib.pyplot.subplots`를 통해 한번에 세팅할 수 있다. 또한, axes들이 `numpy.array`형태로 저장되기 때문에, 접근성이나 데이터 처리에도 이전 방법보다 더 유용한 장점이 있다.


## Docs [subplots]
`Docs comments`  
Create a figure and set of subplots
This utility wrapper makes it convenient to create common layouts of subplots, including the enclosing figure objtect, in a single call.

```python
matplotlib.pyplot.subplots(nrows=1, ncols=1, *, sharex=False, squeeze=True, subplot_kw=None, gridspec_kw=None, **fig_kw)
```

## Usage

```python
fig, axes = plt.subplots(nrows=2, ncols=1)

print(axes)
print(type(axes))
print(axes[0])
```

## Usage plt.subplots(nrows and cols)
`subplots`는 다음과 같이 하나의 변수에 모든 axes 받아 배열형태로 사용하는 것 외에, 각 변수별로 `axes`를 받아서 사용할 수 있다.
```python
fig, (ax1, ax2) = plt.subplots(2, 1, 
                               figsize=(7, 7), 
                               facecolor='linen')
```

## plt.subplots(Indexing 2-D Axes)
`subplots`을 사용해 2Dimensions 생성하는 경우 배열의 접근방법이 달라진다. 이전의 `add_subplots`을 사용해 `axes`를 작성한 경우, 러프한 접근이 가능했지만, `subplots`로 만들어진 axes에는 러프한 접근이 불가능하다. 또한, `numpy.array`로 저장되기 때문에, 반복문을 통해 접근시에 불편함이 존재한다.
```python
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 2, 
                         figsize=(7, 7),
                         facecolor='linen')

print(axes)
print(axes[0])
print(axes[1])
print(axes[0, 0])
print(axes[0, 1])
```
`Code output`
<p align="center"><img src="https://user-images.githubusercontent.com/50191848/156508298-ea46a91f-1601-4cd2-a3bf-1a56f4fd1df4.png" alt="code output" width="100%" height="100%"></p>


## Reference
[matplotlib - subplot](https://matplotlib.org/stable/api/figure_api.html?highlight=subplots#matplotlib.figure.Figure.subplots)