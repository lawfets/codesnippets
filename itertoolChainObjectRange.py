from itertools import chain

a1 = range(10,0,-2)
a2 = range(30,20,-2)
a3 = range(50,40,-2)

final = chain(a3,a2,a1)

#print(final) #generator object

print(list(final))
print(list(final)) #from here we get [] as final is a generator object, as soon as it has gone through it's body it has nothing more to give.


for i in final:
    if list(final) == []:
        print("Nothing to see")
    else:
        print(i)
print("this is it")








# https://www.datacamp.com/community/tutorials/python-range-function?utm_source=adwords_ppc&utm_campaignid=898687156&utm_adgroupid=48947256715&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=332602034352&utm_targetid=dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9040096&gclid=CjwKCAjw3riIBhAwEiwAzD3TicCWTJKUsYDp-jGcbUhwgFR1TCZrTWhHdKgzqXKrhtQqqwsjFwQqvBoCE-EQAvD_BwE
