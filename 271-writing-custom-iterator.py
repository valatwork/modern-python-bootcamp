# example 1

class Counter:
    def __init__(self,low,high):
        self.low = low
        self.high = high
        
c = Counter(0.10)        
        
iter(c) # TypeError: 'Counter'  object is not iterable
        
for n in Counter(50,55)
    print(n)

## example 1 continued

class Counter:
    def __init__(self,low,high):
        self.low = low
        self.high = high
        
    def __iter__(self):
        return self

c = Counter(0,10)
iter(c)

for x in Counter(0,10):
    print(x)
    
# TypeError: iter() returned non-iterator of type 'Counter'

## example 1 continued

class Counter:
    def __init__(self,low,high):
        self.low = low
        self.high = high
        
    def __iter__(self):
        return self

    def __next__(self):
        # return 1 - infinite loop
    
    
for x in Counter(0,10):
    print(x)

## example 1 - infinite loop fixed

class Counter:
	def __init__(self, low, high):
		self.current = low
		self.high = high

	def __iter__(self):
		return self

	def __next__(self):
		if self.current < self.high:
			num = self.current
			self.current += 1
			return num
		raise StopIteration




for x in Counter(50,70):
	print(x)
 
# it will print all numbers up to 69