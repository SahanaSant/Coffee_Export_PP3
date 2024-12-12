# final_plots.py
# ENDG 233 F24
# STUDENT NAME(S): Amar Kaber, Sahana Santhanam
# GROUP NAME: Group 17 
# A terminal-based data analysis and visualization program in Python.
# You must follow the specifications provided in the project description.
# Remember to include docstrings and comments throughout your code. 

from design_project import years
from design_project import countries
from design_project import ask_country
from design_project import ask_year
from design_project import Error_Message
from user_csv import read_csv
from user_csv import write_csv
import matplotlib.pyplot as plt
import user_csv
import numpy as np
#Initializing for interacting with the user 
user_ans = ""

def coffee_type_graph(exports):
    '''
    Takes the extracted data for exports and displays a pie chart 
    visualizing the percentage of countries using different coffee types. 

    Parameters:
        exports 
            (2d list): [countries, exported coffee per year, coffee type primarily used]

    '''
    #Initializing count of countries that use certain coffee types
    count_arab = 0
    count_robus = 0
    count_lib = 0
    count_excel = 0
    #For loop counting occurences of coffee types primarily exported from countries
    #32nd column pertains to coffee type 
    for row in exports:
        if row[32] == "Arabica\n":
            count_arab += 1
        elif row[32] == "Robusta\n":
            count_robus += 1
        elif row[32] == "Liberica\n":
            count_lib += 1
        else:
            count_excel += 1
    #Counting total (country total)
    total_count = count_arab+count_robus+count_lib+count_excel
    #Converting into percents
    percent_arab = count_arab/total_count*100
    percent_robus = count_robus/total_count*100
    percent_lib = count_lib/total_count*100
    percent_excel = count_excel/total_count*100
    #Add data into numpy array
    percent_list = np.array([percent_arab, percent_robus, percent_lib, percent_excel])
    label_list = ["Arabica", "Robusta", "Liberica", "Excelsa"]
    colours = ["chocolate", "sienna", "peru", "saddlebrown"]
    #Put in user_history this data about the plots graphs
    write_csv("User_History.txt", ("\t"+str(percent_list)+"\n"), False)
    write_csv("User_History.txt", ("\t"+str(label_list)+"\n"), False)
    write_csv("User_History.txt", ("\t"+str(colours)+"\n"), False)
    #Plot data as pie chart
    plt.subplot(1,2,1)
    plt.pie(percent_list, labels = label_list, startangle = 90, shadow = True, colors = colours)
    plt.title('Coffee Type Popularity Globally')
    plt.legend(title = 'Coffee Types', loc = "upper left")

def exports_products_graph(exports, production, years, country):
    '''
    Takes the data for exports and production, the list of years and the selected country and 
    produces a line plot comparing exports and production for a country over the years 1990-2019

    Parameters:
        exports 
            (2d list): [countries, exported coffee per year, coffee type primarily used]
        production
            (2d list): [countries, coffee produced per year]
        years (list)
        country (str): a valid country
    
    ''' 
    #Set the x values from the years list. 
    #Values do not include first element of years list as it is '0'.
    x_values = years[1:]
    #Initializing lists for y-axis values.
    y1_list = []
    y2_list = []
    #Create lists stored with casted integers of the y values.
    export_values = []
    production_values = []
    #Loop through the 2D export and production lists and extract y values. 
    #These are at indexes 1 to 31.
    for data in exports:
        if data[0] == country:
            y1_list = data[1:31]
    for data in production:
        if data[0] == country:
            y2_list = data[1:31]
    #Casting is done through two for loops
    for value in y1_list:
        export_values.append(int(value))   
    for value in y2_list:
        production_values.append(int(value))
    #Store this data about the y1 and y2 values
    write_csv("User_History.txt", ("\t"+str(y1_list)+"\n"), False)
    write_csv("User_History.txt", ("\t"+str(y2_list)+"\n"), False)
    #Create Plot
    plt.subplot(1,2,2)
    plt.plot(x_values,export_values) 
    plt.plot(x_values,production_values)
    #Add labels and title and legend
    plt.xlabel("Years")
    plt.ylabel("Export and Production (Kilos)")
    plt.title(f'Production and Exports in {country}')
    plt.legend(["Exports", "Products"], loc = "upper right")

#Start the main. If playing this file only,
if __name__ == "__main__":
    print(f'ENDG 233 PORTFOLIO PROJECT')
    #Create the User_History File
    write_csv("User_History.txt", "START OF FILE; Visual Graphs Portion\n", False)
    #Start main. 
    while (True):
        #Prepare to track user's inputs.  
        write_csv("User_History.txt", "When asked to enter or exit, the user put:\n", False)
        #Ask the user first if they'd like to enter the game or exit. 
        user_ans = (input("Please type enter to see graphs for a country and year, or type exit to exit the prompt.\n\t")).upper()
        #Write User's Input
        write_csv("User_History.txt", ("\t" + user_ans+ "\n"), False)
        #If user wants to exit, break out of the loop.
        if (user_ans=="EXIT"):
            break
        #Otherwise generate the graph
        elif (user_ans=="ENTER"):
            #Prepare to track the user's inputs and their attempts. 
            write_csv("User_History.txt", "When Asking For Year, User Put:\n", False)
            #Ask the user the year, and keep track of the column 
            #(when accessing each csv file's array).
            ask_year_data= ask_year(years)
            # At index 0, the column the user chooses is retrieved. 
            # At index 1, the year the user chose is retrieved. 
            index_Col = ask_year_data[0]
            user_year = ask_year_data[1]
            #Store the next information on user's inputs
            write_csv("User_History.txt", "When Asking For Country, User Put:\n", False)
            #Ask the user the country, keep track of the row 
            index_Row = ask_country(countries)
            #Divider
            print(f"{'':=^70s}")
            #Copy and pasted from main in design_project.py; 
            #Show calculated plots and data visuals
            print(f'Calculating graphs and data......')
            print(f"{'':=^70s}")
            #For the visuals, we will not use numpy arrays. Thus we will have non-numpy 2D Lists
            production_2D = read_csv("data_files/Coffee_production.csv", False, False)
            export_2D = read_csv("data_files/Coffee_export.csv", False, False)
            #Setting the size of the figure
            plt.figure(figsize = (14, 5)) # Create and set the size of the figure
            #Display to user that the graphs are ready to view.
            print(f'Please view your graphs in desktop! Click close to generate a new graph or exit the prompt.')
            print(f"{'':=^70s}")
            #Prepare to store data related to visual plots in the User History File. This is for the pie chart.
            write_csv("User_History.txt", "When Given a Pie Chart, The Data is:\n", False)
            #Call the plot functions
            coffee_type_graph(export_2D)
            #This is the repeated the same with the line graph.
            write_csv("User_History.txt", "When Given a Line Chart, The Values are:\n", False)
            exports_products_graph(export_2D, production_2D, years, countries[index_Row])
            #Plot the final graphs.
            plt.show()
            plt.savefig("coffee_graphs.png")
        #If user doesn't say enter or exit, que the error message.  
        else:
            Error_Message()
    #Indicate the end of the user_history file tracking user activity
    print(f'You have exited the terminal. Thank you for playing!')
    print(f"{'':=^70s}")
    write_csv("User_History.txt", "END OF FILE; Visual Graphs Portion\n\n", False)
