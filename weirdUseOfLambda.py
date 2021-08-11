# Python program to demonstrate ternary operator
a, b = 10, 20
  
# Use tuple for selecting an item
# (if_test_false,if_test_true)[test]
print( (b, a) [a < b] )
  
# Use Dictionary for selecting an item
print({True: a, False: b} [a < b])
  
# lamda is more efficient than above two methods
# because in lambda  we are assure that
# only one expression will be evaluated unlike in
# tuple and Dictionary
# if false lambda: b, if true: lambda: a
#   so position is critical for false and true
# but I still don't know why () is necessary
# potentially because lambda is a function and a function uses brackets
print((lambda: b, lambda: a)[a < b]())
#########################################################################

# use of map on lambda function

nums = [48, 6, 9, 21, 1]

square_all = map(lambda num: num ** 2, nums)

print(square_all)
# gives <map object at 0x103e065c0>
print(list(square_all))
#gives [2304, 36, 81, 441, 1]
