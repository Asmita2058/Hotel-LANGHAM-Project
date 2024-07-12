rooms = []

def add_room():
    room_number = input("Enter room number: ")
    room_type = input("Enter room type (Single/Double/Suite): ")
    room_price = input("Enter room price: ")

    room = {
        'number': room_number,
        'type': room_type,
        'price': room_price,
        'allocated': False
    }

    rooms.append(room)
    print(f"Room {room_number} added successfully.")

def delete_room():
    room_number = input("Enter room number to delete: ")

    global rooms
    rooms = [room for room in rooms if room['number'] != room_number]
    print(f"Room {room_number} deleted successfully.")

def display_room_details(room_number):
    for room in rooms:
        if room['number'] == room_number:
            print(f"Room Number: {room['number']}")
            print(f"Room Type: {room['type']}")
            print(f"Room Price: {room['price']}")
            return
    print(f"No room found with number {room_number}.")

def display_all_rooms():
    if not rooms:
        print("No rooms available.")
    for room in rooms:
        display_room_details(room['number'])
