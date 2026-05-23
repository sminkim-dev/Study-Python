symbol_list = []
sym = input("기호를 입력하시오 > ")
symbol_list.append(sym[0])
symbol_list.append(sym[-1])
information = input("문자열을 입력하시오 > ")
result_Value = symbol_list[0] + information + symbol_list[1]
print(result_Value)