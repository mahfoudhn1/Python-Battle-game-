import random
from .magic import spell
from .inventory import item
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class person:
    def __init__(self, name, hp, mp, atk, df, magic, item) :
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.name = name
        self.actions = ["attak","magic","items"]
        self.item = item

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp (self):
        return self.hp

    def get_maxhp (self):
        return self.maxhp

    def get_mp (self):
        return self.mp

    def get_maxmp (self):
        return self.maxmp

    def reduce_mp (self, cost):
        self.mp -= cost

    def chose_action(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.WARNING    + self.name + bcolors.ENDC)
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "ACTIONS" + bcolors.ENDC )
        for item in self.actions:
            print("    " + str(i)+  ".", item)
            i += 1

    def chose_magic (self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD +"MAGiC" + bcolors.ENDC)
        for spell in self.magic:
            print ("    " + str(i) + ".", spell.name , "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_item (self):
        i = 1
        print( bcolors.OKBLUE + bcolors.BOLD +"ITEMS" + bcolors.ENDC)
        for item in self.item:
            print ("    " + str(i) + " . " + item["item"].name + " : ", item["item"].description, " (x" , str(item["quantity"]))
            i += 1
    def chose_target(self, enmies):
        i = 1
        for enemy in enmies :
            if enemy.get_hp != 0:
            print ("    " + str(i) + "." + enemy.name)
            i += 1
        choice = int(input("    chose an enemy"))
        return choice
    def get_enemy_stat(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 2
        while bar_ticks > 0 :
            hp_bar += "█"
            bar_ticks -= 1
        while len(hp_bar) < 50 :
            hp_bar += " "
        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""
        if len(hp_string) < 9 :
            descrese = 9 - len(hp_string)
            while descrese < 0:
                current_hp += " "
                descrese -= 1

            current_hp += hp_string
        else :
            current_hp = hp_string
        print(bcolors.BOLD + self.name + "      " + current_hp + "|" + bcolors.FAIL + hp_bar + bcolors.ENDC + "|")

    def get_stat(self):
        hp_bar = ""
        barticks = (self.hp / self.maxhp) * 100 / 4
        while barticks > 0 :
            hp_bar += "█"
            barticks -= 1
        while len(hp_bar) < 25 :
            hp_bar += " "
        mp_bar = ""
        mp_bar_ticks = (self.mp / self.maxmp) * 100 / 10
        while mp_bar_ticks > 0:
            mp_bar += "█"
            mp_bar_ticks -= 1
        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""
        if len(hp_string) < 9 :
            descrese = 9 - len(hp_string)
            while descrese < 0:
                current_hp += " "
                descrese -= 1

            current_hp += hp_string
        else :
            current_hp = hp_string
        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp = ""
        if len(mp_string) > 7:
            descrese = 7 - len(hp_string)
            while descrese < 0:
                current_mp += " "
                descrese -= 1
            current_mp +=mp_string
        else :
            current_mp = mp_string
        print("                     _________________________          __________")
        print(bcolors.BOLD + self.name + "      " + current_hp + "|" + bcolors.OKGREEN + hp_bar + bcolors.ENDC +
        "|" + "   " + current_mp + "|" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")
