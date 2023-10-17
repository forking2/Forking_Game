import time
import random
import logging
import sqlite3
import requests
import cv2
from PIL import Image

print("It`s Terraria in Python")

res_parse_list = []
response = requests.get("https://terraria.fandom.com/wiki/Terraria_Wiki")
response_text = response.text
response_parse = response_text.split("<span>")
try:                 
    connection = sqlite3.connect('Terka.sl3',5)
    cur = connection.cursor()
    cur.execute('CREATE TABLE terraria (stats TEXT);')
    cur.execute('INSERT INTO terraria VALUES("\nRanger:hp=600,mana=200,dmg=2500, patron = 0, summon = 1");')
    cur.execute('INSERT INTO terraria VALUES("\nSummoner:mana=20,hp=500,dmg=4500, patrons = 0, summon = 11");')
    cur.execute('INSERT INTO terraria VALUES("\nMelee:hp=800,mana=20,dmg=1900, patron = 0, summon = 1");')
    cur.execute('INSERT INTO terraria VALUES("\nWizard:mana=200,hp=400,dmg=9900, patrons = 0, summon = 1");')
    cur.execute('INSERT INTO terraria VALUES("\nMoonlord:hp=250000,damage=400");')
    cur.execute('SELECT * FROM terraria')
    connection.commit()
    connection.close()
except:
    print(' ')

'image_path = "moonl.jpg"'
'image = cv2.imread(image_path)'
'cv2.imshow("Moonlord",image)'
'ml = Image.open(image_path)'
'ml = ml.convert("RGBA")'


'img_path = "clas.png"'
'img = cv2.imread(img_path)'
'cv2.imshow("Classes",img)'
'cl = Image.open(img_path)'
'cl = cl.convert("RGBA")'
class Player:
    def __init__(self,hp=600,mana=200,dmg=2500, patron = 0, summon = 1):
        self.hp = hp
        self.mana = mana
        self.dmg = dmg
        self.patron = patron
        self.summon = summon
    def Print(self):
        print('_____________________________________','\nHealth: ', self.hp, '\nMana: ', self.mana,'\nDamage: ',self.dmg,'\npatron:',self.patron,'\nSummon Pets:',self.summon,'\n_____________________________________',)
    def IsAlive(self):
        if self.hp  >= 1:
            return true
        else:
            print('You lose:(')
class Ranger(Player):
    def __init__(self,mana=20,hp=600,dmg=3320, patron = 1000):
        super().__init__(hp,mana,dmg,patron)
    def damage(self,hp1):
        self.hp = self.hp - hp1
    def Phantasm(self,Moonlord1):
        self.patron = self.patron - 35
        Moonlord1.damageHaving(8070)
    def Phasm(self,Moonlord1):
        self.patron = self.patron - 25
        Moonlord1.damageHaving(6090)
    def Celebration(self,Moonlord1):
        self.patron = self.patron - 25
        Moonlord1.damageHaving(4090)
    def Heal(self,hp):
        self.hp = self.hp + 200
    def Regen(self,hp):
        self.hp = self.hp + 100
    def HavePatrons(self):
        if self.patrons  >= 1:
            return true
        else:
            self.hp = self.hp - 100
            self.patrons = self.patrons + 550
class Summoner(Player):
    def __init__(self,mana=20,hp=500,dmg=4500, patrons = 0, summon = 11):
        super().__init__(hp,mana,dmg,patrons,summon)
    def damage(self,hp1):
        self.hp = self.hp - hp1
    def Dragon(self,Moonlord1):
        Moonlord1.damageHaving(11000)
    def Knut(self,Moonlord1):
        Moonlord1.damageHaving(2400)
    def Heal(self,hp):
        self.hp = self.hp + 200
    def Regen(self,hp):
        self.hp = self.hp + 120

class Melee(Player):
    def __init__(self,mana=20,hp=800,dmg=1900, patrons = 0, summon = 1):
        super().__init__(hp,mana,dmg,patrons,summon)
    def damage(self,hp1):
        self.hp = self.hp - hp1
    def solarrage(self,Moonlord1):
        Moonlord1.damageHaving(4000)
    def solarspice(self,Moonlord1):
        Moonlord1.damageHaving(3000)
    def Heal(self,hp):
        self.hp = self.hp + 200
    def Regen(self,hp):
        self.hp = self.hp + 320
        
class Mage(Player):
    def __init__(self,mana=2000,hp=420,dmg=9900, patrons = 0, summon = 1):
        super().__init__(hp,mana,dmg,patrons,summon)
    def NebulaFire(self,Moonlord1):
        Moonlord1.damageHaving(9900)
        self.mana = self.mana - 120
    def NebulaNeb(self,Moonlord1):
        Moonlord1.damageHaving(7000)
        self.mana = self.mana - 80
    def Heal(self,hp):
        self.hp = self.hp + 200
    def Regen(self,hp):
        self.hp = self.hp + 120
        
class Moonlord:
    def __init__(self,hep=400000,damage=400):
        self.hep = hep
        self.damage = damage
    def damageHaving(self,hep1):
        self.hep = self.hep - hep1
    def print1(self):
        print('_____________________________________','\nHealth: ', self.hep,'\nDamage: ',self.damage, '\n_____________________________________', )

    def PhantasmLaser(self,Ranger1):
        Ranger1.damage(400)
    def PhantasmSphere(self,Ranger1):
        Ranger1.damage(100)
    def PhantasmBull(self,Ranger1):
        Ranger1.damage(50)
    def IsAlive(self):
        if self.hep  >= 1:
            return true
        else:
            print('You win!')
pl = Player()
ma1 = Mage()
ma1.Print()
mel1 = Melee()
mel1.Print()
summon1 = Summoner()
summon1.Print()
range1 = Ranger()
range1.Print()
Enemy = Moonlord()
Enemy.print1()

summon1.Print()
range1.Print()
mel1.Print()
ma1.Print()
Enemy.print1()
while True:
    pl.IsAlive
    Enemy.IsAlive
    print('\t\tSummoner:')
    summon1.Print()
    print('\t\tRanger:')
    range1.Print()
    print('\t\tMelee:')
    mel1.Print()
    print('\t\tWizard:')
    ma1.Print()
    print('\t\tEnemy:')
    Enemy.print1()

    print('Select skill:')
    print('1 - Phantasm')
    print('2 - Phasm')
    print('3 - Celebration')
    print('4 - Dragon')
    print('5 - Knut')
    print('6 - Nebula nebul')
    print('7 - Nebula fire')
    print('8 - Multi attack')
    selected = int(input())
    if selected == 1:
        range1.Phantasm(Enemy)
        print('\tSummoner:')
        summon1.Print()
        print('\tRanger:')
        range1.Print()
        print('\tMelee:')
        mel1.Print()
        print('\tWizard:')
        ma1.Print()
        print('\tEnemy:')
        Enemy.print1()
    elif selected == 2:
        range1.Phasm(Enemy)
        Enemy.PhantasmSphere(range1)
        range1.Regen(range1)
        print('\tSummoner:')
        summon1.Print()
        print('\tRanger:')
        range1.Print()
        print('\tMelee:')
        mel1.Print()
        print('\tWizard:')
        ma1.Print()
        print('\tEnemy:')
        Enemy.print1()
        
    elif selected == 3:
        range1.Celebration(Enemy)
        Enemy.PhantasmBull(range1)
        range1.Regen(range1)
        print('\tSummoner:')
        summon1.Print()
        print('\tRanger:')
        range1.Print()
        print('\tMelee:')
        mel1.Print()
        print('\tWizard:')
        ma1.Print()
        print('\tEnemy:')
        Enemy.print1()
        
    elif selected == 4:    
        mel1.solarrage(Enemy)
        Enemy.PhantasmSphere(summon1)
        summon1.Dragon(Enemy)
        Enemy.PhantasmSphere(mel1)
        summon1.Regen(summon1)
        mel1.Regen(mel1)
        print('\tRanger:')
        range1.Print()
        print('\tSummoner:')
        summon1.Print()
        print('\tMelee:')
        mel1.Print()
        print('\tWizard:')
        ma1.Print()
        print('\tEnemy:')
        Enemy.print1()
        
    elif selected == 5:
        summon1.Knut(Enemy)
        summon1.Regen(summon1)
        mel1.solarspice(Enemy)
        mel1.Regen(mel1)
        Enemy.PhantasmBull(summon1)
        Enemy.PhantasmBull(mel1)
        print('\tRanger:')
        range1.Print()
        print('\tSummoner:')
        summon1.Print()
        print('\tMelee:')
        mel1.Print()
        print('\tWizard:')
        ma1.Print()
        print('\tEnemy:')
        Enemy.print1()
        
    elif selected == 6:
        ma1.NebulaNeb(Enemy)
        ma1.Regen(ma1)
        print('\tRanger:')
        range1.Print()
        print('\tSummoner:')
        summon1.Print()
        print('\tMelee:')
        mel1.Print()
        print('\tWizard:')
        ma1.Print()
        print('\tEnemy:')
        Enemy.print1()
        
    elif selected == 7:
        ma1.NebulaFire(Enemy)
        ma1.Regen(ma1)
        print('\tRanger:')
        range1.Print()
        print('\tSummoner:')
        summon1.Print()
        print('\tMelee:')
        mel1.Print()
        print('\tWizard:')
        ma1.Print()
        print('\tEnemy:')
        Enemy.print1()
        
    elif selected == 8:
        range1.Phantasm(Enemy)
        summon1.Dragon(Enemy)
        mel1.solarrage(Enemy)
        Enemy.PhantasmLaser(range1)
        Enemy.PhantasmLaser(summon1)
        Enemy.PhantasmLaser(mel1)
        range1.Heal(range1)
        summon1.Heal(summon1)
        mel1.Heal(mel1)
        print('\tSummoner:')
        summon1.Print()
        print('\tRanger:')
        range1.Print()
        print('\tMelee:')
        mel1.Print()
        print('\tWizard:')
        ma1.Print()
        print('\tEnemy:')
        Enemy.print1()
    else:
        print('\n===========================')
        print('(Type:1 or 2 or 3 or 4 or 5 or 6 or 7 or 8)')
        print('\n===========================')
