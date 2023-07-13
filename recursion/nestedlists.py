def flatten(l):
   result = []
   for el in l:
     if isinstance(el, list):
       flat = flatten(el)
       result += flat
     else:
       result.append(el)
   return result

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
