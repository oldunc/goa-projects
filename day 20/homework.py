# 2) შექმენით ცვლადი სადაც შეინახავთ ინტეჯერ ტიპის მონაცემს, შემდეგ შეამოწმეთ თუ ეს რიცხვი რომელიც ცვლადში გაქვთ შენახული მეტია 10 ზე დაპრინტეთ "more than 10" სხვა შემთხვებაში დაპრინტეთ "less than 10"
# num = int(input("enter ur age: "))
# if num > 10:
#     print("more than 10")
# else:
#     print("less than 10")


# # 3) მომხმარებელს შემოაყვანინეთ რიცხვი, შემდეგ შეამოწმეთ თუ ეს რიცხვი უდრის 15 ს დაუპრინტეთ "equal to 15" სხვა შემთხვევაში დაუპრინტეთ "not equal to 15"
# num = int(input("enter ur age: "))
# if num = 15:
#     print("equal to 15")
# else:
#     print("not equal to 15")

# 4) მომხმარებელს შემოატანეთ სტრინგი. შენი დავალებაა შეამოწმო, თუ მომხამრებლის მიერ შემოყვანილი სტრინგი არის group84 დაუპრინტეთ 'you are correct" სხვა შემთხვევაში დაუპრინტეთ "you are wrong"
# gr = "group84"
# num = str(input("enter ur word"))
# if num == gr:
#     print("you are correct")
# else:
#     print("you are not correct")

# 5) დაატრიალეთ for ციკლი 50 დან 100 მდე 5 ის გამოტოვებით

# for i in range(50 , 100 , 5):
#     print(i)
# # 6) for ციკლის დახმარებით გამოიტანეთ ტერმინალში თქვენი სახელი და გვარი
# i = "giorgi barbakadze"
# l =  0
# for i in i:
#     print(str( l) + i)
#     l += 1
# # 7) while loop ის დახმარებით ტერმინალში გამოიტანეთ რიცხვები 20 დან 50 მდე
# num1 = 20
# while num1 < 50:
#     print(num1)
#     num1 += 1

# # 8) დაბეჭდეთ 0-დან 100-მდე ყველა რიცხვი. (for-თაც და while-თაც)
# num2 = 0
# while num2 < 100:
#     print(num2)
#     num2 += 1

# for i in range(1,100):
#     print(i)
# # 9) დაბეჭდეთ 0-დან 100-ის ჩათვლით ყველა რიცხვი. (for-თაც და while-თაც)
# num3 = 0
# while num3 <= 100:
#     print(num3)
#     num3 += 1

# for i in range(1,101):
#     print(i)
# # 10) დაბეჭდეთ 10-დან 20-მდე ყველე რიცხვი (for-თაც და while-თაც)
# num4 = 10
# while num4 < 20:
#     print(num4)
#     num4 += 1

# for i in range(10,20):
#     print(i)
# # 11) დაბეჭდეთ 100-დან 200-ის ჩათვლით ყოველი მე-5 რიცხვი (for-თაც და while-თაც)
# num5 = 100
# while num5 < 200:
#     print(num5)
#     num4 += 5

# for i in range(100,200,5):
#     print(i)
# # 12) დაბეჭდეთ 10-დან 0-ის ჩათვლით ყველა რიცხვი (for-თაც და while-თაც)
# num6 = 10
# while num6 < 0:
#     print(num6)
#     num6 -= 1

# for i in range(10,0):
#     print(i)
# # 13) მომხმარებელს შემოაყვანიეთ რაიმე რიცხვი(მთელი/ათწილადი); შეამოწმეთ ეს რიცხვი - 
# # --> თუ დადებითია დაპრინტეთ 'ეს რიცხვი დადებითი რიცხვია'
# # --> თუ უარყოფითია დაპრინტეთ 'ეს რიცხვი უარყოფითი რიცხვია'
# # --> თუ ნულია დაპრინტეთ 'ეს რიცხვი ნულია'
# b = int(input("enter ur number"))
# if b > 18:
#     print("dadebitia es ricxvi")
# elif b <= 0:
#     print("es ricxvi nolia")
# else:
#     print("es ricxvi uaryopitia")
# # 14) მომხმარებელს შემოაყვანიეთ თავისი ასაკი:
# # 0–12 წლის ასაკი --> დაპრინტეთ 'ბავშვი ხარ'
# # 13-19 წლის ასაკი --> დაპრინტეთ 'მოზარდი/თინეიჯერი ხარ'
# # 20-64 წლის ასაკი --> დაპრინტეთ 'ზრდასრული ხართ'
# # 65-120 წლის ასაკი --> დაპრინტეთ 'ხანში შესული ხართ'
# # 120 და ზემოთ --> დაპრინტეთ 'გურუ ან ჯადოქარი'
# # თუ შემოყვანილი ასაკი უარყოფითია --> დაპრინტეთ 'არასწორი ინფო'
# age = int(input("seiyvane seni asaki: "))

# if age < 0:
#     print("araswori informacia")
# elif 0 <= age <= 12:
#     print("bavsvi xar")
# elif 13 <= age <= 19:
#     print("mozardi an tineijeri xar")
# elif 20 <= age <= 64:
#     print("zrdasruli xar")
# elif 65<= age <= 120:
#     print("xansi sesuli xar")
# else:
#     print("guru an jadocari")
# # 15) მომხმარებელს შემოატანიეთ სამი რიცხვი(მთელი/ათწილადი) და ამ სამი რიცხვთაგან დაბეჭდეთ უდიდესი
# # ?
# # 16) შემოატანიეთ მომხმარებელს რიცხვი 1-დან 7-ჩათვლით
# # თუ 1 --> დაპრინტეთ 'ორშაბათი'
# # თუ 2 --> დაპრინტეთ 'სამშაბათი'
# # თუ 3 --> დაპრინტეთ 'ოთხშაბათი'
# # თუ 4 --> დაპრინტეთ 'ხუთშაბათი'
# # თუ 5 --> დაპრინტეთ 'პარასკევი' 
# # თუ 6 --> დაპრინტეთ 'შაბათი'
# # თუ 7 --> დაპრინტეთ 'კვირა' 
# # სხვა დანარჩენი --> 'არ ვიცი ეგ რა დღეა'
# e = int(input("enter ur number but only from 1 to 7"))
# if e <= 1:
#     print("orsabati")
# elif e <= 2:
#     print("samsabati")
# elif e <= 2:
#     print("samsabati")
# elif e <= 3:
#     print("otxsabati")
# elif e <= 4:
#     print("xutsabati")
# elif e <= 5:
#     print("paraskevi")
# elif e <= 6:
#     print("sabati")
# elif e <= 7:
#     print("kvira")
# 17) მომხმარებელს შემოატანინეთ რიცხვი, თუ ის მეტია 50-ზე დაბეჭდეთ ეს რიცხვი გამრავლებული 5-ზე, სხვა შემთხვევაში დაბეჭდეთ ეს რიცხვი კვადრატში
# l = int(input("enter ur num: "))
# if l > 50:
#     print(l*5)
# else:
#     print(l*l)    
# # 18) მომხმარებელს შემოატანინეთ პაროლი თუ ის უდრის მაგალითად "goa123"-ს დაბეჭდეთ "Password is correct!", სხვა შემთხვევაში დაბეჭდეთ "Incorrect password!"
# password = 123123
# h = int(input("enter ur num: "))
# if h <= password:
#     print("Password is correct!")
# else:
#     print("Incorrect password!")
# 19) მომხმარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ 1-დან შემოტანილის ჩათვლით ყველა რიცხვის ჯამი

# f = int(input("enter ur num: "))
# the = 0
# for i in range(1 , f + 1):
#     the += 1
# print(the)
arra = ["helo", 12, 1.1]
print(arra)

