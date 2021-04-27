# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.

def rev_int(x):
    string = str(x)

    if string[0] == '-':
        return int('-' + string[:0:-1])
    else:
        return int(string[::-1])

print(rev_int(-739))
print(rev_int(567))

# For a given sentence, return the average word length.

sentence1 = "Hi all, my name is Tom...I am originally from Australia."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"

# Remember to remove punctuation first.
def  avg_length(sentence):
    for i in "?!,.'!;:":
        sentence = sentence.replace(i, '')

    word = sentence.split()

print(avg_length(sentence1))
print(avg_length(sentence2))