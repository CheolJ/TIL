# 1. title : 제목없음 = Windows 메모장
# 2. 메뉴 : 파일, 편집, 서식, 보기, 도움말
# 3. 실제 메뉴 구현 : 파일 메뉴 내에서 열기, 저장, 끝내기 3개만 처리
# 3-1 열기 : mynote.txt 파일 내용 열어서 보여주기
# 3-2. 저장 : mynote.txt 파일에 현재 내용 저장하기
# 3-3. 끝내기 : 프로그램 종료


from tkinter import *

root = Tk()
root.title("제목없음 - windows 메모장")
root.geometry("640x480")

menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기")
menu_file.add_command(label="저장")
menu_file.add_separator()
menu.file_add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

root.config(menu=menu)
root.mainloop()