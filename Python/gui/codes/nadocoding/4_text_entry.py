from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# 텍스트 위젯 만들기
txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요")

# 로그인이나 패스워드가 단일 line 입력이 필요할 때 entry 사용
e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력해요")

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # 1은 첫번쨰라인을 읨하고, 0은 첫번째 컬럼 위치
    print(e.get())
    
    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop()
