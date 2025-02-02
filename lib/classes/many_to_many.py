import re

class NationalPark:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) == str and len(name) >= 3 and not hasattr(self, 'name'):
            self._name = name
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        return list(set([trip.visitor for trip in Trip.all if trip.national_park == self]))
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        visitor_trips = {}
        for trip in self.trips():
            if trip.visitor not in visitor_trips:
                visitor_trips[trip.visitor] = 1
            else:
                visitor_trips[trip.visitor] +=1
        if not visitor_trips:
            return None
        return max(visitor_trips, key=visitor_trips.get)


class Trip:
    
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        date_pattern = r'^[A-Z][a-z]+ \d{1,2}(st|nd|rd|th)$' #this part was hard to find
        if type(start_date) == str and len(start_date) >= 7 and re.match(date_pattern, start_date):
            self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        date_pattern = r'^[A-Z][a-z]+ \d{1,2}(st|nd|rd|th)$' #this part was hard to find
        if type(end_date) == str and len(end_date) >= 7 and re.match(date_pattern, end_date):
            self._end_date = end_date

    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor

    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        

class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) == str and 1 <= len(name) <= 15:
            self._name = name
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        return list(set([trip.national_park for trip in Trip.all if trip.visitor == self]))
    
    def total_visits_at_park(self, park):
        return len([trip for trip in self.trips() if trip.park == park])