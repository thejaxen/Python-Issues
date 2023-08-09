#Working With List and Loops

magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(f"{magician.title()},that was a great trick!")
print('Thanks for your tricks.') 


numbers = [1,2,3,4,5,6,7,8,9]
for x in numbers:
    print(x)
    
    
for value in range(1,5):
    print(value)
    
numbers = list(range(1,6))
print(numbers)
print("\n")   

even_numbers = list(range(2,11,2))
print(even_numbers)

odd_numbers = list(range(1,10,2))
print(odd_numbers)

squares=[]
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)

digits = [1,2,3,4,5,6,7,8,9]
min(digits)
max(digits)
sum(digits)
print(max(digits), min(digits),sum(digits))

squares = [value**2 for value in range(1,11)]
print(squares)