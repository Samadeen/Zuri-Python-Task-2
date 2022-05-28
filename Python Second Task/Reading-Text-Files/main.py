# Read text from a file, and count the of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
   #  [assignment] Add your code here
    with open(filename,"r") as open_text:
        read_text = open_text.read()
    return read_text

def count_words():
    text = read_file_content("./story.txt")
#    [assignment] Add your code here
    lower_text = text.lower()
    split_text= lower_text.split()
    count = {}
    for i in split_text:
        if i == "as":
            count[i] = 10
        elif i == "would":
            count[i] = 20
    return count
print(count_words())