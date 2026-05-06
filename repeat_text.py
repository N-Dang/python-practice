phrase = input("enter some text: ")

while True:
    number = input("enter a whole number: ")
    try:
        number = int(number)
        break
    except:
        print("That is not a whole number. Try again.")

for i in range(number):
    print(phrase)
