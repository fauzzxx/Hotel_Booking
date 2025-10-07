import pandas as pd

reader = pd.read_csv('hotel.csv')

reader['is_booked'] = reader['is_booked'].astype(str).str.lower().map({'true': True, 'false': False})

def show_available_rooms():
    available = reader[reader['is_booked'] == False]
    if available.empty:
        print("No rooms available at the moment.")
    else:
        print("\nAvailable Rooms:")
        print(available[['id', 'type']].to_string(index=False))
    return available

def book_room(room_type):
    available_rooms = show_available_rooms()
    rooms_of_type = available_rooms[available_rooms['type'].str.lower() == room_type.lower()]
    if rooms_of_type.empty:
        print(f"\nNo available '{room_type}' rooms at the moment.")
    else:
        room_index = rooms_of_type.index[0]
        reader.at[room_index, 'is_booked'] = True
        room_id = reader.at[room_index, 'id']
        reader.to_csv('hotel.csv', index=False)
        print(f"\nRoom ID {room_id} of type '{room_type}' has been booked successfully!")

while True:
    print("\n--- Hotel Booking System ---")
    print("1. Show available rooms")
    print("2. Book a room")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        show_available_rooms()
    elif choice == '2':
        room_type_input = input("Enter room type to book (Single/Double/Deluxe): ")
        book_room(room_type_input)
    elif choice == '3':
        print("Thank you for using the Hotel Booking System!")
        break
    else:
        print("Invalid choice. Please try again.")