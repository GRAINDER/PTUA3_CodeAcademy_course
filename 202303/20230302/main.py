#Create a Plane, Boeing, Airbus classes.
#Base class should contain methods to get:  plane name, plane type (A320, B737 etc), max_speed (should be the funciotn: base_speed * model_speed_coeficient).
#Both plane subclasses should only take model as input argument.

class Plane:
    BASE_SPEED = 750

    def __init__(self, model_type: str, model_speed_coeficient: float, name_suffix:  str):

        self.model_type = model_type 
        self.model_speed_coeficient = model_speed_coeficient
        self.name_suffix = name_suffix
        

    def get_plane_name(self) -> str:
        return self.name_suffix 

        
    def get_plane_type(self) -> str:
        return self.model_type
        
        
    def get_max_speed(self):
        return self.model_speed_coeficient * self.BASE_SPEED
        


class Boeing(Plane):
    NAME_SUFIX = "B"
    BOEING_TYPE_SPEED_COEF = {
        "737": 1,
        "747": 1.2,
        "757": 1.35,
        "767": 1.5,
        "777": 1.8,

    }
    def __init__(self, model_type: str):
        self.model_speed = model_type
        speed_coeficient = _get_type_speed_coeficient(self.model_type)
        
        
        super().__init__(model_type=model_type, name_suffix=self.NAME_SUFIX, model_speed_coeficient= speed_coeficient)

    def _get_type_speed_coeficient(self) -> float:
        return self.BOEING_TYPE_SPEED_COEF.get(self.model_type)
    

my_plane = Boeing("737")
print(my_plane.get_plane_name())




# class Airbus(Plane):
#     NAME_SUFIX = "A"
#     def __init__(self, model_type: str):
#         super().__init__(model_type)


