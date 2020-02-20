from pyspark import SparkContext
File = "file:////home/ubuntu/data/taskdcleantweets.txt"
sc = SparkContext("local", "first app")
keywords = ['safe','accident','expensive','friendly','immigrants','immigrant','pollution','bus','parks','parking']
text_file = sc.textFile(File)
counts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .filter(lambda x: x[0] in keywords) \
             .reduceByKey(lambda a, b: a + b)
counts.saveAsTextFile("file:////home/ubuntu/data/keywordstaskd")