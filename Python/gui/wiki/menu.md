# Menu

## Basic Setting
```python
from tkinter import *

window = tkinter.Tk()
window.title("Example")
window.geometry("640x480+100+100")
window.resizable(False, False)
```

## Menu setting
```python
def close():
    window.quit()
    window.destroy()

# window에 menu 추가
menubar = Menu(window) 

# 상위 및 하위메뉴 1
menu_1 = Menu(menubar, tearoff=0)
menu_1.add_command(label='하위메뉴 1-1')
menu_1.add_command(label='하위메뉴 1-2')
menu_1.add_separator()
menu_1.add_command(label="하위메뉴 1-3", command=cloase)
menubar.add_cascade(label="상위메뉴 1", menu=menu_1)

# 상위 및 하위메뉴 2
menu_2 = Menu(menubar, tradeoff=0, selectcolor="red")
menu_2.add_radiobutton(label="하위메뉴 2-1", state="disable")
menu_2.add_radiobutton(label="하위메뉴 2-2")
menu_2.add_radiobutton(label="하위메뉴 2-3")
menubar.add_cascade(label="상위메뉴 2", menu=menu_2)

# 상위 및 하위메뉴 3
menu_3 = Menu(menubar, tradeoff=0, selectcolor="red")
menu_3.add_radiobutton(label="하위메뉴 3-1", state="disable")
menu_3.add_radiobutton(label="하위메뉴 3-2")
menu_3.add_radiobutton(label="하위메뉴 3-3")
menubar.add_cascade(label="상위메뉴 3", menu=menu_3)

window.config(menu=menubar)
window.mainloop()
```


## Menu subscription



## Reference
- [tkinter-python docs](https://docs.python.org/ko/3/library/tkinter.html)
- [Daehee Yun Tech Blog](https://076923.github.io/posts/Python-tkinter-8/)