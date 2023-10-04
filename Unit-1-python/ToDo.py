ToDo = ['get cash', 'spend cash', 'cry']
# Made a list i think
s= True
while s == True: #just to make sure it keeps running
    print("This is your todo list") 
    m = 1 # m is my index 
    for items in ToDo:
        print(str(m) + '. ' + items) # when you add m plus items it would give you the item to the number.
        m+=1
    #print(ToDo)# its to print what's inside of the list
    print()
    # the print is their to space it out
    a = str(input("Do you want to remove or add?(add, rem)")) # i made a string that ask you if you would like to add or remove something 
    if a == 'add':
        ToDo.append(input(print('Add your item'))) # The append means to add something at the back of  your list 
    elif a =='rem':
        r = int(input('What number do you want to delete')) # What number do you want to remove
        r -= 1
        ToDo.pop(r)
        print("Your item has been removed")
    else:
        print("Please give correct")