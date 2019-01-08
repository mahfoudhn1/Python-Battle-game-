from classes.game import person, bcolors
from classes.magic import spell
from classes.inventory import item
import random


#black magic
fire = spell("fire", 10, 100, "black")
Thunder = spell("Thunder", 17, 130, "black")
Blizzer = spell("Blizzer", 17, 130, "black")
meteor = spell("meteor", 20, 160, "black")
quak = spell("Quak", 12, 120, "black")

#white magic
cure = spell("cure", 12, 120, "white")
cura = spell("cura", 18, 200, "white")

#creat some items

potion = item("potion",  "potion", "heals for 50 HP", 50)
hight_potion = item("hi_potion",  "potion", "heals for 100 HP", 100)
super_potion = item("supper_potion", "potion", "heals for 150 HP", 500)
exiler = item("exiler","exiler", "fully restor  HP/MP for party memeber", 99990)
hiexiler = item("mega_exiler", "exiler", "fully restor  HP/MP for Player", 99990)
grenad = item("grenad", "attak", "generate damage 50 HP ", 50)

player_spells = [fire, Thunder, Blizzer, meteor, quak, cure, cura]
player_items= [{"item" : potion, "quantity" : 5}, {"item" :hight_potion, "quantity" : 5},
                {"item" :super_potion, "quantity" : 5}, {"item" :exiler, "quantity" : 5}, {"item" :hiexiler, "quantity" : 2},
                {"item" :grenad, "quantity" : 5}]


player1 = person("valos", 3000, 65, 80, 34, player_spells , player_items)
player2 = person("jhony", 2500, 65, 60, 34, player_spells , player_items)
player3 = person("mikey", 2500, 65, 60, 34, player_spells , player_items)

enemy1 = person("enemy1", 700, 65, 800, 25, [], [])
enemy2 = person("enemy2", 3700, 65, 500, 25, [], [])
enemy3 = person("enemy3", 700, 65, 800, 25, [], [])
enmies = [enemy1, enemy2, enemy3]
players = [player1, player2, player3]
runing = True
i = 0

print  (bcolors.FAIL + bcolors.BOLD + " an enemy attaques" + bcolors.ENDC)

while runing :
    print (' \n =============================')
    for player in players :
        print("\n")
        print("name :              HP                               MP")
        player.get_stat()

    print("\n")
    for enemy in enmies:
        enemy.get_enemy_stat()

    for player in players :

        player.chose_action()
        choice = input(" chose an  action ")
        index = int(choice)-1
        if index == 0 :
            dmg = player.generate_damage()
            enemy = player.chose_target(enmies)
            enmies[enemy].take_dmg(dmg)
            print("you attacked for ", dmg, "point ")
            if enmies[enemy].get_hp == 0 :
                print(enmies[enemy].name + " has no dies")
                del enmies[enemy]
            #plyer magic**********************

        elif index == 1 :
            player.chose_magic()
            magicchoice = int(input("chose a  magic ")) - 1
            if magicchoice == -1 :
                continue
            spell = player.magic[magicchoice]
            magic_dmg = spell.generate_damage()
            curent_mp = player.get_mp()
            if spell.cost > curent_mp :
                print("dont have mp ")
                continue
            player.reduce_mp(spell.cost)

            if spell.type  == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + spell.name + " heals for " + str(magic_dmg) + "hp . " + bcolors.ENDC)
            elif spell.type  == "black" :
                enemy = player.chose_target(enmies)
                enmies[enemy].take_dmg(magic_dmg)
                print (spell.name , " deals", magic_dmg, "points" )
                if enmies[enemy].get_hp == 0 :
                    print(enmies[enemy].name + " has no dies")
                    del enmies[enemy]
    #items choice
        elif index == 2 :
            player.choose_item()
            item_chose = int(input("chose an item : ")) - 1
            if item_chose == -1 :
                continue
            item = player.item[item_chose]["item"]
            player.item[item_chose]["quantity"] -= 1
            if player.item[item_chose]["quantity"] == 0 :
                print(bcolors.OKGREEN + "\n" + "none item left ... ")
                continue
            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.FAIL + item.name + " heals for "+ str(item.prop) + " HP " + bcolors.ENDC)
            elif item.type == "exiler":
                if item.name == "mega_exiler":
                    for i in players :
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(item.type + " " + item.description)
            elif item.type == "attak":
                enemy = player.chose_target(enmies)
                enmies[enemy].take_dmg(item.prop)
                print(item.name + " " + item.description)
                if enmies[enemy].get_hp == 0 :
                    print(enmies[enemy].name + " has no dies")
                    del enmies[enemy]

     #enemy attacks*********************

    defeted_enemies = 0
    defeted_players = 0
    for enemy in enmies:
        if enemy.get_hp() == 0 :
            defeted_enemies += 1

        if defeted_enemies == 2 :
            print( bcolors.OKGREEN + "you win !")
            runing = False
    for t in players :
        if t.get_hp() == 0:
            defeted_players += 1

        if defeted_players == 2:
            print(bcolors.OKGREEN + "you lose !")
            runing = False

    for enemy in enmies:
        enemy_choice  = random.randrange(0, 3)
        if enemy_choice == 0 :
            target = random.randrange(0, 2)
            enemy_dmg = enemy.generate_damage()
            players[target].take_dmg(enemy_dmg)
            print("enemy attaks for ", enemy_dmg )

        elif enemy_choice == 1 :
            magicchoice = random.randrange(0, len(enemy.magic))
            spell = enemy.magic[magicchoice]
            magic_dmg = spell.generate_damage()
            if enemy.mp < spell.cost :
                print("sorry not enough ")
            else:
                target = random.randrange(0, 2)
                players[target].take_dmg(magic_dmg)
                print("enemy attaks for ", magic_dmg )
