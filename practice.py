#practice.py
#Melissa Dunlap CS50 Python

#def main():
    #name = input("What is your name? ")
    #print(f"hello, {name}")

    # Python3 program introducing f-string
   # val = 'Geeks'
   # print(f"{val}for{val} is a portal for {val}.")

# Create our own function
def hello(to):
    print("hello,", to)


# Output using our own function
name = input("What's your name? ")
hello(name)



def main():

    # Output using our own function
    name = input("What's your name? ")
    hello(name)

    # Output without passing the expected arguments
    hello()


# Create our own function
def hello(to="world"):
    print("hello,", to)


main()


