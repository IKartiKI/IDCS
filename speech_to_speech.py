# Python program to translate
# speech to text and text to speech


import speech_recognition
import pyttsx3 

# Initialize the recognizer 
r = speech_recognition.Recognizer() 

# Function to convert text to
# speech
def SpeakText(command):
	
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command) 
	engine.runAndWait()
	
	
# Loop infinitely for user to
# speak

while(1): 
	
	# Exception handling to handle
	# exceptions at the runtime
	try:
		
		# use the microphone as source for input.
		with speech_recognition.Microphone() as mic:
			
			# wait for a second to let the recognizer
			# adjust the energy threshold based on
			# the surrounding noise level 
			r.adjust_for_ambient_noise(mic, duration=0.2)
			
			#listens for the user's input 
			audio = r.listen(mic)
			
			# Using google to recognize audio
			MyText = r.recognize_google(audio)
			MyText = MyText.lower()

			print("Did you say ",MyText)
			SpeakText(MyText)
			
	except speech_recognition.RequestError as e:
		print("Could not request results; {0}".format(e))
		
	except speech_recognition.UnknownValueError:
#		print("unknown error occurred")
		r = speech_recognition.Recognizer() 
		continue

