#faces.py
#Melissa Dunlap CS50 Python

# function to convert smiley and sad face to emojis
def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

# function to get input and print converted ouput
def main():
    input_text = convert(input("Enter text here: "))
    print(input_text)

main()
