# -*- coding: utf-8 -*-

from lxml import html
import requests
import json

fjoldiFugla = 83

url = "https://fuglavefur.is/birdinfo.php?val=1&id="
currfuglNafn = ""
hljod = "https://fuglavefur.is/audio/"+ currfuglNafn +".ogg"
mynd = "https://fuglavefur.is/"

allBirds = []

for i in range(1, fjoldiFugla+1):
    page = requests.get(url + str(i))
    tree = html.fromstring(page.content)
    currfugl = tree.xpath('//h1[@class="pictText"]')[0]
    # print(currfugl)

    # það er eitthvað leiðinlegt new line þarna
    currfuglNafn = tree.xpath('//h1[@class="pictText"]/text()')[0].split("\n")[1]
    par = currfugl.getparent()
    # print(html.tostring(par, pretty_print=True))
    myndurl = par.get("data-image")
    imgUrl = mynd + myndurl
    soundName = myndurl.split("/")[2].split(".")[0].lower()
    str2 = "0123456789"
    soundName = ''.join(c for c in soundName if c not in str2)
    print('soundName '+soundName)

    # sum audio nofn eru rong, tharf ad amnually ad setja semi,
    if currfuglNafn == 'Hrossagaukur':
        soundName = 'hrossagaukur'
    if soundName == 'heidlo':
        soundName = 'heidloa'

    # passa uppa isl stafi
    soundName = ''
    dict = {'ó':'o', 'ö':'o', 'þ':'th', 'ý':'y', 'í':'i', 'ð':'d', 'ú': 'u','æ':'ae', 'á':'a', 'é':'e'}
    for char in currfuglNafn.lower():
        if char in dict:
            soundName += dict[char]
        else:
            soundName += char
    print('soundName '+soundName)
    if soundName == 'hettumafur':
        soundName = 'hettumavur'
    elif soundName == 'silamafur':
        soundName = 'silamavur'


    hljod = 'https://fuglavefur.is/audio/'+ soundName +".ogg"
    print(currfuglNafn)

    print(imgUrl)
    print(hljod)
    print()
    bird = {
    "imgUrl":imgUrl,
    "name":currfuglNafn,
    "soundUrl":hljod
    }
    allBirds.append(bird)

with open('data.json', 'w', encoding='utf-8') as outfile:
    json.dump(allBirds, outfile, ensure_ascii=False)
