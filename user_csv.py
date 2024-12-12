# user_csv.py
# ENDG 233 F24
# STUDENT NAME(S): Amar Kaber, Sahana Santhanam
# GROUP NAME: Group 17 
# A terminal-based data analysis and visualization program in Python.
# You must follow the specifications provided in the project description.
# Remember to include docstrings and comments throughout your code.
import numpy as np 

def read_csv (file_name, include_headers, np_array):
    '''
     Reads data from the CSV file and converts it into a numpy array optionally including headers

    Parameters:
        file_name (str): name of the CSV file
        include_headers (bool): if True, the first line of file is included. 
                                If False, first line is not included
        np_array (bool): if True, CSV file will be converted into a numpy array. 
                         If False, it will be a python 2D list.
    
    '''
    #Initializing the variables.  
    csv_master_list = []
    sub_list=[]
    start = 0
    #Open the file and the reader. 
    file = open (file_name, "r")
    #First read all the lines from the file and store them. 
    data = file.readlines()
    #Check if we need headers. If we don't; we will start from the second line of the file. 
    if (include_headers==False):
        start = 1
    #Organize the data into a 2D List starting from whichever declared line of the file
    for line in data[start:]:
        #Split the line into a list seperated by the commas. 
        sub_list = line.split(",")
        #If the values are numbers, they will be converted into integers to prepare it to convert to a numpy array
        if np_array == True:
            for i in range(len(sub_list)):
                isNumber = sub_list[i].isdigit()
                #If a string is detected, it is most likely the country label or the label 
                #for type of coffee bean exported. The values will be changed to 0 since the strings have no effect on operations. 
                if isNumber==False:
                    sub_list[i]=0
            #Cast the entire list into floats 
            sub_list = [float(data) for data in sub_list]
        #Append the final line list into the 2D master list
        csv_master_list.append(sub_list)
    #Convert this into an numpy array for ease of operations if desired
    if np_array == True: 
        csv_master_list = np.array(csv_master_list)
    #Return the final array
    return csv_master_list

def write_csv (file_name, data, overwrite):
    '''
    Takes data given and stores it within a CSV file, either appending or overwriting to an exisitng file.

    Parameters:
        file_name (str): name of file in which user history will be stored
        data: 2D list or other form of data
        overwrite (bool): if True, file will be overwritten by new data. If False, data will be appended onto previous data.
        
    ''' 
    #Lets create an empty string that will store the casted list. 
    file_line = ""
    #Open the file and the writer, but in append mode so it adds to the file line by line. 
    file = open(file_name, "a")
    #If the file needs to be reset and encoded with new data, then empty the file
    if (overwrite == True):
        file.truncate(0)
    #Append every row in the 2D List / or of the data given (can be single list) 
    for line in data:
        #Convert each list row into a string seperated by commas 
        file_line = ','.join(line)
        #Write into the file, continue to the next list row. 
        file.write(file_line)
    #Close the writer
    file.close()

    