#!/usr/bin/env python
# coding: utf-8

# In[5]:


import import_ipynb
from rooms import Room
import environment.support as support
import environment.inventory as inventory
import traceback
import environment.strings as strings
import sys
import time


# In[ ]:


#Defining rooms, their connections, then running the starting room

class SampleRoom:
    def runRoom(isRepeat):
        messages = strings.sampleRoom
        people = {}
        items = {}
        interactions = {}
        if not support.Inventory.inventory.get("Gun"):
            items["gun"] = strings.gun
        if not support.globalFlags.get("Bob"):
            people["Bob"] = strings.Bob
        if not support.globalFlags.get("Bob2"):
            people["Bob2"] = strings.Bob2
        if not support.globalFlags.get("moveWest"):
            interactions["moveWest"] = strings.moveWest
        return Room(messages, people, items, interactions, isRepeat = isRepeat).runRoom()
    
class SampleRoom2:
    def runRoom(isRepeat):
        messages = strings.sampleRoom2
        people = {}
        items = {}
        interactions = {}
        if support.Inventory.inventory.get("Gun") and not support.globalFlags.get("target"):
            interactions["shootTarget"] = strings.shootTarget
        interactions["moveEast"] = strings.moveEast
        return Room(messages, people, items, interactions, isRepeat = isRepeat).runRoom()
    
class Meadows:
    def runRoom(isRepeat):
        messages = strings.meadows
        people = {}
        items = {}
        interactions = {}
        if all(support.globalFlags.get("poemLines")) and support.globalFlags.get("finalScene") == 0:
            support.globalFlags["finalScene"] = 1
        interactions["Dancing Cave"] = strings.moveDancingCave
        interactions["Summer House"] = strings.moveSummerHouse
        return Room(messages, people, items, interactions, isRepeat = isRepeat).runRoom()
    
class DancingCave:
    def runRoom(isRepeat):
        messages = strings.dancingCave
        people = {}
        items = {}
        interactions = {}
        interactions["Meadows"] = strings.moveMeadows
        interactions["Mist Machine"] = strings.moveMistMachine
        if support.Inventory.inventory.get("Consumable Goods") and support.globalFlags.get("dancingBoyPhase"):
            interactions["Return Consumables"] = strings.returnGoods
        if not support.globalFlags.get("dancingBoyPhase"):
            people["Dancing Boy"] = strings.dancingBoy
        elif support.globalFlags.get("dancingBoyPhase") == 2 and all(support.globalFlags.get("poemLines")) and support.globalFlags.get("finalScene") == 1:
            people["Dancing Boy"] = strings.dancingBoy3
        else:
            people["Dancing Boy"] = strings.dancingBoy2
        return Room(messages, people, items, interactions, isRepeat = isRepeat).runRoom()
    
class MistMachine:
    def runRoom(isRepeat):
        messages = strings.mistMachine
        people = {}
        items = {}
        interactions = {}
        interactions["Dancing Cave"] = strings.moveDancingCave
        if not isRepeat:
            people["Dancing Boy"] = strings.dancingBoy4
        else:
            people["Dancing Boy"] = strings.dancingBoy5
            interactions["Mist Machine Box"] = strings.mistMachineBox
        return Room(messages, people, items, interactions, isRepeat = isRepeat).runRoom()
    
class SummerHouse:
    def runRoom(isRepeat):
        messages = strings.summerHouse
        people = {}
        items = {}
        interactions = {}
        interactions["Meadows"] = strings.moveMeadows2
        interactions["Ruins Library"] = strings.moveRuinsLibrary
        interactions["Mistmoss"] = strings.mistmoss
        if not support.Inventory.inventory.get("Artisanal Contract"):
            interactions["Artisanal Contract"] = strings.artisanalContract
        interactions["Stone Grave"] = strings.moveStoneGrave
        return Room(messages, people, items, interactions, isRepeat = isRepeat).runRoom()
    
class StoneGrave:
    def runRoom(isRepeat):
        messages = strings.stoneGrave
        people = {}
        items = {}
        interactions = {}
        interactions["Summer House"] = strings.moveSummerHouse
        interactions["Stone Grave stones"] = strings.stoneGraveStones
        return Room(messages, people, items, interactions, isRepeat = isRepeat).runRoom()
    
class RuinsLibrary:
    def runRoom(isRepeat):
        messages = strings.ruinsLibrary
        people = {}
        items = {}
        interactions = {}
        interactions["Summer House"] = strings.moveSummerHouse
        interactions["Ruins Factory"] = strings.moveRuinsFactory
        if all(support.globalFlags.get("poemLines")) and not support.Inventory.inventory.get("Black Book"):
            items["Book"] = strings.enlightenedBook
        elif not support.Inventory.inventory.get("White Book"):
            items["Book"] = strings.unenlightenedBook
        if not support.globalFlags.get("skullListened"):
            interactions["Skull"] = strings.skull
        if not support.Inventory.inventory.get("Consumable Goods") and not support.globalFlags.get("returnedConsumableGoods"):
            interactions["Consumable Goods"] = strings.consumableGoods
        return Room(messages, people, items, interactions, isRepeat = isRepeat).runRoom()
    
class RuinsFactory:
    def runRoom(isRepeat):
        messages = strings.ruinsFactory
        people = {}
        items = {}
        interactions = {}
        interactions["Ruins Library"] = strings.moveRuinsLibrary2
        interactions["Giants Town"] = strings.moveGiantsTown
        interactions["Enter Factory"] = strings.moveIntoFactory
        return Room(messages, people, items, interactions, isRepeat = isRepeat).runRoom()
    
class RuinsFactoryInner:
    def runRoom(isRepeat):
        messages = strings.ruinsFactoryInner
        people = {}
        items = {}
        interactions = {}
        interactions["Ruins Factory"] = strings.moveRuinsFactory
        interactions["Inspect Room"] = strings.inspectRuinsFactoryInner
        interactions["Wait"] = strings.waitingRuinsFactoryInner
        return Room(messages, people, items, interactions, isRepeat = isRepeat).runRoom()
    
class GiantsTown:
    def runRoom(isRepeat):
        messages = strings.giantsTown
        people = {}
        items = {}
        interactions = {}
        interactions["Ruins Factory"] = strings.moveRuinsFactory
        interactions["Move Further"] = strings.moveFurther
        interactions["Wait"] = strings.waiting
        if not support.Inventory.inventory.get("Mistmoss Leaflet"):
            items["Mistmoss Leaflet"] = strings.mistmossLeaflet
        return Room(messages, people, items, interactions, isRepeat = isRepeat).runRoom()
    
class End:
    def runRoom(isRepeat):
        messages = strings.end
        people = {}
        items = {}
        interactions = {}
        if not support.globalFlags.get("endingFace"):
            support.writeConsole("..!", delay = 1)
            support.writeConsole(":)")
            time.sleep(2)
            support.globalFlags["endingFace"] = True
        support.writeConsole("Thank you for playing!")
        support.Inventory.inventory = dict()
        support.Inventory.inventory["About"] = inventory.About
        return Room(messages, people, items, interactions, isRepeat = isRepeat).runRoom()
    
playing = True
support.globalFlags["location"] = "Meadows"
support.globalFlags["poemLines"] = [0, 0, 0, 0, 0]
room = None
pastRoom = None
isRepeat = False
while playing:
    try:
        room = support.globalFlags["location"]
        if room == pastRoom:
            isRepeat = True
        else:
            isRepeat = False
        eval(room).runRoom(isRepeat)
        pastRoom = room
    except Exception:
        print(traceback.format_exc())
        sys.exit()


# In[ ]:




