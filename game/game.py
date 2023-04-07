def addToInventory(inventory,addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item]+=1
        else:
            inventory[item]=1
    return inventory

def displayInventory(stuff):
    total=0
    result=""
    for item, amount in stuff.items():
        total+=amount
        result+=str(amount) + " " + item + "\n"
    return "Inventory:\n" + result + str(total)

def accessInventory():
    with open("inventory.txt") as f:
        inventory={}
        for line in f:
            x,y=line.split(":")
            inventory[x]=int(y)
        return inventory
    
def saveInventory(Inventory):
    tosave=""
    with open("inventory.txt", "w") as w:
        for item, amount in Inventory.items():
            tosave+=str(item)+": "+str(amount)+"\n"
        w.write(tosave)

def inspect(object):
    fil=".\objects\ ".strip()+str(object)
    if object in loadedObjects:
        print(getObject(fil,"Description"))
    else:
        print ("There is no " + object + ".")

def loadArea(areaID):
    global loadedObjects
    global loadedArea
    loadedObjects=getObject(areaID,"Objects").split(",")
    print(getObject(areaID,"Description"))
    loadedArea = areaID

def getObject(object, index):
    file=object+".txt"
    result={}
    with open(file) as f:
        inf=f.read()
        inf=inf.split("___")
        for i in range(0,len(inf)-1,2):
            result[inf[i].strip()]=inf[i+1].strip()
        return (result[index])

def lootGet(stuff):
    saveInventory(addToInventory(accessInventory(),[stuff]))

def gather(object):
    global loadedObjects
    if object in loadedObjects:
        if getObject(".\objects\ ".strip()+object,"pickUp") == "True":
            loot=getObject(".\objects\ ".strip()+object,"loot")
            lootGet(loot)
            print("You pick up one "+loot+".")
        else:
            print("You cannot pick up " + object + ".")
    else:
        print ("There is no "+object+".")

def move(path):
    connect=getObject(loadedArea,"Connections").split(",")
    result={}
    for i in range(0,len(connect)-1,2):
        result[connect[i]]=connect[i+1]
    loadArea(result[path])



loadedObjects=[]
command=""
loadedArea="area01"
loadArea(loadedArea)
while command!="stop":
    command=input("Do what? ")
    if command == "inspect":
        inspect(input("inspect what? "))
    elif command == "gather":
        gather(input("Gather what? "))
    elif command == "move":
        move(input("Where would you like to go? "))