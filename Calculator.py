# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Kalkulyator hyzmaty")
print("1.Goshmak")
print("2.Aýyrmak")
print("3.Köpeltmek")
print("4.Bölmek")

while True:
    # take input from the user
    choice = input("Herekedi saylaň(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Birinji sany giriziň: "))
        num2 = float(input("Ikinji sany giriziň: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Kalkulýatorda herekediň dowam etdirmek isleýäňizmi? (howwa/yok): ")
        if next_calculation == "yok":
          break
    
    else:
        print("Bagyshlarsynyz. Nadogry san yazdynyz!")