# `ax.set_yscale`
`matplotlib`에서는 각 축의 스케일을 지정할 수 있다. 시각화과정에서 값이 너무 클 경우 logscale을 사용하기도 하는데, 데이터를 한번 더 바꿔줘야하는 번거러움이 있다. 이떄, set_yscale을 사용, 추가적인 데이터 값 변경 없이, 바로 데이어 시각화가 가능하다.
## Doc

```python
Axes.set_yscale(value, **kwargs)
```
`parameters`  
<b>value</b> : {"linear", "log", "symlog", "logit", ...} or ScaleBase
- The axis scale type to apply.

**kwargs  
- Different keyword arguments are accepted, depending on the scale. See the respective class keyword arguments:

추가적으로, `log scale` 사용시, 밑(base)를 지정할 수 있다. 이와 관련된 예제를 아래에 첨부하였다. ~~(basey 옵션은 사라져서 base 옵션을 사용하는 것이 맞다.)~~

## Usage
```python
import matplotlib.pyplot as plt
import numpy as np

p = np.linspace(0.001, 0.999, 300)
information = -np.log2(p)

fig, ax = plt.subplots(figsize=(7, 7))
ax.set_yscale('log', base=2)
ax.plot(p, information)
```
`code output`
<p align="center"><img src="https://user-images.githubusercontent.com/50191848/156988752-bd15a4e0-c1ac-4f6a-9e97-174ca2b192c4.png" alt="code output" width="70%" height="70%"></p>


## Reference
[matplotlib doc](https://matplotlib.org/3.5.1/index.html)