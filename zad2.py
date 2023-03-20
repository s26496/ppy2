first_number = int(input("Podaj pierwszą liczbę: "))
second_number = int(input("Podaj drugą liczbę: "))
operator = input("Podaj typ operacji: +, -, / lub *: ")

if operator == "+":
    print(first_number+second_number)
elif operator == "-":
    print(first_number-second_number)
elif operator == "/":
    print(first_number/second_number)
elif operator == "*":
    print(first_number*second_number)
else:
    print("Podano nieprawidłowy typ operatora")




