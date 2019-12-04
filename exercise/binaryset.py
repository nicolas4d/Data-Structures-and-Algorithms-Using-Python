class Set:
    def __init__(self):
        self._theElements = list()

    def __len__(self):
        return len(self._theElements)

    def __contains__(self, el):
        ndx = self._findPosition(el)
        return ndx < len(self) and self._theElements[ndx] == el

    def add(self, element):
        if element not in self:
            ndx = self._findPosition(element)
            self._theElements.insert(ndx, element)

    def remove(self, element):
        assert element in self, "The element must be in the set."
        ndx = self._findPosition(element)
        self._theElements.pop(ndx)

    def isSubsetOf(self, setB):
        for element in self:
            if element not in setB:
                return False
        return True

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        else:
            for i in range(len(self)):
                if self._theElements[i] != other._theElements[i]:
                    return False
            return True

    def __iter__(self):
        return _SetIterator(self._theElements)

    def _findPosition(self, element):
        low = 0
        high = len(self) - 1
        while low <= high:
            mid = (low + high) // 2
            if element == self._theElements[mid]:
                return mid
            elif element < self._theElements[mid]:
                high = mid - 1
            else :
                low = mid + 1
        return low

    def union(self, setB):
        newSet = Set()
        a = 0
        b = 0

        while a < len(self) and b < len(setB):
            valueA = self._theElements[a]
            valueB = setB._theElements[b]
            if valueA < valueB:
                newSet._theElements.append(valueA)
                a += 1
            elif valueA > valueB:
                newSet._theElements.append(valueB)
                b += 1
            else :
                newSet._theElements.append(valueA)
                a += 1
                b += 1

        while a < len(self):
            newSet._theElements.append(self._theElements[a])
            a += 1

        while b < len(setB):
            newSet._theElements.append(setB._theElements[b])
            b += 1

        return newSet

    def isSubsetOf(self, other):
        """is subset of other set."""
        selfNdx = 0
        otherNdx = 0

        while selfNdx < len(self) and otherNdx < len(other) :
            # same value plus 1 each indx
            if self._theElements[selfNdx] == other._theElements[otherNdx]:
                selfNdx += 1
                otherNdx += 1
                # value bigger than others valuse plus one other ndx
            elif self._theElements[selfNdx] > other._theElements[otherNdx]:
                otherNdx += 1
                # value lower than others do nothing
            else :
                pass

        if selfNdx == len(self):
            return True
        else:
            return False

    def intersect(self, other):
        intersection = Set()
        selfNdx = 0
        otherNdx = 0

        while selfNdx < len(self) and otherNdx < len(other):
            curSelfValue = self._theElements[selfNdx]
            curOtherValue = other._theElements[otherNdx]

            if curSelfValue == curOtherValue:
                intersection.add(curSelfValue)
                selfNdx += 1
                otherNdx += 1
            elif curSelfValue > curOtherValue:
                otherNdx += 1
            else:
                selfNdx += 1

        return intersection

    def difference(self, other):
        diffSet = Set()
        selfNdx = 0
        otherNdx = 0

        while selfNdx < len(self) and otherNdx < len(other):
            curSelfValue = self._theElements[selfNdx]
            curOtherValue = other._theElements[otherNdx]

            if curSelfValue == curOtherValue:
                selfNdx += 1
                otherNdx += 1
            elif curSelfValue > curOtherValue:
                otherNdx += 1
                if otherNdx < len(other) or \
                   (otherNdx < len(other) and \
                   curSelfValue < other._theElements[otherNdx]):
                   diffSet.add(curSelfValue)
            else:
                selfNdx += 1
                diffSet.add(curSelfValue)

        return diffSet

class _SetIterator:
    def __init__(self, elements):
        self._elements = elements
        self._ndx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._ndx < len(self._elements) :
            el = self._elements[self._ndx]
            self._ndx += 1
            return el
        else :
            raise StopIteration
