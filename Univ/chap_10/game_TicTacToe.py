from tkinter import *
from tkinter import messagebox
# start
# --- 26.05.29 --- #
window = Tk()
window.title("Game_tictaktok")

Button_list = []
turn = True # 턴을 주고 받아야 해서
# true / false 이전에 배열 9를 홀/짝 기준으로 턴제를 만들어봤는데 ["state"] = Disabled에서 문제 생겨서 변경함.
# 지금 생각해보면, mod 이용해서 홀/짝 유지해서 배열 인덱스 칸 맞추면 될 것 같긴함.
# 추가로 문자열 O / X 로도 기준을 잡아봤는데, 턴 변경 잡기가 애매했음.
# --- 26.05.30 --- #
# 게임 종료 로직 미 구현. 3줄 연속으로 이어지면 해당 턴의 사용자 승리로 판정할 것.
# --- 26.05.31 --- #
# 1.승리 판정 구현 2.Reset, Exit 구현 3.window 창 늘릴 때 비율 유지 구현
# 나중에 따로 이미지나 기능들을 추가로 넣어서 동작 외에 외관도 그럴싸하게 만들어볼 예정.

Win_Lines = [
    # 승리 판정 조건
    [0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [2,4,6],[0,4,8]
]
def reset_game():
    global turn
    turn = True

    for button in Button_list:
        button["text"] = ""
        button["state"] = NORMAL

def quit_game():
    window.destroy()

def check_winner(mark):
    for line in Win_Lines:
        a,b,c = line
        if(
            Button_list[a]["text"] == mark and 
            Button_list[b]["text"] == mark and
            Button_list[c]["text"] == mark
        ):
            return True
    return False

def click(key):
    global turn

    if turn == True:
        mark = "O"
    else:
        mark = "X"

    Button_list[key]["text"] = mark
    Button_list[key]["state"] = DISABLED

    if check_winner(mark):
        messagebox.showinfo("Game Over", mark + " 승리!")

        for button in Button_list:
            button["state"] = DISABLED
        return
    
    turn = not turn

# 추가 정보
# rowconfigure / columnconfigure
# 기본적으로 tkinter의 grid는 위젯의 크기에 딱 맞춰 있음. 창을 늘려도 위젯은 가운데에만 있거나 원래 크기를 유지함.
# 이를 "창을 늘렸을 때 남는 공간을 누가 가져갈 것인가?" 를 설정하는 핵심 함수임.
# weight (가중치) : 핵심 속성임. weight = 1이라고 설정하면, 창이 늘어날 때 그 행(또는 열)이 남는 공간을 비율대로 나누어 가짐.
# 예) column 0에 weight = 0, column 1에 weigth = 1을 주면, 창을 늘릴 때 column 1만 가로로 길어짐
# column 1에 weight = 1, column 2에 weight = 1을 주면, 창이 늘어날 때 두 column이 동일한 비율로 늘어남.

for row in range(4):
    window.rowconfigure(row, weight=1)
for column in range(3):
    window.columnconfigure(column,weight=1)

for i in range(9):
    def processs(t=i):
        click(t)
    
    temp = Button(window, text="", font=("times 26 bold"), width=8, height=4, command=processs)
    # matrix 3 x 3 (0 ~ 8)
    nRow = i // 3 # 0 1 2
    rColumn = i % 3 # 0 1 2 mv 0 1 2 mv ...
    temp.grid(row=nRow, column=rColumn, sticky=N+S+E+W) #sticky="nsew"로 사용해도 결과는 동일.
    # 중요 sticky #
    # 위에서 rowconfigure로 행/ 열의 공간을 확보했더라도, sticky 속성을 설정하지 않으면 위젯은 그 커진 공간의 중앙에만 머물러 있음.
    # sticky="nesw"(North, East, South, West)를 버튼 배치기 추가하면, 버튼이 해당 칸 전체를 꽉 채우며 늘어나게 됨
    Button_list.append(temp)
reset_button = Button(
    window,
    text="Reset",
    font=("times 16 bold"),
    command=reset_game
)
quit_button = Button(
    window,
    text="Exit",
    font="times 16 bold",
    command=quit_game
)

reset_button.grid(row=3, column=0, columnspan=2, sticky="nsew")
quit_button.grid(row=3, column=2, sticky="nsew")
window.mainloop()