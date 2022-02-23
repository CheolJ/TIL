from tkinter import *

root =Tk()
root.title("Nado GUI")

# 파일 프레임
file_frame = Frmae(root)
file_frame.pack()

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일추가")
btn_add_file.pack(side="left")
btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="선택삭제")
btn_add_file.pack(side="right")



root.resizable(False, False)
root.mainloop()