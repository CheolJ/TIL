from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

chkvar = IntVar() # chkvar 에 int형으로 저장한다.
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# chkbox.select()
# chkbox.deselect()
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)


def btncmd():
    print(chkvar.get()) # 0 : 체크 해제., 1, 체크
    print(chkvar2.get())
btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop()