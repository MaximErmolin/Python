# Python HW 4 Cycles
#
# Циклы While
count = 0 # Создать переменную count со значением 0
range_count = 10 # Создать переменную range_count со значением 10
for_count = 0 # Создать переменную for_count со значением 0
run = True # Создать переменную run  со значением True
#
#Сделать цикл while который будет работать пока run
while run:
  print("5.1Hello Cycle") #     5.1 Выводить в консоль “Hello Cycle”
#
  print("6.1Step =", count)  # 6.1 Выводить в консоль (“Step =”, count)
  break

# Сделать цикл while который будет работать пока run
 # Тело цикла:
while run:#     6.2 Переменной count прибавлять 1 с присвоением.
     count += 1
     break

# Сделать цикл while который будет работать пока count < range_count
while count < range_count:
     print("7.1Step =", count) # Тело цикла: 7.1 Выводить в консоль (“Step =”, count)
     count += 1 # 7.2Переменной count прибавлять 1 с присвоением.

# Сделать цикл while который будет работать пока count < range_count
count = 0
while count < range_count:
     print("8.1Step =", count) # Тело цикла: 8.1 Выводить в консоль (“Step =”, count)
     count += 1 #     8.2 Переменной count прибавлять 1 с присвоением.
     if count == 3:
        print("8.3Step =", count, "If body")#     8.3 Сделать if с условием, если count равен 3 то выводить в консоль (“Step =”, count, ‘If body’)

# Сделать цикл while который будет работать пока run
count = 0
while run: #run:
 # Тело цикла:
     print("9.1Step =", count)#     9.1 Выводить в консоль (“Step =”, count)
     count += 1 #     9.2 Переменной count прибавлять 1 с присвоением.
     if count == range_count:
          #  9.2 Сделать if с условием, если count равен range_count то цикл остановится.
      print("9.3     Stop =", count)  #     9.3 В теле if вывести в консоль (“STOP”, count)
      break
#
# Цилы For

# Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от for_count  до range_count
for item in range(for_count, range_count):
 print("10.1Step =", item)# Тело цикла: # 10.1 Вывести в консоль (‘Step =’, item)


# Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до 30
for item in range(0, 30):
# Тело цикла:
 print("11.1Step =", item)# 11.1 Вывести в консоль (‘Step =’, item)
 if item == 5:
      print("    11.2Item =", item) # 11.2 Сделать if с условием, если item равен  5, то вывести в консоль (‘Item =’, item).
 if item == 10:
    print("    11.3Item =", item) # 11.3 Сделать if с условием, если item равен  10, то вывести в консоль (‘Item =’, item).
 if item < 4:
    print("    11.4Item <", item) # 11.4 Сделать if с условием, если item меньше 4, то вывести в консоль (‘Item <’, item).
 if item >= 27:
    print("    11.5Item >=", item) # 11.5 Сделать if с условием, если item больше или равно 27, то вывести в консоль (‘Item >=’, item).
#
#
# Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до range_count +1
# Тело цикла:
for item in range(0, range_count +1):
 print("12.1Item =", item)# 12.1 Вывести в консоль (‘Step =’, item)
 if item == 7: # 12.2 Сделать if с условием, если item равен  7.
  inner_count = 0#      - В теле if создать переменную inner_count равную 0
  print("-- inner_count =", inner_count)#      - В теле if вывести в консоль (‘-- inner_count =’, inner_count)
  for inner_item in range(0, item):#      - В теле if сделать ещё одни цикл for с переменной inner_item который будет работать пока счётчик range досчитает от 0 до item.
# #     Тело внутреннего цикла For:
   print("-------- Inner_Step =", inner_item)#         -- Вывести в консоль (‘-------- Inner_Step =’, inner_item)
   if inner_item == 5:
    inner_count = inner_item#         -- Сделать if если inner_item равен 5, то в inner_count присвоить inner_item.
   print("-- inner_count =", inner_count)#     - За пределами тела предыдущего цикла вывести в консоль (‘-- inner_count =’, inner_count)
