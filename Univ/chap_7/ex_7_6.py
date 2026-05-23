class GradeManager:
    def __init__(self, score):
        self.score = score
    def getGrade(self):
        if 90 <= self.score: return "A"
        elif 80 <= self.score: return "B"
        elif 70 <= self.score: return "C"
        else:return "F"

score = int(input("점수를 입력 >> "))
manager = GradeManager(score)
print(f"당신의 학점은 {manager.getGrade()}학점입니다.")