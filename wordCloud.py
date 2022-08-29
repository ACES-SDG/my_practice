# Python program to generate WordCloud

# importing all necessary modules
from traceback import print_tb
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

# Reads 'Youtube04-Eminem.csv' file
df = pd.read_csv(r"Youtube04-Eminem.csv", encoding ="latin-1")

comment_words = ''
stopwords = set(STOPWORDS)

# iterate through the csv file
for val in df.CONTENT:
	
	# typecaste each val to string
	val = str(val)

	# split the value
	tokens = val.split()
	
	# Converts each token into lowercase
	for i in range(len(tokens)):
		tokens[i] = tokens[i].lower()
	
	comment_words += " ".join(tokens)+" "
# print(comment_words)  
wordcloud = WordCloud(
				stopwords = stopwords,
				min_font_size = 10).generate(comment_words)
# word_freq = nmf.topic_word_frequency(topic_idx)

# plot the WordCloud image					
plt.figure(figsize = (7,5), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

plt.show()
