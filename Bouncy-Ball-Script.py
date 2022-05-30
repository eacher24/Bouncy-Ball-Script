#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHYS20161 - Bouncy Ball Assignment 
Last Updated 22/10/2021
@author: Elise Acher

Aim of Assignment: To be able to produce the integer number of bounces above 
a minimum height. In which the initial height, minimum height and efficiency 
are receieved as inputs by the user. A series of validation checks are 
performed in order to make sure no errors occur in the functions. Furthermore,
a calculation in the case that the minimum height is zero i.e. no friction is
included as an option at the end for the user to be able to investigate more
variables that can be calculated.
"""
import math
import numpy as np




acceleration_g = 9.81



print("             ----------Welcome to the Bouncy Ball Calculator----------")
   

 

def number_of_bounces(minimum_height, initial_height, efficiency):
    """
    
    Calculate the number of bounces achieved above input minimum height.
    
    Parameters
    ----------
    initial_height: float,the starting height that the ball is dropped from.
    minimum_height : float, the minimum value we are looking to get some 
    bounces above.
    efficiency_value : float, gives the energy lost after each bounce.
    --------
    Returns:  Number of bounces above the min height as a float

    """ 
    no_of_bounces = int(math.log((minimum_height/initial_height),efficiency))

    return no_of_bounces

def total_time(integer_bounce,acceleration_g ,initial_height):
    """
    Calculates the time taken for the integer number of bounces calculated in
    the previous section.

    Parameters
    ----------
    integer_bounce : integer, an integer number of bounces above the minimum 
    height.    
    acceleration_g : float, acceleration due to gravity, is a constant.   
    initial_height : float, the initial height the ball was dropped from. 
    -------
    Returns: The time taken for these bounces as a float.
    
    """
    first_bounce = np.sqrt((2*initial_height)/acceleration_g )
    for i in range(1,integer_bounce+1):
        first_bounce += np.sqrt(efficiency**i)*(np.sqrt((2*initial_height)/acceleration_g )*2)
    return first_bounce


def finite_sum(initial_height,integer_bounce,efficiency):
    """
    Calculates the sum of the distances covered by the ball when the number of 
    bounces is greater than zero.
    
    Parameters
    ----------
    initial_height : float,the initial height the ball was dropped from.
    integer_bounce : integer, an integer number of bounces above the minimum 
     height.   
    efficiency_value : float, gives the energy lost after each bounce

    -------
    Returns: The distance travalled by the ball for a specified minimum height.

    """
    finite_dist = abs(2*((initial_height)*((efficiency**integer_bounce)-1)/(efficiency - 1)) - initial_height)
    
    return finite_dist


def infinite_sum(initial_height,integer_bounce, efficiency):
    """
    Calculates the infinite sum of distances in the case that there is no 
    friction, i.e when minimum_height is zero
    Parameters
    ----------
    initial_height : float, the initial height the ball was dropped from.
    integer_bounce : integer, the number of bounces above the minimum height.   
    efficiency : float, gives the energy lost after each bounce.
    
    
    -------
    Returns: The distance travalled by the ball direction when minimum height
    = 0.

    """
    infinite_dist = (((initial_height)/(1-efficiency))*2) - (initial_height)
    return infinite_dist





while True:
    try: 
        initial_height = float(input("Please enter an initial height in meters: "))
    except ValueError:
        print("The input is not a number please try again")
        continue
    except NameError:
        print("The initial height cannot be a word, please try again...")
        continue
    if initial_height <= 0:
        print("Sorry, your response must be greater than 0, please try again...")
        continue
    else:
        break
if initial_height > 0:
   print("Value for initial height aceepted!")


# Validation check for minimum height - Question is asked until the input satifies the conditions.
while True:
    try: 
         minimum_height = float(input("Please enter the minimum height in meters: "))
    except ValueError:
        print("The minimum height needs to be a number, please try again...")
        continue
        
    except NameError:
        print("The minimum height cannot be a word, please try again...")
        continue   
    if initial_height < minimum_height :
        print("Sorry, your response for minimum height cannot be greater than maximum height, please try again...")
        continue
    if  minimum_height <= 0 :
        print("Sorry, your value for the minimum height must be greater than 0, please try again...")
        continue
    else:
        break
if initial_height > minimum_height > 0 :
    print("Value for minimum height accepted!")
    
# Validation check for efficiency valaue - Question is asked until the input satifies the conditions.
while True:
    try: 
         efficiency = float(input("Please enter an efficiency number between 0 and 1: "))
    except ValueError:
        print("The minimum height needs to be a number, please try again...")
        continue
        
    except NameError:
        print("The minimum height cannot be a word, please try again...")
        continue
        
    if efficiency < 0 or efficiency > 1 :
    
        print("Sorry, your response for the efficiency value must be between 0 and 1, please try again...")
        continue
    
    else:
        break
if 0 < efficiency < 1 :
    print("Value of efficiency accepted!")
    
#Extra - validation for distance travelled by ball

                    
integer_bounce = number_of_bounces( minimum_height, initial_height, efficiency)
time_taken = float(total_time(integer_bounce, acceleration_g , initial_height))
infinite_dist = infinite_sum(initial_height, integer_bounce, efficiency)
finite_dist = finite_sum(initial_height, integer_bounce, efficiency)

print("\n" + "-----The results of your inputs are being tabulated below, please wait...-----" + "\n")

done = False



while True:
    if integer_bounce == 0:
        print("The ball did not bounce over " + str(minimum_height) + "m as too much energy was lost.")
        break
    if integer_bounce == 1 :
        print("The ball bounced once above " + str(minimum_height) + "m. The time taken was {0:0.2f}s.".format(time_taken))
        break
    elif integer_bounce == 2 :
        print("The ball bounced twice above " + str(minimum_height) + "m. The time taken was {0:0.2f}s.".format(time_taken))
        break  
    else:
        print("The ball bounced " + str(integer_bounce) + " times over " + str(minimum_height) + "m. The time taken was {0:0.2f}s.".format(time_taken))
        break
            

        


while True:
    distance = input("Would you like to know the total distance travelled by the ball? [Y/N]" )    

    if distance == ("Y") :
        print("The ball travelled {0:0.2f}m during this time.".format(finite_dist))
        break
    if distance == ("N")  :
        print("\n" +"Next Question: ")
        break
    else:
        print("Please specify Y or N.")
        
        
while True:
    zero_friction_input = input("Would you like to know the distance travelled by the ball, in the case where there is no friction? [Y/N]")
    
    if zero_friction_input == ("Y")  :
        print("\n"+ "The ball bounces infinitely many times and covers a distance of {0:0.2f}m. ". format(infinite_dist))
        print("\n" + "----------Thank you for your inputs!----------")
        break
    elif zero_friction_input ==("N"):
        print("\n" + "----------Thank you for your inputs!----------")
        break
    else: 
        print("Please specify Y or N.")
    


