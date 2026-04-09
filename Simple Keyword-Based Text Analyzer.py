#Simple Keyword-Based Text Analyzer

#Step 1: take input from user
text=input("Enter a paragraph: ").lower() #used lower to remove case sensitivity 
#Step 2: Tokenization(split the sentence into words)
import re
words = re.findall(r'\b[a-zA-Z]+\b', text)
#Step 3: Create word frequency dictionary
word_count={} #empty dictionary
for word in words:
    if word in word_count:
     word_count[word]+=1
    else:
     word_count[word]=1
#step 4: Find most common word
# Find the highest frequency (largest number of times any word appears)
most_common_word = max(word_count, key=word_count.get)




#step 5: Define most important keywords
keywords=["ai", "nlp", "python", "data", "model", "analysis"]
found_keywords=[] #empty list to store found keywords
for word in word_count:
    if word in keywords:
        found_keywords.append(word)
#step 6: text analysis report 
print("////BASIC KEYWORD ANALYSER///")
print("Total words:", len(words))
print("Most common word:", most_common_word)
print("Keyword found:", found_keywords)
