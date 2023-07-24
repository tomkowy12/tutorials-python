import datetime as dt
from typing import List
 
class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end
 
    def check_data(self):
        assert len(self.title) == 0, "Title is empty!"
        assert self.start <= self.end, "Start date is later than end date!"
    
    @classmethod
    def publish_offer(cls, trips):
        list_of_errors = []
        for trip in trips:
            try:
                trip.check_data()
            except ValueError as e:
                list_of_errors.append("{}: {}".format(trip.symbol, str(e)))
            except Exception as e:
                list_of_errors.append("{}: {}".format(trip.symbol, str(e)))
        assert list_of_errors, "The list of trips has below errors: \n{}".format(list_of_errors)
        print("The offer will be published...")
 
trips = [
            Trip('IT-VNC', '', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
            Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
            Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
        ]

try:
    print("Trips checking started...")
    Trip.publish_offer(trips)
    print("Done.")
except Exception as e:
    print("Something went wrong. Details: \n{}".format(e))