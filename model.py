import datetime

class BookingData:    
    def __init__(self):
        self.one_way = True
        self.start_date = None
        self.return_date = None

    def reset(self):
        self.start_date = None
        self.return_date = None
        
    def is_valid(self):
        if self.one_way:
            error = self.start_date is None
        else:
            error = self.start_date is None or self.return_date is None or self.return_date < self.start_date
        return not error

    

class BookingClient:
    def book(self, data):
        if data.is_valid():
            import random
            if random.choice([True, False]):
                pass
            else:
                raise IOError("Couldn't book flight")
        else:
            raise ValueError("Invalid dates")
