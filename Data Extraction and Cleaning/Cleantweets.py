import json


#ref: https://stackoverflow.com/questions/33404752/removing-emojis-from-a-string-in-python
def removeemojis(text):
    tweet =text.encode('latin-1', 'ignore').decode('latin-1')
    return tweet


def transform():
    file1 = open("taskdcleantweets.txt", "w")
    with open('TaskD.json') as f:
        for idx, line in enumerate(f):
            if line != '\n':

                data = (json.loads(line))
                #Change to 'full_text' for processing SearchFile and text for processing StreamFile
                tweet = data['text']
                tweet = removeemojis(tweet)
                print tweet
                words = tweet.split(" ")
                for word in words:
                    if word.isalpha():
                        try:
                            file1.write(word + " ")
                        except:
                            pass
                file1.write("\n")


transform()
