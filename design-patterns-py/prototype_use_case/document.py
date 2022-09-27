import copy # a python library useful for deep copying
from interface_prototype import IPrototype

class Document(IPrototype):
    "A concrete class"

    def __init__(self, name, l):
        self.name = name
        self.list = l

    def clone(self, mode):
        "This clone method uses different copy techniques"

        if mode == 1:
            #result in a 1 level shallow copy of the Document
            doc_list = self.list
        
        if mode == 2:
            #results in a 2 level shallow copy of the doc
            # since it also create new references for the 
            # 1st level list elevement as well.
            doc_list = self.list.copy()

        if mode == 3:
            #recursive deep copy. Slower but results in a new
            # copy where no sub elements are shared by ref.
            doc_list = copy.deepcopy(self.list)

        return type(self)(self.name, doc_list)

    def __str__(self):
        "Overriding the default __str__ method for our object"
        return f"{id(self)}|\tname={self.name}\tlist={self.list}"