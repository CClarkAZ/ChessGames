import json
from collections import defaultdict
import datetime
import matplotlib.pyplot as plt 
import matplotlib.mlab as mlab
from scipy.stats import norm
import numpy as np
from pprint import pprint



with open('JuliusDLUser.json') as data_file:
	user_info = json.load(data_file)

with open('gamelist.json') as game_file:
	game_list = json.load(game_file)

results = defaultdict(int)
num_moves = defaultdict(int)
opening = defaultdict(int)


for index, game in enumerate(game_list['list']):
	results[game['status']] += 1
	num_moves[game['turns']] += 1
	if 'opening' in game:
		opening[game['opening']['code']] += 1


#start move analysis

mu, sigma = norm.fit(num_moves.keys())

plt.xlabel('Number of Moves')
plt.ylabel('Frequency')
plt.title(r'$\mathrm{Histogram\ of\ Chess\ moves:} \ \mu=%.2f,\ \sigma=%.2f$' % (mu, sigma))

for key, val in num_moves.items():
	num_moves[key] =  float(val) / 200

binwidth = 15



n, bins, patches = plt.hist(num_moves.keys(), bins=np.arange(min(num_moves), max(num_moves) + binwidth, binwidth), facecolor='green', normed=True, alpha=0.75)
y = mlab.normpdf(bins, mu, sigma)
l = plt.plot(bins, y, 'r--', linewidth=1)
plt.axis([2, 220, 0, 0.015])
plt.grid(True)
plt.xticks(range(min(num_moves.keys()), max(num_moves.keys()), 15))
plt.savefig("MoveHisto.pdf")

plt.clf()

# end move analysis
# start opening analysis
fig = plt.figure(figsize=(20,8))
plt.bar(range(0, len(opening.keys())), height=opening.values(), width=0.5)
plt.xticks(range(0, len(opening.keys())), opening.keys())
plt.axis([-1, len(opening.keys()), 0, 32])
plt.grid(True)
plt.show()
