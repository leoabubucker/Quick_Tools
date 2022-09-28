from time import sleep #Sleep Delay
import os #Clear Screen
import concurrent.futures #Threading

#Global Definition For Use Across Program
global user_input
user_input = ""
#Program Functions
def input_listen():
    #Threaded Function to Simultaneously Check User Input 
    global user_input
    user_input = ""
    listening = True;
    while listening:
        if(user_input.lower() == "r"):
            print("Restarting Program...")
            restartProgram(2, 'start')
            return "Restart"

def startProgram():
    #Initial Request for User Input to Direct to Appropriate Subprograms
    global user_input

    tools_list = ['Conversions Program','Slope Calculator ', 'Inverse Calculator','More Tools Coming Soon']
    print("Welcome to the Quick Tools Program.")
    print("At any time, type 'R' to restart the program completely, type 'B' to restart the individual subprogram you are in.")
    user_input = input(f"Which tool do you want to run (respond with the appropriate numeric selector): \n{ [i for i in enumerate_from_1(tools_list)]} ")

    if(user_input == '1'):
        print("Starting Conversion Program")
        restartProgram(2, 'convert')
    elif(user_input == '2'):
        print("Starting Slope Calculator")
        restartProgram(2, 'slope')
    elif(user_input == '3'):
        print("Tool Not Available. \nRestarting Program...")
        restartProgram(2, 'start')
    elif(user_input.lower() == "b"):
        print("Restarting Subprogram")
        restartProgram(2, 'start')
    elif(user_input.lower() != "r"):
        print("Invalid User Input. Please type the appropriate numeric selector for your chosen tool. \nRestarting Program")
        restartProgram(2, 'start')

def conversionProgram():
    #Program to Run Multiple Conversions
    converters_list = ['Base to Base Conversions (i.e binary to decimal)']

    #Conversion Functions

    def base_to_base(init_number, init_base, conv_base):
        #Converts a number from one base to the appropriate number in another base
        num_digits = -1
        ind_digits = []
        mult_digits = []
        decimal_conv = 0
        for i in str(init_number):
            num_digits += 1
            ind_digits.append(int(i))
        for i in ind_digits:
           mult_digits.append(i * (init_base ** num_digits))
           num_digits -=1;
        for i in mult_digits:
            decimal_conv += i;
    
        quotients_list = []
        remainders_list = []
        q = int(decimal_conv / conv_base)
        r = int(decimal_conv % conv_base)
        quotients_list.append(q)
        remainders_list.append(r)

        while q != 0:
            r =  q % conv_base
            q /= conv_base
            quotients_list.append(int(q))
            remainders_list.append(int(r))
    
        conv_factor = 1
        remainder_total = 0
        for  i in remainders_list:
            remainder_total += i * conv_factor
            conv_factor *= 10

        if(conv_base == 10):
            return decimal_conv
        else:
            return remainder_total

    #Program Run
    global user_input
    user_input = input(f"What conversion do you wish to complete. \nCurrent Supported Conversions are: \n{ [i for i in enumerate_from_1(converters_list)]}  \nPlease type the selection number of your preferred conversion.\n")
    if(user_input == '1'):
        print("Warning. This converter only works if the answer remains numeric (i.e 55) not including alpha characters (i.e 1B). Additionally, the number must be a float")
        try:
            init_base = int(input("Please input the base of the number you wish to convert\n"))
            init_number = int(input("Please input the number you wish to convert\n"))
            conv_base = int(input("Please input the base of that you wish to convert to. \n"))
        except ValueError:
            print("Please ensure your number is an integer. \n Restarting Program...")
            restartProgram(2, 'convert')
        print(f" {init_number} (base {init_base} to base {conv_base}: {base_to_base(init_number, init_base, conv_base)}")
    elif(user_input.lower() == "b"):
        print("Restarting Subprogram")
        restartProgram(2, 'convert')
    elif(user_input.lower() != "r"):
        print("Invalid User Input. Please only enter given choices. \nRestarting Program...")
        restartProgram(2, 'convert')

def slopeProgram():
    pointlst = []
    numlst = []
    def calcSlopePoints(y2, y1, x2, x1):
        pointlst.append(y2)
        pointlst.append(y1)
        pointlst.append(x2)
        pointlst.append(x1)
 
        for i in pointlst:
            if(i.lower() == "r"):
                print("Restarting Program...")
                restartProgram(2, 'start')
            elif(i.replace('.', '').replace('-', '').isnumeric() == False):
                print("Invalid user input, please only use integers or decimals. \nRestarting Subprogram...")
                restartProgram(2, 'slope')
            elif(i.count('.') == 0):
                numlst.append(int(i))
            elif(i.count('.') == 1):
                numlst.append(float(i))

        return (numlst[0] - numlst[1]) / (numlst[2] - numlst[3])
    def calcSlopeCoords(coord1, coord2):
        init_coordlst= []
        coordlst = []
        init_coordlst.append(coord1)
        init_coordlst.append(coord2)
        for i in init_coordlst:
          coordv1=  i.replace('(', '')
          coordv2=  coordv1.replace(')', '')
          coordv3 = coordv2.split(", ")
          coordlst.extend(coordv3)

        return calcSlopePoints(coordlst[3], coordlst[1], coordlst[2], coordlst[0])

    global user_input
    user_input = input("Do you want to input \n1. 2 coordinates \n2. The values of y2, y1, x2, and x1?")
    if(user_input == "1"):
        coord1 = input("First coordinate in the following form (x, y): ")
        coord2 = input("Second coordinate in the following form (x, y): ")
        if(coord1.lower() == "r" or coord2.lower() == "r"):
            print("Restarting Program...")
            restartProgram(2, 'start')
        elif(coord1.lower() == "b" or coord2.lower() == "b"):
            print("Restarting Subprogram...")
            restartProgram(2, 'slope')
        else:
            print(f"The slope of your inputted coordinates is: {calcSlopeCoords(coord1, coord2)}")
    elif(user_input == "2"):
        y2 = input("Value of y2: ")
        y1 = input("Value of y1: ")
        x2 = input("Value of x2: ")
        x1 = input("Value of x1: ")
        print(f"The slope of your inputted points is: {calcSlopePoints(y2, y1, x2, x1)}")
    elif(user_input.lower() == "b"):
        print("Restarting Subprogram...")
        restartProgram(2, 'slope')
    elif(user_input.lower() != 'r'):
        print("Please ensure that you only entered the numeric selector for the given choices. \nRestarting Subprogram...")
        restartProgram(2, 'slope')

#General Functions
def clear_screen():
    #Clears Windows 
    if os.name == 'nt':
        _ = os.system('cls')

    #Clears Mac and Windows (os name is 'posix')
    else:
        _ = os.system('clear')

def restartProgram(sleep_time, programName):
    #Restarts the inputted program with an inputted sleep delay
    sleep(sleep_time)
    clear_screen()
    sleep(sleep_time)
    if(programName == 'start'):
        initProgram()
    elif(programName == 'convert'):
        conversionProgram()
    elif(programName == 'slope'):
        slopeProgram()

def enumerate_from_1(lst):
    #Takes an inputted list and enumerates it from 1
   list_enumerated = []
   for index, converter in enumerate(lst):
       list_enumerated.append(f"{index + 1}. {converter}")
   return list_enumerated

def initProgram():
    #Starts threading and then calls the main program 
    with concurrent.futures.ThreadPoolExecutor() as executor:
        f1 = executor.submit(input_listen)
        startProgram()

#Program Start Call
initProgram()
