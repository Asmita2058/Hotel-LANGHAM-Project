from rooms import add_room, delete_room, display_room_details, display_all_rooms
from allocations import allocate_room, display_allocation_details, bill_and_deallocate

def main():
    while True:
        print("\nLANGHAM Hotel Management System")
        print("1. Add Room")
        print("2. Delete Room")
        print("3. Display Room Details")
        print("4. Allocate Room")
        print("5. Display Room Allocation Details")
        print("6. Billing & De-Allocation")
        print("0. Exit Application")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_room()
        elif choice == '2':
            delete_room()
        elif choice == '3':
            display_all_rooms()
        elif choice == '4':
            allocate_room()
        elif choice == '5':
            display_allocation_details()
        elif choice == '6':
            bill_and_deallocate()
        elif choice == '0':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
