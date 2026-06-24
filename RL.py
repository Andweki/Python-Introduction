import random #it allows us to generate a list of random choices
#A list of actions that AI can choose from in the game

actions = ["Attack", "Defend", "Heal"]

#restore total rewards collected for each action
total_reward = {"Attack":0, "Defend":0, "Heal":0}

#store how many times each action has been used
count = {"Attack":0, "Defend":0, "Heal":0}

#The game system. Create a function that gives different rewards depending on the action chosen
def game_reward(action):
    #if the AI choses attack
    if action == "Attack":
        return random.randint(5,10)
    #if the AI choses defend
    elif action == "Defend":
        return random.randint(2,6)
    #if the AI choses defend
    else:
        return random.randint(4,8)

#Training phase(exploration)
#Repeat the learning process 100 times

for i in range(100):
    #AI randomly selects an action
    action = random.choice(actions)

    #Get rewards based on actions
    reward = game_reward(action)

    #Add reward to total score of that action
    total_reward[action] += reward

    #Increases count of number of times action is taken
    count[action] += 1

#Calculation phase (Learning output)
#Create an empty dictionary to store averages
avg={}
#Loog through each action to calculate its average reward
for a in actions:
    avg[a] = total_reward[a] / count[a]

#Results
print("Learning results:\n")

# print average for each action
for a in avg:
    print(a, ":", round(avg[a],2))

#Print best action (highest average reward)
print("\nBEST ACTION:", max(avg, key=avg.get))


