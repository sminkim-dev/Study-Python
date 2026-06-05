from PIL import Image , ImageTk
import tkinter as tk
import numpy as np

img = Image.open("/Users/ruin/Dev/Python/Univ/chap_12/haku.jpg.webp")

# console 에 image 정보 출력
print(img.size, img.mode, img.format)

# 윈도우 생성하고 윈도우 안에 캔버스 생성
window = tk.Tk()
canvas = tk.Canvas(window, width=img.size[0], height=img.size[1])
canvas.pack()

# im_array = np.asarray(img) #valueError :  Assignment destination is read-only
im_array = np.asarray(img).copy()
print(len(im_array))

for i in range(len(im_array)):
    for j in range(len(im_array[0])):
        # 흑백느낌으로 색을 낮춘 것.
        # mean = (int(im_array[i,j,0]) + int(im_array[i,j,1]) + int(im_array[i,j,2])) / 3
        # im_array[i,j,0] = im_array[i,j,1] = im_array[i,j,2] = mean

        # int() 를 안하면 overflow로 인해 색이 밝아지지 않고, 꺠짐.
        # 그 이유는 uint8로 부호 없는 정수의 8비트 값을 가지는데 8비트면 255까지만 값을 가짐. 근데 255를 넘어가니 overflow가 일어난 것임.
        r = int(im_array[i,j,0]) + 50
        g = int(im_array[i,j,1]) + 50
        b = int(im_array[i,j,2]) + 50

        if r > 255:im_array[i,j,0] = 255
        else: im_array[i,j,0] = r
        if g > 255:im_array[i,j,1] = 255
        else: im_array[i,j,1] = g
        if b > 255: im_array[i,j,2] = 255
        else: im_array[i,j,2] = b

print("좌측 상단 첫 번째 픽셀의 RGB 값 : ", im_array[0,0])
img_mean = Image.fromarray(im_array)
tk_img = ImageTk.PhotoImage(img_mean)

canvas.create_image(0,0, anchor=tk.NW, image=tk_img)

window.mainloop()