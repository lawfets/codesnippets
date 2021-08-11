def greetingsFunction(*names): # You don't know how many items in the attribute
    for name in names:          # so you use an asterix before the attribute
        print('Welcome ' + name )

greetingsFunction('John','Tim', 'Tom')

def greetingsFunction2(*names):
    print('Welcome ' + names[0]) #although names is a tuple, you still use [] to show the index, just like in a list
    print(type(names))

greetingsFunction2('John','Tim', 'Tom')


    
