num_books = int(input("Enter the number of books you purchased this month:\n"))

if num_books <= 1:
    points = 0
elif num_books <= 3:
    points = 5
elif num_books <= 5:
    points = 15
elif num_books <= 7:
    points = 30
else:
    points = 60

print("Points Earned:", points)
