# #improt nltk package and download punkt library if not on machine 
# import nltk
# nltk.download('punkt')

# #improt nltk package and download stopwords library if not on machine 
# import nltk
# nltk.download('stopwords')

#majority of code sourced from:
# https://livecodestream.dev/post/intro-to-natural-language-processing-with-python/
#https://livecodestream.dev/post/detecting-the-sentiment-on-elon-musks-tweets-with-python/

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

#show what stopwords are
from nltk.corpus import stopwords
stopwords = stopwords.words("english")
print("Stopwords that are filtered out: \n" + str(stopwords) + "\n")

#seperate stopwords from sentences
from nltk.corpus import stopwords
stopwords = stopwords.words("english")
Text = ["Good", "morning", "How", "you", "doing", "Are", "you", "coming", "tonight"]
nonstop_words = []
for i in Text:
   if i not in stopwords:
       nonstop_words.append(i)
print("\n Print the words \"{}\" without stop words".format(Text))
print(str(Tokenized) + "\n")


#get the stems of words 
from nltk.stem import PorterStemmer
ps = PorterStemmer()
words = ["Loving", "Chocolate", "Retrieved", "Being"]
word_stems = []
for i in words:
   word_stems.append(i)
print("\nGet the word stems from \"{}\" ".format(words))
print("Word stems: " + str(word_stems) + "\n")


#count words 
import nltk
words = ["truck", "truck", "car", "boat", "train", "house", "house", "house", "house", "house"]
FreqDist = nltk.FreqDist(words)
print("\nPrint the word counts from \"{}\" ".format(words))
for i,j in FreqDist.items():
   print(i, "---", j)
print("\n")

#fix spelling mistakes 
from textblob import TextBlob
Text = "Hhow long does it takde to drived to California?"
spelling_mistakes = TextBlob(Text)
print("Print spelling mistakes in the sentence \"{}\"".format(Text))
print(spelling_mistakes.correct()+"\n")


