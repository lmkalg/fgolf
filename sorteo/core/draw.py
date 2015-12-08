#!/usr/bin/python
import random
import constants
import sys

from argparse import ArgumentParser
from player import Player
from line import Line
from constants import countries_images


def generate_players_list(name_country_file):
	players = []
	with open(name_country_file,'r') as f:
		content = f.readlines()
		content = [line.rstrip() for line in content]	
		content = [line for line in content if line]

		if ((len(content) % 4) != 0):
			raise Exception("ERROR. Number of players is not a multiple of 4")
		for row in content:
			name, country = row.split(',')
			players.append(Player(name.strip(), country.strip()))
	return players


def generate_lines_list(date_file):
	lines = []
	with open(date_file,'r') as f:
		content = f.readlines()
		line_number = 1
		for row in content:
			lines.append(Line(line_number,row))	
			line_number += 1
	return lines



def write_result(result_file, lines):
	with open(result_file,'w') as f:
		#Sort it by line number
		lines.sort(key= lambda l: l.number)

		for line in lines:
			f.write(line.toString())

def write_json(json_file, lines):
	with open(json_file, 'w') as f:
		#Sort it by line number
		lines.sort(key= lambda l: l.number)
		f.write('[\n')
		for line in lines:
			f.write('\t{')
			f.write('\"line_number\":\"{0}\",\n'.format(line.number))
			f.write('\t\"line_info\":\"{0}\",\n'.format(line.date))
			f.write('\t\t\"players\":[\n')
			for player in line.players:
				f.write('\t\t\t{\"country\":\"%s\", \"player\":\"%s\"}' % (countries_images[player.country], player.name))
				if not player == line.players[-1]:
					f.write(',')	
				f.write('\n')
			f.write('\t\t]\n')
			f.write('\t}')
			if not line == lines[-1]: 
				f.write(',')
			f.write('\n')
		f.write(']\n')






def put_player_somewhere(player,lines):
	possible_index_lines = range(len(lines)) #list that will control which line we already used
	while possible_index_lines:
		rand_index = random.randint(0,len(possible_index_lines)-1)
		if lines[rand_index].canAddPlayer(player):
			lines[rand_index].addPlayer(player)
			return True
		else:
			possible_index_lines.pop(rand_index)	

	return False

def reorganize_to_put(player, lines, players):
	possible_index_lines = range(len(lines)) #list that will control which line we already used
	while possible_index_lines:
		rand_index = random.randint(0,len(possible_index_lines)-1)

		if lines[rand_index].canAddPlayer(player):
			#Lo puedo meter de una
			lines[rand_index].addPlayer(player)
			return True

		elif lines[rand_index].canAddPlayerExchanging(player):
			#Lo meto, y me quedo con el player de intercambio
			old_player = lines[rand_index].addPlayerExchanging(player)
			#print 'Entra:%s , Sale: %s, en la linea: %s' % (player.name, old_player.name, lines[rand_index].number)

			#Agrego esta linea
			players.append(old_player)
			return True
		else:
			possible_index_lines.pop(rand_index)	

	return False



def first_turn(players, lines):
	times = len(players)

	for time in range(times):
		#Choose random player
		rand_player = random.randint(0,len(players)-1)
		choosen_player = players.pop(rand_player)

		#If the player couldn't be added to any line, just add it 
		if not put_player_somewhere(choosen_player,lines):
			players.append(choosen_player)
			


def second_turn(players,lines):
	while players:
		rand_player = random.randint(0,len(players)-1)
		choosen_player = players.pop(rand_player)

		if not reorganize_to_put(choosen_player,lines, players):
			raise Exception("Is impossible to make a draw with the current input. Please check it out!.")



def begin_draw(name_country_file, date_file, result_file, json_file):
	times = 10
	i = 0

	while True:
		try: 
			players = generate_players_list(name_country_file)
			lines = generate_lines_list(date_file)
			if len(players) / 4 != len(lines):
				raise Exception("The amount of players must be 4 times the amount of lines. Amount of players is: {0} and lines is: {1}".format(len(players),len(lines)))
		
			#first round where we try to put players like beasts:P 
			first_turn(players,lines)

			#Second round --> Try to switch already saved players
			second_turn(players,lines)


			write_result(result_file, lines) #Human frindly file
			write_json(json_file, lines)
			#print "%s" % str(i)
			break
		except Exception,e :
			if i < times:
				i += 1
				pass
			else:
				raise Exception("%s"%e)


if __name__ == '__main__':
	parser = ArgumentParser()

	parser.add_argument('-d', dest='dates', help='Path to file with the time of line.')
	parser.add_argument('-n', dest='names', help='Path to file of names and countries relationship.')
	parser.add_argument('-o', dest='output', help='Path where the output will be placed.')
	parser.add_argument('-j', dest='json', help='Path where the output in json will be placed.')

	args  = parser.parse_args()

	begin_draw(args.names, args.dates, args.output, args.json)

