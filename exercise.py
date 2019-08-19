class Trip:
    all_locations = []  # Stores all Locations for Trip.

    def __init__(self):
        pass

    def add(self, location):  # Add a Location to the Trip.
        Trip.all_locations.append(location)
        return f'Adding {location} to the trip.'

    @classmethod
    def list_all(self):  # Display all Locations.
        if self.all_locations.__len__() > 1:

            print('Began trip.')
            for idx, item in enumerate(self.all_locations):  # Iterates through each location in Trips.
                if (idx+1 != self.all_locations.__len__()):  # The last item won't run.
                    print(f'Travelled from {self.all_locations[idx]} to {self.all_locations[idx+1]}.')
                else:
                    print(f'Travelled back from from {self.all_locations[idx]} to {self.all_locations[0]}.')
        else:
            print('You didn\'t go anywhere.')
                

class Location:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


vacation_2020 = Trip()

toronto = Location('Toronto')
cayo_coco = Location('Cayo Coco')
puerto_vallarta = Location('Puerto Vallarta')
los_angeles = Location('Los Angeles')
paris = Location('Paris')
ireland = Location('Ireland')

print(vacation_2020.add(toronto))
print(vacation_2020.add(cayo_coco))
print(vacation_2020.add(puerto_vallarta))
print(vacation_2020.add(los_angeles))
print(vacation_2020.add(paris))
print(vacation_2020.add(ireland))
print()

vacation_2020.list_all()