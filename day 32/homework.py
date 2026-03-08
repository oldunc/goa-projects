# .append() ფუნქცია ამატებს ელემენტს სიის ბოლოში

# .insert() ფუნქცია ამატებს ელემენტს სიის კონკრეტულ ინდექსზე (ადგილზე)

# .pop() ფუნქცია შლის სიის ელემენტს (ნაგულისხმევად ბოლო ელემენტს)

my_list = [10, 20, 30, 40]

print(len(my_list))


numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

print(numbers)


colors = ["red", "green", "blue", "yellow", "purple"]

colors.pop()

print(colors)


animals = ["dog", "cat", "elephant", "lion"]

animals.insert(1, "monkey")

print(animals)

students = []

for i in range(3):
    name = input("Enter student name: ")
    students.append(name)

students.insert(0, "Teacher")
students.pop()                  

print(len(students))            
print(students)  