from pyspark import SparkContext
File = "file:////home/ubuntu/data/taskdcleantweets.txt"
sc = SparkContext("local", "first app")
text_file = sc.textFile(File)
counts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)
counts.saveAsTextFile("file:////home/ubuntu/data/taskd")