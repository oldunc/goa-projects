# 1) მომხმარებელს შემოატანინეთ სახელი და დაბეჭდეთ ის uppercase-ში.
name = input("enter ur name: ")
print(name.upper())

# 2) მომხმარებელს შემოატანინეთ სახელი დაბეჭდეთ lowercase-ში.
print(name.lower())

# 3) მომხმარებელს შემოატანინეთ სახელი და დაბეჭდეთ ისე, რომ მისი პირველი ასო იყოს uppercase-ში დაწერილი, ხოლო დანარჩენი lowercase-ში.
print(name.capitalize())

# 4) შექმენით ცვლადი, სადაც შეინახავთ ნებისმიერ სიტყვას. მომხმარებელს შემოატანინეთ სიმბოლო, რომლის ინდექსიც უნდა იპოვოთ სთრინგში და დუბეჭდოთ შემდეგი ფორმატით "a - 0"
nameg = "gamarjoba"
choose = input("enter ur symbol: ")
povna = nameg.find(choose)
if povna == -1:
    print("the symbol is not in the word")
else:
    print(choose, "-", povna)


# თუ მომხმარებელმა ჩაწერა ისეთი სიმბოლო, რომელიც არ არის სიტყვაში. დაუბეჭდეთ რომ "This symbol is not in word"

# 5) შექმენით ცვლადი და შიგნით შეინახეთ თქვენი სახელი, გაიგეთ თქვენი სახლის სიგრძე შესაბამისი ფუნქციის მეშვეობით.
name = "Giorgi"
length = len(name)
print(length)

# 6) მომხმარებელს შემოატანინეთ სახელი და შეამოწმეთ იწყება თუ რა იგი ასო-ბგერა "g"-თი.
name = input("Enter your name: ")

if name.startswith("g"):
    print("The name starts with the letter g")
else:
    print("The name does not start with the letter g")
# 7) მომხმარებელს შემოატანინეთ სახელი და შეამოწმეთ მთავრდება თუ რა იგი ასო-ბგერა "l"-თი
name = input("Enter your name: ")

if name.endswith("l"):
    print("The name ends with the letter l")
else:
    print("The name does not end with the letter l")