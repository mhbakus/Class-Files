import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import __init__

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(os.environ['GMAIL'], os.environ['GMAIL_PASSWORD'])
def add_contact():
	name = input("please enter your name : ")
	email = input("please enter your email : ")
	host[name] = email
	print("thank you for registration")

def get_email(user_dict, name):
	if name in user_dict.keys():
		return user_dict[name]
	else:
		return "none"

def send_mail(user_dict):
	for name, email in user_dict.items():
		if name == 'eyram':
			content = '''
			Hello {}
			Sorry you're not allow to the party
			'''.format(name)
		else:
			content = '''
			Hello {}
			Thank your for attending our event
			here some details about the event
			place : MEST
			DJ : Dj ANDREW
			dresscode : python PEP8
			'''.format(name)	
		
		fromadress = "andrew@meltwater.org"
		msg = MIMEMultipart()
		msg['From'] = fromadress
		msg['To'] = email
		msg['Subject'] = "Details about the hotest party of Accra"
		body = content
		msg.attach(MIMEText(body, 'plain'))
		text = msg.as_string()
		server.sendmail(fromadress, email, text)
exit = False
host = {}
while not exit:
	answer = input("welcome to your event apps choose your action \n 1 . registration \n 2 . get a email for specific contact \n 3 . send email to evryone \n 4 . exit \n")
	if answer == "1":
		add_contact()
	elif answer == "2":
		name = input("please enter the name : ")
		print(get_email(host, name))
	elif answer == "3":
		send_mail(host)
	elif answer == "4":
		exit = True
	else:
		raise Exception("error please enter a valid answer between 1, 2, 3, 4")

		

