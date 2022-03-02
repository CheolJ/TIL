# Figures and Axes
Matplotlib 안에서 figure와 ax 사이의 정확한 관계를 이해하면 데이터 시각화시 조금 더 효과적인 그래프 배치가 가능하다. 본 wiki는 figure와 ax 사이의 관계에 대해 정리하고 예제를 포함하고 있다.

## figures, axes
<p align="center"><img src="https://user-images.githubusercontent.com/50191848/156308848-e8837f53-3f58-476a-89d9-86c209223ee3.png" alt="anatomy of figure" width="50%" height="50%"></p>

## codes
### matplotlib.pyplot.figure
```python
matplotlib.pyplot.figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True, FigureClass=<class 'matplotlib.figure.Figure'>, clear=False, **kwargs)
```

### fig.add_subplot(Adding subplots)
```python
add_subplot(self, *args, **kwargs)
# Add an Axes to the figure as part of a subplot arrangement
```

### fig.add_subplot(axes grid)
```python
add_subplot(nrows, ncols, index, **kwargs)
add_subplot(pos, **kwargs)
add_subplot(ax)
add_subplot()
```

### fig.add_subplot(1D Axes)
```python
fig = plt.figure(figsize=(7, 7),
                 facecolor='linen')
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)

ax1.plot([2, 5, 10])
ax2.plot([10, 5, 2])
```

### fig.add_subplot(2D Axes)
```python
fig = plt.figure(figsize=(7, 7),
                 facecolor='linen')
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

ax1.plot([2, 5, 10])
ax2.plot([10, 5, 2])
```

### fig.add_subplot(Irregular Arrangement)
>Irregular arrangement의 경우 matplotlib가 grid를 인식하는 방법을 잘 볼 수 있는 예이다. `grid`를 세세하게 나누어 놨어도, 러프한 범위에서도 `grid`에 접근이 가능하다. 이를 통해, 서로 다른 사이즈를 가지는 그래프를 배치할 수도 있고, 그래프를 겹쳐 그릴 수도 그 응용은 매우 다양하다.
```python
fig = plt.figure(figsize=(7, 7),
                 facecolor='linen')
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(212) # Irregular part
```

## example
```python
import matplotlib.pyplot as plt
import numpy as np

# 오브젝트 형태로 할당받아서 편집하는 것이 더 좋다.
fig = plt.figure()
fig = plt.figure(figsize=(7, 7))
fig = plt.figure(figsize=(15, 15),
                 facecolor='linen',
                 )

# figure 안에 그래프를 그릴 수 있는 ax 추가
ax = fig.add_subplot()
ax.plot([2, 3, 1]) # line plot
ax.scatter([2, 3, 1], [2, 3, 4]) # scatter plot
```

## Reference
[FaceForensics++: Learning to Detect Manipulated Facial Images](https://openaccess.thecvf.com/content_ICCV_2019/html/Rossler_FaceForensics_Learning_to_Detect_Manipulated_Facial_Images_ICCV_2019_paper.html)
[matplotlib](https://matplotlib.org/stable/index.html)