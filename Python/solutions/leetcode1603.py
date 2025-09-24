# 1603. Design Parking System

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.free_spot  = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.free_spot[carType - 1] > 0:
            self.free_spot[carType - 1] -= 1
            return True
        return False

if __name__ == "__main__":
    parking = ParkingSystem(1, 1, 0)
    print(parking.addCar(1)) # True
    print(parking.addCar(2)) # True
    print(parking.addCar(3)) # False
    print(parking.addCar(1)) # False