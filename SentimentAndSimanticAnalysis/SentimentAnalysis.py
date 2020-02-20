def createdic():
    polarity = {}
    with open('negative-words.txt') as f:
        for line in f:
            line = line.rstrip()
            polarity[line] = -0.25
    with open('positive-words.txt') as f:
        for line in f:
            line = line.rstrip()
            polarity[line] = 0.35
    return polarity


def createstopdic():
    stopwords = []
    with open('stopwords.txt') as f:
        for line in f:
            line = line.rstrip()
            stopwords.append(line)
    return stopwords

#Extarct and clean tweets
def extractandcleantweets():
    file1 = open("cleanstreamtweets.txt", "w")
    with open('rawstreamtweets.json') as f:
        for idx, line in enumerate(f):
            if line != '\n':

                data = (json.loads(line))
                # Change to 'full_text' for processing SearchFile and text for processing StreamFile
                tweet = data['text']
                print tweet
                words = tweet.split(" ")
                for word in words:
                    if word.isalpha():
                        try:
                            file1.write(word + " ")
                        except:
                            pass
                file1.write("\n")

#remove stop words
def removestopwords():
    print"Removing stop words"
    stopwords = createstopdic()
    file1 = open("removedstopwordstweets.txt", "w")
    with open('cleanedtweets.txt') as f:
        for line in f:
            words = line.split(" ")
            for word in words:
                word = word.lower()
                word = word.rstrip()
                if word not in str(stopwords):
                    file1.write(word + " ")
            file1.write("\n")
    print"Completed removing stop words"

#analyze tweets and assign polairty
def analyze():
    print"Sentiment Analysis started"
    polarity = createdic()
    pol = 0
    file1 = open("output.txt", "w")
    with open('removedstopwordstweets.txt') as f:
        for idx, line in enumerate(f):
            #print line
            words = line.split(" ")
            for word in words:
                if word.lower() in polarity.keys():
                    res = polarity[word.lower()]
                    pol = pol + res
            if pol > 0:
                file1.write(line.rstrip() + " " + "polarity:" + str(pol) + " " + "positive")
                file1.write("\n")
            elif pol < 0:
                file1.write(line.rstrip() + " " + "polarity:" + str(pol) + " " + "negative")
                file1.write("\n")
            else:
                file1.write(line.rstrip() + " " + "polarity:" + str(pol) + " " + "neutral")
                file1.write("\n")
            pol = 0
    print"Sentiment Analysis completed"


removestopwords()
analyze()
