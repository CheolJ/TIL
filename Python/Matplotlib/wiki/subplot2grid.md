# matplotlib.pyplot.subplot2grid
`subplot2grid`는 이전의 `add_subplot`, `subplots`와는 달리 다양한 사이즈의 axes를 보다 자유롭게 배치하게 해주는 명령어이다. nxm 형태의 axes 배치는 앞서 언급한 두 명령어가 더 효율적이지만, 아래 그림과 같은 배치에서는 `subplot2grid`가 더 효과적이다.

<p align="center"><img src="https://user-images.githubusercontent.com/50191848/156511444-5cf9b3bc-58bd-4506-a7e0-3e1ca376f896.png" alt="code output" width="65%" height="65%"></p>

## Doc
```python
matplotlib.pyplo.subplot2grid(shape, loc, rowspan=1, colspan=1, fig=None, **kwargs)
```
`doc comments`  
<b>shape</b>: (int, int)  
- Number of rows and of columns of the gird in which to place axis.  

<b>loc</b>: (int, int)  
- Row number and column number of the axis location within the grid  

<b>rowspan</b>: int, default:1  
- Number of rows the axis to span to the right  

<b>colspan</b>: int, default:1
- Number of columns of the axis to span downwards


## Usage
`figure`를 먼저 설정해준 후에, axes를 추가하는데, 명령어 자체가 plt.subplot2grid 이기 때문에, 안에서 어떤 figure에 그릴건지 `fig=(figure명)`와 같이 설정해줘야 한다. 또한 `colspan` 이나 `rowspan`으로 원하는 배치를 가지는 axes를 작성하기 용이하다.
```python
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7, 7),
                 facecolor='linen')

ax1 = plt.subplot2grid((3, 3), (0, 0), 
                       colspan=2,
                       fig=fig)

ax2 = plt.subplot2grid((3, 3), (1, 0),
                       colspan=3,
                       fig=fig)

ax3 = plt.subplot2grid((3, 3), (2,0), fig=fig)
ax4 = plt.subplot2grid((3, 3), (2,1), fig=fig)
ax5 = plt.subplot2grid((3, 3), (2,2), fig=fig)
```
`code ouput`  
<p align="center"><img src="https://user-images.githubusercontent.com/50191848/156514963-538a04a9-6670-48c8-9ed4-cc5ab38250ce.png" alt="code output" width="50%" height="50%"></p>

## Reference
[matplotlib.pyplotsubplot2grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot2grid.html)  
[공대형아-데이터시각화과정](https://www.inflearn.com/course/%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%8B%9C%EA%B0%81%ED%99%94-%ED%8C%8C%EC%9D%B4%EC%8D%AC)