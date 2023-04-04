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
            print (tosave)
        w.write(tosave)
def inspect(object):
    fil=str(object)+".txt"
    if object in loadedObjects:
        with open(f".\objects\{fil}") as f:
            for line in f:
                if "_" in line:
                    break
                print (line,end="")
    else:
        print ("There is no " + object + ".")
def loadArea(areaID):
    toload=str(areaID)+".txt"
    global loadedObjects
    loadedObjects = []
    inf="load"
    with open(toload) as f:
        for line in f:
            if "_" in line:
                inf="desc"
            if inf=="load":
                x,y=line.split("\n")
                loadedObjects.append(x)
            if inf=="desc":
                if "---" in line:
                    break
                print(line,end="")

loadedObjects=[]
command=""
loadArea("area01")
while command!="stop":
    command=input("Do what? ")
    if command == "inspect":
        inspect(input("inspect what? "))