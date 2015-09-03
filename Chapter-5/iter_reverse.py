class iter_reverse:
    def __init__(self,l):
        self.i=0
        self.length=len(l)
        l.reverse()
        self.lis=l
    def __iter__(self):
        return self
    def next(self):
        if self.i < self.length:
            i=self.i
            self.i += 1
            return self.lis[i]
        else:
            raise StopIteration()
    


i=iter_reverse([1,2,3,4,5])
print i.next()
print i.next()
print i.next()
print i.next()
print i.next()
print i.next()
