import tkinter as tk
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

class FreeLineDrawer:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack()
        
        # 이전 좌표를 기억하기 위한 변수
        self.last_point = None
        
        # 이벤트 바인딩
        self.canvas.bind("<Button-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def on_press(self, event):
        # 마우스를 누른 지점을 시작점으로 설정
        self.last_point = Point(event.x, event.y)

    def on_drag(self, event):
        # 현재 마우스 위치
        current_point = Point(event.x, event.y)
        
        # 마지막 지점부터 현재 지점까지 선을 그림
        self.canvas.create_line(
            self.last_point.x, self.last_point.y,
            current_point.x, current_point.y,
            fill="black", width=2, capstyle=tk.ROUND, smooth=True
        )
        
        # 현재 지점을 다음 선의 시작점으로 업데이트
        self.last_point = current_point

    def on_release(self, event):
        # 마우스를 떼면 추적 종료
        self.last_point = None

# 실행
root = tk.Tk()
app = FreeLineDrawer(root)
root.mainloop()