#get user input
name  = input("Enter Your name: ")

#Remove whitespace from string and capitalize first letter of each word
name = name.strip().title()

#split user name into name, middlename and surname
first, middle, surname = name.split(" ")

#print out user name with greeting 'hello'
print(f"Hello, {surname} {first} {middle}")

