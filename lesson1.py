# Python. HW_1:
variable_String = str("s1") #1) Создать переменную типа String
variable_Integer = int(1) # 2) Создать переменную типа Integer
variable_Float = float(2.8)# 3) Создать переменную типа Float
variable_Bytes = bytes(1)# 4) Создать переменную типа Bytes
variable_List = [1, 33, 6, 9]# 5) Создать переменную типа List
variable_Tuple = (36.6, 'Normal', None, False)# 6) Создать переменную типа Tuple
variable_Set = {1, 2, 3, 4, 5, 6} # 7) Создать переменную типа Set
variable_Frozen_set = frozenset(variable_List)# 8. Создать переменную типа Frozen set
variable_Dict = {'dict': 1, 'dictionary': 2}# 9) Создать переменную типа Dict
print("переменная типа String:", type(variable_String))# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print("переменная типа Integer:", type(variable_Integer))#
print("переменная типа Float:", type(variable_Float))
print("переменная типа Bytes:", type(variable_Bytes))
print("переменная типа List:", type(variable_List))
print("переменная типа Tuple:", type(variable_Tuple))
print("переменная типа Set:", type(variable_Set))
print("переменная типа Frozen set:", type(variable_Frozen_set))
print("переменная типа Dict:", type(variable_Dict))

StringForSum1 = str("sum1")
StringForSum2 = str("sum2")
StringForSum1Sum2 = StringForSum1 + StringForSum2
print("переменная в которой суммируются String:",StringForSum1Sum2)
# 11) Создать 2 переменные String, создать переменную в которой суммируете эти переменные. Вывести в консоль.

IntForSum1 = int(2)
IntForSum2 = int(1)
IntForSum1Sum2 = IntForSum1 + IntForSum2
print("переменная в которой суммируются Integer:",IntForSum1Sum2 )
# 12) Создать 2 переменные Integer, создать переменную в которой суммируете эти переменные. Вывести в консоль.

IntForDiv1 = int(28)
IntForDiv2 = int(3)
IntForDiv1Div2 = IntForDiv1 / IntForDiv2
print("переменная в которой делятся Integer:", IntForDiv1Div2)
# 13) Создать переменную в которой Разделите эти переменные Int. Вывести в консоль.

IntForMul1 = int(5)
IntForMul2 = int(4)
IntForMul1Mul2 = IntForMul1 * IntForMul2
print("переменная в которой умножаются Integer:", IntForMul1Mul2)
# 14) Создать переменную в которой Умножите эти переменные Int. Вывести в консоль.

IntForDivF1DivF2 = IntForDiv1 // IntForDiv2
print("переменная в которой делятся Integer без остатка:", IntForDivF1DivF2)
# 15) Создать переменную в которой Разделите без остатка эти переменные Int. Вывести в консоль.

IntForDiv1Div2eDivF1DivF2 = IntForDiv1Div2 - IntForDivF1DivF2
print("переменная в которой надо присвоить остаток от деления этих переменных Int:", IntForDiv1Div2eDivF1DivF2)
# 16) Создать переменную в которой надо присвоить остаток от деления этих переменные Int. Вывести в консоль.

arrr = (7 + 12) **3 + 7 * 4 - 44 / 2 **4
print(arrr)
# 17) (7 + 12)  3 + 7 * 4 - 44 / 2  4 расставить точки так чтобы получилось 6884.25. Вывести в консоль.





# Здесь записанно все то что мы вводили на занятии:
# a = 5
# b = 2
# c = a + b
#
# print('C = ', c)
#
# d = c + 10
# print("D = ", d)
#
# if d > 10:
#
#         print ('D > 10')
#
# print('Next_func')
#
# a = 'Elochka'
# b = ' Zelenoya'
#
# c = a + b
# print(c)
#
# result = a + str(d)
#
# print(result)
#
# print(a*d)
#
# print(a[1]*d)
