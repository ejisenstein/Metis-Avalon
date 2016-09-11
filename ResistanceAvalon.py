""" import libraries """

import random, math

""" define initial lists, dictionaries, and variables """

creationAndQuests = {5 : [[3,2] , [2,3,2,3,3]] , 6 : [[4,2] , [2,3,4,3,4]] , 7 : [[4,3] , [2,3,3,4,4]] , 8 : [[5,3] , [3,4,4,5,5]] , 9 : [[6,3] , [3,4,4,5,5]] , 10 : [[6,4] , [3,4,4,5,5]] , 11 : [[7,4] , [4,5,4,5,5]]}
numberOfPlayers = int(input("How many players will be playing in total (including yourself)? "))
playerOrients = ['good','evil']
gamePlayers = []
goodChars = []
evilChars = []
# possible orients for special characters (subtract 1 from evil for Assassin)
specialOrients = ['good'] + ['evil' for e in range(creationAndQuests[numberOfPlayers][0][1]-2)]
# types of characters - assassin, normal, special
specialEvilOptions = ['mordred','oberon']
chosenEvil = random.choice(specialEvilOptions)
charTypes = ['assassin',chosenEvil] + ['normal' for n in range(creationAndQuests[numberOfPlayers][0][0]-1)] + ['special' for s in range(creationAndQuests[numberOfPlayers][0][1]-1)]
# random human character index generated
humanPlayer = random.randint(1,numberOfPlayers)

""" define general classes """

# parent class for all players (human and computer)
class Players():
	
	def __init__(self,numberPlayer,orient,characterType):
		self.numberPlayer = numberPlayer
		self.orient = orient
		self.characterType = characterType
		if self.characterType == 'oberon':
			self.hiddenOrient = 'good'
		elif self.characterType == 'mordred':
			self.hiddenOrient = 'evil'
		else:
			self.hiddenOrient = 'none'
		
	def vote(self):
		if self.numberPlayer == humanPlayer:
			return (input("\nWill you help make the quest a success or a fail? ")).lower()
		else:
			if self.orient == "evil" or self.hiddenOrient == 'evil':
				return random.choice(["success","fail"])
			else:
				return "success"
			
	def returnIdentity(self):
		if self.orient == 'good':
			return 'Loyal Servant of Arthur'
		else:
			return 'Oberon'
		
	def approveOrReject(self):
		if self.numberPlayer == humanPlayer:
			return (input("Do you approve or reject this quest? ")).lower()
		else:
			if self.characterType == 'normal':
				return random.choice(['approve','reject'])
			else:
				correlation = {'good' : ['reject','approve'] , 'evil' : ['approve','reject']}
				allOrients = []
				for questMember in chooseQuest:
					if questMember.orient == 'evil':
						return correlation[self.orient][0]
					else:
						allOrients.append('good')
				if len(allOrients) == len(chooseQuest):
					return correlation[self.orient][1]

# 1st level descendant class for special characters - assassin, merlin, minion of mordred
class SpecialChars(Players):
	def __init__(self,numberPlayer,orient,characterType):
		Players.__init__(self,numberPlayer,orient,characterType)
		
	def knowledgeOfEvil(self):
		for p in gamePlayers:
			if (self.orient == 'evil' or self.hiddenOrient == 'evil') and (p.characterType == 'mordred' or p.characterType == 'oberon'):
				print("Player " + str(p.numberPlayer) + ": " + p.hiddenOrient)
			else:
				print("Player " + str(p.numberPlayer) + ": " + p.orient)
			
	def returnIdentity(self):
		if self.orient == 'good':
			return 'Merlin'
		else:
			return 'Minion of Mordred'

# 2nd level descendant class for assassin		
class Assassin(SpecialChars):
	def __init__(self,numberPlayer,orient,characterType):
		SpecialChars.__init__(self,numberPlayer,orient,characterType)
		
	def killMerlin(self):
		if self.numberPlayer == humanPlayer:
			return int(input("\nWhich player do you believe to be Merlin? "))
		else:
			return random.choice(goodChars)
			
	def returnIdentity(self):
		return 'Assassin'
		
# 2nd level descendant class for mordred
class Mordred(SpecialChars):
	
	hiddenOrient = 'evil'
	
	def __init__(self,numberPlayer,orient,characterType):
		SpecialChars.__init__(self,numberPlayer,orient,characterType)
		
	def returnIdentity(self):
		return 'Mordred'
	
# create all players and related lists
counter = 1
while len(charTypes) != 0:
	charType = random.choice(charTypes)
	if charType == 'special':
		specialOrientChoice = random.choice(specialOrients)
		newSpecialChar = SpecialChars(counter,specialOrientChoice,charType)
		specialOrients.remove(specialOrientChoice)
		gamePlayers.append(newSpecialChar)
		if specialOrientChoice == 'good':
			goodChars.append(newSpecialChar.numberPlayer)
			merlinIndex = counter-1
		else:
			evilChars.append(newSpecialChar.numberPlayer)
	elif charType == 'normal':
		newPlayer = Players(counter,'good',charType)
		gamePlayers.append(newPlayer)
		goodChars.append(newPlayer.numberPlayer)
	elif charType == 'mordred':
		newMordred = Mordred(counter,'good',charType)
		gamePlayers.append(newMordred)
		goodChars.append(newMordred.numberPlayer)
		evilChars.append(newMordred.numberPlayer)
	elif charType == 'oberon':
		newPlayer = Players(counter,'evil',charType)
		gamePlayers.append(newPlayer)
		evilChars.append(newPlayer.numberPlayer)
	else:
		newAssassin = Assassin(counter,'evil',charType)
		gamePlayers.append(newAssassin)
		assassinIndex = counter-1
		evilChars.append(newAssassin.numberPlayer)
	charTypes.remove(charType)
	counter += 1

# define human player
humanChar = gamePlayers[humanPlayer-1]
print("\nYou are " + humanChar.returnIdentity() + " and Player " + str(humanPlayer) + " in the circle.\n")

allowedKnowledgeOfEvil = ['special','assassin','mordred']
if humanChar.characterType in allowedKnowledgeOfEvil:
	humanChar.knowledgeOfEvil()
	
for l in gamePlayers:
	print(l.numberPlayer,l.characterType,l.orient,l.hiddenOrient)
		
# define specific rotating class - quest leader
class Leader(Players):
	def __init__(self,numberPlayer,orient,characterType):
		Players.__init__(self,numberPlayer,orient,characterType)
		
	def pickQuest(self,numberQuest):
		# append quest members to quest list
		questMembers = []
		goodCharsTemp = list(goodChars)
		evilCharsTemp = list(evilChars)
		gamePlayersTemp = list(gamePlayers)
		if self.numberPlayer == humanPlayer:
			for questers in range(creationAndQuests[numberOfPlayers][1][numberQuest]):
				newQuester = int(input("Name one player whom you would recommend for this quest: "))
				questMembers.append(gamePlayersTemp[newQuester-1])
		else:
			if self.orient == 'good' and self.characterType != 'Merlin':
				for questers in range(creationAndQuests[numberOfPlayers][1][numberQuest]):
					newQuester = random.choice(gamePlayersTemp)
					questMembers.append(newQuester)
					gamePlayersTemp.remove(newQuester)
			elif self.characterType == 'Merlin':
				for questers in range(creationAndQuests[numberOfPlayers][1][numberQuest]):
					newQuester = random.choice(goodCharsTemp)
					questMembers.append(gamePlayersTemp[newQuester-1])
					goodCharsTemp.remove(newQuester)
			else:
				guaranteedEvil = random.choice(evilCharsTemp)
				questMembers.append(gamePlayersTemp[guaranteedEvil-1])
				evilCharsTemp.remove(guaranteedEvil)
				gamePlayersTemp.remove(gamePlayers[guaranteedEvil-1])
				for questers in range(creationAndQuests[numberOfPlayers][1][numberQuest]-1):
					newQuester = random.choice(gamePlayersTemp)
					questMembers.append(newQuester)
					gamePlayersTemp.remove(newQuester)
		return questMembers

# game loop 
resultSequence = []
numberOfFails = 0
numberOfSuccesses = 0
leaderCounter = 0
keepingTrack = {}
for quest in range(5):
	trialCounter = 0
	acceptances = 0
	# do not continue until quest is approved, but only allow a limited number of repeats
	while acceptances < numberOfPlayers/2 and trialCounter < 5:
		acceptances = 0
		# cycle around the circle
		if leaderCounter == numberOfPlayers:
			leaderCounter = 0
		leaderIndex = gamePlayers[leaderCounter]
		newLeader = Leader(leaderIndex.numberPlayer,leaderIndex.orient,leaderIndex.characterType)
		print('\n' + '*' * 30)
		print("\nRound " + str(quest+1) + ":\nNew Leader - " + str(newLeader.numberPlayer) + "\nQuest Members (" + str(creationAndQuests[numberOfPlayers][1][quest]) + " total): ")
		# leader picks quest members
		chooseQuest = newLeader.pickQuest(quest)
		# display prospective quest members
		for eachMember in chooseQuest:
			print("Player " + str(eachMember.numberPlayer)),
		print()
		# display each player reaction to new quest
		for playerIndex in gamePlayers:
			playerInput = playerIndex.approveOrReject()
			print("Player " + str(playerIndex.numberPlayer) + ": " + playerInput)
			if playerInput == 'approve':
				acceptances += 1
		# break out of the loop if there are enough acceptances
		if acceptances >= math.ceil(float(numberOfPlayers)/2):
			trialCounter = 5
		trialCounter += 1
		leaderCounter += 1
	# end game in favor of Evil if 5 or more leaders in a round
	if trialCounter == 5:
		print('\nEvil has overcome the Good in Camelot because the questing process has been delayed five times!')
		break
	# collect and display quest results - success vs. failure
	questResults = []
	for finalQuestMember in chooseQuest:
		questResults.append(finalQuestMember.vote())
	print("\nQuest Results: ")
	for result in questResults:
		print(result)
	# determine if the quest has failed or succeeded
	failCount = 0
	for product in questResults:
		if product == 'fail':
			failCount += 1
	if quest == 3 and numberOfPlayers >= 7:
		if failCount >= 2:
			resultSequence.append('fail')
			numberOfFails += 1
		else:
			resultSequence.append('success')
			numberOfSuccesses += 1
	else:
		if 'fail' in questResults:
			resultSequence.append('fail')
			numberOfFails += 1
		else:
			resultSequence.append('success')
			numberOfSuccesses += 1
	# display overall result history
	print('\nProgress:')
	for result in resultSequence:
		print(result)
	# if game ends, show Evil characters
	if numberOfFails == 3 or numberOfSuccesses == 3:
		print('\nEvil Characters Revealed: ')
		for evilChar in evilChars:
			print('Player ' + str(evilChar) + " as " + gamePlayers[evilChar-1].returnIdentity())
	if numberOfFails == 3:
		print("\nEvil has overcome the Good in Camelot!")
		break
	# if Good wins, allow Evil 1 last chance to guess Merlin's identity and win
	if numberOfSuccesses == 3:
		print("\nGood has successfully defended Camelot from the forces of Evil!")
		lastChance = gamePlayers[assassinIndex].killMerlin()
		print('\nPlayer ' + str(assassinIndex+1) + ' says: We think Merlin is Player ' + str(lastChance) + '.')
		if lastChance == merlinIndex+1:
			print("\nBecause Assassin has guessed Merlin's identity correctly, Evil now prevails over Camelot.")
		else:
			print("\nBecause Assassin has guessed Merlin's identity incorrectly, Good remains the dominant force in Camelot.")
		print('\nMerlin is Player ' + str(merlinIndex+1) + '.')
		break
