class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    def cal_avg(self):
        return (self.korean + self.math + self.english + self.science) / 4
    def getName(self):
        return self.name

Students = [
    Student("ksm", 80, 75, 60, 90),
    Student("fgd", 50, 40,  30 , 70),
    Student("lice", 40, 50 , 70, 88),
    Student("ruin", 100, 98, 88, 89),
    Student("adel", 100, 99, 79, 91)
]
#Students.sort(key=lambda s: s.cal_avg() , reverse=True)
# 위의 lamda를 포함한 sort가 아래의 하드코딩과 동일한 결과를 냄.
for i in range(len(Students)): # C++, Java 와는 달리 len(target)으로 ~까지 반복함. 즉, size(), length()가 아님.
    max_index = i
    for j in range(i + 1 , len(Students)):
        if Students[j].cal_avg() > Students[max_index].cal_avg():
            max_index = j
    Students[i], Students[max_index] = Students[max_index], Students[i] # temp 를 하지 않아도 변경이 가능함.

for i in Students:
    print(f"{i.getName()} {i.cal_avg()}") # 문자열 출력 방식에 소수 및 정수를 출력할 때 + 안되는 경우 있어서, f-string, format 이용할 것.


    