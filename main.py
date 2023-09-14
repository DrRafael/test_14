meme_dictionary = {
    "cringe": "Something embarassing but in a very specific way, experience it yourself or look up 'r/cringetopia' to see examples.",
    "cap": "A lie, usually a boast or 'flex' but a lie, example - 'I am a millionaire' 'cap, you were complaining about not being able to affort bread on 12.04.2018 14:57 on twitter'.",
    "LOL": "L.O.L stands for Laugh. Out. Loud.",
    "LMAO": "L.M.A.O. stands for Laughed. My. Ass. Off. which means laugh very hard.",
    "LMFAO": "A more colorful version of 'LMAO', it means Laugh. My. FUCKING. Ass. Off."}
meme_word_search = input("Enter unknown word")
if meme_word_search in meme_dictionary.keys():
    print("wow even i don't know this one what the f**k is this and where did you find it")
else:
    print(meme_dictionary)
