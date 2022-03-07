
# `ax.set_xlim`, `ax.set_ylim`
축의 범위를 지정하는 api로서, 축의 범위를 재설정할 수 있는 기능을 가지고 있다.
## Doc
```python
Axes.set_xlim(left=None, right=None, emit=True, auto=False, *, xmin=None, xmax=None)
```
`paraemter`  
<b>left</b> : float, optional
- The left xlim in data coordinates. Passing None leaves the limit unchanged.  
- The left and right xlims may also be passed as the tuple (left, right) as the first positional argument (or as the left keyword argument).

<b>right</b> : float, optional  
- The right xlim in data coordinates. Passing None leaves the limit unchanged.

<b>emit</b> : bool, default: True
- Whether to notify observers of limit change.

<b>auto</b> : bool or None, default: False  
- Whether to turn on autoscaling of the x-axis. True turns on, False turns off, None leaves unchanged.

<b>xmin, xmax</b> : float, optional
- They are equivalent to left and right respectively, and it is an error to pass both xmin and left or xmax and right.

## Usage
```python
fig, ax = plt.subplots(figsize=(7, 7))
ax.set_xlim([-10, 10])
```

`code output`  
<p align="center"><img src="https://user-images.githubusercontent.com/50191848/156974176-699caff3-8c4b-4bd9-a88f-1b97c105dc6b.png" alt="code output" width="50%" height="50%"></p>

## Reference
[matplotlib doc](https://matplotlib.org/3.5.1/index.html)