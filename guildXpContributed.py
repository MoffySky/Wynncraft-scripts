import requests
import json
#Guild name with %20 in the place of spaces
guildname = "CHANGEME"
# Get the guild stats
url = f"https://api.wynncraft.com/public_api.php?action=guildStats&command={guildname}"
response = requests.get(url)
data = json.loads(response.text)

# Get the guild level and xp
xplvl = data["xp"]
lvl = data["level"]
print("Level " + str(lvl)+ " | " + str(xplvl) +"% to next level")

# Get the guild members contribution
members = data["members"]

# Get the guild members names
names = []
for member in members:
    names.append(member["name"])

# Get the guild members contribution
contributions = []
for member in members:
    contributions.append(member["contributed"])

# Get the guild members rank
ranks = []
for member in members:
    ranks.append(member["rank"])

# print the guild members names, contribution and rank
for i in range(len(names)):
    print(names[i], contributions[i], ranks[i])