import string

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

# For a given sentence, return all words in a sentence in a list.

sentence1 = "Hi all, my name is Annie...I am originally from America."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"

# Remember to remove punctuation first.
def  avg_length(sentence):
    punctuation = string.punctuation
    for i in punctuation:
        sentence = sentence.replace(i, '')
        return sentence.split()

print(avg_length(sentence1))
print(avg_length(sentence2))