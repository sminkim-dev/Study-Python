#text = int(input("정수만을 입력하고 공백으로 구분한다. >> ").split())

flist = [8,4,3,2,9,10]
up_arr = []
down_arr = []

def downToUp():
    for i in range(len(flist)):
        for a in range(len(flist) - 1):
            if flist[a] > flist[a+1]:
                tmp = flist[a]
                flist[a] = flist[a+1]
                flist[a+1] = tmp
def upToDown():
    for i in range(len(flist)):
        for a in range(len(flist) - 1):
            if flist[a] < flist[a+1]:
                tmp = flist[a+1]
                flist[a+1] = flist[a]
                flist[a] = tmp
select = int(input("select ' 1 (down to up)' or ' 2 (up to down)' >> "))
if select == 1:
    downToUp()
else:
    upToDown()
print(flist)
