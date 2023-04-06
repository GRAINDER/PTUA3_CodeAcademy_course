class Flat:                    
    def __init__(self, country: str, city: str, district: str, price: int):                                                          
        self.country = country                                              
        self.city = city
        self.district = district
        self.price = price

    def get_flat_country(self):
        print(f"my vacation country is {self.country}")
    def get_rent_city(self):
        return self.city
    def get_district_of_city(self):
        print(f"i will live in {self.district}")
    def get_rent_price(self):
        print(f"my rent costs {self.price}")

AirBnB = Flat(country="Lithuania", city="Kaunas", district="Žaliakalnis", price=50)
# print(AirBnB.country,AirBnB.city,AirBnB.district,AirBnB.price)


class Rooms(Flat):                                 
        def __init__(self, area: float , floor: int, interior: str):                 
            super().__init__(country="Lithuania", city="Kaunas", district="Žaliakalnis", price=50)
            self.area = area
            self.floor = floor
            self.interior = interior
            
            print(self.country,self.city,self.district,self.price)

betkas = Rooms(area=1000, floor=1, interior="2")

print(betkas.country,betkas.city,betkas.district,betkas.price)


        




# my_rent_flat = Rooms(area=65, floor=2, interior="luxury")
# print(my_rent_flat.area,my_rent_flat.floor,my_rent_flat.interior)










# class Designers(Employee):                                           

#         def __init__(self,name,age,exp,salary,position):               
#             super().__init__(name,age,exp,salary)                    
#             self.position = position                                 
        
#         def show(self):                                              
#             super().show()                                          
#             print(self.position)        