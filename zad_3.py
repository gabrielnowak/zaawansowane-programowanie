def print_even_values (list):#
   even_values = []
   for i in range(0,len(list)):
      if list[i]%2==0:
         even_values.append(list[i])
   print(even_values)
def print_even_elements (list):#
   even_elements = []
   for i in range(0,len(list)):

      if i%2:
         even_elements.append(list[i])
   print(even_elements)

list2 = [3,2,1,6,12,22,0,39,1,14]
print_even_values(list2)
print_even_elements(list2)