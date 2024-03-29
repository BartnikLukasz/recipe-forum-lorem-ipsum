import itertools

from lorem import get_paragraph, get_sentence
import os
import random

def random_combination_ingredients(ilosci, miary, produkty):
    ingredients_string = ''
    for x in range(random.randint(4, 10)):
        ilosc = random.choice(ilosci)
        miara = random.choice(miary)
        produkt = random.choice(produkty)
        ingredients_string += f"{ilosc} {miara} {produkt}, "
    ingredients_string += "\n"
    return ingredients_string

def random_combination_tags(tags):
    s = []
    length = random.randint(2, 5)
    for x in range(length):
        s.append(random.choice(tags))
    return ' '.join(s) + "\n"


tagsStr = "banany boczek budyń bulion buraki cebula cukier cukier puder cukinia cynamon cytryna czekolada czekolada gorzka czosnek dania wigilijne dla dzieci drożdże dynia feta galaretka grzyby jabłka jajka jogurt kakao kapusta koperek kukurydza kurczak majonez mąka pszenna mąka pszenna tortowa makaron maliny marchew mascarpone masło masło klarowane miód mleko mozzarella musztarda natka pietruszki ogórki olej roślinny oliwa orzechy orzechy włoskie papryka parmezan pieczarki piersi kurczaka pietruszka pomidory pomysł na obiad pomysł na śniadanie rodzynki ryż seler ser żółty sezam skrobia ziemniaczana śledź śliwki śmietana śmietanka szczypiorek szpinak szybki obiad szynka truskawki twaróg wieprzowina wołowina ziemniaki"
tags = tagsStr.split()

ilosci = "1/4 1/3 1/2 1 2 3 4 5 6 jedna jeden dwa trzy pół półtora".split()
miary = "łyżeczki łyżki szczypty sztuki szklanki kg ml l g krople cm".split()
produkty = "mąka jajka masło olej cukier sól pieprz mleko śmietana ser twaróg jogurt kefir miód dżem chleb bułki makaron ryż kasza płatki musli orzechy rodzynki mięso kiełbasa szynka boczek parówki ryba tuńczyk łosoś dorsz śledź warzywa pomidor ogórek marchew kapusta ziemniak owoce jabłko banan gruszka pomarańcza cytryna przyprawy papryka kurkuma bazylia sosy ketchup musztarda majonez chrzan napoje woda sok herbata kawa piwo".split()

tagsFile = open("tags.txt", "w")
print("Tags:")
for i in range(100):
    print("{}%".format(i))
    for j in range(1000):
        tagsFile.write(random_combination_tags(tags))
tagsFile.close()

ingredients = open("ingredients.txt", "w")
print("Ingredients:")
for i in range(100):
    print("{}%".format(i))
    for j in range(1000):
        ingredients.write(random_combination_ingredients(ilosci, miary, produkty))
ingredients.close()

content = open("content.txt", "w")
for i in range(100):
    print("{}%".format(i))
    content.write(get_paragraph(count=1000, comma=(0, 4), word_range=(10, 20), sentence_range=(20, 25), sep=os.linesep).replace("\n", ""))
    content.write("\n")
content.close()

title = open("title.txt", 'w')
for i in range (100):
    print("{}%".format(i))
    title.write(get_sentence(count=1000, comma=(0,2), word_range=(3, 5), sep=os.linesep).replace("\n", ""))
    title.write("\n")
title.close()

comment = open("comment.txt", "w")
for i in range(100):
    print("{}%".format(i))
    comment.write(get_paragraph(count=5000, comma=(0, 2), word_range=(4, 10), sentence_range=(1, 5), sep=os.linesep).replace("\n", ""))
    comment.write("\n")
comment.close()

description = open("description.txt", "w")
for i in range(100):
    print("{}%".format(i))
    description.write(get_paragraph(count=2, comma=(0, 2), word_range=(6, 12), sentence_range=(3, 6), sep=os.linesep).replace("\n", ""))
    description.write("\n")
description.close()
