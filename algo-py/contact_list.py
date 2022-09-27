'''
trienode model.
'''

class trieNode:
    def __init__(self):
        self.endOfWord = 0 
        self.children = {}
        self.memo = 0
    

def add(trie, word):
    cursor = trie
    for letter in word:
        if cursor.children.get(letter) is None:
            cursor.children[letter] = trieNode()
        cursor = cursor.children[letter]
        cursor.memo = cursor.memo + 1
    cursor.endOfWord = 1
    

def find(trie, partial):
    cursor = trie
    for letter in partial:
        cursor = cursor.children.get(letter)
        if cursor is None:
            return 0
    return cursor.memo


def contacts(queries):
    contactsList = trieNode()
    countList = []
    for queryType, queryValue in queries:
        if queryType == 'add':
            add(contactsList, queryValue)
        else:
            pCount = find(contactsList, queryValue)
            countList.append(pCount)
    return countList


a = [['add', 'hack'], 
     ['add', 'hackerrank'], 
     ['add', 'philipe'],
     ['add', 'hpilipe'],
     ['find', 'hac'], 
     ['find', 'hak'],
     ['find', 'h']]


print(contacts(a))