"""
Consider an array of sheep where some sheep
 may be missing from their place.
  We need a function that counts 
  the number of sheep present in the array (true means present).

"""
def count_sheeps(arrayOfSheeps):
    new_list = list(filter((lambda x: x != None),arrayOfSheeps))
    new_list = sum([int(i) for i in new_list ] )
    return new_list



