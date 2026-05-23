# 8번 up, down()를 이용하여 선 긋기를 멈추고 새로운 곳에 시작하는 코드 구현
import turtle as t

t.shape("turtle")

#일단 가로줄 긋기
t.forward(100)

#up() 함수로 펜 들어올리기 & 위로 올라가기
t.up()
t.goto(0,200)

#down() 함수를 불러서 펜을 내린 뒤 다시 선 긋기
t.down()
t.forward(100)

#그림 그리는 것이 끝날 때까지 유지
t.done()