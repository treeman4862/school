# Icecream Sort

class Icecream():
    def __init__(self): #Initialise properties of object
        #Private
        self.__array = [None, None, None, None, None] 
        self.__pointer = 0 
        self.__maxCapacity = len(self.__array) # =5

    def push(self, flavour): #creates method adding scoop of icecream
        if self.__pointer < self.__maxCapacity: #range check to see if icecream is full
            self.__array[self.__pointer] = flavour #if not add flavour to where pointer is 0,1,2,3,4
            self.__pointer = self.__pointer + 1 #increment pointer value
            print(flavour + "  is added!")
        else:
            print("No more space!") #nothing is done user is told there is no space
    def pop(self): # eating top piece of icecream
        if self.__pointer > 0: #
            self.__pointer = self.__pointer -1 #minuses pointer because icecream is eaten
            flavour = self.__array[self.__pointer] #points to removed icecream
            self.__array[self.__pointer] = '' #empties array
            return flavour
        else:
            return False

myIcecream = Icecream() #creates instance of class, object

myIcecream.push("fortnite")

print("ate " + myIcecream.pop())