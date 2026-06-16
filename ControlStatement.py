num = int(input("Enter a number: "))
print("Calculating the factorial of", num)
if num <= 0:
    print("The factorial is 1")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print("The factorial of", num, "is", factorial)

x, y = input("Enter two numbers separated by space: ").split()
x = int(x)
y = int(y)
if x > y:
    print(x, "is greater than", y)
elif x < y:
    print(x, "is less than", y)
else:
    print(x, "is equal to", y)

for i in range(1, 11):
    print(x, "x", i, "=", x * i)
    print(y, "x", i, "=", y * i)
num = int(input("Enter a number for multiplication table: "))
i = 10
while i>0:
    print(i, "*", num, "=", i * num)
    i -= 1
for i in range(10):
    print(i)
    if i  == 5:
        print("This is break point for the loop")
        break
        
for j in range(10):
   
    if j % 2 == 0:
        print(j,"This is continue point for the loop")
        continue
              

while True:
    user_input = input("Enter 'exit' to quit: ")
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break
    else:
        print("You entered:", user_input)


