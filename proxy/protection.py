class Car:

    def __init__(self, driver):
        self.driver = driver

    def drive(self):
        print(f'The car is being driven by {self.driver.name}.')


class CarProxy:

    def __init__(self, driver):
        self.driver = driver
        self._car = Car(driver)

    def drive(self):
        if self.driver.age >= 18:
            self._car.drive()
        else:
            print(f'The driver {self.driver.name} is underage.')


class Driver:

    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == "__main__":
    zilong = Driver('Zilong', 28)
    julia = Driver('Julia', 16)
    car = Car(driver=zilong)
    car_proxy = CarProxy(driver=julia)
    car.drive()
    car_proxy.drive()
