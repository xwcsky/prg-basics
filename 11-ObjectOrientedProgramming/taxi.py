class TaxiRide:
    def __init__(self, rate_per_km, distance):
        self.rate_per_km = rate_per_km 
        self.fare = 0
        self.distance = distance

    def calculate_fare(self):
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print("Taxi Ride Receipt:")
        print(f"Distance: {self.distance} km")
        print(f"Rate: €{self.rate_per_km} per km")
        print(f"Total Fare: €{self.fare:.2f}")
        print("-" * 30)


def main():
    ride1 = TaxiRide(2.5,15)  # €2.5 per km
    ride2 = TaxiRide(3.0,25)  # €3.0 per km


    ride1.calculate_fare()
    ride2.calculate_fare()
    ride1.print_receipt()
    ride2.print_receipt()


if __name__ == "__main__":
    main()
