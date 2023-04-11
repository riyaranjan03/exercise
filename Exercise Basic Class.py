class MedPlus:
    def __init__(self, name: str, batch_no: int, price: float):
        self.name = name
        self.batch_no = batch_no
        self.price = price
        try:
            if type(name) != str:
                raise TypeError("Name should be a string value")
            if type(batch_no) != int:
                raise TypeError("Batch number should be an integer value")
            if type(price) != float:
                raise TypeError("Price should be a float value")
        except TypeError as e:
            print(f"Error: {e}")
            return

    def get_name(self):
        return self.name
    
    def get_batch_no(self):
        return self.batch_no
    
    def get_price(self):
        return self.price
      
a = MedPlus("Riya",7,300)

print(a.get_name())
print(a.get_batch_no())
print(a.get_price())
