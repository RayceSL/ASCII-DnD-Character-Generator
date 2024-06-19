# Fixed Medium size category weight, I forgot to multiply the height modifier by a weight modifier before adding it to the base weight
import random # Gives access to the .randint() method
import math   # Gives access to the .floor() method, needed to round numbers down
from ability_roll import *
from portrait import *
import codecs # this enables UTF-8


#  █████  ██████  ██ ██      ██ ████████ ██ ███████ ███████ 
# ██   ██ ██   ██ ██ ██      ██    ██    ██ ██      ██      
# ███████ ██████  ██ ██      ██    ██    ██ █████   ███████ 
# ██   ██ ██   ██ ██ ██      ██    ██    ██ ██           ██ 
# ██   ██ ██████  ██ ███████ ██    ██    ██ ███████ ███████

# Rolls for Strength
str = ability_roll()
str_mod = math.floor((str - 10) / 2)

# Rolls for Dexterity
dex = ability_roll()
dex_mod = math.floor((dex - 10) / 2)

# Rolls for Constitution
con = ability_roll()
con_mod = math.floor((con - 10) / 2)

# Rolls for Wisdom
wis = ability_roll()
wis_mod = math.floor((wis - 10) / 2)

# Rolls for Intelligence (iq)
iq = ability_roll()
iq_mod = math.floor((iq - 10) / 2)

# Rolls for Charisma
cha = ability_roll()
cha_mod = math.floor((cha - 10) / 2)

#  ██████ ██   ██  █████  ██████   █████   ██████ ████████ ███████ ██████  
# ██      ██   ██ ██   ██ ██   ██ ██   ██ ██         ██    ██      ██   ██ 
# ██      ███████ ███████ ██████  ███████ ██         ██    █████   ██████  
# ██      ██   ██ ██   ██ ██   ██ ██   ██ ██         ██    ██      ██   ██ 
#  ██████ ██   ██ ██   ██ ██   ██ ██   ██  ██████    ██    ███████ ██   ██ 

# Chooses Medium or Small Size Category
choose_size = random.randint(1, 10)
if choose_size == 1:
    size = "Small"
else:
    size ="Medium"

# ↓ MEDIUM SECTION ↓
# Base height is 56 in • Height mod is +2d10
# Base weight is 110 lb • Weight mod is * 2d4 lb

# Rolls for height modifier
med_hgt_mod = (random.randint(1, 10) + random.randint(1, 10))
# Calculates height in inches
pre_med_hgt = 56 + med_hgt_mod

# Converts height to feet & inches
pre_med_ft = pre_med_hgt / 12
med_ft = math.floor(pre_med_ft) # Feet portion of height
med_ft_remainder = pre_med_ft - med_ft
med_in = round(med_ft_remainder * 12) # Inches portion of height

# Calculates weight (lb)
med_wgt = 110 + med_hgt_mod * (random.randint(1, 4) + random.randint(1, 4))

# ↓ SMALL SECTION ↓
# Base height is 31 in • Height mod is 2d4
# Base weight is 35 lb • Weight mod is * 1 lb

# Rolls height modifier
small_hgt_mod = random.randint(1, 4) + random.randint(1, 4)
# Calculates height
pre_small_hgt = 31 + small_hgt_mod
# Converts height to feet & inches
pre_small_ft = pre_small_hgt / 12
small_ft = math.floor(pre_small_ft) # Feet portion of height
small_ft_remainder = pre_small_ft - small_ft
small_in = round(small_ft_remainder * 12) # Inches portion of height

# Calculates weight (lb)
small_wgt = 35 + small_hgt_mod

# Chooses an ethnicity
eth = ["Calishite", "Chondathan", "Damaran", "Illuskan", "Mulan", "Rashemi", "Shou", "Tethyrian", "Turami", "Arkaiun", "Bedine", "Ffolk", "Gur", "Halruaan", "Imaskari", "Nar", "Shaaran", "Tuigan", "Ulutiun"]

# Chooses sex
sex = ["♂", "♀"]

#  ██████ ██       █████  ███████ ███████ 
# ██      ██      ██   ██ ██      ██      
# ██      ██      ███████ ███████ ███████ 
# ██      ██      ██   ██      ██      ██ 
#  ██████ ███████ ██   ██ ███████ ███████ 
#
# Barbarian: STR
# Bard: CHA
# Cleric: WIS
# Druid: WIS
# Fighter: STR or DEX
# Monk: DEX & WIS
# Paladin: STR & CHA
# Ranger: DEX & WIS
# Rogue: DEX
# Sorcerer: CHA
# Warlock: CHA
# Wizard: INT

if str < 10:
    sug_class = "Do not choose Barbarian, Fighter, or Paladin."
elif dex < 10:
    sug_class = "Do not choose Fighter, Monk, Ranger, or Rogue."
elif wis < 10:
    sug_class = "Do not choose Cleric, Druid, Monk, or Ranger."
elif iq < 10:
    sug_class = "Do not pick Wizard."
elif cha < 10:
    sug_class = "Do not pick Bard, Sorcerer, or Warlock."
else:
    sug_class = "You have good Ability Scores! Feel free to pick any class you want."

#  ██████  ██    ██ ████████ ██████  ██    ██ ████████ 
# ██    ██ ██    ██    ██    ██   ██ ██    ██    ██    
# ██    ██ ██    ██    ██    ██████  ██    ██    ██    
# ██    ██ ██    ██    ██    ██      ██    ██    ██    
#  ██████   ██████     ██    ██       ██████     ██    

file = codecs.open("character_sheet.txt", 'w', 'utf-8') # the w means we open the file intending to write to it

if choose_size == 1:
    file.write(f"""
{random.choice(FACE_1)}
{random.choice(FACE_2)}
{random.choice(FACE_3)}
┌──────────────────────────────
│ ℂ𝕙𝕒𝕣𝕒𝕔𝕥𝕖𝕣 𝕊𝕙𝕖𝕖𝕥
│ 
│ Race: Human • {random.choice(eth)} • {random.choice(sex)}
│ Size: {size}
│ HGT: {small_ft}′ {small_in}″ • WGT: {small_wgt} lb
│ 
│ • Strength:.......({str}) {str_mod}
│ • Dexterity:......({dex}) {dex_mod}
│ • Constitution:...({con}) {con_mod}
│ • Wisdom:.........({wis}) {wis_mod}
│ • Intelligence:...({iq}) {iq_mod}
│ • Charisma:.......({cha}) {cha_mod}
╘══════════════════════════════
Tips: {sug_class}
""")
else:
    file.write(f"""
{random.choice(FACE_1)}
{random.choice(FACE_2)}
{random.choice(FACE_3)}
┌──────────────────────────────
│ ℂ𝕙𝕒𝕣𝕒𝕔𝕥𝕖𝕣 𝕊𝕙𝕖𝕖𝕥
│
│ Race: Human • {random.choice(eth)} • {random.choice(sex)}
│ Size: {size}
│ HGT: {med_ft}′{med_in}″ • WGT: {med_wgt} lb
│
│ • Strength:.......({str}) {str_mod}
│ • Dexterity:......({dex}) {dex_mod}
│ • Constitution:...({con}) {con_mod}
│ • Wisdom:.........({wis}) {wis_mod}
│ • Intelligence:...({iq}) {iq_mod}
│ • Charisma:.......({cha}) {cha_mod}
╘══════════════════════════════
Tips: {sug_class}
""")
    
file.close()