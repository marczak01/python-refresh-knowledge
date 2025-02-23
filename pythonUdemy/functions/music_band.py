def book_tickets(band, no_ticket, / , * , ticket_type, section):
    return f"{band} - number of tickets: {no_ticket} ({ticket_type}) \n\ton section: {section}"


band = input("Podaj nazwe zespołu: ")
no_ticket = int(input("Podaj ilosc biletow: "))
ticket_type = input("Podaj rodzaj biletow: ")
section = input("Podaj wybrana sekcje: ")

print(book_tickets(band, no_ticket, section=section, ticket_type=ticket_type ))