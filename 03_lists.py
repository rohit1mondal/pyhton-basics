marks = [85, 97, 45, 76,59]

'''
print(marks)
print(len(marks))
print(marks[0])
print(marks[1])
'''


list = [2,4,5]
list.append(9)
list.sort()
# print(list)
# list.reverse()
# list.insert(2,7)
# print(list)
# list.remove(5)
# list.pop(2)
# print(list)

# tuples

tup = (2,3,4,8)
tup1 = (1,) # for single element tuple
print(tup)
print(type(tup))
print(tup[1:3])

#1 write a program to ask the user to enter names of their 3 favorite movies & store them in a list.

# movies = []
# movies.append(input("Enter 1st movie: "))
# movies.append(input("Enter 2nd movie: "))
# movies.append(input("Enter 3rd movie: "))

# print(movies)

#2 Write a program to check if a list contains a palindrome of elements or not.
list1 = [1,2,3,2,1]

copy_list1 = list1.copy()
copy_list1.reverse()
if (list1 == copy_list1):
    print("palindrome")
else:
    print("not a palindrome")

#3 write a program to count the number of studnets with the " A" grade in the following tuple:
grades = ("C", "D", "A", "A", "B", "B", "A")
print(grades.count("A"))

# store the above values in a list & store them from "A" to "D"

grades_list = ["C", "D", "A", "A", "B", "B", "A"]
grades_list.sort()
print(grades_list)