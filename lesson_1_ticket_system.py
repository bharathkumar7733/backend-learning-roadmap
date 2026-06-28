tickets = []

while True:
    
    print("\n1 Create Ticket")
    print("2 View Tickets")
    print("3 Exit")
    print("4 Close Ticket status")

    choice = input("Choose: ")

    if choice == "1":

        title = input("Enter title: ")

        ticket = {
            "id": len(tickets)+1,
            "title": title,
            "status": "open"
        }

        tickets.append(ticket)

        print("Ticket Created")

    elif choice == "2":

        for t in tickets:
            print(t)

    elif choice == "3":

        break
    elif choice == "4":
        ticket_id = int(input("Enter ticket id: "))

        for t in tickets:
            if t["id"] == ticket_id:
                t["status"] = "closed"
                print(f"Ticket status closed {ticket_id}")
                break
                