import math 
def distance(x_coordinate, y_coordinate):
    dis = math.sqrt(math.pow(x_coordinate,2) + math.pow(y_coordinate,2))
    return dis

if __name__ == '__main__':
    x = int(input("Enter X coordiante :- "))
    y = int(input("Enter Y coordiante :- "))
    print(distance(x,y))