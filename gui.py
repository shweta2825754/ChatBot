import io
import random
import string
import warnings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

import nltk
from nltk.stem import WordNetLemmatizer
 





with open('RGIT.txt','r', encoding='utf8', errors ='ignore') as fin:
    raw = fin.read().lower()

#Tokenisation
sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)

# Preprocessing
lemmer = WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))



  


import tkinter
from tkinter import *
def send():
	GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
	GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

	def greeting(sentence):
		for word in sentence.split():
			if word.lower() in GREETING_INPUTS:
				return random.choice(GREETING_RESPONSES)


	def response(user_response):
		robo_response=''
		sent_tokens.append(user_response)
		TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
		tfidf = TfidfVec.fit_transform(sent_tokens)
		vals = cosine_similarity(tfidf[-1], tfidf)
		sent_tokens.remove(user_response)
		idx=vals.argsort()[0][-2]
		flat = vals.flatten()
		flat.sort()
		req_tfidf = flat[-2]
		if(req_tfidf==0):
				robo_response=robo_response+"I am sorry! I don't understand you"
				return robo_response
		else:
				robo_response = robo_response+sent_tokens[idx]
				return robo_response


	msg = EntryBox.get("1.0",'end-1c').strip()
	EntryBox.delete("0.0",END)
	if msg != '':
		ChatBox.config(state=NORMAL)
		ChatBox.insert(END, "You: " + msg + '\n\n')
		msg=msg.lower()
		ChatBox.config(foreground="#446665", font=("Verdana", 12 ))
		if(msg!='bye'):
			if(msg=='thanks' or msg=='thank you' ):
				res="ROB: You are welcome.."
			else:
				if(greeting(msg)!=None):
					res=greeting(msg)
				else:
					res=response(msg)
		else:
			res="Bye! take care.." 
			root.destroy()
        
		ChatBox.insert(END, "ROB: " + res + '\n\n')
		ChatBox.config(state=DISABLED)
		ChatBox.yview(END)



root = Tk()
root.title("Chatbot")
root.geometry("400x500")
root.resizable(width=FALSE, height=FALSE)
#Chat window
ChatBox = Text(root, bd=0, bg="white", height="8", width="50", font="Arial",)
ChatBox.insert(END, "ROB: Ask me Anything about RGIT. " + '\n\n')
ChatBox.config(state=DISABLED)


scrollbar = Scrollbar(root, command=ChatBox.yview, cursor="heart")
ChatBox['yscrollcommand'] = scrollbar.set

SendButton = Button(root, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                    bd=0, bg="blue", activebackground="red",fg='yellow',
                    command= send )

root.bind('<Return>', lambda event=None: SendButton.invoke())
EntryBox = Text(root, bd=0, bg="white",width="29", height="5", font="Arial")



scrollbar.place(x=376,y=6, height=386)
ChatBox.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90, width=100)
root.mainloop()

