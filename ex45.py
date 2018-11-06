import random

class Room1(object):

	def play(self):
		print "\nHi da bb"
		print "You're supposed to grade my homework"
		print "I'm not creative and I don't like looking at 800 print statements,"
		print "so this won't be super exciting. But I love u :)"
		raw_input()
		print "U find a castle in the woods and u think da bb is somewhere inside."
		print "U go inside and there is a door forward or a trap door downward."
		print "Do u go forward or down?\n"
		go = raw_input("-> ")
		if go == 'down':
			return 'tictactoe'
		elif go == 'forward':
			return 'room2'
		else:
			print "Your answer was not one of the options I gave you."
			print "Oh well, looks like you fell through the trap door anyway!"
			return 'tictactoe'


class Room2(object):

	def play(self):
		print "\nThere are 4 doors here.\n"
		print "	Door 1: pink! Bubble gum pink"
		print "	Door 2: green like the grass"
		print "	Door 3: this door is brown, like da poopy"
		print "	Door 4: super duper white, like da yeezys\n"
		print "Which one do u want to open da bb? Type a number:\n"
		door = raw_input("-> ")
		if door == '1':
			return 'pink'
		elif door == '2':
			return 'green'
		elif door == '3':
			return 'brown'
		elif door == '4':
			return 'white'
		else:
			return 'death'


class TicTacToe(object):

	board = [
		'e', 'e', 'e',
		'e', 'e', 'e',
		'e', 'e', 'e'
		]

	def print_board(self):
		print ' '.join(self.board[0:3])
		print ' '.join(self.board[3:6])
		print ' '.join(self.board[6:9]), "\n"
		return self.board

	def take_turn(self):
		move = raw_input("-> ")
		self.board[int(move) - 1] = 'X'
		return self.board

	def computer_turn(self):
		print "\nMy turn."
		while True:
			pos = random.randint(0, 8)
			if ((self.board[int(pos)] != 'X') and (self.board[int(pos)] != 'O')):
				break
		self.board[int(pos)] = 'O'
		return self.board

	def play(self):
		print "\nThere is a furry monster here. It starts talking to u:"
		print "\"U have to beat me at a game of tic tac toe or u die."
		print "I'm not that smart so it shouldn't be hard.\""
		raw_input()
		self.print_board()
		print "The board is currently empty. See? 'e'."
		raw_input()
		print "Left to right, top to bottom, positions are 1-9."
		print "You are Xs and I am Os. Make ur move by picking a position."
		n = 0
		while n < 9:
			self.take_turn()
			wins = [self.board[0:3], self.board[3:6], self.board[6:9],
				self.board[0:9:3], self.board[1:9:3], self.board[2:9:3],
				self.board[0:9:4], self.board[2:8:2]
				]
			if ['X', 'X', 'X'] in wins:
				self.print_board()
				print "You won. Bummer. Well, looks like you may proceed."
				raw_input()
				return 'room2'
			else:
				self.computer_turn()
				self.print_board()
				if ['O', 'O', 'O'] in wins:
					print "Aha! I won!!"
					return 'death'
				n += 1


class GuessingGame(object):

	def play(self):
		print "There is a new monster giving u instructions here."
		print "U now have 2 guess a number between 1 and 10."
		print "I will tell u higher or lower but u only have 3 guesses."
		print "I am thinking of my number."
		raw_input()
		num = random.randint(1, 10)
		print "Oki now guess."
		g = 0
		while g < 2:
			g += 1
			guess = int(raw_input("-> "))
			if guess < num:
				print "Higher.."
			elif guess > num:
				print "Lower.."
			elif guess == num:
				print "Dammit, you have guessed my number. Oki, proceed."
				return 'bb'
		final_guess = int(raw_input("-> "))
		if final_guess == num:
			print "Dammit, you have guessed my number. Oki, proceed."
			raw_input()
			return 'bb'
		else:
			print "U did not guess da numberrr!!"
			return 'death'


class Death(object):

	def play(self):
		raw_input()
		print "I'm sorry da bb, u didn't make it."
		print "You deaded. I am sad."
		print "I will wait for u..."
		exit(0)


class DeathByChocolate(object):

	def play(self):
		print "A chocolate avalanche comes at you!!"
		print "I guess we know now why this door was brown..."
		raw_input()
		print "You r eat so many."
		print "Da bb... u shouldn't eat this many..."
		raw_input()
		return 'death'


class DeathByMarshmallows(object):

	def play(self):
		print "This room is filled with marshmallows!"
		print "U begin to eat away at them."
		print "Eating... eating.. they r beginnig to clog your airway..."
		raw_input()
		return 'death'


class Animals(object):

	animals = ['pig', 'dog', 'cat', 'horse']
	sounds = ['oink', 'woof', 'meow', 'neigh']

	def play(self):
		print "Aminals! Look, there are some aminals here."
		print "A pink aminal with a curly tail is walking up to u."
		raw_input()
		print "'Woof! Woof!' he says."
		print "Wait... that's not the right sound, is it?"
		raw_input()
		print "Looks like these aminals are confused."
		print "U are going to have to fix their sounds."
		print "Listen to everyone."
		raw_input()
		print "The pink aminal with the curly tail says 'woof'"
		print "The big floofy aminal with the tongue says 'neigh'"
		print "The smaller fuzzy aminal with pointy ears says 'oink'"
		print "The really tall aminal with a long tail sayd 'meow'"
		raw_input()
		print "Ok, now time for the matchy."
		print "But I don't know what the aminals are called, so u first"
		print "have to name all of them in the order I said them.\n"
		an_1 = raw_input("Aminal 1: ").lower()
		an_2 = raw_input("Aminal 2: ").lower()
		an_3 = raw_input("Aminal 3: ").lower()
		an_4 = raw_input("Aminal 4: ").lower()
		animal_guesses = [an_1, an_2, an_3, an_4]
		print "\nAnd now u have to tell them thr right sound they should make.\n"
		so_1 = raw_input("Sound 1: ").lower()
		so_2 = raw_input("Sound 2: ").lower()
		so_3 = raw_input("Sound 3: ").lower()
		so_4 = raw_input("Sound 4: ").lower()
		sound_guesses = [so_1, so_2, so_3, so_4]
		print "\nAccording to my dictionary that just magically appeared,"
		if animal_guesses == self.animals:
			print "U got the aminal names right..."
			if sound_guesses == self.sounds:
				print "...and you got the sounds right too!"
				print "The aminals are all happy again!"
				print "Oki, u r now moving forward."
				raw_input()
				return 'guessinggame'
			else:
				print "...but the sounds are wrong."
				print "This is bad da bb. They r mad now..."
				raw_input()
				return 'death'
		else:
			print "U weren't exactly correct."
			print "This is bad da bb. They r mad now..."
			raw_input()
			return 'death'


class Bb(object):

	def play(self):
		text = open('ex45text.txt', 'r')
		print text.read()
		text.close()
		exit(0)


class WhackAMole(object):
	
	def play(self):
		print "\nThere are 4 holes in front of you."
		print "U see these little critters jumping up and down out of them."
		print "If u an hit 3 out of the next 10 that pop up, u win!"
		raw_input()
		print "Hit a number from 1 to 4!"
		guesses = 0
		wins = 0
		while guesses < 10:
			if wins < 3:
				position = random.randint(1, 4)
				guess = int(raw_input("-> "))
				if guess == position:
					print "Got him!!"
					wins += 1
				else:
					print "Not this time. Try again."
				guesses += 1
			elif wins == 3:
				print "\nLook at u hitting all da moles. U got it!!"
				raw_input()
				return 'bb'
				break
		print "\nOh no the Freddy. U didn't hit enough of da moles."
		raw_input()
		return 'death'



class Scenes(object):

	options = {
		'death': Death(),
		'guessinggame': GuessingGame(),
		'tictactoe': TicTacToe(),
		'room1': Room1(),
		'room2': Room2(),
		'pink': Animals(),
		'green': WhackAMole(),
		'brown': DeathByChocolate(),
		'white': DeathByMarshmallows(),
		'bb': Bb()
	}

	def __init__(self, start_scene):
		self.start_scene = Scenes.options.get(start_scene)

	def next_scene(self, current_scene):
		return Scenes.options.get(current_scene)

	def opening(self):
		return self.next_scene(self.start_scene)

	def go(self):
		current = (self.start_scene).play()
		while True:
			nextscene = self.next_scene(current)
			current = nextscene.play()
			print "--------------------\n"


a = Scenes('room1')
a.go()

















