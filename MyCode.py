#Ex:1
num = 7
for i in range(2,num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")

#Ex:2
number = int(input("Enter any number: "))


if number > 1:                                     # prime number is always greater than 1
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

                                                    # if the entered number is less than or equal to 1
                                                    # then it is not prime number
else:
    print(number, "is not a prime number")

