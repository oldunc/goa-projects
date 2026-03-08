# 1) შექმენით რამდენიმე ელემენტიანი სია და დაბეჭდეთ ამ სიის სიგრძე შესაბამისი ფუნქციის მეშვეობით
arr = ["hello" , "bye" , "goodnight"]
print(len(arr))
# 2) შექმენით სახელების სია (minimum 5 elements), მომხმარებელს input ფუნქციის მეშვეობით შემოატანინეთ სახელი და ჩაამატეთ მომხმარებლის შემოტანილი მნიშვნელობა სიის ბოლოში. გამოიყენეთ შესაბამისი ფუნქცია.
arr1 = ["gio" , "dati" , "gabu" , "davit" , "barbare"]
name = input("enter you name: ")
arr1.append(name)
print(arr1)

# 3) insert ფუნქციის მეშვეობით ჩაამატეთ 3-ე index-ზე ახალი სახელი "Tarieli"
arr1.insert(3, "tarieli")
print(arr1)
# 4) pop ფუნქციის მეშვეობით სიაში წაშალეთ მე-4-ე index-ზე მყოფი მნიშვნელობა სიიდან
arr1.pop(4)
print(arr1)
# 5) remove ფუნქციის მეშვეობით წაშალეთ 1 ნებისმიერი სახელი თქვენი წინასწარ გამზადებული სიიდან.
arr1.remove("gio")
print(arr1)
# 6) მომხმარებელს შემოატანინეთ სახელი და შეამოწმეთ თუ რომელ index-ზე დგას ელემენტი თუა სიაში რა თქმა უნდა, თუ არაა სიაში მაშინ დაუბეჭდეთ რომ "not index in list"
names = ["giorgi", "nino", "luka", "ana"]

user_name = input("შეიყვანე სახელი: ")

if user_name in names:
    print(names.index(user_name))
else:
    print("not index in list")

# 7) შექმენით 5 რიცხვიანი ელემენტიანი სია. for ციკლის მეშვეობით მომხმარებელს შემოატანინეთ კიდევ 5 რიცხვი და თითოეული შემოტანილი რიცხვი .append ფუნქციის მეშვეობით ჩაამატეთ არსებულ სიაში. საბოლოოდ დაბეჭდეთ ეს სია.
numbers = [1, 2, 3, 4, 5]

for i in range(5):
    num = int(input("შეიყვანე რიცხვი: "))
    numbers.append(num)

print(numbers)
