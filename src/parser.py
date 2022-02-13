# Parser.py file 
import database 
import shlex

def main():
    data= {
        'cities': {'fields' : {'lat', 'lng', 'population'},
                    'values' : {'Abuja','Ahmadabad','Alexandria','Amsterdam','Ankara','Atlanta','Bangkok','Barcelona',
                                'Beijing','Belo Horizonte','Bengaluru', 'Berlin', 'Bern', 'Bloemfontein', 'Boston',
                                'Brasilia', 'Brussels', 'Buenos Aires', 'Cairo', 'Canberra', 'Cape Town', 'Chengdu',
                                'Chennai', 'Chicago', 'Chittagong', 'Chongqing', 'Copenhagen', 'Dallas', 'Delhi',
                                'Dhaka', 'Dongguan', 'Dublin', 'Guadalajara', 'Guangzhou', 'Hanoi', 'Haora', 'Hechi',
                                'Helsinki', 'Ho Chi Minh City', 'Houston', 'Hyderabad', 'Istanbul', 'Jakarta',
                                'Jerusalem', 'Kolkata', 'Kuala Lumpur', 'Lagos', 'London', 'Los Angeles', 'Madrid',
                                'Manila', 'Melbourne', 'Mexico City', 'Miami', 'Moscow', 'Mumbai', 'New Delhi', 
                                'New York', 'Oslo', 'Ottawa', 'Paris', 'Philadelphia', 'Phoenix', 'Porto Alegre',
                                'Pretoria', 'Pune', 'Rio de Janeiro', 'Riyadh', 'Rome', 'Saint Petersburg', 'Sao Paulo',
                                'Seoul', 'Shanghai', 'Shenyang', 'Shenzhen', 'Stockholm', 'Surat', 'Sydney', 'The Hague',
                                'Tianjin', 'Toronto', 'Vienna', 'Warsaw', 'Washington', 'Wuhan', "Xi'an"}},

        'countries' : {'fields': {'capital', 'population', 'ubanPop', 'worldShare'}, 
                        'values' : {'Argentina', 'Australia', 'Austria', 'Bangladesh', 'Belgium', 'Brazil', 'Canada', 
                                    'China', 'Denmark', 'Egypt', 'Finland', 'France', 'Germany', 'India', 'Indonesia', 
                                    'Ireland', 'Israel', 'Italy', 'Malaysia', 'Mexico', 'Netherlands', 'Nigeria', 'Norway', 
                                    'Philippines', 'Poland', 'Russia', 'Saudi Arabia', 'South Africa', 'South Korea', 'Spain', 
                                    'Sweden', 'Switzerland', 'Thailand', 'Turkey', 'United Kingdom', 'United States', 'Vietnam'}},
        'many' : {'fields' : {'how'},
                  'values' : {'cities', 'countries'}}
    }
    
    get_input(data)
    #print(make_query("cities", "population", "New York"))

def check_table(data, vals):
    ### Check if table requested is valid
    valid = False
    for i in data:
        if vals[1].lower() == i.lower(): valid = True

    if (not valid):
        print("Please enter your field request by using one of the following fields: \n")
        for i in data:
            print('----: ' + i) 

    return valid

def check_field(data, vals):
    ### Check if field is in table
    valid = False
    for i in data[vals[1].lower()]['fields']:
        if vals[0].lower() == i.lower(): valid = True

    if (not valid):
        print("Please enter your dataset request by using one of the following datasets: \n")
        for i in data[vals[1].lower()]['fields']:
            print('----: ' + i)
        
    return valid

def check_request(data, vals):
    ### Check if value is in table
    valid = False
    for i in data[vals[1].lower()]['values']:
        if vals[2].lower() == i.lower(): valid = True

    if (not valid):
        print("Please enter your request by using one of the following values: \n")

        ### Print out all possible values for that table request by first letter in alphabetical order
        char_val = ord('a')
        while char_val <= ord('z'):
            print('--' + chr(char_val).upper() + '--: ', end="")
            for i in data[vals[1].lower()]['values']:
                if ord(i[0].lower()) == char_val:
                    print(i, end=", ")
            print('')
            char_val += 1

    return valid

def get_input(data):
    cont = True
    print('To exit the program, enter "exit()"')
    while (cont):
        request = input('> ')

        if (request == "load_data()") :
            database.db.load_data()
        
        ### Help / Manual
        if (request == "help()" ): 
            print ("Help Manual")
            print ("For cities, commands include: population, lat, and lng")
            print ("For countries, commands include: capital, population, urbanPop, and worldShare")
            print ("Example command: lng cities 'Boston' OR capital countries 'Australia'")
            print ("Other commands include: load_data(), how many [cities OR countries], or exit() which will quit the program.")
            request = input('> ')

        ### See if User wants to exit
        if ( request == "exit()" ): cont = False

        ### Continue if they did not enter exit command
        if cont:
            ### Split the input on spaces, using quotes to allow for multi-word input
            vals = []
            try:
                vals = shlex.split(request)
            except Exception:
                pass
            ### Make sure input follows designed format
            if (len(vals) != 3):
                print('Please enter your request in the format [ FIELD TABLE "datapoint" ]\n'
                        + 'an example query is [ population cities "New York" ]')
                continue
            
            if (not check_table(data, vals)) : continue
            if (not check_field(data, vals)) : continue
            if (not check_request(data, vals)) : continue

            table = vals[1]; field = vals[0]; request = vals[2]

            output = make_query(table, field, request)
            ## Output return is a list of tuples, so print the first item in the first element of return.
            print(output[0][0])

                   
def make_query(table, field, request):
    ### Code to convert the inputs to a query

    ### TODO: Adjust the query line so that it wil return the value of the specific choice
    if (table == 'cities'):
        query = 'SELECT ' + field + ' FROM '  + table  + ' WHERE city LIKE "'+ request + '"'
    elif (table == 'countries'):
        query = 'SELECT ' + field + ' FROM ' + table + ' WHERE country LIKE "'+ request + '"'
    else: 
        query = 'SELECT COUNT(1) FROM ' + request


    return database.db.return_Data(query)


main()
