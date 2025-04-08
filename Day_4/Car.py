class Car:
    def __init__(self , make, model, speed):
        self.make = make
        self.model = model
        self.speed = speed

    @property
    def make(self):
        return self._make
    
    @make.setter
    def make(self, value):
        self._make = value

    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, value):
        if value <= 0:
            raise ValueError('Speed cannot be 0 or negative')
        else:
            self._speed = value

    

    def __str__(self):
        return f'Make : {self.make}, Model : {self.model}, Speed: {self.speed}'
    
    def __repr__(self):
        return f'Car.Car({self.make}, {self.model}, {self.speed})'
    
    @staticmethod
    def display_count():
        print('Total Cars :', {Car.count})
    
