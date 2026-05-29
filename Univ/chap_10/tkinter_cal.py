from tkinter import *
window = Tk()
window.title("Calulator")
display = Entry(window, width=33, bg="black")
display.grid(row=0,column=0,columnspan=5)

button_list = [
    "7","8","9","/","C",
    "4","5","6","*","//",
    "1","2","3","-","+","**",
    "0",".","=","BS"
]
def click(self,key):
    if self.is_result and key not in ["+", "-", "*", "/", "//", "**"]:
            self.display.delete(0, END) # 화면을 싹 지우고
            self.is_result = False      # 다시 일반 입력 상태로 복귀
            # 그 외의 경우 (이미 숫자가 입력 중이거나, 연산자를 누른 경우)
            # 평소처럼 입력 이어감.
    if key == "=":
        result = eval(display.get()) #eval은 문자열로 받은 수식을 계산해서 그 값을 반환하는 함수. ex "4 x 3" return 12
        s = str(result)
        display.insert(END, "=" + s) # display에는 str 값이 들어감으로 str 형변환 한뒤에 넣기
    elif key == "C":
        display.delete(0, END)
    elif key == "BS":
        #strlen = len(display.get())
        strlen=display.index('end') # 현재 입력된 총 길이, 마지막 인덱스 값을 찾음.
        display.delete(strlen-1, 'end') # BS는 마지막에서 한칸만 지우는 기능이므로, start = 전체 길이 - 1, end = END
    else:
        display.insert(END, key)
row_index = 1
column_index = 0
for button_text in button_list:
    def process(t=button_text):
        click(t)
    Button(window, text=button_text, width=5,
           command=process).grid(row=row_index, column=column_index)
    column_index+=1
    if column_index > 4:
        row_index += 1
        column_index = 0

window.mainloop()
