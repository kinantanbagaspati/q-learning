import random
import math

episodes = 10000
max_steps = 100
max_reward = 5
start_state = 3
min_reward = -999999
rewards = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
q_table = [{} for i in range(10)]
q_table[0][1] = 0
for i in range(1, 9):
    q_table[i][i-1] = 0
    q_table[i][i+1] = 0
q_table[9][8] = 0

learning = 0.1
discount = 0.1
exploration_rate = 1.0
exploration_decay_rate = 0.01
min_exploration_rate = 0.01

reward_avg = 0
for episode in range(episodes):
    steps = 0
    state = start_state
    reward = 0
    while(abs(reward)<max_reward and steps<max_steps):
        rand = random.uniform(0,1)
        new_state = state
        max_value = min_reward
        #Bakal eksploit
        for key in q_table[state].keys():
            if(max_value < q_table[state][key]):
                max_value = q_table[state][key]
                new_state = key
        if(rand < exploration_rate): #Bakal eksplor
            keys = list(q_table[state].keys())
            rand = random.randint(0, len(keys)-1)
            new_state = keys[rand]

        max_value = min_reward
        for key in q_table[new_state].keys():
            if(max_value < q_table[new_state][key]):
                max_value = q_table[new_state][key]
            
        q_table[state][new_state] = q_table[state][new_state]*(1 - learning) + learning*(rewards[new_state] + discount * max_value)
        state = new_state
        reward += rewards[new_state]
        steps += 1
    
    #decay
    exploration_rate = min_exploration_rate + (1 - min_exploration_rate) * math.exp(-exploration_decay_rate*episode)
    reward_avg += reward

    if((episode+1)%1000 == 0):
        print("Episode", str(episode+1), "kelar dengan rata-rata:", str(reward_avg/1000))
        reward_avg = 0

print(q_table)
    