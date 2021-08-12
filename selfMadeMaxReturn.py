list1 = [2,5,4,6,3,8,9,7,1]
list2 = [-4,5,-3,8,-7,2,5,1,3,6]

def maxFunction(attrList,attrList2):
    value1 = attrList[0]
    
    for item in attrList:
        if item <= value1:
            value1 = item
    attrList2.append(value1)
    attrList.remove(value1)
    if len(attrList)> 0:
        maxFunction(attrList,attrList2)
    return attrList2
    
print(maxFunction(list2, []))

# weird little story here, if I put the return immediately after if
#   attrList2 is effectively returned.
#   but if I put it in an else construction it only prints but doesn't return anything.
            
    
                 
    
    
      
