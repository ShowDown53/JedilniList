#!/usr/bin/env python
# -*- coding: utf-8 -*-
jedList = {}

while True:
    jedi = raw_input("Vnesi ime jedi: ")
    cena = raw_input("Vnesi ceno za '%s': " % jedi)

    jedList[jedi] = cena

    novaJed = raw_input("Želiš vnesti še eno jed? (da/ne) ")
    if  novaJed.lower() == "ne" or  novaJed.lower() == "n":
        break

print "Jedilni list"
i = 1
for key, value in jedList.iteritems():
    print(str(i) + ". " + key + " " + value + " " + "EUR")
    i += 1

with open("JedilniList.txt", "w+") as JedilniList:
    JedilniList.write("Jedilni list\n")
    i = 1
    for key, value in jedList.iteritems():
        JedilniList.write(str(i) + ". " + key + " " + value + " " + "EUR" + "\n")
        i += 1

print "Jedilni list je shranjen v datoteki 'JedilniList.txt'"