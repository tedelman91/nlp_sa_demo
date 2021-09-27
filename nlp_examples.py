# #improt nltk package and download punkt library if not on machine 
# import nltk
# nltk.download('punkt')


#seperate all words from a string 
from nltk.tokenize import word_tokenize
Text = "Good morning, How are you doing? Are you coming tonight?"
Tokenized = word_tokenize(Text)
print("\n Print the string \"{}\" as seperate words".format(Text))
print(str(Tokenized) + "\n")


#seperate a paragraph into individual sentences 
from nltk.tokenize import sent_tokenize
Text = "Good morning, How are you doing? Are you coming tonight?"
Tokenized = sent_tokenize(Text)
print("\n Print the paragraph \"{}\" as seperate sentences".format(Text))
print(str(Tokenized) + "\n")
