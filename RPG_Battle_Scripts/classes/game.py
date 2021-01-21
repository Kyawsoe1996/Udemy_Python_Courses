import random

class bcolors:
    """
    bcolors is a class with the terminal colors we are going to be using
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    """
    Person is a class with our hero
    """
    def __init__(self, hp, mp, atk, df, magic,items):
        """
        Set up our here
        :param hp: The heroes HP
        :param mp: The heroes mp
        :param atk: The Heroes attack
        :param df: The heroes defence
        :param magic: the heroes magic
        """
        #our max hit points
        self.maxhp = hp
        #our current hit point
        self.hp = hp
        #our max magic points
        self.maxmp = mp
        #our current magic points
        self.mp = mp
        #low attack
        self. atkl = atk - 10
        #high attack
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        # self.items = items
        self.actions = ["Attack", "Magic","Items"]

        self.items = items

    
    def generate_damage(self):
        """
        Generates a random damage
        :return: a random damage number
        """
        return random.randrange(self.atkl, self.atkh)


    def take_damage(self, dmg):
        """
        Function to tell how much damage we took
        :param dmg: the damage we've taken
        :return: How much HP the player has left
        """
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp
    
    def get_hp(self):
        """
        Get the Heroes HP
        :return: Heroes current hp
        """
        return self.hp

    
    def get_max_hp(self):
        """
        Get the Heroes Max HP that they can have
        :return: Max HP a the hero can have
        """
        return self.maxhp

    def get_mp(self):
        """
        Get Heroes Magic points
        :return: Current magic points
        """
        return self.mp

    def get_max_mp(self):
        """
        Get Heroes total magic points
        :return: Max MP a hero can have
        """
        return self.maxmp
    

    def reduce_mp(self, cost):
        """
        Reduce mp when a hero cast a spell
        :param cost: The cost of the spell
        :return: How much MP they have left
        """
        self.mp -= cost

   

    def choose_action(self):
        """
        The action the hero is going to take
        :return: print the action the hero is taking
        """
        i = 1
        print("\n"+ bcolors.OKBLUE + bcolors.BOLD + "ACTIONS:" + bcolors.ENDC)
        for item in self.actions:
            print("    " + str(i) + ".", item)
            i += 1


    def choose_magic(self):
        """
        The magic spell the hero is going to cast
        :return: prints the spell and cost the hero is going to cast
        """
        i = 1
        print("\n"+ bcolors.OKBLUE + bcolors.BOLD + "MAGIC:" + bcolors.ENDC)
        for spell in self.magic:
            print("    " + str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1
    
    def choose_items(self):
        print("\n"+ bcolors.OKGREEN + bcolors.BOLD + "ITEMS:" + bcolors.ENDC)
        i = 1
        for item in self.items:
            print("    " + str(i) + ".",item["item"].name,":",item["item"].description," (x" + str(item["quantity"])+")")
            i+= 1

    
    def heal(self, dmg):
        """
        Heals the player
        :param dmg: The ammount to heal the player
        :return: 
        """
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

        

    # def generate_spell_damage(self,i):
    #     """
    #     Generate Spell Damage.
    #     :param i : magic index
    #     :return: a random spell damage number

    #     """
    #     mgl = self.magic[i]["dmg"] - 5
    #     mgh = self.magic[i]["dmg"] + 5

    #     return random.randrange(mgl,mgh)


    # def get_spell_name(self,i):
    #     """
    #         Get the spell name
    #         :param i = magic index
    #     """
    #     return self.magic[i]["name"]
    
    # def get_spell_mp_cost(self,i):
    #     """
    #         Get the spell mp_cost
    #         :param -i == magic index 
    #     """
    #     return self.magic[i]["cost"]

        
    

  