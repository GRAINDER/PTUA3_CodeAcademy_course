class Reservation:
    def __init__(self, name, date, time, seats):
        self.name = name
        self.date = date
        self.time = time
        self.seats = seats

    def update_reservation(self, name, date, time, seats):
        self.name = name
        self.date = date
        self.time = time
        self.seats = seats

    def cancel_reservation(self):
        self.name = None
        self.date = None
        self.time = None
        self.seats = None

class ReservationTable:
    def __init__(self, num_seats, num_slots):
        self.num_seats = num_seats
        self.num_slots = num_slots
        self.table = [[None for i in range(num_seats)] for j in range(num_slots)]

    def make_reservation(self, name, date, time, seats):
        for i in range(self.num_slots):
            for j in range(self.num_seats - seats + 1):
                if not any(self.table[i][j:j+seats]):
                    reservation = Reservation(name, date, time, seats)
                    for k in range(seats):
                        self.table[i][j+k] = reservation
                    return reservation
        return None

    def cancel_reservation(self, reservation):
        for i in range(self.num_slots):
            for j in range(self.num_seats):
                if self.table[i][j] == reservation:
                    self.table[i][j] = None
                    reservation.cancel_reservation()
                    return True
        return False

    def print_table(self):
        print('Reservations:')
        print('Time\t' + '\t'.join(str(i) for i in range(self.num_seats)))
        for i in range(self.num_slots):
            print(str(i) + '\t' + '\t'.join(str(self.table[i][j].name) if self.table[i][j] else '-' for j in range(self.num_seats)))
