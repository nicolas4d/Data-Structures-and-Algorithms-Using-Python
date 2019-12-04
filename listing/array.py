# Implements the Array ADT using array capabilities of the ctypes module.
import ctypes

class Array :
    # Creates an array with size elements.
    def __init__( self, size ):
        assert size > 0, "Array size must be > 0"
        self._size = size
        # Create the array structure using the ctypes module.
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        # Initialize each element.
        self.clear( None )

    # Returns the size of the array.
    def __len__( self ):
        return self._size

    # Gets the contents of the index element.
    def __getitem__( self, index ):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        return self._elements[ index ]

    # Puts the value in the array element at index position.
    def __setitem__( self, index, value ):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        self._elements[ index ] = value

    # Clears the array by setting each element to the given value.
    def clear( self, value ):
        for i in range( len(self) ) :
            self._elements[i] = value

    # Returns the array's iterator for traversing the elements.
    def __iter__( self ):
        return _ArrayIterator( self._elements )

# An iterator for the Array ADT.
class _ArrayIterator :
    def __init__( self, theArray ):
        self._arrayRef = theArray
        self._curNdx = 0

    def __iter__( self ):
        return self

    def __next__( self ):
        if self._curNdx < len( self._arrayRef ) :
            entry = self._arrayRef[ self._curNdx ]
            self._curNdx += 1
            return entry
        else :
            raise StopIteration

# Implementation of the Array2D ADT using an array of arrays.
class Array2D :
    # Creates a 2-D array of size numRows x numCols.
    def __init__( self, numRows, numCols ):
        # Create a 1-D array to store an array reference for each row.
        self._theRows = Array( numRows )

        # Create the 1-D arrays for each row of the 2-D array.
        for i in range( numRows ) :
            self._theRows[i] = Array( numCols )

    # Returns the number of rows in the 2-D array.
    def numRows( self ):
        return len( self._theRows )

    # Returns the number of columns in the 2-D array.
    def numCols( self ):
        return len( self._theRows[0] )

    # Clears the array by setting every element to the given value.
    def clear( self, value ):
        for row in range( self.numRows() ):
            row.clear( value )

    # Gets the contents of the element at position [i, j]
    def __getitem__( self, ndxTuple ):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
            and col >= 0 and col < self.numCols(), \
                "Array subscript out of range."
        the1dArray = self._theRows[row]
        return the1dArray[col]

    # Sets the contents of the element at position [i,j] to value.
    def __setitem__( self, ndxTuple, value ):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
            and col >= 0 and col < self.numCols(), \
                "Array subscript out of range."
        the1dArray = self._theRows[row]
        the1dArray[col] = value

# Implementation of the MultiArray ADT using a 1-D array.
class MultiArray :
    # Creates a multi-dimensional array.
    def __init__( self, *dimensions ):
        assert len(dimensions) > 1, "The array must have 2 or more dimensions."
        # The variable argument tuple contains the dim sizes.
        self._dims = dimensions

        # Compute the total number of elements in the array.
        size = 1
        for d in dimensions :
            assert d > 0, "Dimensions must be > 0."
            size *= d

        # Create the 1-D array_type to store the elements.
        self._elements = Array( size )
        # Create a 1-D array to store the equation factors.
        self._factors = Array( len(dimensions) )
        self._computeFactors()

    # Returns the number of dimensions in the array.
    def numDims( self ):
        return len(self._dims)

    # Returns the length of the given dimension.
    def length( self, dim ):
        assert dim >= 1 and dim < len(self._dims),\
            "Dimension component out of range."
        return self._dims[dim - 1]

    # Clears the array by setting all elements to the given value.
    def clear( self, value ):
        self._elements.clear( value )

    # Returns the contents of element (i_1, i_2, ..., i_n).
    def __getitem__( self, ndxTuple ):
        assert len(ndxTuple) == self.numDims(), "Invalid # of array subscripts."
        index = self._computeIndex( ndxTuple )
        assert index is not None, "Array subscript out of range."
        return self._elements[index]

    # Sets the contents of element (i_1, i_2, ..., i_n).
    def __setitem__( self, ndxTuple, value ):
        assert len(ndxTuple) == self.numDims(), "Invalid # of array subscripts."
        index = self._computeIndex( ndxTuple )
        assert index is not None, "Array subscript out of range."
        self._elements[index] = value

    # Computes the 1-D array offset for element (i_1, i_2, ... i_n)
    # using the equation i_1 * f_1 + i_2 * f_2 + ... + i_n * f_n
    def _computeIndex( self, idx ):
        offset = 0
        for j in range( len(idx) ):
            # Make sure the index components are within the legal range.
            if idx[j] < 0 || idx[j] >= self._dims[j] :
                return None
            else : # sum the product of i_j * f_j.
                offset += idx[j] * self._factors[j]
        return offset

    # Computes the factor values used in the index equation.
    def _computeFactors( self ):
        pass
