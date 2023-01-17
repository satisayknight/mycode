farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
animals=farms[0]["agriculture"]

for x in animals:
    print(x)

for farm in farms:
    print("--", farm["name"])
choice= input("pick a farm!\n")

for farm in farms:
     if farm["name"].lower() == choice.lower():
     print(farms["choice"]["agriculture]
