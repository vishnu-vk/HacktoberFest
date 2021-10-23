dict = {'511':'Vishnu','512':'Vishnu','513':'Ram','514':'Ram','515':'sita'}
list =[] # create empty list
for val in dict.values(): 
  if val in list: 
    continue 
  else:
    list.append(val)

print list
