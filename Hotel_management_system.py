import os

GUESTS_FILE = 'guests.txt'
ROOMS_FILE = 'rooms.txt'

# Helper Functions
def load_data(file):
    if not os.path.exists(file):
        return []
    with open(file, 'r') as f:
        return [line.strip().split('|') for line in f.readlines()]

def save_data(file, data):
    with open(file, 'w') as f:
        for record in data:
            f.write('|'.join(record) + '\n')

# Guest Management 
def add_guest():
    guest_id = input("Enter Guest ID: ")
    name = input("Enter Guest Name: ")
    phone = input("Enter Phone Number: ")
    address = input("Enter Address: ")

    guests = load_data(GUESTS_FILE)
    for guest in guests:
        if guest[0] == guest_id:
            print("❌ Guest ID already exists.")
            return

    guests.append([guest_id, name, phone, address])
    save_data(GUESTS_FILE, guests)
    print("✅ Guest Added Successfully.")

def search_guest():
    guest_id = input("Enter Guest ID to Search: ")
    guests = load_data(GUESTS_FILE)
    for guest in guests:
        if guest[0] == guest_id:
            print(f"Guest Found: ID: {guest[0]}, Name: {guest[1]}, Phone: {guest[2]}, Address: {guest[3]}")
            return
    print("❌ Guest Not Found.")

def update_guest():
    guest_id = input("Enter Guest ID to Update: ")
    guests = load_data(GUESTS_FILE)
    for guest in guests:
        if guest[0] == guest_id:
            print("Leave blank to keep existing info.")
            name = input(f"Enter New Name ({guest[1]}): ") or guest[1]
            phone = input(f"Enter New Phone ({guest[2]}): ") or guest[2]
            address = input(f"Enter New Address ({guest[3]}): ") or guest[3]
            guest[1], guest[2], guest[3] = name, phone, address
            save_data(GUESTS_FILE, guests)
            print("✅ Guest Updated Successfully.")
            return
    print("❌ Guest Not Found.")

def delete_guest():
    guest_id = input("Enter Guest ID to Delete: ")
    guests = load_data(GUESTS_FILE)
    updated_guests = [guest for guest in guests if guest[0] != guest_id]
    if len(guests) == len(updated_guests):
        print("❌ Guest Not Found.")
    else:
        save_data(GUESTS_FILE, updated_guests)
        print("✅ Guest Deleted Successfully.")

# Room Management 
def book_room():
    room_no = input("Enter Room Number to Book: ")
    guest_id = input("Enter Guest ID for Booking: ")

    rooms = load_data(ROOMS_FILE)
    for room in rooms:
        if room[0] == room_no:
            print("❌ Room already booked.")
            return

    guests = load_data(GUESTS_FILE)
    if not any(guest[0] == guest_id for guest in guests):
        print("❌ Guest ID not found. Add Guest first.")
        return

    rooms.append([room_no, guest_id])
    save_data(ROOMS_FILE, rooms)
    print("✅ Room Booked Successfully.")

def cancel_booking():
    room_no = input("Enter Room Number to Cancel Booking: ")
    rooms = load_data(ROOMS_FILE)
    updated_rooms = [room for room in rooms if room[0] != room_no]
    if len(rooms) == len(updated_rooms):
        print("❌ Booking not found.")
    else:
        save_data(ROOMS_FILE, updated_rooms)
        print("✅ Booking Cancelled Successfully.")

def check_availability():
    total_rooms = [str(i) for i in range(101, 111)]  # Example Rooms 101-110
    booked_rooms = [room[0] for room in load_data(ROOMS_FILE)]

    print("\nRoom Availability:")
    for room in total_rooms:
        status = "Booked" if room in booked_rooms else "Available"
        print(f"Room {room}: {status}")

# Main Menu
def main_menu():
    while True:
        print("\n--- Hotel Management System ---")
        print("1. Add Guest Record")
        print("2. Search Guest Record")
        print("3. Update Guest Record")
        print("4. Delete Guest Record")
        print("5. Book Room")
        print("6. Cancel Booking")
        print("7. Check Room Availability")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            add_guest()
        elif choice == '2':
            search_guest()
        elif choice == '3':
            update_guest()
        elif choice == '4':
            delete_guest()
        elif choice == '5':
            book_room()
        elif choice == '6':
            cancel_booking()
        elif choice == '7':
            check_availability()
        elif choice == '8':
            print("Exiting Hotel Management System. Goodbye!")
            break
        else:
            print("Invalid Choice. Try Again.")

if __name__ == "__main__":
    main_menu()
