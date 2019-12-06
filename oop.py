# Exploring Python magic methods
# https://rszalski.github.io/magicmethods/

class MyMagicObject(object):
    '''
    Object that uses Python magic methods
    '''

    def __init__(self):
        '''
        Initiate object
        '''
        self.n = 0
        self.capacity = 1
        self.array = self.make_array(self.capacity)

    def __len__(self):
        '''
        Return n
        '''
        return self.n

    def __getitem__(self, n):
        '''
        Get element at index n
        '''
        self._checkboundaries(n)
        return self.array[n] # Return element

    def __setitem__(self, n, el):
        '''
        Set new element at index n
        '''
        self._checkboundaries(n)
        self.array[n] = el
        
    def __delitem__(self, n):
        '''
        Delete element at index n
        '''
        self._checkboundaries(n)
        del self.array[n]
        self.n -= 1 # Reset n
        self.capacity -= 1 # Reset capacity

    # def __iter__(self):
    #     '''
    #     Iterate through elements
    #     '''
    #     return iter(self.array)

    def _checkboundaries(self, n):
        '''
        Check if n is in the capacity of array
        '''
        if not 0 <= n < self.n:
            return IndexError('Index out of bounds')

        return n
    
    def _resize(self, size):
        '''
        Resize capacity
        '''
        temp = self.make_array(size) # Make the new array
        for i in range(self.n):
            temp[i] = self.array[i] # Copy everything to temp

        self.array = temp # Swap arrays
        self.capacity = size # Reset capacity

    def make_array(self, capacity):
        '''
        Make an array like list with modified size
        '''
        return [None] * capacity

    def append(self, el):
        '''
        Add element to the end
        '''
        if self.n == self.capacity:
            self._resize(self.capacity + 1) # Make some room
        
        self.array[self.n] = el
        self.n += 1

    def get(self, n):
        '''
        Get an element at index n
        '''
        self._checkboundaries(n)
        return self.array[n] # Return element

myObject = MyMagicObject()

print('Object length {}'.format(len(myObject)))
print('Append 1')
myObject.append(1)
print('Append 2')
myObject.append(2)
print('Object length {}'.format(len(myObject)))
print('Object at {} is {}'.format(0, myObject[0]))
print('Object at {} is {}'.format(1, myObject.get(1)))
print('Change element at 0 to 9')
myObject[0] = 9
print('Object at {} is {}'.format(0, myObject[0]))
print('Delete element at 0')
del myObject[0]
print('Object length {}'.format(len(myObject)))
print('Object at {} is {}'.format(0, myObject[0]))
print('Append 4')
myObject.append(4)
print('Append 6')
myObject.append(6)
print('iterate elements')
print(', '.join([str(i) for i in myObject]))