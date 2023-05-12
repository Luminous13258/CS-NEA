#Tkinter is imported as it allows root to be declared as a global variable and is accessible by all files
import tkinter as tk
from tkinter import ttk

#This is where all variables that are used in multiple files are declared as global variables
global main_page, plan_route_page, planned_routes_page, route_type_page, StartLocation, EndLocation
global root, home_button, enter_button, dropdownStart, dropdownEnd, filenameStations, filenameZones
global filenamePrevRoutes, optionsStarting, optionsEnding, optionsRouteType, dropdownRouteType
global RouteType, planning_page, results_page, tree, columns, dfprev, PrevRoutesFile, Routes
global prevous_Routes, PrevRoutesTable, result_page, table

dfprev = [[],[]]

#This defines root for the program to access tkinter
root =tk.Tk()

table = ttk.Treeview(root)

#This creates the lists that will be used to create the drop down lists
optionsStarting = []
optionsEnding = []
optionsRouteType = ["Shortest by Time", "Cheapest", "Shortest by Distance"]

#This creates the frames that will be used to create the pages
main_page = tk.Frame(root)
plan_route_page = tk.Frame(root)
planned_routes_page = tk.Frame(root)
route_type_page = tk.Frame(root)
planning_page = tk.Frame(root)
result_page = tk.Frame(root)
displayPrevRoutesPage = tk.Frame(root)

#This is the paths to the files that will be used in the program
filenameStations = "C:/Users/benpi/Desktop/Computer Science/V2 - GUI using tkinter/CountiesTest.csv"
filenameZones = "C:/Users/benpi/Desktop/Computer Science/V2 - GUI using tkinter/ZonePrices.json"
filenamePrevRoutes = "C:/Users/benpi/Desktop/Computer Science/V2 - GUI using tkinter/StoredRoutes.jsonc"

#This creates the variables that will be used to store the start and end locations
StartLocation = ""
EndLocation = ""
RouteType = ""