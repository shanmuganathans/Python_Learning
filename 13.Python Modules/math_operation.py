class MathOperation:
    """
    Class it contains the basic operation for math operations
    """
    def __init__(self,number1,number2):
        """
        Initiliaze the value
        """
        self.num1 = number1
        self.num2 = number2
        
    def add(self):
        """
        Retrun the added value
        """
        return(self.num1 + self.num2)
    def sub(self):
        """
        Return the subtraced value
        """
        return(self.num1 - self.num2)
    def mul(self):
        """
        Return the multiplication value
        """
        return (self.num1 * self.num2)
    
    def div(self):
        """
        Return the divided value
        """
        return (self.num1 / self.num2)

    @staticmethod
    def new_add(a,b):
        return (a+b)
        
    
obj = MathOperation(10,2)
obj.add()