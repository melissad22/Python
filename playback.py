#playback.py
#MelissaDunlap CS50 Python

def playback():
    input_string = input("Please enter some text here: ")
    input_string = input_string.replace(" ", "...")
    return input_string

print(playback())
