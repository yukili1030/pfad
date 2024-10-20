def start_game():
    print("Welcome to the adventure game!")
    print("You wake up and find yourself in a mysterious forest.")
    first_choice()

def first_choice():
    print("\nThere are two roads in front of you：")
    print("1. Turn left")
    print("2. Turn right")
    
    choice = input("Which path do you choose？（Input 1 or 2）: ")
    
    if choice == "1":
        left_path()
    elif choice == "2":
        right_path()
    else:
        print("Invalid selection, please select again.")
        first_choice()

def left_path():
    print("\nYou go to the left，found a scary wolf！")
    print("You can choose：")
    print("1. Escape")
    print("2. Confrontation with wolves")
    
    choice = input("What do you choose?（Input 1 or 2）: ")
    
    if choice == "1":
        print("\nYou managed to escape！You are back to the beginning of the forest.")
        first_choice()
    elif choice == "2":
        print("\nThe wolf attacked you，You failed！")
        play_again()
    else:
        print("Invalid selection, please select again.")
        left_path()

def right_path():
    print("\nYou go to the right，Found an old castle.")
    print("You can choose：")
    print("1. Entering the Castle")
    print("2. Keep going")
    
    choice = input("What do you choose?（输入 1 或 2）: ")

    if choice == "1":
        print("\nThere is a treasure in the castle！You win！")
        play_again()
    elif choice == "2":
        print("\nYou keep going，found a beautiful garden。")
        print("You can choose：")
        print("1. Picking flowers")
        print("2. Rest")
        
        choice = input("What do you choose?（Input 1 or 2）: ")
        
        if choice == "1":
            print("\nYou picked a beautiful flower，feeling very happy！")
            play_again()
        elif choice == "2":
            print("\nYou rest in the garden，enjoy the quiet time.")
            play_again()
        else:
            print("Invalid selection, please select again.")
            right_path()
    else:
        print("无Invalid selection, please select again.")
        right_path()

def play_again():
    choice = input("\nDo you want to play again？（Input yes or no）: ")
    if choice.lower() == "yes":
        start_game()
    elif choice.lower() == "no":
        print("Thanks for playing this game! Bye!")
    else:
        print("Invalid selection, please select again.")
        play_again()

# 启动游戏
start_game()