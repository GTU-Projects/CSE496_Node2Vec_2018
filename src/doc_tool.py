import nltk
import re

def readFile(fname="dataset/turkishText1.txt"):
    text = None
    with open(fname,"r") as f:
        text = f.read()
    return text

def text2sentences(text):
    sentences = nltk.tokenize.sent_tokenize(text.lower())
    # capture characters which are not a-zA-Z0-9 and whitespace then change them with space character
    pureSentences = [re.sub(r'([^\w\s])|[\n]'," ",x) for x in sentences]
    return pureSentences

def sentences2Words(pureSentences,stopwords={}):
    # now, join all sentences and make one text document.
    pureText = " ".join(pureSentences)
    # split text according to whitespace(space) character
    words =  [word for word in pureText.split() if not is_stop_word(word,stopwords)]
    return words

def load_stop_words(file="dataset/tr_stopwords.txt"):
    """
    Read file which contains stopwors and return dictionary of this words
    """
    stopwords = None
    try:
        with open(file,"r") as f:
            lines = f.read().splitlines()
            stopwords = dict(zip(lines,lines))
    except Exception as e:
        stopwords = None
    return stopwords

def is_stop_word(word,stopwords):
    return word in stopwords.keys()

if __name__=="__main__":
    # test codes
    stopwords = load_stop_words("/home/hmenn/Workspace/doc2graph/dataset/tr_stopwords.txt")
    print("Stopwords:",stopwords)

    text = readFile("/home/hmenn/Workspace/doc2graph/dataset/turkishText1.txt")

    sent = text2sentences(text)
    print("Sentences:",sent)

    words = sentences2Words(sent,stopwords)
    print("Words:",words)