import hashlib
class Secret:
	def __init__(self, secret, password):
		self.__secret = secret
		self.__password = self.__hash_password(password)

	def get_secret(self, password):
		if self.__hash_password(password) == self.__password:
			print(self.__secret)
		else:
			print("Go Away, MOM")

	def change_password(self, old_password, new_password):
		if self.__hash_password(old_password) == self.__password:
			self.__password = self.__hash_password(new_password)
		else:
			print("unable to change")

	def __hash_password(self, password):
		return hashlib.sha256(password.encode('utf-8')).hexdigest()

andrew_secret = Secret("I'm beautiful", "thetruth")

andrew_secret.get_secret("thetruth")