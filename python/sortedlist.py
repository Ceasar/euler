import bisect

#Need to do something about methods like extend, append
#Methods should ideally be removed

class Queue(list):
    '''A queue object.'''

    def pop(self):
        '''Pop the next element in the queue.'''
        return super(Queue, self).pop(0)

class Cycle(list):
    '''A cycling queue.'''

    def pop(self):
        '''Pop the next element in the queue.'''
        n = super(Queue, self).pop(0)
        self.append(n)
        return n

class SortedList(list):
    '''A sorted list.'''
    def __init__(self, xlist):
        xlist.sort()
        super(SortedList, self).__init__(xlist)

    def insert(self, n):
        '''Insert an element into the list.'''
        super(SortedList, self).insert(bisect.bisect(self, n), n)

    def contains(self, n):
        '''Check if the list contains n.'''
        return self[bisect.bisect_left(self, n)] == n

    def index(self, n):
        '''Get the index of n if it exists.'''
        if self.contains(n):
            return bisect.bisect_left(self, n)
        else:
            raise ValueError('list.index(n): n not in list')

    def count(self, n):
        '''Get the number of occurences of n.'''
        count = 0
        len_self = len(self)
        i = bisect.bisect_left(self, n)
        while i < len_self:
            if self[i] == n:
                count += 1
            else:
                break
            i += 1
        return count

    def remove(self, n):
        '''Remove an element from the list.'''
        if self.contains(n):
            del self[bisect.bisect_left(self, n)]
        else:
            super(SortedList, self).remove(n)
