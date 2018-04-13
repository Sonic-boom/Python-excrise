from urllib import request
import pickle
def get_challenge(s):
    return request.urlopen('http://www.pythonchallenge.com/pc/' + s).read()
banner = get_challenge('def/banner.p')
print(banner[:60])
data = pickle.loads(banner)
print(data)
print('\n'.join([''.join([p[0] * p[1] for p in row]) for row in data]))