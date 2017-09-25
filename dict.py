# mydict = {"sam": [6,4,8,5], "samuel(theotherone)": [4,5,1,3,8], "Tino": [7,8,5,5,6,]}

# winning_nums = [6,4,8,5]

# if winning_nums in mydict.values():
# 	print("someone wins")
import smtplib
from email.message import EmailMessage
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
	msg = EmailMessage()
	for name, email in user_dict.items():
		content = '''
		Hello {}
		Thank your for attending our event
		here some details about the event
		place : MEST
		DJ : Dj ANDREW
		dresscode : python PEP8
		'''.format(name)
		msg.set_content(content)
		msg['Subject'] = 'Details about the hotest party'
		msg['From'] = 'Dj Andrew'
		msg['To'] = email

		s = smtplib.SMTP('localhost')
		s.send_message(msg)
		s.quit()
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
		raise Exception("error ")

		

