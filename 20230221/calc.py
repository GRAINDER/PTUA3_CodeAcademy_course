
def add(x: int,y: int) -> int:
     return x + y
 
def sub(x: int,y: int) -> int:
     return x - y
 
def prod(x: int,y: int) -> int:
    return x * y
 
def div(x: int,y: int) -> float:
    return x / y

#if __name__ == "__main__": si eilute rasome tam, kad suprasti, ar pagrindiame kodo lange, leidziam importuoto modulio funckija.


print(f'The __name__ from script1 is "{__name__}"')
if __name__ == "__main__":

     print(f"Name is: {__name__}")
     
