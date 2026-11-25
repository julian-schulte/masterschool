'''
Herausforderung 1 – ✏️ Listen
Erstelle eine Liste mit dem Namen original_list, die mindestens 5 Elemente enthält (z. B. Zahlen, Texte oder gemischt).


1. Gib die ursprüngliche Liste aus.
2. Ändere das erste Element der Liste und gib sie erneut aus.
3. Füge am Ende der Liste ein neues Element hinzu und gib sie aus.
4. Verwende Slicing, um einen Teil der Liste zu ersetzen (z. B. Elemente von Index 2 bis 4), und gib die Liste danach aus.
'''

#1
original_list = [1,2,3,4,5]
print(original_list)

#2
original_list[0] = 67
print(original_list)

#3
original_list.append("Baddie <3")
print(original_list)

#4
original_list[2:4] = ["six", "seven"]
print(original_list)


