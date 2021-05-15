import random,json
from wiggleface import *
w = wiggleface()

"""
GOLD. Get all the gold to win.
Rhema Linder, 4/26/2021
Uses WiggleFace: https://github.com/AZHenley/wiggleface
"""

game_maps = []


game_maps +=  ["----------------\n"
		+     "----------------\n"
		+     "----------------\n"
		+     "----------------\n"
		+     "----------------\n"
		+     "----------------\n"
		+     "----------------\n"
		+     "----------------\n"
		+     "-x----------o---\n"
		+     "----------------\n"
		+     "----------------\n"
		+     "----------------\n"
		+     "----------------\n"
		+     "----------------\n"
		+     "----------------\n"
		+     "----------------"]


game_maps +=  ["----------------\n"
		+     "----------------\n"
		+     "----------------\n"
		+     "-------x--------\n"
		+     "----------------\n"
		+     "----------------\n"
		+     "----------------\n"
		+     "----------------\n"
		+     "----------------\n"
		+     "----------------\n"
		+     "-------o--------\n"
		+     "----------------\n"
		+     "----------------\n"
		+     "----------------\n"
		+     "----------------\n"
		+     "----------------"]

game_maps +=  ["................\n"
		+     "......x.........\n"
		+     ".....---........\n"
		+     ".....---........\n"
		+     ".....---........\n"
		+     ".....---........\n"
		+     ".....---........\n"
		+     ".....---........\n"
		+     ".....---........\n"
		+     ".....---........\n"
		+     ".....---........\n"
		+     ".....---........\n"
		+     ".....---........\n"
		+     ".....---........\n"
		+     "......o.........\n"
		+     "................"]


game_maps +=  ["x------.........\n"
		+     "......-.........\n"
		+     "......-.........\n"
		+     "......-----.....\n"
		+     "..........-.....\n"
		+     "..........-.....\n"
		+     "..........-.....\n"
		+     "..........-.....\n"
		+     "..........--....\n"
		+     "...........----o\n"
		+     "................\n"
		+     "................\n"
		+     "................\n"
		+     "................\n"
		+     "................\n"
		+     "................"]

game_maps +=  ["--x-------------\n"
		+     "----------------\n"
		+     "-----...........\n"
		+     "----------------\n"
		+     "............----\n"
		+     "----------------\n"
		+     "----------------\n"
		+     "----------------\n"
		+     ".............---\n"
		+     "----------------\n"
		+     "---.............\n"
		+     "----------------\n"
		+     ".............---\n"
		+     "----------------\n"
		+     "---.............\n"
		+     "------------o---"]

game_maps +=  ["................\n"
		+     ".---------.----.\n"
		+     ".-.....---.----.\n"
		+     ".-.----x--......\n"
		+     ".-.---.-.-.----.\n"
		+     ".-.---.-.-.----.\n"
		+     ".-.---.-.-.----.\n"
		+     ".-.---.-.-.----.\n"
		+     ".-.....-.-.----.\n"
		+     ".-.---...-.----.\n"
		+     ".-.--..o.-.----.\n"
		+     ".-.--..-.-.----.\n"
		+     ".-.--..-.-.----.\n"
		+     ".-.--..-...----.\n"
		+     ".---.-----.----.\n"
		+     "................"]


game_maps +=  ["----------------\n"
		+     "--..........-.--\n"
		+     "---.---------.--\n"
		+     "---.---------.--\n"
		+     "---.---------.--\n"
		+     "---.---------.--\n"
		+     "---.---------.--\n"
		+     "---.-------...--\n"
		+     "-x-.-------.o---\n"
		+     "---.-------...--\n"
		+     "---.---------.--\n"
		+     "---.---------.--\n"
		+     "---.---------.--\n"
		+     "---.---------.--\n"
		+     "-.............--\n"
		+     "----------------"]


game_maps +=  ["----------------\n"
		+     "--.---.---------\n"
		+     "--.---.---------\n"
		+     "--.---.---------\n"
		+     "--.-.-.---------\n"
		+     "--..-..---------\n"
		+     "--.---.---------\n"
		+     "--------.-------\n"
		+     "--------.-------\n"
		+     "--------.-------\n"
		+     "--------.-------\n"
		+     "----------.---.-\n"
		+     "----------..--.-\n"
		+     "----------.-.-.-\n"
		+     "----------.--..-\n"
		+     "----------.---.-"]


# w.delayMax = 30
# w.delay = w.delayMax
w.fillWiggle(False)
w.fillColor(-1)
fallthings = []
dude = {"x":0,"y":0}
cooldown_frames = 25
w.last_update_at = 0
w.gameCursor = 0

def setScreenTo(gamestring):
	rows = gamestring.split("\n")
	#iterate over each row
	for i in range(0,16):
		row = rows[i]
		for j in range(0,16):
			char = row[j]
			if char == "-":
				w.grid[j][i] = (-1,False)#Blank clear space
			if char == ".":
				w.grid[j][i] = (0,False)#White wall
			if char == "x":
				w.grid[j][i] = (1,False)#Red player
				dude["x"] = j
				dude["y"] = i
			if char == "o":
				w.grid[j][i] = (3,True)#GOLD spinner

	return True

def init():
	setScreenTo(game_maps[0])
	# last_update_at = w.time
def update():
	if w.gameCursor == len(game_maps):
		return
	x = int(random.random()*16)
	y = int(random.random()*16)
	dirty = False
	may_update = False
	if (w.time - w.last_update_at) > cooldown_frames:
		may_update = True
	else:
		return
	# try to move dude
	new_spot = json.loads(json.dumps(dude))
	if w.keys[w.Key_Left]:
		new_spot["x"] -= 1
		dirty = True
	if w.keys[w.Key_Right]:
		new_spot["x"] += 1
		dirty = True
	if w.keys[w.Key_Up]:
		new_spot["y"] -= 1
		dirty = True
	if w.keys[w.Key_Down]:
		new_spot["y"] += 1
		dirty = True
	#check new spot is valid
	if dirty and new_spot["x"] >= 0 and new_spot["x"] <= 15 and new_spot["y"] >= 0 and new_spot["y"] <= 15 and (w.grid[new_spot["x"]][new_spot["y"]][0] == -1 or w.grid[new_spot["x"]][new_spot["y"]][0] == 3):
		#did we win?
		win = w.grid[new_spot["x"]][new_spot["y"]][0] == 3
		#undraw
		w.grid[dude["x"]][dude["y"]] = (-1,False)
		w.grid[new_spot["x"]][new_spot["y"]] = (1,False)
		dude["x"] = new_spot["x"]
		dude["y"] = new_spot["y"]
		w.last_update_at = w.time
		if win:
			print("win!")
			w.gameCursor += 1
			setScreenTo(game_maps[w.gameCursor])

w.start(init, update)