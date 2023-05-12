#json is imported to help deal with file handling of the stored routes as they are stored in a json file
import json
#datalist is another python file I have created which contains all of the variables and file names to reduce errors across files
import datalist as data
#These are the 3 A* searches that I have programmed
#import CheapestRoute as cheapest
#import FastestRoute as fastest
#import ShortestRoute as shortest
#Tkinter is used to create the GUI of the project
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbox

#This is the function that is called when the user clicks the plan route button on the main page
def plan_route(): 
    data.main_page.pack_forget()
    data.plan_route_page.pack()

#This is the function that is called when the user clicks the previously planned routes button on the main page
def previously_planned_routes():
    #This loads the previously plannded routes page
    data.main_page.pack_forget()
    data.planned_routes_page.pack()
    #This loads the routes and formats them into a table on the previously planned routes page
    PrevRoutesFile = open(data.filenamePrevRoutes, "r")
    Routes = json.load(PrevRoutesFile)
    PrevRoutesTable()

#This is the function that is called when the user clicks the home button on either the plan route page or the previously planned routes page
def switch_to_main():
    #This closes all pages open or closed
    data.plan_route_page.pack_forget()
    data.planned_routes_page.pack_forget()
    data.table.pack_forget()
    data.result_page.pack_forget()
    #This loads the main page
    data.main_page.pack()

#This is the function that is called when the user clicks the quit button on the main page
def exit_program():
    result = msgbox.askyesno("Quit Program", "Are you sure you want to exit?")
    if result:
        data.root.destroy()

#This is the function that creates the drop down list for the starting location
def starting_drop_down_list(plan_route_page, optionsStarting):
    #this creates the dropdown list and tells it that the variable type in it will be StringVar
    data.StartLocation = tk.StringVar()
    #This sets the default value of the dropdown list
    data.StartLocation.set("Select Starting Location")
    #This tells the list to be on the plan route page and is called StartLocation and packs it to the page
    data.dropdownStart = tk.OptionMenu(plan_route_page, data.StartLocation, *optionsStarting)
    data.dropdownStart.pack()

#This is the function that creates the drop down list for the ending location
def end_location_drop_down_list(plan_route_page, optionsEnding):
    #this creates the dropdown list and tells it that the variable type in it will be StringVar
    data.EndLocation = tk.StringVar()
    #This sets the default value of the dropdown list
    data.EndLocation.set("Select Ending Location")
    #This tells the list to be on the plan route page and is called StartLocation and packs it to the page
    data.dropdownEnd = tk.OptionMenu(plan_route_page, data.EndLocation, *optionsEnding)
    data.dropdownEnd.pack()

#This is the function that creates the drop down list for the route type
def route_type_drop_down_list(route_type_page, optionsRouteType):
    #this creates the dropdown list and tells it that the variable type in it will be StringVar
    data.RouteType = tk.StringVar()
    data.RouteType.set("Select Route Type")
    #This tells the list to be on the route type page and is called RouteType and packs it to the page
    data.dropdownRouteType = tk.OptionMenu(route_type_page, data.RouteType, *optionsRouteType)
    data.dropdownRouteType.pack()

#This is the function that is called when the user clicks the submit button on the route type page
def SaveConfirmLocations():
    #This sets all the information selected into variables where it is useable
    StartLocaion = data.StartLocation.get()
    EndLocation = data.EndLocation.get()
    RouteType = data.RouteType.get()
    #This makes the user confirm their start and end locations and the chosen route type
    result = msgbox.askyesno("Confirm Locations", "Your starting location is {}, & your ending location is {}. This is using the {} route. Is this correct?".format(StartLocaion, EndLocation, RouteType))
    if result == True:
        resultpage()

#This is the function that is called when the user clicks the back button the route type page
def switch_from_route_type():
    data.route_type_page.pack_forget()
    data.plan_route_page.pack()

#This is the function that is called when the user clicks the submit button on the route type page
def sumbitbutton():
    data.plan_route_page.pack_forget()
    data.route_type_page.pack()
    result = msgbox.askyesno("Rider Information", "Is the rider travelling during peak times?")
    if result == True:
        x=1

# This is the function that is called when the user has confirmed that their locations and route type are correct
def resultpage():
    #This closes the route type page and displays the results page
    data.route_type_page.pack_forget()
    data.result_page.pack()
    #This works out which route to plan and calls the corresponding funciton to run
    if data.RouteType.get() == "Cheapest":
        cheapest.cheapest_route()
    elif data.RouteType.get() == "Fastest":
        fastest.fastest_route()
    elif data.RouteType.get() == "Shortest":
        shortest.shortest_route()
    #This then displays the route planned onto the results page
    result_label = tk.Label(data.result_page, text="Your Planned Route is:")
    result_label.pack()

#This is the function that creates the table for the previously planned routes page
def PrevRoutesTable():
    #This sets up the columns in the table
    columns = list(data.dfprev.columns)
    data.table = ttk.Treeview(data.planned_routes_page, columns=columns, show="headings")
    #This works out the heading names for the columns
    for column in data.dfprev.columns:
        data.table.heading(column, text=column)
        data.table.column(column, width=100)
    #This works out the rows and names for the columns
    for index, row in data.dfprev.iterrows():
        data.table.insert("", "end", values=row.tolist())
    data.table.pack()

#This is the function that is called when the user clicks on a row in the previously planned routes table
def PrevRoutesTableSelect(event):
    selected_row = data.table.focus()
    value = data.table.item(selected_row, "values")
    print(value)
    displayPrevRoutes()

#This is the function that changes the page to display the selected route
def displayPrevRoutes():
    data.planned_routes_page.pack_forget()
    data.table.pack_forget()
    data.result_page.pack_forget()
    data.display_prev_routesPage.pack()

#This is the function that is called when the user presses the home button on the route result page
def SaveRouteBackToMain():
    result = msgbox.askyesno("Save Route", "Would you like to save this route?")
    if result == True:
        with open(data.filenamePrevRoutes, "w") as routeFile:
            json.dump(data.Route, routeFile)
        switch_to_main()
    else:
        switch_to_main()