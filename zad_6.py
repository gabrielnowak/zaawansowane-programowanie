def join_lists (list1, list2):
   joined = set(list1+list2)
   powered = []
   for x in joined:
      powered.append(x**3)
   return powered
list = [1,2,3,4]
list1 = [1,5,6,7,8,9]
print(join_lists(list,list1))