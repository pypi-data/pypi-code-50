from ski import *

seed = 1234
decay = 1000
lr = .1
episodes = 10000

set_seed(seed)
policy = EpsilonGreedy(decay=decay)
agent = [DoubleQLearning]
method = ['approx']
for i in range(len(agent)):
    env = Environment(sale=3,wholesale=5,retail=7,r=.1,gamma=1/(1+.1),N=7,M=20,lam=9)
    agent[i] = agent[i](policy=policy,lr=lr,method=method[i],degree=5)
    agent[i].fit(env,init=True,episodes=episodes,plot_freq=.5)