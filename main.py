# by Popov Roman
class Animals:
    type = "rodents"
    planet = "earth"
    size = "small"

    def __init__(self, name, max_age, environment):
        self.name = name
        self.max_age = max_age
        self.environment = environment


animal1 = Animals(name="Rat", max_age="2 years", environment="steppe")
animal2 = Animals(name="Hamster", max_age="3 years", environment="semi-desert")
animal3 = Animals(name="Mouse", max_age="18 months", environment="almost everywhere")

print(f"Info animal1 Type {Animals.type}, Planet {Animals.planet}, Size {Animals.size}, Name {animal1.name}, Max age {animal1.max_age}, Environment {animal1.environment}")
print(f"Info animal2 Type {Animals.type}, Planet {Animals.planet}, Size {Animals.size}, Name {animal2.name}, Max age {animal2.max_age}, Environment {animal2.environment}")
print(f"Info animal3 Type {Animals.type}, Planet {Animals.planet}, Size {Animals.size}, Name {animal3.name}, Max age {animal3.max_age}, Environment {animal3.environment}")

print(" ")
print(" ")


class Devices:
    type = "smartphone"
    os = "android"
    cpu_brand = "snapdragon"

    def __init__(self, name, brand, snapdragon_model):
        self.name = name
        self.brand = brand
        self.snapdragon_model = snapdragon_model


smartphone1 = Devices(name="Samsung galaxy S24 Ultra", brand="Samsung", snapdragon_model="8 Gen 3")
smartphone2 = Devices(name="Poco F5 Pro", brand="Poco", snapdragon_model="8 Gen 2")
smartphone3 = Devices(name="Xiaomi Redmi Note 12", brand="Xiaomi", snapdragon_model="685")

print(f"Info smartphone1 Type {Devices.type}, Os {Devices.os}, Cpu Brand {Devices.cpu_brand}, Name {smartphone1.name}, Brand {smartphone1.brand}, Snapdragon model {smartphone1.snapdragon_model}")
print(f"Info smartphone2 Type {Devices.type}, Os {Devices.os}, Cpu Brand {Devices.cpu_brand}, Name {smartphone2.name}, Brand {smartphone2.brand}, Snapdragon model {smartphone2.snapdragon_model}")
print(f"Info smartphone3 Type {Devices.type}, Os {Devices.os}, Cpu Brand {Devices.cpu_brand}, Name {smartphone3.name}, Brand {smartphone3.brand}, Snapdragon model {smartphone3.snapdragon_model}")
# by Popov Roman