
def show_menu():
    """Displays the genre selection menu to the user."""
    print("\n=== NETFLIX ===")
    print("\nSelect a genre:\n")
    print("1. Technology")
    print("2. Action")
    print("3. Science Fiction")


def get_genre():
    """Prompts the user for an option and returns it."""
    # We use a loop to ensure the user inputs a valid number from the menu
    while True:
        try:
            option = int(input("\nOption: "))
            if option in [1, 2, 3]:
                return option
            else:
                print("Invalid option. Please choose 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number.")


def recommend_content(genre):
    """Receives the genre number and prints the corresponding recommendations."""
    print("\nRecommendations:\n")
    
    if genre == 1:
        print("- Silicon Valley")
        print("- The Social Network")
    elif genre == 2:
        print("- Deadly Code")
        print("- Operation Delta")
    elif genre == 3:
        print("- Interstellar")
        print("- Blade Runner 2049")


def main():
    """Main program loop to control the execution flow."""
    keep_searching = True
    
    while keep_searching:
        show_menu()
        user_choice = get_genre()
        recommend_content(user_choice)
        
        # Ask the user if they want to continue
        repeat = input("\nWould you like to perform another search? (Y/N): ").strip().upper()
        
        if repeat != 'Y':
            keep_searching = False
            print("\nThank you for using Netflix Recommendation System. Goodbye!")

# This ensures the program runs when executing the script
if __name__ == "__main__":
    main()