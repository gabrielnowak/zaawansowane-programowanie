def is_in_list (list, x):
   return x in list

list = [1,2,3,4]
list1 = [1,5,6,7,8,9]
inlist = is_in_list(list,1)
if(inlist):
   print("That number is in list")
else:
   print("That number is not in list")