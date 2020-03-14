from ski import *

seed = 1234
decay = 1000
lr = .1
episodes = 1000

set_seed(seed)
policy = EpsilonGreedy(decay=decay)
agent = [MonteCarlo,Sarsa,QLearning,DoubleQLearning,Sarsa]
method = ['tabular','tabular','tabular','tabular','approx']
for i in range(len(agent)):
    env = Environment(sale=3,wholesale=5,retail=7,r=.1,gamma=1/(1+.1),N=7,M=20,lam=9)
    agent[i] = agent[i](policy=policy,lr=lr,method=method[i])
    agent[i].fit(env,init=True,episodes=episodes)