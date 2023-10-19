#!/usr/bin/env python

print('WHAT GENRE YOU PREFER ?')
"""Choose either Pop20an,Jazz or Rock"""
user_pick = input().casefold()

pop20an = ['Cinta Adam dan Hawa – Misha Omar.' , 
"Dan Sebenarnya – Yuna." ,
'Dingin – Ziana Zain.' ,
'Lagu Kita – Aizat Amdan.', 
"Dengarkan – Shiela Amzah. " ,
 ]

jazz = [" Ku Mohon– Shiela Majid." , 
"Hanya Dikau – P.Ramlee",
"Lihatlah – Asiah",
"Puteri Remaja – Jasni" 
] 

rock = ["Bila Aku Sudah Tiada – Hujan", 
"Pelita – Buncface ", 
"Mata Hati – Azlan & Typewriter", 
"Roman Cinta – Mojo", 
"Potret – Akim & Typewriter",
]
genre = ["pop20an", "jazz" , "rock"]

import random
i = user_pick
for i in genre :
    if user_pick == "pop20an":
        blues_song = random.choice(pop20an)
        print(blues_song)
        break
    elif user_pick == "jazz" :
        jazz_song = random.choice(jazz)
        print(jazz_song)
        break      
    elif user_pick == "rock" :
        rock_song = random.choice(rock)
        print(rock_song)
        break
    else:
        print("pick another genre")
        break
