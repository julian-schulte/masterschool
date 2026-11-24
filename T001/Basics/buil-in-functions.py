'''
🧪 Deine Aufgaben:
get_max(numbers)
➤ Gib die größte Zahl in einer Liste zurück.
only_unique(items)
➤ Gib die Liste ohne Duplikate zurück.
starts_with(text, start)
➤ Prüfe, ob text mit dem String start beginnt.
factorial(n)
➤ Gib die Fakultät der Zahl n zurück.
all_equal(items)
➤ Gib True zurück, wenn alle Elemente in der Liste identisch sind.
'''

def get_max(numbers):
    max_num = max(numbers)
    return max_num

def only_unique(items):
    unique_items = list(set(items))
    return unique_items 

def starts_with(text, start):
    return text.startswith(start)

def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

def all_equal(items):
    return len(set(items)) == 1
