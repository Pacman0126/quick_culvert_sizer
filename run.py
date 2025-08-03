import numpy as np
import math

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

    

def get_catchment_area_properties(flow_velocity = None):    
    """
    The catchment charactersistics for the catchment of interest are calculated based on user input of catchment area
    """


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

    global assumed_flow_velocity

    if(flow_velocity is None):
       
      assumed_flow_velocity = 5.0

    else:
       assumed_flow_velocity = flow_velocity


    Tc_Area = {Tc: round(b / math.pow((Tc + d),e),2)  for Tc in range(10,110,10)}
    print(' ')

    get_runoff_coefficient()

    global Tc_Q
    Tc_Q = {}

    Tc_Q = {Tc: round((runoff_coefficient * (b / math.pow((Tc + d),e)) * catchment_area),1)  for Tc in range(10,110,10)}

    global Tc_A

    Tc_A = {}

    Tc_A = {Tc: round((runoff_coefficient * b / math.pow((Tc + d),e) * catchment_area / assumed_flow_velocity),1)  for Tc in range(10,110,10)}


    return



def get_box_culvert_options(flow_velocity = 5.0):
       
        max_box_height = 0

        query = ''
        query2 = ''

        assumed_flow_velocity = flow_velocity

        query2 = input(f"The default assumed flow velocity for box culverts is {assumed_flow_velocity} ft/s. \nA minimum of 2.5 ft/s is required to be self cleaning, a maximum of 8.0 ft/s is allowed to prevent downstream erosion damage\nThe higher the velocity, the smalller the box solutions. Enter new value or press enter to continue with default value: ")

        while True:
            try:                                              
            
              if(query2 == '' or query2 == ' '):
                
                break
              
              else:
                 assumed_flow_velocity = float(query2)

                 if(float(query2) < 2.5 or float(query2) > 8.0):
                    print("Enter value between 2.5 and 8.0")
                    continue
                 break           

            except:
              print("Invalid input. Must be number.")
            continue

        while True:

          try:
            str_max_box_height = input("At this culvert location, what is the maximum height up to 10 the box culvert can be: ")
            if(int(str_max_box_height) < 4 or int(str_max_box_height) > 10):
                
                if int(str_max_box_height) < 4:
                   scenario = '1'

                elif int(str_max_box_height) > 10:
                    scenario = '2'

                match scenario:
                  case '1':

                    query = input("Box culverts should have a minimum height of 4 ft. Would you like to use a different height (y/n): ")

                    while True:
                       try:
                                             
                        
                          if(query == 'y' or query == 'Y'):
                            break
                          elif (query == 'n' or query == 'N'):
                            print("Try circular pipe instead. This appliaction is for box culverts only.")
                            break


                       except:
                        print("Invalid input. Must be y or n")
                        continue
                      
                    if (query == 'n' or query == 'N'):
                          break
                      
                    continue

                  case '2':
                      
                      query = input("Precast box culcerts should not be more than 10 ft tall due to roadway lane widths while being delivered.\nWould you like to use a different height (y/n):")
                      while True:
                                               
                        try:
                          
                          if(query == 'y' or query == 'Y'):
                            break
                          elif (query == 'n' or query == 'N'):
                            break

                        except:
                          print("Invalid input. Must be y or n")             
                          continue

                      if (query == 'n' or query == 'N'):
                        break
                      
                      continue
            else:
              max_box_height = int(str_max_box_height)

              print(' ')
              break
               

          except:
            print("Invalid input. Must be a number from 1, 2, 3,...10")
            continue
   
        if (query == 'n' or query == 'N'):
          return

        print(f"maximum box height = {max_box_height}")

        """
        Manning's formula for open channel flow in culvert structures and water channels: Q = A * 1.486/n * R^(2/3) * S^(1/2)

        Q = Discharge (cu. ft./sec.)
        A = Cross-sectional Area of Flow (sq. ft.)
        n = Coefficient of Roughness, 0.012 for concrete
        R = Hydraulic Radius (ft.) = P/A
        S = Slope of Pipe (ft./ft.)
        P = Wetted perimeter (ft.)
        """

        n = 0.012

        slopes = []
        slopes = [round(0.0120 + (s * 0.0005),4) for s in range(1,37)]

        barrel_count = 0

#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv begin main algorithim vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv#

        """
        The code block below now drills down on all the solution possibilites found above and finds the smallest(i.e. most ecenoical)
        box culvert solution in each time of concentration, Tc, and collects them into a dictionary with key=Tc, value=(width,height)
        """

        print(f"Catchment area size = {catchment_area} acres")
        print(f"Composite runoff coefficient for this catchment area = {runoff_coefficient}")
        print("")

        box_dimen_Qcap = {}
        box_dimen_total_cross_sectional_area = {}
        box_dimen_number_of_barrels = {}

        S_Barrels = {}

        for Tc in range(10,110,10):

          for box_height in range(4,max_box_height + 1, 1):
            
            for span in range(box_height, 11, 1):

              """
              The code block below iterates thru S_Barrels{} and extracts the number of barrrels required for each slope condition 1.25% to 3.00%
              and finds the number of barrels that appears in this range. Then adds the maximum number of occurences (e.g. out of 4,5,6 barrels 
              5 appears 20 times out of 36 slope conditions). The box size 5 ft x 4 ft as key with value=3 is added to dicctionary of solutions{}
              as (5,4):3
              """

              A = span * (box_height - 1.5)
              P = (box_height - 1.5) * 2 + span
              R = A/P

              for slope in slopes:

                Qcap = round((1.486/n) * A * math.pow(R,(2/3)) * math.pow(slope,0.5),1)
                Areq = Qcap/assumed_flow_velocity

                S_Barrels.update({slope:math.ceil(Tc_A[Tc]/Areq)})

              box_dimen_Qcap.update({(span,box_height):S_Barrels})

              number_of_barrels = [] #list of all barrel counts in slope range
              barrel_count_vs_frequency = {}

              for key in S_Barrels:
                    
                number_of_barrels.append(S_Barrels[key])

              for x in range(1,11):  #iterate thru width number of required barrels 1 to 10. typically not more than 6 barrels
                  if(number_of_barrels[x] == 0):
                      continue
                  
                  if(number_of_barrels.count(x) == 0):
                      continue
                  else:
                    barrel_count_vs_frequency.update({x:number_of_barrels.count(x)})

              most_frequent_barrel_num = max(barrel_count_vs_frequency, key=barrel_count_vs_frequency.get)
                    
              box_dimen_total_cross_sectional_area.update({(span,box_height):most_frequent_barrel_num *span * box_height})
              box_dimen_number_of_barrels.update({(span,box_height):most_frequent_barrel_num})    
              S_Barrels = {} 

          barrel_count = box_dimen_number_of_barrels.get((span,box_height))   
          most_econonomical_design = min(box_dimen_total_cross_sectional_area, key=box_dimen_total_cross_sectional_area.get)

          print(f"most_econonomical_design for Tc = {Tc} is {barrel_count} - {most_econonomical_design[0]} ft (span) x {most_econonomical_design[1]} ft (height)" )
          box_dimen_total_cross_sectional_area = {}
          box_dimen_number_of_barrels = {}

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ end main algorithm ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

        print('')
        query1 = input("Do you have any more catchments to consider (y/n): ")

        while True:
            try:                                      
            
              if(query1 == 'y' or query1 == 'Y'):
                get_catchment_area_properties()
                get_box_culvert_options()

                break
              elif (query1 == 'n' or query1 == 'N'):
              
                break

            except:
              print("Invalid input. Must be y or n")
              continue
            


def main():

    get_catchment_area_properties()

    get_box_culvert_options()    

    return

main()