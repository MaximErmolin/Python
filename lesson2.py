# Python_2 HW_2
# Arithmetic

print ("Arithmetic")

import math

item_1 = int(49) #  1. Создать переменную item_1 типа integer.
item_2 = int(11) #  2. Создать переменную item_2 типа integer.
result_sum = item_1 + item_2 #  3. Создать переменную result_sum в которой вы суммируете item_1 и item_2.
print (result_sum) #  4. Вывести result_sum в консоль.
result_subtr = int
if item_1 > item_2:
 result_subtr = item_1 - item_2
else:
 result_subtr = item_2 - item_1 #  5. Создать переменную result_subtr в которой вы вычитаете большую по значению переменную из меньшей по значению.
print(result_subtr) #  6. Вывести result_subtr в консоль.
result_multi = item_1 * item_2 #  7. Создать переменную result_multi в которой вы умножаете item_1 на item_2.
print(result_multi) #  8. Вывести result_multi в консоль.
result_exp = item_1 ** item_2 #  9. Создать переменную result_exp в которой вы item_1 возводите в степень item_2.
print (result_exp) #  10. Вывести result_exp в консоль.
result_m_exp = math.pow(item_1, item_2)#  11. Создать переменную result_m_exp в которой вы item_1 возводите в степень item_2 используя библиотеку math.
print (result_m_exp) #  12. Вывести result_m_exp в консоль.
result_s_root = item_1 ** (0.5) #  13. Создать переменную result_s_root в которой вы найдёте квадратный корень любой из переменной item
print (result_s_root)#  14. Вывести result_s_root в консоль.
result_m_s_root = math.sqrt(item_1) #  15. Создать переменную result_m_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math.
print (result_m_s_root) #  16. Вывести result_m_s_root в консоль.
result_mp_s_root = math.pow(item_1, 0.5)#  17. Создать переменную result_mp_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math используя метод pow.
print (result_mp_s_root) #  18. Вывести result_mp_s_root в консоль.
item_1 = 999 #  19. Присвоить переменной item_1 odd значение
item_2 = 4 #  20. Присвоить переменной item_2 even значение
result_division = item_1 / item_2 #  21. Создать переменную result_division в которой вы разделите item_1 на item_2.
print (result_division)#  22. Вывести result_division в консоль.
result_m_floor = math.floor(result_division) #  23. Создать переменную result_m_floor и result_division округлить до ближайшего целого меньшего чем result_division.
print (result_m_floor)#  24. Вывести result_m_floor в консоль.
result_m_ceil = math.ceil(result_division)#  25. Создать переменную result_m_ceil и result_division округлить до ближайшего целого большего чем result_division.
print (result_m_ceil) #  26. Вывести result_m_ceil в консоль.
result_int = int(result_division)#  27. Создать переменную result_int и result_division округлить до ближайшего целого через явное приведение.
print (result_int) #  28. Вывести result_int в консоль.
result_no_division_loss = int(item_1 / item_2) #  29. Создать переменную result_no_division_loss в которой вы разделите item_1 на item_2 без остатка.
print (result_no_division_loss) #  30. Вывести result_no_division_loss в консоль.
result_division_loss = item_1 / item_2 - result_no_division_loss#  31. Создать переменную result_division_loss в которой вы найдёте остаток от деления item_1 на item_2.
print (result_division_loss)#  32. Вывести result_division_loss в консоль.

# Дальше Будет Реализация Через Арифметические Действия С присваиванием
print("Дальше Будет Реализация Через Арифметические Действия С присваиванием")

item_3 = int(4) #  33. Создать переменную item_3 и присвоить ей целое число
item_3 = item_3 + 10 #  34. Прибавить 10 к item_3 с присвоением.
print(item_3) #  35. Вывести item_3 в консоль.
item_3 = item_3 - 5 #  36. Отнять 5 от item_3 с присвоением.
print(item_3) #  37. Вывести item_3 в консоль.
item_3 = item_3 * 3 #  38. Умножить item_3 на 3 с присвоением.
print(item_3) #  39. Вывести item_3 в консоль.
item_3 = item_3 / 3 #  40. Разделить item_3 на 2 с присвоением.
print(item_3) #  41. Вывести item_3 в консоль.
item_3 = item_3 ** 2 #  42. Возвести в степень 2 item_3 с присвоением.
print(item_3) #  43. Вывести item_3 в консоль.
item_3 = item_3 ** (0.5) #  44. Найти квадратный корень item_3 с присвоением.
print(item_3) #  45. Вывести item_3 в консоль.
item_3 = item_3 / 64 #  46. Присвоить остаток от деления item_3
item_3 = item_3 - int(item_3)
print(item_3) #  47. Вывести item_3 в консоль.
#
# Boolean
print("Boolean")
#
b_item_t = True #  48. Создать переменную b_item_t и присвоить True
b_item_f = False #  49. Создать переменную b_item_f и присвоить False
b_item_relult_sum = b_item_t + b_item_f #  50. Создать переменную b_item_relult_sum и присвоить сумму b_item_t и b_item_f
print(bool(b_item_relult_sum)) #  51. Вывести b_item_relult_sum в консоль.
b_item_relult_subtr = b_item_t - b_item_f #  52. Создать переменную b_item_relult_subtr и присвоить разницу b_item_t и b_item_f
print(bool(b_item_relult_subtr)) #  53. Вывести b_item_relult_subtr в консоль.
b_item_relult_multi = b_item_t * b_item_f#  54. Создать переменную b_item_relult_multi и присвоить умножение b_item_t и b_item_f
print(bool(b_item_relult_multi)) #  55. Вывести b_item_relult_multi в консоль.
b_item_relult_division = bool(b_item_t) / bool(b_item_f) #  56. Создать переменную b_item_relult_division и присвоить деление b_item_t и b_item_f
print(bool(b_item_relult_division)) #  57. Вывести b_item_relult_division в консоль. (Получить ошибку)
b_item_1_int = int(b_item_t) #  58. Создать переменную b_item_1_int и присвоить явное приведение b_item_t к int
print(b_item_1_int) #  59. Вывести b_item_1_int в консоль.
b_item_2_int = int(b_item_f) #  60. Создать переменную b_item_2_int и присвоить явное приведение b_item_2 к int
print(b_item_2_int) #  61. Вывести b_item_2_int в консоль.
#











# Далее записанно все что мы писали на занятии
# import math
#
#
# i_1 = 0
# I_2 = 3
# i_2 = 10
# i_3 = 7
# i_4 = 22
# i_5 = 159
#
#
#
# s_1 = i_2 + i_4
# m_1 = i_2 - i_3
# u_1 = i_3 * i_2
# d_1 = i_5 / I_2
# sq = i_3 ** I_2
# ii = i_2 + I_2
# do_1 = i_4 // i_3
# dop1 = i_4 % i_3
# dd = (i_3 + i_2) * (i_1 + i_2)
# sqr = 49
# mm = math.sqrt(sqr)
#
# print('s_1 = ', s_1)
# print('m_1 = ', m_1)
# print('u_1 = ', u_1)
# print('d_1 = ', d_1, type(d_1))
# print('sq = ', sq, type(sq))
# print('ii = ', ii)
# print('do_1 = ', do_1, type(do_1))
# print('dop1 = ', dop1, type(dop1))
# print('dd = ', dd, type(dd))
# print('mm = ', mm)