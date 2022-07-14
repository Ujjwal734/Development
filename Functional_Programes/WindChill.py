import math
def temperature(temp, windspeed):
   """temperature t (in Fahrenheit) and wind Speed v(in miles per hour)""" #Docstring
   if temp < 50 and 3 < windspeed < 120:
       windchill = 35.75 + 0.6215 + (0.4275 * temp - 35.75) * math.pow(windspeed,2)
       return "windchill" + str(windchill)S
   else:
       print("cannot comply with temperature or windspeed values")
       return 0

if __name__ == '__main__':
    t = int(input("Enter temperature value :- "))
    w = int(input("Enter windspeed value :- "))
    print(temperature(t,w))