#This is a challenge I set for myself, I wanted to take every Algebra II math class equation and 'Function' and convert the logic into Python.



# SkyeGamesYT
# Date Created: 8/21/2025
# Date Last Edited: 8/21/2025


#Unit 1: Soda Example Function

def vendingMachineFunction(choice: int):
    if choice < 6 and choice > 0:
        if choice == 1:
            return "Fanta"
        else if choice == 2:
            return "Dr. Pepper"
        else if choice == 3:
            return "Coca Cola"
        else if choice == 4:
            return "Root Beer"
        else if choice == 5:
            return "Sprite"
        else:
            return "Mountain Dew"
    else:
        return None

