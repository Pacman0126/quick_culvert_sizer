import numpy as np
#from matplotlib import pyplot as plt
import math


def get_catchment_area_properties():

    global catchment_area

    while True:
      
      try:

        
        str_catchment_area = input("Input size of catchment in acres. Maximum area is 200 acres: ")
        catchment_area = float(str_catchment_area)

        if(catchment_area <= 0 or catchment_area > 200):
           print("Invalid input, size must be acres a whole number\n or decimal greater than zero and not more than 200 acres")
           continue
           
      except ValueError:
         
         print("Invalid input, size must be acres a whole number or decimal.")

         continue
      
      else:
         break
      
      finally:
         catchment_area = float(round(catchment_area,1))

    global Tc_Area
    Tc_Area = {}
    Tc = 0
    e = 0.8052
    b = 68.99
    d = 9.76

    Tc_Area = {Tc: round(b / math.pow((Tc + d),e),2)  for Tc in range(10,110,10)}
    print(' ')
    get_runoff_coefficient()

    #print(Tc_Area)

    return

def get_runoff_coefficient():
   
    """
    This function builds a runoff coefficient for rural watersheds based on
    a methodology from Texas Department of Transportation's Hydraulic Design Manual
    and stores in a global variable since it is a critical value that needs to be
    available throughout the application.
    """
    global runoff_coefficient
    
    """
    Watershed relief characteristics.
    """
    #Cr
    Cr = 0.0

    print("[1] - Extreme: Steep, rugged terrain with average slopes above 30%")
    print("[2] - High: Hilly, with average slopes of 10-30%")
    print("[3] - Normal: Rolling, with average slopes of 5-10%")
    print("[4] - Low: Relatively flat land, with average slopes of 0-5%\n")
  
    while True:

        try:
            str_Cr = input("What are the watershed relief characteristics of this catchment area. Select from above: ")
            if(int(str_Cr) < 1 or int(str_Cr) > 4):
               print("Not a valid selection. Selection not available.")
               continue


        except:
            print("Invalid input. Must be a number from 1, 2, 3, 4")
            continue
        
        else:
           print(' ')
           break
       
            
    match str_Cr:
       case '1':
        Cr = 0.315

       case '2':
         Cr = 0.24

       case '3':
          Cr = 0.17

       case '4':
          Cr = 0.11

  
    
    """
    Watershed soil infiltration characteristics.
    """
    #Ci
    Ci = 0.0

    print("[1] - Extreme: No effective soil cover; either rock or thin soil mantle of negligible infiltration capacity")
    print("[2] - High: Slow to take up water, clay or shallow loam soils of low infiltration capacity or poorly drained")
    print("[3] - Normal: Normal; well drained light or medium textured soils, sandy loams")
    print("[4] - Low: Deep sand or other soil that takes up water readily; very light, well-drained soils\n")

    while True:

        try:
            str_Ci = input("What are the watershed soil infiltration characteristics of this catchment area. Select from above: ")
            if(int(str_Ci) < 1 or int(str_Ci) > 4):
               print("Not a valid selection. Selection not available.")
               continue


        except:
            print("Invalid input. Must be a number from 1, 2, 3, 4")
            continue
        
        else:
           print(' ')
           break
       
            
    match str_Ci:
       case '1':
        Ci = 0.14

       case '2':
         Ci = 0.10

       case '3':
          Ci = 0.07

       case '4':
          Ci = 0.05

    """
    Watershed Vegetal cover characteristics.
    """
    #Cv
    Cv = 0.0

    print("[1] - Extreme: No effective plant cover, bare or very sparse cover")
    print("[2] - High: Poor to fair; clean cultivation, crops or poor natural cover, less than 20% of drainage area has good cover")
    print("[3] - Normal: Fair to good; about 50% of area in good grassland or woodland, not more than 50% of area in cultivated crops")
    print("[4] - Low: Good to excellent; about 90% of drainage area in good grassland, woodland, or equivalent cover\n")

    while True:

        try:
            str_Cv = input("What are the watershed vegetation characteristics of this catchment area. Select from above: ")
            if(int(str_Cv) < 1 or int(str_Cv) > 4):
               print("Not a valid selection. Selection not available.")
               continue


        except:
            print("Invalid input. Must be a number from 1, 2, 3, 4")
            continue
        
        else:
           print(' ')
           break
       
            
    match str_Cv:
       case '1':
        Cv = 0.14

       case '2':
         Cv = 0.10

       case '3':
          Cv = 0.07

       case '4':
          Cv = 0.05

    """
    Watershed surface storage characteristics.
    """
    #Cs
    Cs= 0.0

    print("[1] - Extreme: Negligible; surface depressions few and shallow, drainageways steep and small, no marshes")
    print("[2] - High: Well-defined system of small drainageways, no ponds or marshes")
    print("[3] - Normal: Normal; considerable surface depression, e.g., storage lakes and ponds and marshes")
    print("[4] - Low: Much surface storage, drainage system not sharply defined; large floodplain storage, large number of ponds or marshes\n")

    while True:

        try:
            str_Cs = input("What are the watershed surface storage characteristics of this catchment area. Select from above: ")
            if(int(str_Cs) < 1 or int(str_Cs) > 4):
               print("Not a valid selection. Selection not available.")
               continue


        except:
            print("Invalid input. Must be a number from 1, 2, 3, 4")
            continue
        
        else:
           print(' ')
           break
       
            
    match str_Cs:
       case '1':
        Cs = 0.11

       case '2':
         Cs = 0.09

       case '3':
          Cs = 0.07

       case '4':
          Cs = 0.05

    runoff_coefficient = round(Cr + Ci + Cv + Cs,2) 

    return

      

          

     




    





   




    
def main():

    get_catchment_area_properties()
    print(f"rainfall intensity for times of concentration, Tc, of 10 min to 100 min: {Tc_Area}")
    print(' ')
    print(f"runoff coefficient: {runoff_coefficient}")
    #return

main()