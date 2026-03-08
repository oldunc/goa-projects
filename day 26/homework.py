# # 1) mteli ricxvebis sia

# numbers = [3, 7, 2, 9, 4]

# # 1.1 yvela elementis dabedchdva
# for num in numbers:
#     print(num)

# # 1.2 elementebis jami
# total = 0
# for num in numbers:
#     total += num
# print("jami:", total)


# # 2) lugi ricxvebis raodenoba

# numbers = [1, 2, 4, 7, 10, 13]
# count_even = 0

# for num in numbers:
#     if num % 2 == 0:
#         count_even += 1

# print("lugi ricxvebis raodenoba:", count_even)


# # 3) umciresi da udidesi elementi

# numbers = [5, 2, 9, 1, 7]
# min_num = numbers[0]
# max_num = numbers[0]

# for num in numbers:
#     if num < min_num:
#         min_num = num
#     if num > max_num:
#         max_num = num

# print("umciresi:", min_num)
# print("udidesi:", max_num)


# # 4) mxolod kenti ricxvebis dabedchdva

# numbers = [1, 2, 3, 4, 5, 6]

# for num in numbers:
#     if num % 2 == 0:
#         print(num)

#     print((5 + 5 + 5 + 5)/4)
# # 5) ricxvebis sheyvana 0-mde da jamis datvla

# total = 0
# while True:
#     num = int(input("sheiyvanet ricxvi: "))
#     if num == 0:
#         break
#     total += num

# print("jami:", total)


# # 6) ricxvebis sheyvana uaryofitamde

# while True:
#     num = int(input("sheiyvanet ricxvi: "))
#     if num < 0:
#         break


# # 7) ricxvebis sheyvana 5-ze gayofadamde

# while True:
#     num = int(input("sheiyvanet ricxvi: "))
#     if num % 5 == 0:
#         break


# # 8) ricxvebis sheyvana lugamde da mcdelobebis datvla

# attempts = 0
# while True:
#     num = int(input("sheiyvanet ricxvi: "))
#     attempts += 1
#     if num % 2 == 0:
#         break

# print("mcdelobebis raodenoba:", attempts)


# # 9) ricxvebis sheyvana kentamde

# while True:
#     num = int(input("sheiyvanet ricxvi: "))
#     if num % 2 == 0:
#         break


# # 10) continue da break gamoyeneba

# while True:
#     num = int(input("sheiyvanet ricxvi: "))

#     if num < 0:
#         continue
#     if num == 0:
#         break

#     print("migebuli ricxvi:", num)


# # 11) ricxvebis sheyvana 100-mde, uaryofitebis gamotovebit

# while True:
#     num = int(input("sheiyvanet ricxvi: "))

#     if num < 0:
#         continue
#     if num == 100:
#         break

#     print("migebuli ricxvi:", num)






num = 1
while num <= 30:
   print(str(num) + " ვაშლი")
   num += 1
