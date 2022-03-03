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
```python
import matplotlib.pyplot as plt
import numpy as np

rect1 = [0.1, 0.1, 0.5, 0.5]

fig = plt.figure(figsize(7, 7))
ax = fig.add_axes(rect1)