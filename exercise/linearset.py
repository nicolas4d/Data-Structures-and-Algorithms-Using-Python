class Set:
    def __init__(self, *initElements):
        if initElements == None:
            self._theElements = list()
        else :
            self._theElements = list(initElements)

    def __len__(self):
        return len(self._theElements)

    def __contains__(self, element):
        return element in self._theElements

    def add(self, element):
        if element not in self:
            self._theElements.append(element)

    def remove(self, element):
        assert element in self, "The element must be in the set."
        self._theElements.remove(element)

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        else :
            return self.isSubsetOf(other)

    def isSubsetOf(self, other):
        for element in self:
            if element not in other:
                return False
        return True

    def __iter__(self):
        return _SetIterator(self._theElements)

    def union(self, other):
        newSet = Set()
        newSet._theElements.extend(self._theElements)
        for element in other:
            if element not in self:
                newSet._theElements.append(element)
        return newSet

    def intersect(self, setB):
        newSet = Set()

        for element in self:
            if element in self and element in setB:
                newSet.add(element)

        for element in setB :
            if element in self and element in setB:
                newSet.add(element)

        return newSet

    def difference(self, setB):
        differSet = Set()

        # in self not in setB
        for e in self:
            if e not in setB:
                differSet.add(e)

        return differSet

    def isEmpty(self):
        return len(self._theElements) == 0

    def properSubset(self, other):
        """A is a proper subset of B, if A is a subset of B and A does not
equal B."""
        if self.isSubsetOf(other) and len(self) != len(other) :
            return True
        else :
            return False

    def __str__(self):
        printString = "("
        for elem in self:
            printString += str(elem) + ", "
        printString = printString[0:-2] + ")"

        return printString

    def __add__(self, other):
        return self.union(other)

    def __mul__(self, other):
        return self.intersect(other)

    def __sub__(self, other):
        return self.difference(other)

    def __lt__(self, other):
        return self.isSubsetOf(other)

class _SetIterator:
    def __init__(self, elements):
        "docstring"
        self._elements = elements
        self._ndx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._ndx < len(self._elements) :
            e = self._elements[self._ndx]
            self._ndx += 1
            return e
        else :
            raise StopIteration

