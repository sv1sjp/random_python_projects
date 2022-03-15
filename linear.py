def linearCongruentialGenerator(Xo, m, a, c,random_numbers,random_no_of_randoms):

    #Initialize the seed state
    random_numbers[0] = Xo

    #Generate random numbers
    for i in range(1, random_no_of_randoms):
        
        random_numbers[i] = ((random_numbers[i - 1] * a) + c) % m  

#Seed value
Xo = 27
#Modulus parameter
m = 57    
#Multiplier term
a = 17   
#Increment term
c = 45

#Number of Random numbers to be generated
random_no_of_randoms = 47

#Variable to declare the random number
random_numbers = [0] * (random_no_of_randoms)

#Call the function
linearCongruentialGenerator(Xo, m, a, c,random_numbers,random_no_of_randoms)

plainttext = input("Give me a Plaintext: ")
unique = set(plainttext)
random_numbers = [39, 23, 41, 11, 91, 19, 20, 31, 9]
mapping = dict(zip(unique, random_numbers))    
print(mapping)