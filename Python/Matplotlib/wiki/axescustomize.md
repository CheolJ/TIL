# Axes customizing
## `matplotlib.axes.Axes.set_title`
`ax`의 제목을 설정할 때 사용
### Doc
```python
matplotlib.axes.Axes.set_title(label, fontdict=None, loc=None, pad=None, **kwargs)
```
`dec commnet`  
Set one of the three available Axes titles. The available titles are positioned above the Axes in the center, flush with the left edge, and flush with the right edge.

## `matplotlib.axes.Axes.set_xlabel`
`x-axis`의 제목을 설정
### Doc
```python
matplotlib.axes.Axes.set_xlabel(xlabel, frontdict=None, labelpad=None, *, Loc=None, **kwargs)
```
`doc comments`  
Set the label for the x-axis  
`parameter`  
<b>xlabel</b> : str
- The label text  

<b>labelpad</b> : float, default(4.0)
- Spacing in points from the Axes bounding box including ticks and tick labels. If None, the previous vlaue is left as is

<b>loc</b> : {'left', 'center', 'rgiht'}, default:'center'
- The label position. This is a high-level alternative for passing parameters x and horizontalalignment.  


## `matplotlib.axes.Axes.set_ylabel`
`y-axis`의 제목을 설정
### Doc
```python
matplotlib.axes.Axes.set_ylabel(ylabel, frontdict=None, labelpad=None, *, Loc=None, **kwargs)
```
`doc comments`  
Set the label for the y-axis  
`parameter`  
<b>ylabel</b> : str
- The label text  

<b>labelpad</b> : float, default(4.0)
- Spacing in points from the Axes bounding box including ticks and tick labels. If None, the previous vlaue is left as is

<b>loc</b> : {'left', 'center', 'rgiht'}, default:'center'
- The label position. This is a high-level alternative for passing parameters x and horizontalalignment.  

## `matplotlib.figure.tight_layout`
`axes`를 커스터마이즈를 하다보면, `figure` 내에서 서로 겹치는 부분이 나타나게 된다. 이 때, padding 값을 조절하여서 axes 간 침범을 막고 깔끔한 그래프를 그리기 위한 설정을 해줄 수 있는 명령어.
### Doc
```python
tight_layout(*, pad=1.08, h_pad=None, w_pad=None, rect=None)
```

### Usage
```python
title_list = ['Ax' + str(i) for i in range(4)]
xlabel_list = ['X Label' + str(i) for i in range(4)]
ylabel_list = ['Y Label' + str(i) for i in range(4)]

print(title_list)
print(xlabel_list)
print(ylabel_list)

fig, axes = plt.subplots(2, 2, figsize=(10, 10))
for ax_idx, ax in enumerate(Axes.flat):
    ax.set_title(title_list[ax_idx], fontsize=30)
    ax.set_xlabel(xlabel_lsit[ax_idx], fontsize=20)
    ax.set_ylabel(ylabel_list[ax_idx], fontsize=20)

# pad 파라미터를 통해 간격을 조정할 수 있음
fig.tight_layout()
```

## fig.subplots_adjust
`figure.tight_layout`과 다르게 `axes`들의 padding과 위치를 조금 더 세밀하게 조정할 수 있다.
### Doc
```python
matplotlib.pyplot.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
```
`parameter`  
<b>left</b> : float, optional  
- The position of the left edge of the subplots, as a fraction of the figure width.

<b>right</b> :float, optional  
- The position of the right edge of the subplots, as a fraction of the figure width.

<b>bottom</b> : float, optional  
- The position of the bottom edge of the subplots, as a fraction of the figure height.

<b>top</b> : float, optional  
- The position of the top edge of the subplots, as a fraction of the figure height.

<b>wspace</b> : float, optional  
- The width of the padding between subplots, as a fraction of the average Axes width.

<b>hspace</b> : float, optional  
- The height of the padding between subplots, as a fraction of the average Axes height.
### Usage
```python
import matplotlib.pyplot as plt
fig, axes = plt.subplots(2, 2, figsize=(2, 2))
for ax_idx, ax in enumerate(axes.flat):
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

# 

```


## Reference
[Matplotlib doc](https://matplotlib.org/stable/index.html)