#CSV is imported so that the station list file can be read to setup the drop down lists
import csv
#datalist is imported so that the required variables can be accessed from the file
import datalist as data
#GUI is imported so that buttons can be placed onto a page that they will be used on
import GUI
#pandas is imported to import the data and place it into a dataframe
import pandas as pd
#tkinter is imported to allow buttons and pop-up windows to be created by this program
import tkinter as tk
from tkinter import messagebox as msgbox
from tkinter import ttk

root = tk.Tk()

#This opens the csv file and reads it to create the drop down list for the starting location
with open(data.filenameStations, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data.optionsStarting.append(row[0])

#This line creates the dropdown list declaring where it is and what data it presents
    #This dropdown list holds the ending stations options
GUI.starting_drop_down_list(data.plan_route_page, data.optionsStarting)

#This opens the csv file and reads it to create the drop down list for the ending location
with open(data.filenameStations, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data.optionsEnding.append(row[0])

#This line creates the dropdown list declaring where it is and what data it presents
    #This dropdown list holds the ending stations options
GUI.end_location_drop_down_list(data.plan_route_page, data.optionsEnding)

#This line creates the dropdown list declaring where it is and what data it presents
    #This dropdown list holds the route type options
GUI.route_type_drop_down_list(data.route_type_page, data.optionsRouteType)

#This creates the button for the user to click to change from the main page to the plan route page
planRoute_button = tk.Button(data.main_page, text="Plan a New Route", command=GUI.plan_route)
planRoute_button.pack()

#This creates the button for the user to click to change from the main page to the previously planned routes page
routeHistory_button = tk.Button(data.main_page, text="Previously Planned Routes", command=GUI.previously_planned_routes)
routeHistory_button.pack()

#This creates the button on the main page for the user to exit the program
quit_button = tk.Button(data.main_page, text="Quit", command=GUI.exit_program)
quit_button.pack()

#This creates the button on the plan route page for the user to submit & confirm their start and end locations
submit_button = tk.Button(data.plan_route_page, text="Submit", command=GUI.sumbitbutton)
submit_button.pack()

#This creates the button on the page where the user confirms their start & end locations and their chosen route type
submit_button = tk.Button(data.route_type_page, text="Submit", command=GUI.SaveConfirmLocations)
submit_button.pack()

#This creates the button on the plan route page for the user to go back to the main page
home_button = tk.Button(data.plan_route_page, text="Home", command=GUI.switch_to_main)
home_button.pack()

#This creates the button on the previously planned routes page for the user to go back to the main page
home_button = tk.Button(data.planned_routes_page, text="Home", command=GUI.switch_to_main)
home_button.pack()

#This creates the button on the result page for the user to go back to the main page
home_button = tk.Button(data.result_page, text="Home", command=GUI.switch_to_main)
home_button.pack()

#This creates the button on the route type page for the user to go back to the plan route page
back_button = tk.Button(data.route_type_page, text="Back", command=GUI.switch_from_route_type)
back_button.pack()

'''
#This creates the save button on the result page for the user to save their route to the JSON file
save_button = tk.Button(data.result_page, text="Save", command=GUI.saveRoute)
save_button.pack()
'''

#This declares the dataframe for the previously planned routes whilst opening the json file
dfprev = pd.read_json("C:/Users/benpi/Desktop/Computer Science/V2 - GUI using tkinter/StoredRoutes.jsonc")

#This sets up the columns for the previously planned routes table
columns = dfprev.columns
tree = ttk.Treeview(root, columns= columns, show="headings")
tree.bind("<<TreeviewSelect>>", GUI.PrevRoutesTableSelect)