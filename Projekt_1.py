
uzivatele = {"bob" : "123", "ann" : "pass123", "mike" : "password123", "liz" : "pass123"}
oddelovac = "~" * 55


text1 = """Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley."""
text2 = """"At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick."""
text3 = """The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present."""

TEXTS = {}

TEXTS[1] = text1
TEXTS[2] = text2
TEXTS[3] = text3

#jmeno a heslo

username = input("Zadej jméno: ")

if username in uzivatele.keys():
    print("Pokračuj..")
else:
    print("Neplatný údaj!")
    exit()

password = input("Zadej heslo: ")
if password in uzivatele.values():
    print("Pokračuj..")
else:
    print("Neplatný údaj!")
    exit()

#pozdravit registrovaneho uzivatele
print(oddelovac)
print("username: ", username)
print("password: ", password)
print(oddelovac)

print(f"Welcome to the app, {username.title()}!")
print(f"We have {len(TEXTS)} texts to be analyzed.")
print(oddelovac)

vyber = int(input("Enter a number btw 1 and 3 to select: "))

print(oddelovac)
if vyber in TEXTS.keys() and vyber  == 1:
    print(TEXTS[1])
    text = TEXTS[1]

elif vyber in TEXTS.keys() and vyber  == 2:
    print(TEXTS[2])
    text = TEXTS[2]

elif vyber in TEXTS.keys() and vyber  == 3:
    print(TEXTS[3])
    text = TEXTS[3]
else:
    print("Neplatný údaj!")
    exit()

#analyza textu
text = text.replace('\n', ' ')
slovnik_textu = text.split(' ')

pocet_zacinajicich_velkym = 0
pocet_velkym_pismem = 0
pocet_malym_písmem = 0
pocet_cisel = 0
soucet_cisel = 0
delky_slov = {}

for slovo in slovnik_textu:
    # slovo_s = slovo.strip()
    if slovo:
        delka = len(slovo)

        if delka in delky_slov:
            delky_slov[delka] += 1
        else:
            delky_slov[delka] = 1

        if slovo.isnumeric():
            pocet_cisel += 1
            soucet_cisel += int(slovo)

            pass
        else:
            #print(slovo)

            if not slovo[0].isnumeric() and slovo[0] == slovo[0].upper():
                pocet_zacinajicich_velkym += 1
            if not slovo[0].isnumeric() and slovo == slovo.upper():
                pocet_velkym_pismem += 1
                #print(slovo)
            if not slovo[0].isnumeric() and slovo[0] == slovo[0].lower():
                pocet_malym_písmem += 1



print(oddelovac)
print(f"There is {len(slovnik_textu)} words in selected text.")
print(f"There are {pocet_zacinajicich_velkym} words in the selected text.")
print(f"There are {pocet_velkym_pismem} uppercase words." )
print(f"There are {pocet_malym_písmem} lowercase words in selected text.")
print(f"There is {pocet_cisel} numeric strings.")
print(f"The sum of all the numbers is {soucet_cisel}." )
print(oddelovac)

padding_length = 16

#print(delky_slov)
print("LEN", "OCCURENCES", "NR.", sep="|".center(padding_length))
print(oddelovac)
sorted_delky_slov = dict(sorted(delky_slov.items()))
for key, value in sorted_delky_slov.items():
    print(str(key).center(10) + "| " + "*" * value + " " * (padding_length - value + 1) + " " * 6 + " | " + str(value))




