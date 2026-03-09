from models import Vehicle, Car, Motorcycle

def main():
    # Create objects
    v1 = Vehicle("Generic", "Transporter", 2020)
    c1 = Car("Toyota", "Camry", 2022, 4)
    m1 = Motorcycle("Yamaha", "MT-07", 2021, "Sport")

    # Store them in a list
    vehicles = [v1, c1, m1]

    # Iterate and demonstrate polymorphism
    for v in vehicles:
        print(v)               # __str__ method
        print(v.start())       # Polymorphic method
        print(v.stop())        # Base class method

        # Call unique methods if they exist
        if isinstance(v, Car):
            print(v.honk())
        elif isinstance(v, Motorcycle):
            print(v.wheelie())

        print("-" * 40)


if __name__ == "__main__":
    main()