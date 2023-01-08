import random

class Character:
	def __init__(self, name):
		self.hp = 100
		self.ammo = 0
		self.isBlock = False
		self.name = name
	def set_opponent(self, opponent):
		self.opponent = opponent
	def reload(self):
		self.isBlock = False
		self.ammo += 1
	def shoot(self):
		if self.ammo <= 0:
			self.reload()
		else:
			self.ammo -= 1
			if self.opponent.isBlock == True:
				print(self.opponent.name + " BLOCKED.")
			else:
				self.opponent.hp -= 25
				print(self.opponent.name + " TAGGED.")
	def block(self):
		self.isBlock = True
	def death(self):
		self.hp = 0

class Player(Character):
	def stats(self):
		print("---STATS:-- \n HP:", self.hp," \n AMMO:", self.ammo, " \n ENEMY HP:", enemy.hp, "\n ENEMY AMMO:", enemy.ammo, "\n =======")
	def death(self):
		super().death()
		print("DEFEAT. " + self.name + " HAS BEEN SHOT BY " + self.opponent.name + ".")

class Enemy (Character):
	def death(self):
		super.death()
		print("VICTORY. " + self.opponent.name + " KILLED " + self.name + ".")


player = Player("PLAYER")
enemy = Enemy("ENEMY")

player.set_opponent(enemy)
enemy.set_opponent(player)

spec = 0

def enemytype():
	global spec
	spec = random.randint(1,3)
def enemybehavior():
	chance = random.randint(1,100)
	if spec == 1:
		if player.ammo > 1:
			if chance < 71:
				return "b"
			elif 70 < chance < 76:
				return "r"
			else:
				return "s"
		else:
			if chance < 61:
				return "b"
			elif 60 < chance < 71:
				return "r"
			else:
				return "s"
	elif spec == 2:
		if chance < 71:
			return "s"
		elif 70 < chance < 91:
			return "b"
		else:
			return "r"
	else:
		if chance < 51:
			return "s"
		elif 50 < chance < 76:
			return "b"
		else:
			return "r"


while player.hp > 0 and enemy.hp > 0:
	enemytype()
	choice = input("((s)hoot / (b)lock / (r)eload) ")
	while(True):
		if choice == "s":
			player.shoot()
			break
		elif choice ==  "b":
			player.block()
			break
		elif choice ==  "r":
			player.reload()
			break
		else:
			print("ENTER s,b  OR  r  (NO CAPS)")
		choice = input("((s)hoot / (b)lock / (r)eload) ")
	enemychoice = enemybehavior()
	if enemychoice == "s":
		enemy.shoot()
	elif enemychoice ==  "b":
		enemy.block()
	elif enemychoice == "r":
		enemy.reload()
	else:
		print("oops")

	player.stats()


if player.hp > 0:
	enemy.death()
elif player.hp <= 0:
	player.death()
else:
	print("DRAW?!?!?")

