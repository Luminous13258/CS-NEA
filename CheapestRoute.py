#datalist is imported so that all the variables 
import datalist as data
#JSON and CSV were imported so that the program can read the required files
    #JSON for the zones and prices
    #CSV for the station list
import json
import csv
#tkinter is imported so that there can be a label of the route can be placed on the results page
import tkinter as tk
from tkinter import messagebox as msgbox
#GUI is imported to allow this program script to change the current page
import GUI

#This is the function to run the A* search algorithm on the selected stations that the user has chosen
def cheapest_route(StartLocation, EndLocation, filenameStations, filenameZones):
    #This opens the JSON file with the zones and their corresponding prices
    with open(filenameZones, 'r') as ZoneFile:
        zoneprices = json.load(ZoneFile)
    #This opens the CSV file that holds the station names from the london underground
    with open (filenameStations, 'r') as file:
        reader = csv.reader(file)
        #This iterates through the data finding the start and end locations
        for row in reader:
            if StartLocation == row[0]:
                start = row[1]
            if EndLocation == row[0]:
                end = row[1]
    #This declares the locations found as the variables stored in datalist
    data.StartLocation = StartLocation
    data.EndLocation = EndLocation
    #i is declared as 0 for this iteration
    i = 0
    #This iteration looks for the starting location and the corresponding zone
    while True:
        #This looks for the start location and then looks for the zone of that station
        if StartLocation == file[[1][i]]:
            start_zone = file[[2][i]]
            break
        else:
            #The value of i is incremented before this section of code is reiterated
            i += 1
    #The value of i is reset back to 0
    i = 0
    #This iteration looks for the ending location and the corresponding zone
    while True:
        #This looks for the end location and then looks for the zone of that section
        if EndLocation == file[[1][i]]:
            end_zone = file[[2][i]]
            break
        else:
            #The value of i is incremented before this section of code is reiterated
            i += 1
    #This looks at calculating the cost of the journey
    #The the start and end zones are compared to ensure that they are between zones 2 and 6
    if start_zone <= 6 and start_zone >=2 and end_zone <= 6 and end_zone >=2:
        #The program then asks the user if they are an adult by using a pop-up window
        result = msgbox.askyesno("Rider Information", "Is the rider an adult?")
        #This asks if the ou
        if result == True:
            #This asks if the user is travelling during peak times
            result1 = msgbox.askyesno("Rider Information", "Is the rider travelling during peak times?")
            if result1 == True:
                #This is then if the user is travelling during peak times and is a adult
                cost = zoneprices["Adult"]["Peak"][start_zone][end_zone]
            else:
                #This is if the user is not travelling during peak times and is a adult
                cost = zoneprices["Adult"]["Off-Peak"][start_zone][end_zone]
        else:
            #This asks if the user is travelling during peak times
            result1 = msgbox.askyesno("Rider Information", "Is the rider travelling during peak times?")
            if result1 == True:
                #This is then if the user is travelling during peak times and is a child
                cost = zoneprices["Child"]["Peak"][start_zone][end_zone]
            else:
                #This is then if the user is not travelling during peak times and is a child
                cost = zoneprices["Child"]["Off-Peak"][start_zone][end_zone]

    elif start_zone <= 6 and start_zone >=1 and end_zone <= 6 and end_zone >=1:
        result = msgbox.askyesno("Rider Information", "Is the rider an adult?")
        if result == True:
            #This asks if the user is travelling during peak times
            result1 = msgbox.askyesno("Rider Information", "Is the rider travelling during peak times?")
            if result1 == True:
                #This is then if the user is travelling during peak times and is a adult
                cost = zoneprices["Adult"]["Peak"][start_zone][end_zone]
            else:
                #This is if the user is not travelling during peak times and is a adult
                cost = zoneprices["Adult"]["Off-Peak"][start_zone][end_zone]
        else:
            #This asks if the user is travelling during peak times
            result1 = msgbox.askyesno("Rider Information", "Is the rider travelling during peak times?")
            if result1 == True:
                #This is then if the user is travelling during peak times and is a child
                cost = zoneprices["Child"]["Peak"][start_zone][end_zone]
            else:
                #This is then if the user is not travelling during peak times and is a child
                cost = zoneprices["Child"]["Off-Peak"][start_zone][end_zone]
    else:
        #This calls the function to move the program to the results page after not having found a route
        GUI.resultpage()
        #This creates a label on the results page saying that there has not been a route found
        no_route_found = tk.Label(data.result_page, text="No route found")
        no_route_found.pack()
        return
    