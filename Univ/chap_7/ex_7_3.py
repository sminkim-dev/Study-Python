data = {"PI" : 3.14159265358979}
radius = 5
def circleArea(radius):
    area = radius**2 * data["PI"]
    return area
def cicleCirnumfenrence(radius):
    c_len = 2 * data["PI"] * radius
    return c_len
print(f"반지름이 {radius}인 원의 면적은 {circleArea(radius):.20f}")
print(f"반지름이 {radius}인 원의 둘레는 {cicleCirnumfenrence(radius):.20f}")