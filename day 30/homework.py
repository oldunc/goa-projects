# 2) კომენტარებით ახსენით თუ რას აკეთებს .upper(); .lower(); .capitalize(); .find() ფუნქციები.
# aqcevs did asoebat 
text = "hello"
print(text.upper())  
# aqcevs patara asoebad
text = "HELLO"
print(text.lower()) 
# aqcevs pirvel asos didad
text = "hELLO"
print(text.capitalize())
# pulobs mititebuls asos
text = "python"
print(text.find("t"))
# 3) მომხმარებელს შემოატანინეთ წინადადება და დაბეჭდეთ იგი პატარა ასოებით.
sentence = input("Enter a sentence: ")
print(sentence.lower())

# 4) მომხმარებელს შემოატანინეთ ელფოსტის მისამართი და გადაამოწმეთ შეიცავს თუ არა '@' სიმბოლოს, შედეგი კი დაბეჭდეთ დიდი ასოებით.
email = input("Enter your email: ")

if "@" in email:
    print("EMAIL CONTAINS @".upper())
else:
    print("EMAIL DOES NOT CONTAIN @".upper())

# 5) მომხმარებელს შემოატანინეთ წიგნის დასახელება და შედეგი დაბეჭდეთ სათაურის სტილში.
book_title = input("Enter a book title: ")
print(book_title.title())

# 6) მომხმარებელს შემოატანინეთ წინადადება და სიმბოლო. თქვენი დავალებაა დაითვალოთ რამდენჯერ გვხვდება ეს სიმბოლო წინადადებაში.
sentence = input("Enter a sentence: ")
charecter = input("Enter a character: ")

count = sentence.count(charecter)
print(count)

# 7) მომხმარებელს შემოატანინეთ სიტყვა და შეამოწმეთ, არის თუ არა იგი დიდი ასოებით, თუ კი — დაბეჭდე "სიტყვა უკვე დიდია!", თუ არა — გადააქციე და დაბეჭდე.

# ?