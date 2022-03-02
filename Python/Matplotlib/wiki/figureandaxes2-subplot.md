## Figure and Axes - subplots

## Docs [subplots]
```python
matplotlib.pyplot.subplots(nrows=1, ncols=1, *, sharex=False, squeeze=True, subplot_kw=None, gridspec_kw=None, **fig_kw)
```
Create a figure and set of subplots
This utility wrapper makes it convenient to create common layouts of subplots, including the enclosing figure objtect, in a single call.

## Usage
```python
fig, axes = plt.subplots()
```


```
fig axes = plt.subplots(nrows=2, ncols=1)
print(axes)

print(type(axes))

print(axes[0])
print(axes[1])
```

## Reference
[matplotlib - subplot](https://matplotlib.org/stable/api/figure_api.html?highlight=subplots#matplotlib.figure.Figure.subplots)