import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
	engine.say(text)
	engine.runAndWait()

def get_info():
	try:
		with sr.Microphone() as source:
			print('listening...')
			voice = listener.listen(source)
			info = listener.recognize_google(voice)
			print(info)
			return info.lower()

	except:
		pass

def send_email(receiver, subject, message):

	client = 'smtp.gmail.com'
	port = 587

	file = 'credentials.txt'
	mode = 'r'

	server = smtplib.SMTP(client, port)
	server.starttls()


	with open(file, mode) as f:
		credentials = f.readlines()

	username = credentials[0]	
	password = credentials[1]

	server.login(username, password)
	email['From'] = username
	email['To'] = receiver
	email['Subject'] = subject
	email.set_content(message)
	server.send_message(email)

file = 'credentials.txt'
mode = 'r'

with open(file, mode) as f:
	email_accounts = f.readlines()

	email_list = {
		'dad' : email_accounts[3],
		'lyne' : email_accounts[4],
		'adrian' : email_accounts[5]
	}


def get_email_info():
	talk('Whom do you want to email?')
	name = get_email_info()
	receiver = email_list[name]
	talk('What is the email subject?')
	subject = get_email_info()
	talk('listening to email body...')
	message = get_email_info
	send_email(receiver, subject, message)

	talk('Do you want to send more emails?')
	send_more = get_info()

	if 'yes' in send_more:
		get_email_info()


get_email_info()
