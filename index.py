
list = [7,15,12,5,6]

def bubble_sort():
    list_2= len(list)
    for x in range(list_2):
        # hodnota nad
        for y in range(0, list_2-x-1):
            # Porovnává hodnoty mezi senou
            if list[y] > list[y+1]:
                # Mění hodnoty mezi sebou
                list[y], list[y+1] = list[y+1], list[y]
    else:
        return list
        

print(bubble_sort())


    
    
       
        
           
           
           
    
      


bubble_sort()
