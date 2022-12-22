import random

class Player:
	def __init__(self):
#		self.name = ""
		self.hp = 100
		self.ammo = 0
		self.isBlock = False
#	def get_name(self):
#		self.name = input("ENTER CHARACTER NAME: ")
#		print(self.name)
	def reload(self):
		self.isBlock = False
		self.ammo += 1
	def shoot(self):
		if self.ammo <= 0:
			self.reload()
		else:
			self.ammo -= 1
			if enemy.isBlock == True:
				print("[ENEMY] BLOCKED.")
			else:
				enemy.hp -= 25
				print("[ENEMY] TAGGED.")
	def block(self):
		self.isBlock = True
	def stats(self):
		print("---STATS:-- \n HP:", self.hp," \n AMMO:", self.ammo, " \n ENEMY HP:", enemy.hp, "\n ENEMY AMMO:", enemy.ammo, "\n =======")
	def death(self):
		self.hp = 0
		print("DEFEAT. PLAYER HAS BEEN SHOT BY [ENEMY].")

class Enemy:
	def __init__(self):
		self.hp = 100
		self.ammo = 0
		self.isBlock = False
	def reload(self):
		self.isBlock = False
		self.ammo += 1
	def shoot(self):
		if self.ammo >= 0:
			self.reload()
		else:
			self.ammo -= 1
			player.hp -= 25
	def block(self):
		self.isBlock = True
	def death(self):
		self.hp = 0
		print("VICTORY. PLAYER KILLED [ENEMY]")


player = Player()
enemy = Enemy()

def enemytype():
	spec = random.randint(1,3)
def enemybehavior():
	chance = random.randint(1,100)
	if spec == 1:
		if player.ammo > 1:
			if chance < 71:
				return "b"
			elif 70 < chance > 76:
				return "r"
			else:
				return "s"
		else:
			if chance < 61:
				return "b"
			elif 60 < chance > 71:
				return "r"
			else:
				return "s"
	elif spec == 2:
		pass
	else:
		pass


while player.hp > 0 and enemy.hp > 0:
	choice = input("((s)hoot / (b)lock / (r)eload) ")
	if choice == "s":
		player.shoot()
	elif choice ==  "b":
		player.block()
	elif choice ==  "r":
		player.reload()
	else:
		print("ENTER s,b  OR  r  (NO CAPS)")
	player.stats()


if player.hp > 0:
	enemy.death()
elif player.hp <= 0:
	player.death()
else:
	print("DRAW?!?!?")

