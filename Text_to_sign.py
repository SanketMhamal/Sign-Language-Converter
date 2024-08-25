
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
import os
from tkinter import ttk
nltk.download('punkt')
def animation_view(request):
	
		
		text = request
		#tokenizing the sentence
		text.lower()
		#tokenizing the sentence
		words = word_tokenize(text)
        
		tagged = nltk.pos_tag(words)
		tense = {}
		tense["future"] = len([word for word in tagged if word[1] == "MD"])
		tense["present"] = len([word for word in tagged if word[1] in ["VBP", "VBZ","VBG"]])
		tense["past"] = len([word for word in tagged if word[1] in ["VBD", "VBN"]])
		tense["present_continuous"] = len([word for word in tagged if word[1] in ["VBG"]])

		#stopwords that will be removed
		stop_words = set(["mightn't", 're', 'wasn', 'wouldn', 'be', 'has', 'that', 'does', 'shouldn', 'do', "you've",'off', 'for', "didn't", 'm', 'ain', 'haven', "weren't", 'are', "she's", "wasn't", 'its', "haven't", "wouldn't", 'don', 'weren', 's', "you'd", "don't", 'doesn', "hadn't", 'is', 'was', "that'll", "should've", 'a', 'then', 'the', 'mustn', 'i', 'nor', 'as', "it's", "needn't", 'd', 'am', 'have',  'hasn', 'o', "aren't", "you'll", "couldn't", "you're", "mustn't", 'didn', "doesn't", 'll', 'an', 'hadn', 'whom', 'y', "hasn't", 'itself', 'couldn', 'needn', "shan't", 'isn', 'been', 'such', 'shan', "shouldn't", 'aren', 'being', 'were', 'did', 'ma', 't', 'having', 'mightn', 've', "isn't", "won't"])

		#removing stopwords and applying lemmatizing nlp process to words
		lr = WordNetLemmatizer()
		filtered_text = []
		for w,p in zip(words,tagged):
			if w not in stop_words:
				if p[1]=='VBG' or p[1]=='VBD' or p[1]=='VBZ' or p[1]=='VBN' or p[1]=='NN':
					filtered_text.append(lr.lemmatize(w,pos='v'))
				elif p[1]=='JJ' or p[1]=='JJR' or p[1]=='JJS'or p[1]=='RBR' or p[1]=='RBS':
					filtered_text.append(lr.lemmatize(w,pos='a'))

				else:
					filtered_text.append(lr.lemmatize(w))

		#adding the specific word to specify tense
		words = filtered_text
		temp=[]
		for w in words:
			if w=='I':
				temp.append('Me')
			else:
				temp.append(w)
		words = temp
		probable_tense = max(tense,key=tense.get)

		if probable_tense == "past" and tense["past"]>=1:
			temp = ["Before"]
			temp = temp + words
			words = temp
		elif probable_tense == "future" and tense["future"]>=1:
			if "Will" not in words:
					temp = ["Will"]
					temp = temp + words
					words = temp
			else:
				pass
		elif probable_tense == "present":
			if tense["present_continuous"]>=1:
				temp = ["Now"]
				temp = temp + words
				words = temp
        # words.upper()

		filtered_text = []
		for w in words:
            
			path = w + ".mp4"
			if path not in os.listdir("./assets"):
			#splitting the word if its animation is not present in database
				for c in w:
					filtered_text.append(c)
			#otherwise animation of word
			else:
				filtered_text.append(w)
		words = filtered_text
		return words
	
import cv2

def play_video(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if the video file is opened successfully
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    # Create a window
    cv2.namedWindow('Video')

    # Play video
    while cap.isOpened():
        # Read a frame from the video
        ret, frame = cap.read()

        # Check if the frame was read successfully
        if not ret:
            break

        # Display the frame
        cv2.imshow('Video', frame)

        # Pause for a while (milliseconds)
        # You can adjust the delay to control the playback speed
        key = cv2.waitKey(30)

        # Check if the user pressed 'q' to exit
        if key == ord('q'):
            break

    # Release the video capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()



import tkinter as tk

def store_words(typed_text):
    global M
    
    M = typed_text
	
def say_words(M):
    
    if M:
        m = animation_view(M)
        for i in m:
            i = i.upper()  # Assign the uppercase value back to i
            videoName = "./assets/" + i + ".MP4"  # 'DJI_0209.MP4'
            play_video(videoName)
    else:
        print("Enter word")


# # Initialize Tkinter
# root = tk.Tk()
# root.title("Simple Python UI")


# # Create a style object
# style = ttk.Style()

# # Set the background and foreground color
# style.configure("TButton", background="#4CAF50", foreground="white")
# style.configure("TEntry", background="#f2f2f2")


# # Create input text bar
# entry = tk.Entry(root, width=40)
# entry.pack(pady=10)

# # Create button to store words
# store_button = tk.Button(root, text="Store Words", command=store_words)
# store_button.pack()

# # Create button to say hello
# hello_button = tk.Button(root, text="Say Hello", command=say_hello)
# hello_button.pack(pady=10)

# # Initialize M
# M = ""

# # Start the Tkinter event loop
# root.mainloop()
