class Camera:
    def take_photo(self):
        print("Taking a photo")
class Phone:
    def make_call(self):
        print("Making a call")
class Smartphone(Camera,Phone):
    def use_internet(self):
        print("Using the internet")

phone=Smartphone()
phone.take_photo()
phone.make_call()
phone.use_internet()