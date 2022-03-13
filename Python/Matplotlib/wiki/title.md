# Title APIs

## `fig.suptitle`
`Figure`의 제목을 설정을 한다. 여러 axes를 포함할때 각 axes를 모두 포함하는 제목을 설정할 때 쓰인다.
### Doc

```python
matplotlib.pyplot.suptitle(t, **kwargs)
```  

### `parameter`
**t** : str
- The suptitle text.

**x** : float, default: 0.5  
- The x location of the text in figure coordinates.

**y** : float, default: 0.98  
- The y location of the text in figure coordinates.

**horizontal alignment, ha** : {'center', 'left', 'right'}, default: center  
- The horizontal alignment of the text relative to (x, y).

**vertical alignment, va** : {'top', 'center', 'bottom', 'baseline'}, default: top  
- The vertical alignment of the text relative to (x, y).

**fontsize, size** : default: rcParams["figure.titlesize"] (default: 'large')  
- The font size of the text. See Text.set_size for possible values.

**fontweight, weight** : default: rcParams["figure.titleweight"] (default: 'normal')  
- The font weight of the text. See Text.set_weight for possible values.

## `ax.set_title`
`ax`별 타이틀을 설정할 때 사용하는 명령어. 각 ax별 소제목을 설정할 때 사용
### Doc

```python
Axes.set_title(label, fontdict=None, loc=None, pad=None, *, y=None, **kwargs)
```

### `parameter`
**label** : str
- Text to use for the title

**fontdict** : dict
- A dictionary controlling the appearance of the title text, the default fontdict is:  

```python
{'fontsize': rcParams['axes.titlesize'],
 'fontweight': rcParams['axes.titleweight'],
 'color': rcParams['axes.titlecolor'],
 'verticalalignment': 'baseline',
 'horizontalalignment': loc}
```

**loc** : {'center', 'left', 'right'}, default: rcParams["axes.titlelocation"] (default: 'center')
- Which title to set.

**y** : float, default: rcParams["axes.titley"] (default: None)
- Vertical Axes loation for the title (1.0 is the top). If None (the default), y is determined automatically to avoid decorators on the Axes.

**pad** : float, default: rcParams["axes.titlepad"] (default: 6.0)
- The offset of the title from the top of the Axes, in points.

## `ax.set_xlabel`, `ax.set_ylabel`

### Doc
`ax`의 각 x-axis, y-axis에 대해 제목을 설정하는 명령어.
```python
Axes.set_xlabel(xlabel, fontdict=None, labelpad=None, *, loc=None, **kwargs)
```  

### `parameter`
**xlabel(ylabel)** : str
- The label text.

**labelpad** : float, default: `rcParams["axes.labelpad"]` (default: 4.0)
- Spacing in points from the Axes bounding box including ticks and tick labels. If None, the previous value is left as is.

**loc** : {'left', 'center', 'right'}, default: `rcParams["xaxis.labellocation"] `(default: 'center')
- The label position. This is a high-level alternative for passing parameters x and horizontalalignment.