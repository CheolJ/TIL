# `ax.twinx` (Different Y values)
하나의 `ax`에 여러개의 그래프를 그릴 때, 축을 공유하게 되면서 서로의 스케일이 너무 달라서, 한쪽의 그래프가 보이지 않게 되는 경우들이 발생한다. `ax.twinx`는 이런 경우에 축을 하나 더 추가해 그래프의 가독성을 높이는 방법이다.

## Doc
```python
Axes.twinx()
```

## Usage
```python
import matplotlib.pyplot as plt
import numpy as np

PI = np.pi
t = np.linspace(0.01, 5*PI, 100)
sin = np.sin(t)
exp = np.exp(t)

fig = plt.figure(figsize=(10, 7))
ax1 = fig.add_subplot()
ax1.plot(t, sin)
ax2 = ax1.twinx()
ax2.plot(t, exp)
```
`code output`
<p align="center"><img src="https://user-images.githubusercontent.com/50191848/156983515-6f084e5d-7104-4be4-8002-801ea4acc68d.png" alt="code output" width="70%" height="70%"></p>

## Reference
[matplotlib doc](https://matplotlib.org/3.5.1/index.html)