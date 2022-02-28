from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

Label(root, text="메뉴를 선택하세요").pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="치즈햄버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="치킨햄버거", value=3, variable=burger_var)
btn_burger4 = Radiobutton(root, text="유라햄버거", value=4, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()
btn_burger4.pack()

Label(root, text="음료를 선택하세요").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text='콜라', value="콜라", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text='콜라', value="사이다", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()


def btncmd():
    print(burger_var.get())
    print(drink_var.get())
    
    
btn = Button(root, text='주문', command=btncmd)
btn.pack()

root.mainloop()