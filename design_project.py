# design_project.py
# ENDG 233 F24
# STUDENT NAME(S) Amar Kaber, Sahana Santhanam
# GROUP NAME
# A terminal-based data analysis and visualization program in Python.
# You must follow the specifications provided in the project description.
# Remember to include docstrings and comments throughout your code.
import user_csv
from user_csv import read_csv
from user_csv import write_csv 
import numpy as np

#List of Years:
years = [0, 1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
#List of Countries: 
countries = ["Angola", "Bolivia", "Brazil" , "Burundi", "Cameroon", "Central African Republic", "Colombia", "Congo", "Costa Rica", "Ivory Coast", "Cuba", "Democratic Republic of Congo", "Dominican Republic", "Ecuador", "El Salvador", "Equatorial Guinea", "Ethiopia", "Gabon", "Ghana", "Guatemala", "Guinea", "Guyana", "Haiti", "Honduras", "India", "Indonesia", "Jamaica", "Kenya", "Lao People's Democratic Republic", "Liberia", "Madagascar", "Malawi", "Mexico", "Nepal", "Nicaragua", "Nigeria", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Rwanda", "Sierra Leone", "Sri Lanka", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Trinidad & Tobago", "Uganda", "Venezuela", "Viet Nam", "Yemen", "Zambia", "Zimbabwe"]

def Error_Message():
    print("Invalid input! Please try again.")

def ask_year(comp_list):
    '''
    Asks the user a year of their choice until a valid year is told. 

    Parameters
    ----------
    comp_list : "comparison list". The list is used to check if the entry the user enters is in our data. 

    '''
    while True:
        #Asking the user for a year
        user_year = (input(f'Please enter a year from 1990 to 2019 to see global data.\n\t'))
        #This will be stored as inputs in the User History, no matter if its invalid or valid. 
        write_csv("User_History.txt", ("\t"+ str(user_year)+"\n"), False)
        #Getting column number
        #If the input the user entered equals 0, is a string without a digit, or etc other than 
        #what is in the years list, display the error message.
        if (user_year == "0"):
            Error_Message()
        elif (user_year.isdigit()==False):
            Error_Message()
        #Otherwise register and return the valid year. 
        elif (int(user_year) in comp_list):
            index_column_ref = comp_list.index(int(user_year))
            return [index_column_ref, int(user_year)]
        else:
            Error_Message()

def ask_country(comp_list):
    '''
    Asks the user a country of their choice until a valid country is told. 

    Parameters
    ----------
    comp_list : "comparison list". The list is used to check if the entry the user enters is in our data.

    '''
    #Asking for a country
    while True:
        #Print all the available options. 
        print(f'Countries Of Export:')
        for i in range(len(countries)):
            print(f'\t\t{str(i)}. {countries[i]}')
        user_country = input(f'Please enter a valid country name (no need for number).\n\t')
        #This will be stored as inputs in the User History, no matter if its invalid or valid. 
        write_csv("User_History.txt", ("\t"+user_country+"\n"), False)
        #Getting row number
        if (user_country in countries):
            index_row_ref = countries.index(user_country)
            #Return this value. 
            return index_row_ref
        else:
            Error_Message()

def introductory_stats(production, export, index_Y, year, index_X, countries):
    '''
    This function displays to the user the basic statistics on coffee from the year they chose. 

    Parameters
    ----------
    production: A 2D Numpy array gathered from the csv file on production of coffee. 
    export: A 2D Numpy array gathered from the csv file on exports of coffee.
    index_Y: The index of the column corresponding to the year the user chose. 
    year: The year the user chose. 
    index_X: The index of the row corresponding to the country the user chose.
    countries: The list of countries in the database. 

    '''
    #Extracting column from the 2d array
    exports_in_yr = export[:, index_Y]
    production_in_yr = production[:, index_Y]
    #Sum all of the exports/products for total export 
    total_exports = np.sum(exports_in_yr)
    total_products = np.sum(production_in_yr)
    #Calculate the amount of coffee exported out of production 
    diff_percent = (total_exports/total_products)*100
    #For the country and year the user requested, lets calculate the difference percent. 
    exports_in_country = export[index_X][index_Y]
    products_in_country = production[index_X][index_Y]
    diff_percent_country = (exports_in_country/products_in_country)*100
    #Print statements and data out to user. 
    print(f'The average coffee exported out of production in {year} globally was {diff_percent:.2f}%.')
    print(f'The total coffee exports globally was worth {total_exports} of one kilo coffee bags in {year}.')
    print(f'The total coffee production globally was worth {total_products} of one kilo coffee bags in {year}.')
    print(f'Specifically, the average coffee exported out of production in {year} in {(countries[index_X]).upper()} was {diff_percent_country:.2f}%.')


def get_mean(production, export, consumption, index_Y, year, index_X, countries):
    '''
    This function displays to the user information on averages on coffee from the year they chose. 

    Parameters
    ----------
    production: A 2D Numpy array gathered from the csv file on production of coffee. 
    export: A 2D Numpy array gathered from the csv file on exports of coffee.
    consumption: A 2D Numpy array gathered from the csv file on consumption of coffee.
    index_Y: The index of the column corresponding to the year the user chose. 
    year: The year the user chose. 
    index_X: The index of the row corresponding to the country the user chose.
    countries: The list of countries in the database.  

    '''
    #Extracting columns from the 2D arrays.
    production_in_yr = production[:, index_Y]
    exports_in_yr = export[:, index_Y]
    consumption_in_yr = consumption[:, index_Y]
    #Extracting country row to find mean
    production_country = production[index_X:,]
    exports_country = export[index_X:,]
    consumption_country = consumption[index_X:,]
    #Find the averages from the three columns
    average_exports = np.mean(exports_in_yr)
    average_products = np.mean(production_in_yr)
    average_consumption = np.mean(consumption_in_yr)
    #Finding averages in row
    average_export_country = np.mean(exports_country)
    average_product_country = np.mean(production_country)
    average_consumption_country = np.mean(consumption_country)
    #Print statements to user. 
    print(f'The average coffee export per country in {year} globally is {average_exports} kilo coffee bags.')
    print(f'The average coffee production per country {year} globally is {average_products} kilo coffee bags.')
    print(f'The average coffee consumption per country {year} globally is {average_consumption} kilo coffee bags.')
    print(f'The average coffee exported in {(countries[index_X]).upper()} is worth {average_export_country:.2f} kilo coffee bags yearly.')
    print(f'The average coffee produced in {(countries[index_X]).upper()} is worth {average_product_country:.2f} kilo coffee bags yearly.')
    print(f'The average coffee consumed in {(countries[index_X]).upper()} is worth {average_consumption_country:.2f} kilo coffee bags yearly.')

def get_max(production, export, consumption, index, list_of_countries, year):
    '''
    This function displays to the user information on maximums on coffee from the year they chose. 

    Parameters
    ----------
    production: A 2D Numpy array gathered from the csv file on production of coffee. 
    export: A 2D Numpy array gathered from the csv file on exports of coffee.
    consumption: A 2D Numpy array gathered from the csv file on consumption of coffee.
    index: The index of the column corresponding to the year the user chose.
    list_of_countries: A list of the countries registered across all 3 csv files.  
    year: The year the user chose. 

    '''
    #Extracting column from the 2d array
    production_in_yr = production[:, index]
    exports_in_yr = export[:, index]
    consumption_in_yr = consumption[:, index]
    #Calculate the maximum found in each column 
    production_max= np.max(production_in_yr, axis = None)
    export_max = np.max(exports_in_yr, axis = None)
    consumption_max = np.max(consumption_in_yr, axis = None)
    #Search which country this max value is from by transposing the column into a row.
    exports_tp = exports_in_yr.T
    production_tp = production_in_yr.T
    consumption_tp = consumption_in_yr.T
    #...And searching the index of where that maximum is located in which country
    #One is added to the index since the year column includes a header, so country list starts one index earlier. 
    country_index_exp= np.argmax(exports_tp, axis = None) 
    country_index_prod = np.argmax(production_tp, axis = None) 
    country_index_cons = np.argmax(consumption_tp, axis = None) 
    #Print data to user 
    print(f'The maximum produced in {year} was {production_max} kilos of coffee bags in the country {list_of_countries[country_index_prod]}.')
    print(f'The maximum exported in {year} was {export_max} kilos of coffee bags in the country {list_of_countries[country_index_exp]}.')
    print(f'The maximum consumed in {year} was {consumption_max} kilos of coffee bags in the country {list_of_countries[country_index_cons]}.')

#Start the main. If playing this file only, 
if __name__ == "__main__":
    print(f'ENDG 233 PORTFOLIO PROJECT')
    #Create a new file storing the user's inputs
    write_csv("User_History.txt", "START OF FILE; Statistics Portion\n", False)
    #Start the prompt
    while (True):
        #Prepare to track user's inputs.  
        write_csv("User_History.txt", "When asked to press enter or exit, the user put:\n", False)
        #Ask the user first if they'd like to enter the game or exit. 
        user_ans = (input("Please type enter to see statistics on global coffee for a country and year, or type exit to exit the prompt.\n\t")).upper()
        #Write User's Input
        write_csv("User_History.txt", ("\t" + user_ans+ "\n"), False)
        #If user says exit, break the loop and que the exit message. 
        if (user_ans=="EXIT"):
            break
        #If the user says enter, start the statistics prompt 
        elif (user_ans=='ENTER'):   
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
            #Import the data from the csv files 
            production_list= read_csv("data_files/Coffee_production.csv", False, True)
            export_list= read_csv("data_files/Coffee_export.csv", False, True)
            consumption_list= read_csv("data_files/Coffee_consumption.csv", False, True)
            #Start listing out basic statistics about year and country
            introductory_stats(production_list, export_list,index_Col, user_year, index_Row, countries)
            print(f"{'':=^70s}")
            #Calculate the averages in the specified year and country
            get_mean(production_list,export_list,consumption_list,index_Col, user_year, index_Row, countries)
            print(f"{'':=^70s}")
            #Finally, calculate the maximums globally
            get_max(production_list, export_list, consumption_list, index_Col, countries, user_year)
            print(f"{'':=^70s}")
            #Loop then starts back at the beginning
        #If the user enter's a input that is not exit or enter, summon the error_message function. 
        else:
            Error_Message()
    print(f'You have exited the terminal. Thank you for playing!')
    print(f"{'':=^70s}")
    write_csv("User_History.txt", "END OF FILE; Statistics Portion\n\n", False)