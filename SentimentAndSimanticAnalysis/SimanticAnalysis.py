import math


def extractandcleanreutersfiles():
    print "processing reuters files"
    file1 = open("AllReutersData.txt", "a+")
    for i in range(22):
        print i
        with open('reutersfiles/reut2-000.txt') as f:
            for idx, line in enumerate(f):
                if line != '\n':

                    words = line.split(" ")
                    for word in words:
                        if word.isalpha():
                            try:
                                file1.write(word + " ")
                            except:
                                pass
                    file1.write("\n")
    print "Completed processing reuters files"


def createdocuments():
    print "Creating documents"
    count = 0
    docno = 0
    file1 = open("documents/1.txt", "w")
    with open('AllReutersData.txt') as f:
        for line in f:
            count = count+1
            if line != '\n':
                if count > 200:
                    file1 = open("documents/"+str(docno)+".txt", "a+")
                    count = 0
                    docno = docno + 1
                words = line.split(" ")
                for word in words:
                    if word != "\n":
                        file1.write(word + " ")
    print "Completed creating documents"


def checkifindoc(filenumber, keyword):
    count = 0
    with open('documents/'+str(filenumber)+'.txt') as f:
        for line in f:
            words = line.split(" ")
            for word in words:
                word = word.lower()
                if word == keyword:
                    count = count + 1
    return count


def termfreq(keyword):
    tf = {}
    for i in range(10559):
        tf["doc"+str(i)] = checkifindoc(i, keyword)
    print "\n" + "TF"
    for key in sorted(tf):
        print key,
        print str(tf[key]),
    return tf


def calIDF(keyword):
    tf = termfreq(keyword)
    idf = {}
    totaldocs = len(tf)
    occurence = 0
    print "\nTotal Documents: " + str(totaldocs)
    for key, value in tf.iteritems():
        if value > 0:
            occurence = occurence + 1
    print "no of docs " + keyword + " occured:" + str(occurence)
    divvalue = float(totaldocs)/float(occurence)
    idfval = math.log(divvalue, 2)
    print "IDF value:" + str(idfval)
    for key, value in tf.iteritems():
        if value > 0:
            idf[str(key)] = idfval * 1
        else:
            idf[str(key)] = 0
    print "IDF"
    for key in sorted(idf):
        print key,
        print str(idf[key]),

    tfidf={}
    for key, value in idf.iteritems():
        tfidf[str(key)] = value*tf[str(key)]
    print "\nTFIDF"
    for key in sorted(tfidf):
        print key,
        print str(tfidf[key]),

    query = []
    query.append(0)
    query.append(float(idfval)/float(occurence))
    print "\n query"
    print query
    return tfidf


def rankdocuments(query):
    i = 10559
    for key, value in sorted(query.iteritems(), key=lambda (k, v): (v, k)):
        print (key, i)
        i = i - 1


#Clean reuters files
extractandcleanreutersfiles()
#create documents
createdocuments()
#Create TFIDF for canda and India can be used for different values
print "Canada"
query = calIDF("canada")
print "\n\nIndia"
calIDF("india")
#Ranking documents based on TF-IDF
rankdocuments(query)
