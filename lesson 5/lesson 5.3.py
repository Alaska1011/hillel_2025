import string
def hashtag_add(input_string):
    cleaned_string = ''.join(char for char in input_string if char not in string.punctuation).replace(" ", "")
    words = cleaned_string.split()
    hashtag = '#'+ ''.join(word.capitalize() for word in words)
    if len(hashtag) > 140:
        hashtag = hashtag[:140]
    return hashtag
print(hashtag_add('Python Community'))
print(hashtag_add('i like python community!'))
print(hashtag_add('Should, I. subscribe? Yes!'))