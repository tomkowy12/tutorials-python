import datetime as dt
from typing import List
 
class TripException(Exception):
    def __init__(self, text: str, description: str) -> None:
        super().__init__(text)
        self.description = description

    def __str__(self) -> str:
        return "{}, info: {}".format(super().__str__(), self.description)
    
class TripNameException(TripException):
    EXCEPTION_DESCRIPTION = "Name of the trip is missing. You need to name the trip somehow..."

    def __init__(self, text: str) -> None:
        super().__init__(text, self.EXCEPTION_DESCRIPTION)

class TripDateException(TripException):
    EXCEPTION_DESCRIPTION = "The dates are incorrect. The starting date should be earlier than the ending date..."

    def __init__(self, text: str) -> None:
        super().__init__(text, self.EXCEPTION_DESCRIPTION)


class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end
 
    def check_data(self):
        if len(self.title) == 0:
            raise TripNameException("Name error")
        if self.start > self.end:
            raise TripDateException("Date error")
    
    @classmethod
    def publish_offer(cls, trips):
        list_of_errors = []
        for trip in trips:
            try:
                trip.check_data()
            except (TripNameException, TripDateException) as e:
                list_of_errors.append("{}: {}".format(trip.symbol, str(e)))
        if list_of_errors:
            raise TripException("The list of trips has below errors: \n{}", list_of_errors)
        else:
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