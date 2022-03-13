# Text and Text alignment
`Figure` 내에서 적절한 위치에 텍스트를 배치하면, `figure` 자체만으로도 강력한 자료전달력을 가진다. 본 wiki에서는 텍스트의 배치에 대해서 설명하였다.

## Doc
```python
matplotlib.pyplot.text(x, y, s, fontdict=None, **kwargs)
```
위 코드 혹은 아래 주어진 `prameter` 이외에도 text api에서 제공되는 수많은 parameter를 사용이 가능하다.

## `paraemter`
**x, y** : float
- The position to place the text. By default, this is in data coordinates. The coordinate system can be changed using the transform parameter.

**s** : str
- The text.

**fontdict** : dict, default: None
- A dictionary to override the default text properties. If fontdict is None, the defaults are determined by rcParams.

**horizontal alignment, ha** : {'center', 'left', 'right'}, default: center  
- The horizontal alignment of the text relative to (x, y).

**vertical alignment, va** : {'top', 'center', 'bottom', 'baseline'}, default: top  
- The vertical alignment of the text relative to (x, y).


## Reference
[matplotlib.pyplot.text](https://matplotlib.org/3.5.1/api/_as_gen/matplotlib.pyplot.text.html#examples-using-matplotlib-pyplot-text)