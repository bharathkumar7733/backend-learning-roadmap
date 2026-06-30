tickets = []


def create_ticket():
    title = input("Enter the title: ")

    ticket = {
        "id": len(tickets) + 1,
        "title": title,
        "status": "open"
    }

    tickets.append(ticket)
    print("Ticket Created")


def view_tickets():
    if len(tickets) == 0:
        print("No tickets found")
        return

    for t in tickets:
        print(t)


def close_ticket(ticket_id):
    for t in tickets:
        if t["id"] == ticket_id:
            t["status"] = "closed"
            print(f"Ticket status closed for ID {ticket_id}")
            return

    print("Ticket not found")


def exit_system():
    print("Exiting the ticket system.")


while True:
    print("\n1 Create Ticket")
    print("2 View Tickets")
    print("3 Exit")
    print("4 Close Ticket status")

    choice = input("Choose: ")

    if choice == "1":
        create_ticket()

    elif choice == "2":
        view_tickets()

    elif choice == "3":
        exit_system()
        break

    elif choice == "4":
        ticket_id = int(input("Enter ticket ID to close: "))
        close_ticket(ticket_id)

    else:
        print("Invalid choice")
