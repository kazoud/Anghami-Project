import requests
import pprint
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import fft
import numpy as np




headers1 = {'XAT': 'interns', 'XATH' : 'c497b2f056036c83f176a691'}

arab_trends = requests.get('https://bus.anghami.com/public/trending?music_language=1', headers = headers1)

international_trends = requests.get('https://bus.anghami.com/public/trending?music_language=2', headers = headers1)

arab_songs = []

international_songs = []

for i in range(len(arab_trends.json())):
    song = arab_trends.json()[i]['title']
    arab_songs.append(song)


for j in range(len(international_trends.json())):
    song = international_trends.json()[j]['title']
    international_songs.append(song)


print(arab_songs)
print(international_songs)
pprint.pprint(international_trends.json())

