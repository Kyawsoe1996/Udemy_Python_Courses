from classes.game import Person,bcolors

from classes.magic import Spell
from classes.inventory import Item

# magic = [{"name":"Fire","cost":10,"dmg":100},
#          {"name":"Thunder","cost":12,"dmg":124},
#          {"name":"Blizzard","cost":10,"dmg":100}

#Create Black Magic
fire = Spell("Fire",10,100,"black")
thunder = Spell("Thunder",10,100,"black")
blizzard = Spell("Blizzard",10,100,"black")
meteor = Spell("Meteor",20,200,"black")
quake = Spell("Quake",14,140,"black")


#Create White Magic
cure = Spell("Cure",12,120,"white")
cura = Spell("Cura",18,200,"white")

#Create Some item

potion = Item("Potion","potion","Heals 50 Hp",50)
hipotion = Item("Hi-Potion","potion","Heals 100 Hp",100)
superpotion = Item("Super Potion","potion","Heals 500 Hp",500)
elixer = Item("Elixer","elixer","Fully restores HP/MP of one party member",9999)
hielixer = Item("MegElixer","elixer","Fully restores party's HP/MP",9999)

grenade = Item("Grendae","attack","Deal 500 damage",500)

player_spells = [fire,thunder,blizzard,meteor,quake,cure,cura]
# player_items = [potion,hipotion,superpotion,elixer,hielixer]

player_items = [{"item":potion,"quantity":15},
                {"item":hipotion,"quantity":5},
                {"item":superpotion,"quantity":5},
                {"item":elixer,"quantity":5},
                {"item":hielixer,"quantity":2},
                {"item":grenade,"quantity":5},


                ]
#Instantiate People        ]
player = Person(460,65,60,34,player_spells,player_items)
enemy = Person(1200,65,45,25,[],[])

# spell_dmg = player.generate_spell_damage(1)
# print(spell_dmg)

# damage = player.take_damage(60)
# print(damage)

# get_curent_hp = player.get_hp()
# print(get_curent_hp)

# mp = player.reduce_mp(12)
# print(player.mp)

# print(player.get_spell_mp_cost(1))

# player.choose_action()
# player.choose_magic()

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)
while running:
    print("Hello")
    player.choose_action()
    choice = int(input("Choose Action: "))
    print(bcolors.OKGREEN + str(player.hp) + bcolors.ENDC)
    index = choice -1
    if index ==0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for ",dmg, "points of damage. Enemy HP:",enemy.get_hp())
    elif index ==1:
        #choose magic
        player.choose_magic()
        #accept user input of magic choice
        magic_choice = int(input("Choose Magic:")) - 1

        #skipping if user wrong choose choice and back to start loop
        if magic_choice == -1:
            continue

        #identify which spell is it
        spell = player.magic[magic_choice]
        #generate damage from specific spell
        magic_dmg = spell.generate_damage()

        #get curent mp
        current_mp = player.get_mp()
        
        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n"+bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)

        if spell.type == "white":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " heals for",str(magic_dmg),"HP." + bcolors.ENDC)
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n"+ spell.name + " deals", str(magic_dmg),"points of damage"+bcolors.ENDC)




    elif index == 2:
        player.choose_items()
        item_choice = int(input("Choose item:")) -1 
        #skipping if user choose wrong items 
        if item_choice == -1:
            continue

        
        item = player.items[item_choice]["item"]
        if player.items[item_choice]["quantity"] == 0:
            print(bcolors.FAIL + "\n"+ "None Left..."+ bcolors.ENDC)
            continue
        player.items[item_choice]["quantity"] -= 1
        

        
        if item.type == "potion":
            player.heal(item.prop)
            print(bcolors.OKGREEN + "\n" + item.name + " heals for " + str(item.prop),"HP" + bcolors.ENDC)
        elif item.type == "elixer":
            player.hp = player.maxhp
            player.mp = player.maxmp
            print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP." + bcolors.ENDC)
        elif item.type == "attack":
            enemy.take_damage(item.prop)
            print(bcolors.FAIL + "\n" + item.name + " deals",str(item.prop)," points of damage" + bcolors.ENDC) 
        






    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacked for ",enemy_dmg," Player HP: ",player.get_hp())

    print("===============================")
    print("Enemy HP:",bcolors.FAIL + str(enemy.get_hp())+"/"+ str(enemy.get_max_mp())+bcolors.ENDC +"\n")
    print("Your HP:",bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp())+bcolors.ENDC +"\n")
    print("Your MP:",bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp())+ bcolors.ENDC)
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + " You win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Your enemy has defeated you !" + bcolors.ENDC)
        running = False




    












