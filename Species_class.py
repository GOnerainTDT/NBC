class Species:
    def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
        # self.num = num #int
        self.sepal_length = sepal_length #float
        self.sepal_width = sepal_width #float
        self.petal_length = petal_length #float
        self.petal_width = petal_width #float
        self.species = species #str

    def get(self, i):
        if i == 0:
            return float(self.sepal_length)
        elif i == 1:
            return float(self.sepal_width)
        elif i == 2:
            return float(self.petal_length)
        elif i == 3:
            return float(self.petal_width)
        

    def __str__(self):
        print(self.sepal_length, self.sepal_width, self.petal_length, self.petal_width, self.species)
        return str(self.sepal_length) + " " + str(self.sepal_width) + " " + str(self.petal_length) + " " + str(self.petal_width) + " " + str(self.species)
    


    