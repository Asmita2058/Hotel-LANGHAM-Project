from rooms import rooms

allocations = []

def allocate_room():
    room_number = input("Enter room number to allocate: ")
    customer_name = input("Enter customer name: ")

    for room in rooms:
        if room['number'] == room_number:
            if room['allocated']:
                print(f"Room {room_number} is already allocated.")
                return

            room['allocated'] = True
            allocation = {
                'room_number': room_number,
                'customer_name': customer_name
            }
            allocations.append(allocation)
            print(f"Room {room_number} allocated to {customer_name}.")
            return
    print(f"No room found with number {room_number}.")

def display_allocation_details():
    if not allocations:
        print("No allocations available.")
    for allocation in allocations:
        print(f"Room Number: {allocation['room_number']}, Customer Name: {allocation['customer_name']}")

def bill_and_deallocate():
    room_number = input("Enter room number to deallocate: ")

    global allocations
    allocations = [alloc for alloc in allocations if alloc['room_number'] != room_number]

    for room in rooms:
        if room['number'] == room_number:
            room['allocated'] = False
            print(f"Room {room_number} is now deallocated and ready for next booking.")
            return
    print(f"No room found with number {room_number}.")
