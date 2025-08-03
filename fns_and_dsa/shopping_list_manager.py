# Function to display the main menu options
def display_menu():
    print(f"Shopping List Manager")
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# Main logic function
def main():
    # Start with an empty shopping list
    shopping_list = []

    # Keep showing the menu until the user decides to exit
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        # Option 1: Add an item to the shopping list
        if choice == '1':
            item = input("Enter item to add: ").strip()

            # Check for empty input
            if not item:
                print("Item name cannot be empty.")
                continue

            # Check if the item already exists (case-insensitive)
            if item.lower() in [x.lower() for x in shopping_list]:
                print(f"'{item}' is already in the list.")
            else:
                shopping_list.append(item)
                print(f"'{item}' added to the shopping list.")

        # Option 2: Remove an item from the shopping list
        elif choice == '2':
            item = input("Enter item to remove: ").strip()

            # Check for empty input
            if not item:
                print("Item name cannot be empty.")
                continue

            # Try to match the item case-insensitively
            matched_items = [x for x in shopping_list if x.lower() == item.lower()]
            if matched_items:
                shopping_list.remove(matched_items[0])  # Remove the actual item
                print(f"'{matched_items[0]}' removed from the list.")
            else:
                print("Item not found in list.")

        # Option 3: View all items in the shopping list
        elif choice == '3':
            if not shopping_list:
                print("Shopping list is empty.")
            else:
                print("\nYour Shopping List:")
                # Display numbered list of items
                for idx, item in enumerate(shopping_list, 1):
                    print(f"{idx}. {item}")

        # Option 4: Exit the program with confirmation
        elif choice == '4':
            confirm = input("Are you sure to Exit? (Y/N): ").strip().lower()
            if confirm == 'y':
                print("Goodbye!")
                break  # Exit the loop and program
            else:
                print("Returning to menu...")

        # Handle any invalid menu option
        else:
            print("Invalid choice. Please try again.")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()

