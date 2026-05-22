i_numbers = int(input("정수 입력 >> "))

""" if i_numbers % 2 == 0:
    print("number of {} is even number".format(i_numbers))
else:
    print("number of {} is odd number".format(i_numbers))
 """
string_text = ["1","2","3","4","5"]
print("::".join(string_text))

# 응용
if i_numbers % 2 == 0:
    print("\n".join([
        "입력한 문자열은 {}이고, ",
        "{}은(는) even numer입니다."
    ]).format(i_numbers,i_numbers))
else:
    print("\n".join([
        "입력한 문자열은 {}이고, ",
        "{}은(는) odd numer입니다."
    ]).format(i_numbers,i_numbers))