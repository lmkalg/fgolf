from player import Player

class Line(object):
	def __init__(self, number, date):
		self.players = []
		self.number = number
		self.date = date.strip()

	def countries_of_players(self):
		countries = []
		for player in self.players:
			countries.append(player.country)
		return countries

	def canAddPlayer(self,player):
		if len(self.players) < 2:
			return True
		elif len(self.players) >= 4:
			return False
		elif len(self.players) >= 2:
			return self.countries_of_players().count(player.country) < 2

	def removePlayer(self,player):
		for i in range(len(self.players)):
			if player.name == self.players[i].name and player.country == self.players[i].country:
				self.players.pop(i)


	def addPlayer(self, player):
		if self.canAddPlayer(player):
			self.players.append(player)
		else:
			raise Exception("Can't add")


	def canAddPlayerExchanging(self, player):
		return self.countries_of_players().count(player.country) < 2


	def addPlayerExchanging(self, player):
		for i in range(len(self.players)):
			if self.players[i].country != player.country:
				old_player = self.players.pop(i)
				self.players.append(player)
				return old_player


	def toString(self):
		template = "Line {0}: {1}".format(self.number, self.date) 
		for times in range(len(self.players)):
			name = self.players[times].name 
			country = self.players[times].country 
			template += '\n\t*) {0} - {1}'.format(name,country)
		return template + '\n\n\n'
