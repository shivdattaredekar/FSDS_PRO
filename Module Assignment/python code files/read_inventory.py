def disply_inventory(file_name):
    with open(file_name,'r') as file:
        for i in file:
            print(i.strip())

disply_inventory('inventory.txt')
