from module import area, circumference

area(4,5)

circumference(9)





shopping_cart = []


def add_item(items):
    shopping_cart.append(items)
    return shopping_cart

def del_item(itemz):
    shopping_cart.remove(itemz)
    return
    
def main():
    while True:
        # clear_output()

        query = input("what would you like to do Add/Delete/See/Quit?")
       
        if query == 'Add':
            item = input("what would you like to add?")
            add_item(item)
        elif query == 'Delete':
            item = input("What would you like to delete?")
            del_item(item)
        elif query == 'See':
            print(shopping_cart)
        elif query == 'Quit':
            break
    
main()


