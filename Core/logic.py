

'''
  Functions Always return a value
    -> Functions which return True, or False only, are Predicate (Functions)
    -> Functions which return Numeric Values
    -> Functions which return Strings/Symbols are State Functions
    
  A Procedure is a Function; which can take arguments,
    which do not return a value
'''




'''
  For any element, apply the *predicate*; Returns *True*
  if any succeed
'''
def for_any(iterable, predicate):
    
    for item in iterable:
      if predicate(item):
          return True
    return False

'''
  For each element apply the *predicate*; Returns *True*
  if all succeed
'''
def for_all(iterable, predicate):
    for item in iterable:
        if not predicate(item):
            return False
    return True 
    
    
    
''' 
     Takes a input Sequence, and applies predicate; 
     if sucessful, records a list of indices successful 
     
     Associated with *filter*
''' 
def extrude(sequence, predicate): 
  indexes = [] 
  for index, element in enumerate(sequence): 
    if predicate(element): 
      indexes.append(index) 
  return indexes  
  
  
  
'''
  Sequence = [0,0,0, 1,2,3]
  Keys = [3, 4, 5]
  
  extrude => 
  
  Takes a sequences and maps another sequences values, to the corresponding
    indices; returning its values.

[0,0,0, 0,0,0, 0,0,0]
[0,1,2, 3,4,5, 6,7,8]


Return a List of Indexes that correspond to a given predicate



'''
  
def filtrate_indexed(sequence, predicate):
  indexes = []
  for index, element in enumerate(sequence):
    if predicate(element): 
      indexes.append(index)
  return indexes
  
'''
  Applies a filter to a sequence, given a predicate
'''
def filtrate(sequence, predicate):
  values = [] 
  for element in sequence: 
    if predicate(element): 
      values.append(element) 
  return values  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
