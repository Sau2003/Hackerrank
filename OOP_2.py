class Fractions:
    numerator=None
    denominator=None

    def __init__(self,x,y):
        self.numerator=x
        self.denominator=y

    def __str__(self):
        return "[0]/[1]".format(self.numerator,self.denominator)
