#CSV is imported to read the station list to find the start and end location
import csv
#Used to manage queues of data
import heapq
#datalist is imported so that variables can be accessed
import datalist as data
#GUI is imported to allow the program to be moved to another page from within this script
import GUI

filenameStations = data.filenameStations

#This is the function tha calculates the fasteset route
def fastest_route(StartLocation, EndLocation):
    #This sets up the queue with the start location
    queue = [(0, StartLocation, [])]
    visited = set()

    #This is run until the path is found as it iterates whilst the queue exists
    while queue:
        (heuristic_cost, current, path) = heapq.heappop(queue)

        #Checks if the current node is the end node and returns the path and current node if it is true
        if current == EndLocation:
            return path + current
        
        #Checks that the current node has been visited
        if current in visited:
            continue
        
        #If the current node is not in the visited array then it adds it to the list
        visited.add(current)

        #
        for neighbor, cost in graph[current].items():
            if neighbor not in visited:
                cost_estimate = cost + heuristic_cost
        
        return None

#Declares the graph
graph = {}
#Opens the file containing stations to then be placed into a graph
with open(filenameStations, 'r') as file:
    reader = csv.DictReader(file)
    #Creates the table of data for the algorithm to search
    for row in reader:
        name = row['Station Name']
        ID = int(row['ID'])
        next_ID = int(row['Next Station'])
        prev_ID = int(row['Previous Station'])
        zone = int(row['Zone'])

        if ID not in graph:
            graph[ID] = {}

        if next_ID != 0:
            graph[ID][next_ID] = zone
        if prev_ID != 0:
            graph[ID][prev_ID] = zone

        if next_ID != 0:
            if next_ID not in graph:
                graph[next_ID] = {}
            graph[next_ID][ID] = zone
        if prev_ID != 0:
            if prev_ID not in graph:
                graph[prev_ID] = {}
            graph[prev_ID][ID] = zone

#This calls the function above to calculate the fastest route providing the parameters of graph and the start and end locations
fastestRoute = fastest_route(graph, data.StartLocation, data.EndLocation)
if fastestRoute is None:
    #This calls the function to move the program to the results page after not having found a route
    GUI.resultpage()
    #This creates a label on the results page saying that there has not been a route found
    no_route_found = tk.Label(data.result_page, text="No route found")
    no_route_found.pack()
else:
    #This calls the function to move the program to the results page after having found a route
    GUI.resultpage()
    #This creates a label on the results page saying that there has been a route found and the labels the route onto the page
    route_found = tk.Label(data.result_page, text="Shortest Route Found:",/
                           '->'.join(str(x) for x in fastest_route))
    route_found.pack()