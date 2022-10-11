def print_list(names):
   names = [name for name in names]
   print (names)
def multiply_list_by_2_v1 (list):
   multiplied = [x*2 for x in list]
   return multiplied

def multiply_list_by_2_v2 (list): # todo
   multiplied = []
   for x in list:
      multiplied.append(x*2)
   return multiplied

print_list({"Ala","Ania","Agata","Angela","Aria"})
list = [1,2,3,4,5]
print(multiply_list_by_2_v1 (list))
print(multiply_list_by_2_v2 (list))
