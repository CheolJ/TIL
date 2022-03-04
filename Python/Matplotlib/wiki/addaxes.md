# figure.add_axes
이전의 `ax`들은 배치에 있어 자유롭지 못한 단점이 있었다. 그래프 안에 그래프를 추가하는 등, 자유롭게 그래프 혹은 그림을 배치하기 위한 기능으로 이전에 정형화된 배치에서 벗어날 수 있는 장점이 있다.

## Doc
```python
add_axes(rect, projection=None, polar=False, **kwargs)
add_axes(ax)
```
`parameter`  
<b>rect</b> : sequence of float  
- The dimensions [left, bottom, width, height] of the new axes, All quantities are in fractions of figure width and hegiht.

## Usage
`add_axes`의 가장 큰 특징은 `ax`의 위치와 사이즈를 지정할 수 있다는 점이다. rect라는 `parameter`를 이용해서, `ax`의 왼쪽 아래 꼭지점을 설정하고, `width`와 `height`를 설정하여 `ax`의 크기를 설정한다. `add_axes` 안에 바로 설정할 수도 있지만, 코드 수정의 용이성을 위해 변수를 따로 설정하는 것이 좋다.  
`rect`는
```python
import matplotlib.pyplot as plt
import numpy as np
# rect1 =[left, bottom, width, height]
rect1 = [0.1, 0.1, 0.5, 0.5]

fig = plt.figure(figsize(7, 7))
ax = fig.add_axes(rect1)
```

## Auto-scaled axes
`left`, `bottom`, `width`, `height`를 미리 설정해두고, 값에 따라 자동적으로 사이즈가 변하는 auto-scale axes는 아래와 같이 작성한다.
```python
import matplotlib.pyplot as plt
import numpy as np

left, bottom = 0.1, 0.1
spacing = 0.05
width1, height1 = 0.5, 0.5
width2 = 1 - (2*left + width1 + spacing)
height2 = 1 - (2*bottom + height1 + spacing)

rect1 = [left, bottom, width1, height1]
rect2 = [left, bottom + height1 + spacing, 1 - 2*left, height2]
rect3 = [left + width1 + spacing, bottom, width2, height1]

fig = plt.figure(figsize=(7, 7))

ax1 = fig.add_axes(rect1)
ax2 = fig.add_axes(rect2)
ax3 = fig.add_axes(rect3)

plt.show()
```
`code output`
<p align="center"><img src="https://user-images.githubusercontent.com/50191848/156690360-fb4c97ba-34ce-4ee1-a03f-b6a59821c968.png" alt="code output" width="50%" height="50%"></p>


## Zomm axes
그래프 내부에 그래프를 배치함으로써, zoom기능을 수행하는 그래프를 배치할 수도 있다.
```python
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(7, 7))

ax = fig.add_subplot(111)
ax_zoom = fig.add_axes([0.4, 0.4, 0.45, 0.45])

plt.show()
```
`code output`
<p align="center"><img src="https://user-images.githubusercontent.com/50191848/156690065-622fcb3e-b442-4abf-915e-9e1a97fcb489.png" alt="code output" width="50%" height="50%"></p>

## Reference
[matplotlib.pyplot.figure.add_axes](https://matplotlib.org/3.5.1/api/figure_api.html)  
[공대형아-데이터시각화과정](https://www.inflearn.com/course/%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%8B%9C%EA%B0%81%ED%99%94-%ED%8C%8C%EC%9D%B4%EC%8D%AC)