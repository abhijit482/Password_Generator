#Password Generator 
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!\nEnter Integer Value.")
nr_letters= int(input("How many letters would you like in your password?: ")) 
nr_symbols = int(input(f"How many symbols would you like?: "))
nr_numbers = int(input(f"How many numbers would you like?: "))




add_letter =[]
for item in range(0,nr_letters):
    a = random.randint(0,len(letters)-1)
    add_letter.append(letters[a])
#print(add_letter)

add_numbers = []
for item in range(0,nr_numbers):
    a = random.randint(0,len(numbers)-1)
    add_numbers.append(numbers[a])
#print(add_numbers)

add_symbols = []
for item in range(0,nr_symbols):
    a = random.randint(0,len(symbols)-1)
    add_symbols.append(symbols[a])
#print(add_symbols)

#adding all together
total_password = []
add_letter.extend(add_numbers)
#print(add_letter)
add_letter.extend(add_symbols)
#print(add_letter)
total_password.extend(add_letter)


#shuffle and generate password
random.shuffle(total_password)
print(f"Your Password : {''.join(total_password)}")
