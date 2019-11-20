import random

class FireDragon(self):
    """
    Class for the Fire Dragon Progmon
    """
    def __init__(self):
        """
        Creates variables associated with FireDragon
        Args:
            self (object) - FireDragon
        Returns:
            None
        """
        self.name = "Fire Dragon"
        self.hp = 300
        self.currentHealth = 300
        self.alive = True
        self.bag = ["healthPotion", "statBoost", "defenseBoost"]
        self.attackList = ["Roar", "Claw Swipe", "Fire Breath", "Tail Whip"]
        self.stunned = False
        self.statBoost = False
        self.defenseBoost = False

    def doDamage(self, damageDone):
        """
        Deals damage to the enemy's health; set alive to False if health goes below 1
        Args:
            self (object) - FireDragon
            damageDone (int) - amount of damage to do
        Returns:
            None
        """
        if(self.defenseBoost == True):
            self.currentHealth = self.currentHealth - damageDone + 10
            self.defenseBoost = False
        else:
            self.currentHealth = self.currentHealth - damageDone

        if(self.currentHealth <= 0):
            self.alive = False

    def checkAlive(self):
        """
        Checks if FireDragon is alive
        Args:
            self (object) - FireDragon
        Returns:
            (bool) - True if FireDragon is alive, otherwise False
        """
        if(self.alive == True):
            return True
        else:
            return False

    def getAttackList(self):
        """
        Gets the attack list of Progmon
        Args:
            self (object)
        Returns:
            Progmon's attackList
        """
        return self.attackList

    def setBag(self, newBag):
        """
        Sets the bag of Progmon
        Args:
            self (object)
            newBag (array) - what to set bag to
        Returns:
            None
        """
        self.bag = newBag

    def getBag(self):
        """
        Gets the bag list of Progmon
        Args:
            self (object)
        Returns:
            Progmon's bag
        """
        return self.bag

    def getCurrentHealth(self):
        """
        Gets the currentHealth of FireDragon
        Args:
            self (object) - FireDragon
        Returns:
            FireDragon's currentHealth
        """
        return self.currentHealth

    def setCurrentHealth(self, newHealth):
        """
        Sets the current health of Progmon
        Args:
            self (object)
            newHealth (int) - what to set current health to
        Returns:
            None
        """
        self.currentHealth = newHealth

    def getHp(self):
        """
        Gets the max health of FireDragon
        Args:
            self (object) - FireDragon
        Returns:
            FireDragon's max health
        """
        return self.hp

    def setStunStatus(self, setter):
        """
        Sets the stun status of Progmon
        Args:
            self (object)
            setter (boolean) - what to set stunned to
        Returns:
            None
        """
        self.stunned = setter

    def getStunStatus(self):
        """
        Gets the stun status of Progmon
        Args:
            self (object)
        Returns:
            Progmon's stunned
        """
        return self.stunned

    def setDefenseBoost(self, setter):
        """
        Sets the defense boost of Progmon
        Args:
            self (object)
            setter (boolean) - what to set defense boost to
        Returns:
            None
        """
        self.defenseBoost = setter

    def getDefenseBoost(self):
        """
        Gets the defense boost of Progmon
        Args:
            self (object)
        Returns:
            Progmon's defense boost
        """
        return self.defenseBoost

    def setStatBoost(self, setter):
        """
        Sets the stat boost of Progmon
        Args:
            self (object)
            setter (boolean) - what to set stat boost to
        Returns:
            None
        """
        self.statBoost = setter

    def getStatBoost(self):
        """
        Gets the defense boost of Progmon
        Args:
            self (object)
        Returns:
            Progmon's defense boost
        """
        return self.statBoost

    def attack1(self, enemyPlayer): # 80 damage, 45 accuracy
        """
        Attacks enemy Progmon with Roar
        Args:
            self (object) - FireDragon
            enemyPlayer (object) - enemy Progmon
        Returns:
            None
        """
        chanceToHit = random.randint(1, 101)
        if(self.statBoost == True and chanceToHit <= 45):
            self.statBoost = False
            enemyPlayer.doDamage(80)
            enemyPlayer.setStunStatus(True)
            return True, "Roar did 80 damage and stunned the enemy!"
        elif(chanceToHit <= 45):
            enemyPlayer.doDamage(80)
            return True, "Roar did 80 damage!"
        else:
            return False, "Roar missed!"

    def attack2(self, enemyPlayer): # 35 damage, 90 accuracy
        """
        Attacks enemy Progmon with Claw Swipe
        Args:
            self (object) - FireDragon
            enemyPlayer (object) - enemy Progmon
        Returns:
            None
        """
        chanceToHit = random.randint(1, 101)
        if(chanceToHit <= 90):
            enemyPlayer.doDamage(35)
            return True, "Claw Swipe did 35 damage!"
        else:
            return False, "Claw Swipe missed!"

    def attack3(self, enemyPlayer): # 140 damage, 30 accuracy
        """
        Attacks enemy Progmon with Fire Breath
        Args:
            self (object) - FireDragon
            enemyPlayer (object) - enemy Progmon
        Returns:
            None
        """
        chanceToHit = random.randint(1, 101)
        if(self.statBoost == True and chanceToHit <= 30):
            self.statBoost = False
            enemyPlayer.doDamage(150)
            enemyPlayer.setStunStatus(True)
            return True, "Fire Breath did 150 damage and stunned the enemy!"
        elif(chanceToHit <= 30):
            enemyPlayer.doDamage(140)
            return True, "Fire Breath did 140 damage!"
        else:
            return False, "Fire Breath missed!"

    def attack4(self, enemyPlayer): # 20 damage, 100 accuracy
        """
        Attacks enemy Progmon with Tail Whip
        Args:
            self (object) - FireDragon
            enemyPlayer (object) - enemy Progmon
        Returns:
            None
        """
        enemyPlayer.doDamage(20)
        return True, "Tail Whip did 20 damage!"

    def AIAttack(self, enemyPlayer):
        """
        Attacks enemy Progmon with a randomly chosen attack
        Args:
            self (object) - FireDragon
            enemyPlayer (object) - enemy Progmon
        Returns:
            (string) - the attack that was used by the AI
        """
        #randomly choose one of FireDragon's attacks and then use it
        #returns a string of which attack was used so that user can know what AI did/if it was successful
        attackToUse = random.randint(1, 5)
        tempHealth = enemyPlayer.getCurrentHealth()
        if(attackToUse == 1):
            self.attack1(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "AI Roar hit!"
            else:
                return "AI Roar missed!"
        if(attackToUse == 2):
            self.attack2(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "AI Claw Swipe hit!"
            else:
                return "AI Claw Swipe missed!"
        if(attackToUse == 3):
            self.attack3(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "AI Fire Breath hit!"
            else:
                return "AI Fire Breath missed!"
        if(attackToUse == 4):
            self.attack4(enemyPlayer)
            if(tempHealth != enemyPlayer.getCurrentHealth()):
                return "AI Tail Whip hit!"
            else:
                return "AI Tail Whip missed!"

    def useHealthPotion(self):
        """
        Uses a healthPotion to heal 30 points of health
        Args:
            self (object) - FireDragon
        Returns:
            None
        """
        if(self.currentHealth+30 > self.hp):
            hpToAdd = self.hp - self.currentHealth
            self.currentHealth + hpToAdd
            print("Health potion healed you for:", hpToAdd, "\n")
            self.bag.remove("healthPotion")
        else:
            self.currentHealth + 30
            print("Health potion healed you for: 30\n")
            self.bag.remove("healthPotion")

    def useStatBoost(self):
        """
        Allows this Progmon to use a statBoost Potion
        Args:
            self (object) - FireDragon
        Returns:
            None
        """
        self.statBoost = True
        print("Stat Boost for Fire Dragon is activated!\n You will do +10 damage and have a chance to stun!\n")
        self.bag.remove("statBoost")

    def useDefenseBoost(self):
        """
        Allows this progmon to use a defense Potion
        Args:
            self (object) - FireDragon
        Returns:
            None
        """
        self.defenseBoost = True
        print("Defense boost for Fire Dragon is now activated!\n You will take 10 less damage on the next attack.\n")
        self.bag.remove("defenseBoost")

    def getDefenseBoost(self):
        return self.defenseBoost

    def bagEmpty(self):
        """
        Checks if the Bag is empty
        Args:
            self (object) - FireDragon
        Returns:
            (bool) - True if Bag is empty, otherwise False
        """
        if(self.bag):
            return False
        else:
            return True
