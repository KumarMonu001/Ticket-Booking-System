
ticket_list = []
for i in range(1, 51):
    ticket_list.append(i)

while True:
    # main menu to show option board
    print("Main Menu".center(35))
    print("""\t1. Book Ticket
    2. Show available seats
    3. Cancel ticket
    4. Exit""")

    choice = int(input('Choose operation from the above list : '))

    # for booking ticket
    if choice == 1:
        ticket_number = int(input('Enter ticket number to book : '))
        if 50 < ticket_number < 1:
            print('Invalid ticket number')
        elif ticket_list.count(ticket_number) == 1:
            print('Your ticket has been Booked!')
            ticket_list[ticket_list.index(ticket_number)] = 'Bb'
        else:
            print('Sorry! The ticket has been already booked!')
    # for showing available seat
    elif choice == 2:
        print('===================== Available seats list ===================')
        # showing all the tickets table
        for tic in ticket_list:
            if tic == 'Bb':
                if ((ticket_list.index(tic))+1) % 10 == 0:
                    print('Bb'.center(5))
                else:
                    print('Bb'.center(5), end=' ')
            elif tic < 10:
                print(f'0{tic}'.center(5), end=' ')
            elif tic % 10 == 0:
                print(f'{tic}'.center(5))
            else:
                print(f'{tic}'.center(5), end = ' ')
        print('\n==========================================================')
    # for cancel ticket
    elif choice == 3:
        cancel_number = int(input('Enter ticket number to cancel : '))
        if 50 < cancel_number < 1:
            print('Enter a valid ticket number')
        elif ticket_list.count(cancel_number) == 1:
            print('Ticket has been successfully canceled')
            ticket_list[cancel_number - 1] = cancel_number
        else:
            print("Ticket not found in bookings; cancellation can't not be done")
    elif choice == 4:
        break
    else:
        print('Enter a valid choice')
