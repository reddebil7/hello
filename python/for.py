#printing using for loop 1st method

#for i in [0,1,2]:
 #   print("meow")

# 2nd method to print for loop

#for i in range(3):
 #   print("meow")

#3rd method to print

#for _ in range(3):
 #   print("meow")

#4th method

#print("meow\n" * 3, end="")
#5th method
#while True:
 #   n = int(input("What's n? "))
  #  if n > 0 :
   #     break
#for _ in range(n):
 #   print("meow")

#6th method 

#def main():
 #   meow(3)


#def meow(n):
 #   for _ in range(n):
  #      print("meow")

#main()

#7th method
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input(" What's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()