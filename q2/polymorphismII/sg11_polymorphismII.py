class Car:
  def move(self):
    print("The car drives on the road.")

class Boat:
  def move(self):
    print("The boat sails on the water.")

class Drone:
  def move(self):
    print("The drone flies in the sky.")

def start_trip(vehicles):
  vehicles.move()

a = [Car(),Boat(),Drone()]
for vehicle in a:
  start_trip(vehicle)
