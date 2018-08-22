#! /usr/bin/python3
import random
from mastodon import Mastodon

dformats = [
		"English: \'{}.\'\nEsperanto: \'{}\'",
		"English: \'{}.\'\nEsperanto: \'{}\'",
		"English: \'{}.\'\nEsperanto: \'{}\'",
		"English: \'{}.\'\nEsperanto: \'{}\'",
		"English: \'{}.\'\nEsperanto: \'{}\'",
		"Instead of \'{}\', try saying \'{}\'",
		"The Esperanto for \'{}\' is \'{}\'",
		"The Esperanto for \'{}\' is \'{}\'",
		"The Esperanto for \'{}\' is \'{}\'",
		"{} = {}",
		"{} = {}",
		"Esperanto: \'{1}\'\nEnglish: \'{0}.\'"
	]

with open("wl.txt", encoding="utf-8-sig") as f:
    content = f.readlines()

wl = [x.strip() for x in content]

l = len(wl)
dl = len(dformats)
r = random.randint(0, l - 1)
dr = random.randint(0, dl - 1)

wpair = wl[r].split(" = ")
eng = wpair[0]
esp = wpair[1].capitalize()

fstr = dformats[dr]
tstr = fstr.format(eng, esp)
print(tstr)


mastodon = Mastodon(
    access_token = "vortaro.secret",
    api_base_url = "https://botsin.space"
)

mastodon.toot(tstr)
