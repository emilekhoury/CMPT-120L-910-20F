def prime_or_composite(number):
    
    #- Add code in the defined function to figure out whether or not the given number is a prime number or not. 

    #- A prime number (or a prime) is a natural number greater than 1 that is not a product of two smaller natural numbers. A natural number greater than 1 that is not prime is called a composite number. - Wikipedia
    
    #- Take in a parameter called number and return “Prime” or “Composite”

    if number<=1:
        return "not a prime or composite number"
    elif number>1:
        for i in range(2, number):
            if number%i==0:
                return "Composite"
        
        return "Prime"
    pass

if __name__ == "__main__":
    numbers = [1, 2, 10, 31, 47, 89, 101, 103, 97, 187, 981, 19201]
    # Optional: If you want to test the efficency of your algorithm add this number to the array above -7
    # Optional: If you want to test the efficency of your algorithm add this number to the array above 47055833459
    answers = []
    for number in numbers:
        answers.append(prime_or_composite(number))
    
    print(answers)