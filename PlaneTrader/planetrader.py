from rich import print
from rich.console import Console
console = Console()

import random
import math
import mariadb

conn = mariadb.connect(
    user="python",
    password="root",
    host="localhost",
    database="airport")
)

cur = conn.cursor()

location = cur.execute("SELECT id FROM airport ORDER BY RAND() LIMIT 1;")
location_name = cur.execute("SELECT name FROM airport WHERE id = location")
location_latitude = round(cur.execute("SELECT latitude_deg FROM airport WHERE id = location"),3)
location_longitude = round(cur.execute("SELECT longitude_deg FROM airport WHERE id = location"),3)
money = 1000
time = 1

hull = 30
fuel = 50

sweaters = 0
gelato = 0
coffee = 0
tea = 0

price_sweaters = 0
price_gelato = 0
price_coffee = 0
price_tea = 0

lv_engine = 0
lv_shield = 0
lv_gun = 0
lv_hull = 0

def flight():
    
    print("")
    
    global hull
    global time
    
    danger = danger_rate(location) + 1
    timefactor = 1.025**(3* time)
    birds = round(random.random() * 16 * danger**2 * timefactor)
    ogbirds = birds
    birds = round(birds * 0.9**lv_shield)
    print(str(ogbirds) + " birds en route.")
    print( str(ogbirds - birds) + " deterred by anti-bird pattern.")
    
    print(str(birds) + " incoming. Activating sound cannon... ")
    input()
    birds = round(birds * 0.9**lv_gun)
    print(str(birds) + " remaining. Brace for impact! ")
    input()
    
    if hull > birds:
        hull = hull - birds
        console.print("Hull integrity at " + str(hull) + ".", style="bold red", highlight=False)
        time = time + 1
        maintenance()
        loc_prompt()
    else:
        console.print("Plane down. Game over.", style="bold red", highlight=False)
        quit()

def prices(location):
    
    global price_sweaters
    global price_gelato
    global price_coffee
    global price_tea
    
    latitude = (location_latitude + 90) / 180
    longitude = (location_longitude + 180) / 360
    
    danger = danger_rate(location)
    
    mult = 1
    
    if danger == 1:
        mult = 3
    if danger == 2:
        mult = 9
        
    flux = 0.25 * math.sin(time - 0.25) + 1
    #print("market flux: " + str(flux))
    #0.25 * sin(x-0.25) + 1
    mult = mult * flux
    
    price_sweaters = round(1000 * latitude * mult)
    price_gelato = round(1000 * (1 - latitude) * mult)
    price_coffee = round(1000 * longitude * mult)
    price_tea = round(1000 * (1 - longitude) * mult)
    
def commodities():
    
    prices(location)
    
    global sweaters
    global gelato
    global coffee
    global tea
    global money
    
    print("")
    console.print(money, "$", style="bold green", highlight=False)
    print("")
    print("1. SWEATERS (" + str(price_sweaters) + "$) (" + str(sweaters) + ")")
    print("2. GELATO (" + str(price_gelato) + "$) (" + str(gelato) + ")")
    print("3. COFFEE (" + str(price_coffee) + "$) (" + str(coffee) + ")")
    print("4. TEA (" + str(price_tea) + "$) (" + str(tea) + ")")
    
    prompt = input()
    prompt.lower()
    
    if prompt == "1" or prompt == "sweaters":
        quant = int(input("Amount: "))
        if (quant < 0 and sweaters >= -quant) or (quant > 0 and money >= (price_sweaters * quant)):
           money = money - (price_sweaters * quant)
           sweaters = sweaters + quant
        commodities()
    elif prompt == "2" or prompt == "gelato":
        quant = int(input("Amount: "))
        if (quant < 0 and gelato >= -quant) or (quant > 0 and money >= (price_gelato * quant)):
           money = money - (price_gelato * quant)
           gelato = gelato + quant
        commodities()
    elif prompt == "3" or prompt == "coffee":
        quant = int(input("Amount: "))
        if (quant < 0 and coffee >= -quant) or (quant > 0 and money >= (price_coffee * quant)):
           money = money - (price_coffee * quant)
           coffee = coffee + quant
        commodities()
    elif prompt == "4" or prompt == "tea":
        quant = int(input("Amount: "))
        if (quant < 0 and tea >= -quant) or (quant > 0 and money >= (price_tea * quant)):
           money = money - (price_tea * quant)
           tea = tea + quant
        commodities()
    else:
        loc_prompt()
           
    

ratings = ["Moderate", "Risky", "Dangerous"]

def danger_rate(location):
    location_name = cur.execute("SELECT name FROM airport WHERE id = location")
    rating = 0
    if "v" in location_name:
        rating = 1
    if "k" in location_name:
        rating = 1
    if "j" in location_name:
        rating = 1
    if "x" in location_name:
        rating = 2
    if "z" in location_name:
        rating = 2
    if "q" in location_name:
        rating = 2
    return rating

def loc_intro():
    print("")
    console.print("---", location_name, " ---", style="bold blue")
    console.print("--", ratings[danger_rate(location)], " --", style="bold purple")
    console.print(str(location_latitude), str(location_longitude))
    console.print("Day", time, style="bold red", highlight=False)
    
def maintenance():
    global hull
    global money
    
    maxhull = round(25 * 1.2**lv_hull)
    cost = round(maxhull - hull)
    
    if hull < maxhull and money > cost:
        money = money - cost
        hull = maxhull
        console.print("Hull fortified for", cost, "$", style="yellow", highlight=False)
    
def loc_prompt():
    
    global time
    global money
    
    loc_intro()
    print("")
    print("1. Commodities")
    print("2. Equipment")
    print("3. Takeoff")
    if money >= 1000000:
        console.print("4. Purchase Airport For 1,000,000 $", style="yellow", highlight=False)
        
    prompt = input()
    prompt.lower()
    
    if prompt == "1" or prompt == "commodities":
        commodities()
    elif prompt == "2" or prompt == "equipment":
        equipment()
    elif prompt == "3" or prompt == "takeoff":
        takeoff()
    elif prompt == "4" or prompt == "purchase" or prompt == "purchase airport":
        if money >= 1000000:
            endgame()
        else:
            loc_prompt()
    elif prompt == "quit" or prompt == "exit":
        quit()
    else:
        time = time + 1
        #money = money * 2
        loc_prompt()
        
def equipment():
    
    global money
    global lv_engine
    global lv_shield
    global lv_gun
    global lv_hull
    
    baseprice = 100
    engineprice = round(baseprice * 1.5**lv_engine)
    shieldprice = round(baseprice * 1.5**lv_shield)
    gunprice = round(baseprice * 1.5**lv_gun)
    hullprice = round(baseprice * 1.5**lv_hull)
    
    print("")
    console.print(money, "$", style="bold green", highlight=False)
    print("")
    print("1. GEN " + str(lv_engine + 1) + " -> " + str(lv_engine + 2) + " EFFICIENCY ENGINE (" + str(engineprice) + "$)" )
    print("2. GEN " + str(lv_shield + 1) + " -> " + str(lv_shield + 2) + " ANTIBIRD PATTERN (" + str(shieldprice) + "$)" )
    print("3. GEN " + str(lv_gun + 1) + " -> " + str(lv_gun + 2) + " AIR CANNON (" + str(gunprice) + "$)" )
    print("4. GEN " + str(lv_hull + 1) + " -> " + str(lv_hull + 2) + " STRIKE RESISTANCE (" + str(hullprice) + "$)" )
    
    prompt = input()
    
    if prompt == "1":
        if money > engineprice:
            money = money - engineprice
            lv_engine = lv_engine + 1
            print("Fuel consumption at " + str(round(0.85**lv_engine,2)))
            equipment()
        else:
            console.print("Insufficient funds", style="bold red", highlight=False)
            equipment()
    elif prompt == "2":
        if money > shieldprice:
            money = money - shieldprice
            lv_shield = lv_shield + 1
            print("Bird deterrence at " + str(round(0.9**lv_shield,2)))
            equipment()
        else:
            console.print("Insufficient funds", style="bold red", highlight=False)
            equipment()
    elif prompt == "3":
        if money > gunprice:
            money = money - gunprice
            lv_gun = lv_gun + 1
            print("Bird defense at " + str(round(0.9**lv_gun,2)))
            equipment()
        else:
            console.print("Insufficient funds", style="bold red", highlight=False)
            equipment()
    elif prompt == "4":
        if money > hullprice:
            money = money - hullprice
            lv_hull = lv_hull + 1
            print("Hull fortification at " + str(round( ((30 * 1.2**lv_hull) / 30) * 100 )) + "%")
            equipment()
        else:
            console.print("Insufficient funds", style="bold red", highlight=False)
            equipment()
    else:
        loc_prompt()
        
        
def takeoff():
    
    global location
    global location_name
    global location_longitude
    global location_latitude
    global money
    
    print("")
    console.print(money, "$", style="bold green", highlight=False)
    print("")
    
    destinations = []
    
    for x in range(8):
        destination = cur.execute("SELECT id FROM airport ORDER BY RAND() LIMIT 1;")
        if destination != location:
            destinations.append(destination)
    
    for x in destinations:
        name = cur.execute("SELECT name FROM airport WHERE id = x")
        latitude = round(cur.execute("SELECT latitude_deg FROM airport WHERE id = x"),3)
        longitude = round(cur.execute("SELECT longitude_deg FROM airport WHERE id = x"),3)
        danger = ratings[danger_rate(x)]
        cost = round((math.sqrt((location_longitude - longitude)**2 + (location_latitude - latitude)**2)) * round(0.85**lv_engine,2))
        print(str(name) + " , " + str(latitude) + " , " + str(longitude) + " , " + str(danger) + ", " + str(cost) + "$")
        print(x)
        print("")
        
    target = int(input("Please enter destination ID number: "))
    
    latitude = round(cur.execute("SELECT latitude_deg FROM airport WHERE id = target"),3)
    longitude = round(cur.execute("SELECT longitude_deg FROM airport WHERE id = target"),3)
    cost = round((math.sqrt((location_longitude - longitude)**2 + (location_latitude - latitude)**2)) * round(0.85**lv_engine,2)) * 1.5
        
        if money > cost:
            location = target
            
            location_name = cur.execute("SELECT name FROM airport WHERE id = location")
            location_latitude = round(cur.execute("SELECT latitude_deg FROM airport WHERE id = location"),3)
            location_longitude = round(cur.execute("SELECT longitude_deg FROM airport WHERE id = location"),3)
            flight()
        else:
            console.print("Insufficient funds", style="bold red", highlight=False)
            loc_prompt()
    else:
        loc_prompt()
    
def endgame():
    console.print(location_name, "is yours. As owner of a whole airport, you can now comfortably retire. Enjoy a game well won.", style="yellow", highlight=False)
    quit()

loc_prompt()