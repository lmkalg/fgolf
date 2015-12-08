import constants

class Player(object):
	def __init__(self, name, country):
		self.name = name
		if country not in constants.COUNTRIES:
			raise Exception("Country of {0} is invalid.".format(name))
		else:
			self.country = country
