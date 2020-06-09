import re

#initialize variables for later use
word_sum = 0
num_word = 0

#Open txt file
File1 = open(r"Resources/paragraph_1.txt","r")

#read contents of txt file
All_text = File1.read()
#split txt file at all spaces and put into list
Words = All_text.split()
#count length of the Word list for word count
word_count = len(Words)
#for loop to go through each word and count its length
for word in Words:
    word_len = len(word)
    #add all word lengths together
    word_sum = word_sum + word_len
    #count total words checked
    num_word = num_word + 1

#take the average word length
avg_word_len = round(word_sum/num_word,1)
#split txt file into a list, where each sentence is a list element
#source: given as a hint to the HW
#Updated command to split on periods when there are at least 2x word characters preceding it
sent_list =  re.split('(?<=\w\w)\.', All_text)

#remove empty strings in list - using split function with delimiter at the end yields an empty string
sent_list_fix = list(filter(None, sent_list))

#count the length of the sentence list, to get total number of sentences
sent_length = len(sent_list_fix)
# Calculate average sentence length
avg_sent = num_word/sent_length

#close the file
File1.close()

#Summary of Analysis

#print the results to the terminal
print(f"""
Paragraph Analysis
(Resources/paragraph_1.txt)
----------------------------
Approximate Word Count: {word_count}
Approximate Sentence Count: {sent_length}
Average Letter Count: {avg_word_len}
Average Sentence Length: {avg_sent}
""")


#create txt file to print to
f= open("Analysis/Results_PyParagraph_1.txt","w")

#write results to txt file
f.write(f"""
Paragraph Analysis
(Resources/paragraph_1.txt)
----------------------------
Approximate Word Count: {word_count}
Approximate Sentence Count: {sent_length}
Average Letter Count: {avg_word_len}
Average Sentence Length: {avg_sent}  
""")
#close txt file
f.close() 
