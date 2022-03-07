# axis_sharing (sharex, sharey)
하나의 `figure`에 여러 그래프를 그리다보면, 축을 공유하도록 그래프를 그려야 하는 경우들이 발생한다. 이때, 활용할 수 있는게 `sharex`, `sharey` 옵션이다. 앞서 배운 `subplots`, `add_subplot`, `subplot2grid` 에서 사용방법은 거의 동일하지만, 출력결과에 차이가 있다. 이부분을 활용하면, 더욱 효과적인 시각화가 가능하다.

## Using `plt.subplots`
`plt.subplots`안에서 `sharex=True`(또는 `sharey=True`) 옵션을 사용하게 되면, 각 축을 공유하게 된다. 각 축의 `tick_label`들이 사라지게 되는 것이 특징이다. 모두 동일하게 적용됨으로, `ax`별 커스터마이즈가 필요할 때는 `subplots`를 통한 `sharex`, `sharey` 사용은 피하는 것이 좋다.

### Usage
```python
import matplotlib.pyplot as plt
fig, axes = plt.subplots(2, 1, figsize=(7, 7), sharex=True)
axes[0].set_xlim([0, 100])
```
`code output`
<p align="center"><img src="https://user-images.githubusercontent.com/50191848/156976959-5403f1f2-0e65-4dac-abc5-0407b3060dea.png" alt="code output" width="50%" height="50%"></p>


## Using `plt.add_subplot`
`add_subplot` 안에서 `sharex` 옵션을 사용할 수 있다. `sharex`는 공유할 `ax`를 선택할 수 있고, 축을 공유한다. `tick_label`모두 잘 살아있고, `set_visible` api를 통해 `ticklabel`을 보이지 않게 설정할 수도 있다.  

### Usage
```python
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(7, 7))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212, sharex=ax1)
ax2.set_xlim([0, 100])
```
`code output`
<p align="center"><img src="https://user-images.githubusercontent.com/50191848/156977480-e0dffb94-5d62-488f-b0b0-a4bc27db9e73.png" alt="code output" width="50%" height="50%"></p>

## Using `plt.subplot2grid`
앞서 언급한 `plt.add_subplot`과 사용법이 동일하다. 사용예제만을 아래에 추가로 첨부하였다.

### Usage
```python
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(7, 7))
ax1_1 = plt.subplot2grid((2, 3), (0, 0), colspan=3, fig=fig)
ax2_1 = plt.subplot2grid((2, 3), (1, 0), colspan=2, fig=fig, sharex=ax1_1)
ax3_1 = plt.subplot2grid((2, 3), (1, 2), fig=fig, sharex=ax1_1)

ax1_1.set_xlim([0, 100])
fig.tight_layout()
```
`code output`
<p align="center"><img src="https://user-images.githubusercontent.com/50191848/156978674-57b89c93-678f-4fd7-adcd-c7c96c291b0f.png" alt="code output" width="50%" height="50%"></p>

## Reference
[matplotlib doc](https://matplotlib.org/3.5.1/index.html)