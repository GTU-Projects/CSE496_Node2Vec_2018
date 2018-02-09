import nltk
import re

class DocTool:

    def __init__(self):
        self.text = None
        self.pureSentences = None

    def readFile(self,fname):
        with open(fname,"r") as f:
            self.text = f.read()
        return self.text

    def getPureSentences(self,text):
        sentences = nltk.tokenize.sent_tokenize(text.lower())

        # capture characters which are not a-zA-Z0-9 and whitespace then change them with ""(empty) character
        pureSentences = [re.sub(r'[^\w\s]','',x) for x in sentences]
        self.pureSentences = [x.replace("\n"," ") for x in pureSentences]
        return self.pureSentences

    def sentences2Words(self,pureSentences):
        # now, join all sentences and make one text document.
        self.pureText = " ".join(pureSentences)
        # split text according to whitespace(space) character
        return self.pureText.split(" ")


if __name__=="__main__":
    # test codes
    doc=DocTool()
    text = doc.readFile("dataset/englishText1.txt")

    sent = doc.getPureSentences(text)
    print("Sentences:",sent)

    words = doc.sentences2Words(sent)
    print("Words:",words)