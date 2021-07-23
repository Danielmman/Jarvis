import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
newVoiceRate = 190
engine.setProperty('rate', newVoiceRate)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def time():
	Time = datetime.datetime.now().strftime("%I:%M:%S")
	speak("The current time is")
	speak(Time)

def date():
	year = int(datetime.datetime.now().year)
	month = int(datetime.datetime.now().month)
	day = int(datetime.datetime.now().day)
	speak("The Current Date is")
	speak(day)
	speak(month)
	speak(year)

def wishme():
	speak("Welcome back sir!")
	#time()
	#date()

	hour = datetime.datetime.now().hour
	if hour >= 6 and hour < 12:
		speak("Good Morning!")
	elif hour >= 12 and hour < 18:
		speak("Good Afternoon!")
	elif hour >=18 and hour <= 24:
		speak("Good Evening!")
	else:
		speak("Good Night!")	 			

	day = int(datetime.datetime.now().weekday())
	weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
	speak(weekdays[day] + "at your service. How I can help you!")

def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio)
		#print(query)
	except Exception as e:
		print(e)
		speak("Say that again please...")

		return "None"

	return query

def sendemail(to, content):
	server =  smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login()
	server.sendmail("", to, content)
	server.close()

def screenshot():
	img = pyautogui.screenshot()
	img.save("E:/Workouts/Jarvis/ss.png")

def cpu():
	usage = str(psutil.cpu_percent())
	speak("CPU is at "+ usage)

	battery = psutil.sensors_battery()
	speak("battery is at ")
	speak(battery.percent )

def joke():
	joke = pyjokes.get_joke()
	print(joke)
	speak(joke)

if __name__ == '__main__':
	
	#wishme()

	while True:
		query = takeCommand().lower()
		print(query)

		if "time" in query:
			time()
		elif "date" in query:
			date()
		elif "offline" in query:
			quit()
		elif "wikipedia" in query:
			speak("Searching...")
			query = query.replace("wikipedia", "")
			result = wikipedia.summary(query, sentences = 2)
			speak(result)
		elif "send email" in query:
			try:
				speak("what should I say?")
				content = takeCommand()
				to = "xyz"
				sendmail(to, content)
				speak("Email send successfully")
			except Exception as e:
				print(e)
				speak(e)
				speak("Unable to send the message")	
		elif "browse" in query:
			speak("What should I search?")
			edgepath = "C:/Program Files/Microsoft/Edge/Application/msedge.exe %s"
			search = takeCommand().lower()
			wb.get(edgepath).open_new_tab("https://darkduskrp.com/websearch.html?q=" + search)
		elif "logout pc" in query:
			os.system("shutdown - 1")
		elif "shutdown pc" in query:
			os.system("shutdown /s /t 1")
		elif "restart pc" in query:
			os.system("shutdown /r /t 1")
		elif "play song" in query:
			songs_dir = "D:/Library/Music/Music"
			songs = os.listdir(songs_dir)
			os.startfile(os.path.join(songs_dir, songs[0]))
		elif "remember that" in query:
			speak("What should I remember?")
			data = takeCommand()
			speak("You said me to remember "+ data)
			remember = open("data.txt", "w")
			remember.write(data)
			remember.close()

		elif "do you know anything" in query:
			remember = open("data.txt", "r")
			speak("You said me to remember that " + remember.read())
		elif "screenshot" in query:
			screenshot()
			speak("Done")
		elif "cpu" in query:
			cpu()
		elif "joke" in query:
			joke()
