import urllib2

games = urllib2.urlopen('http://en.lichess.org/api/game?username=JuliusDL&rated=1&nb=1000&with_opening=1').read()

f = open('gameList.json', 'w')
f.write(games)
f.close()

