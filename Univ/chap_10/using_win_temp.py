# start 26.05.22 13:00
# 섭씨와 화씨를 상호 변환하는 프로그램을 작성하시오.
# - 섭씨 -> 화씨 : F = C * 9 / 5 + 32
# - 화씨 -> 섭씨 : C = (F - 32) * 5 / 9
# mac dark mode와 tkinter의 호환성 및 구 버전으로 인한 코드 구현은 가능하나 실행이 어려운 상황. 육안으로 안보임. 크기 및 색상 변경해도 동일
# 해당 문제는 windows 환경에서 실습하는게 나을 것 같음.
# --------26.05.22 23:26------- # 
# 해결. mac 내부 python 버전이 너무 오래되서 tkinter 자체는 존재하지만, 호환성 문제가 생겨서 python 3.12 버전을 추가 다운 받아서 해결함.
# 추가로 brew로 다운 받은 3.12 버전은 tkinter 지원을 하지 않아서 동작하지 않음.
import tkinter

# font 색상을 추가로 넣은 이유는 호환성 문제로 보이지 않던 문제가 단순 배경 문제인가 싶어 확인하기 위함.
def celsius_to_fahrenheit():
    celsius = float(celsius_box.get())
    fahrenheit = celsius * 9 / 5 + 32

    fahrenheit_box.delete(0, tkinter.END)
    fahrenheit_box.insert(0, fahrenheit)


def fahrenheit_to_celsius():
    fahrenheit = float(fahrenheit_box.get())
    celsius = (fahrenheit - 32) * 5 / 9

    celsius_box.delete(0, tkinter.END)
    celsius_box.insert(0, celsius)


def reset_value():
    celsius_box.delete(0, tkinter.END)
    fahrenheit_box.delete(0, tkinter.END)


win = tkinter.Tk()
win.title("Temperature Converter")
win.geometry("430x160")
win.configure(bg="white")

label1 = tkinter.Label(win, text="섭씨 -> 화씨", bg="white", fg="black")
label1.grid(row=0, column=0, padx=10, pady=10)

celsius_box = tkinter.Entry(
    win,
    width=20,
    bg="white",
    fg="black",
    insertbackground="black",
)
celsius_box.grid(row=0, column=1, padx=10, pady=10)

label2 = tkinter.Label(win, text="화씨 -> 섭씨", bg="white", fg="black")
label2.grid(row=1, column=0, padx=10, pady=10)

fahrenheit_box = tkinter.Entry(
    win,
    width=20,
    bg="white",
    fg="black",
    insertbackground="black",
)
fahrenheit_box.grid(row=1, column=1, padx=10, pady=10)

button1 = tkinter.Button(win, text="섭씨 -> 화씨", command=celsius_to_fahrenheit)
button1.grid(row=2, column=0, padx=10, pady=10)

button2 = tkinter.Button(win, text="화씨 -> 섭씨", command=fahrenheit_to_celsius)
button2.grid(row=2, column=1, padx=10, pady=10)

button3 = tkinter.Button(win, text="reset value", command=reset_value)
button3.grid(row=2, column=2, padx=10, pady=10)

win.mainloop()
