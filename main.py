from src.menu import show_menu, handle_choice
   
if __name__ == "__main__":
    while True:
        show_menu()
        choice = int(input("Enter choice:"))
        if choice == 7:
            break
        elif choice not in [1,2,3,4,5,6]:
            print("Option not recongnised. Please try again!")
        else:
            handle_choice(choice)
    print("Goodbye")