greedy = "Greedy Solver"
hamilton = "Hamiltonsolver"

# Define game modes
class gameMode:
    Normal = "Normal"
    Hard = "Hard"

normal = gameMode.Normal

# Create configuration object
conf = Game.conf()
conf.solver_name = hamilton
conf.mode = normal

print("solve0: %s" % conf.solver_name)
print("Mode: %s" % conf.mode)

conf.run()
 
