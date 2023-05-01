import itertools
from .serializers import SolarDataSerializer

# Date,Time,ModbusID,voltage,current,active_power,power_factor,apperant_power,active_energy


DB_COLUMNS = ["voltage" , "current" , "active_power" , "power_factor" , "apperant_power" , "active_energy" ]

CURRENT_DATA1 = itertools.cycle(["voltage" , "current" , "active_power" , "power_factor" , "apperant_power" , "active_energy" ])
# CURRENT_DATA1 = itertools.cycle(["voltage" , "current" , "frequency" ])
CURRENT_DATA2 = itertools.cycle(["voltage" , "current" , "active_power" , "power_factor" , "apperant_power" , "active_energy" ])
CURRENT_DATA3 = itertools.cycle(["voltage" , "current" , "active_power" , "power_factor" , "apperant_power" , "active_energy" ])
CURRENT_DATA4 = itertools.cycle(["voltage" , "current" , "active_power" , "power_factor" , "apperant_power" , "active_energy" ])

temp_data_2 = []
temp_data_3 = []
temp_data_4 = []
temp_data_1 = []
data_lock_1 = True

def data_for_ID_1(data):
    global data_lock_1
    # [254.781586, 0.13126, 0.08446]
    #  if len of data is 3 and any of value in data in greater than 1000 then it is voltage data
    if len(data) == 3 and any([True for i in data if i > 230]) and data_lock_1:
        #  it is voltage data
        print("Voltage Data")
        data_lock_1 = False

    if not data_lock_1:
        print("Data for 1: ",data)
        parameter = next(CURRENT_DATA1)
        print("Current Temp Data : ",temp_data_1)
        if parameter == "voltage":
            if temp_data_1:
                save_to_db(temp_data_1)
                print("Clearing Data")
                temp_data_1.clear()
            temp_data_1.extend([data])
        else:
            temp_data_1.append(data)
    

def data_for_ID_2(data):
    parameter = next(CURRENT_DATA2)
    if parameter == "voltage":
        if temp_data_2:
            save_to_db(temp_data_2)
            temp_data_2.clear()
        temp_data_2.extend(data)
    else:
        temp_data_2.append(data)


    

def data_for_ID_3(data):
    parameter = next(CURRENT_DATA3)
    if parameter == "voltage":
        if temp_data_3:
            save_to_db(temp_data_3)
            temp_data_3.clear()
        temp_data_3.extend(data)
    else:
        temp_data_3.append(data)


def data_for_ID_4(data):
    parameter = next(CURRENT_DATA4)
    if parameter == "voltage":
        if temp_data_4:
            save_to_db(temp_data_4)
            temp_data_4.clear()
        temp_data_4.extend(data)
    else:
        temp_data_4.append(data)


def save_to_db(data):
    print("writing to database" , data)
    # creating dict for saving data using DB_COLUMNS 

    data_dict = {}

    for index , value in enumerate(data):
        data_dict[DB_COLUMNS[index]] = value


    # data_dict = {
    #     "voltage" : data[0],
    #     "current" : str(data[1]),
    #     # "frequency" : str(data[2]),
    #     #  "power_factor" : str(data[3][0]),
    #     #  "apperant_power" : str(data[4][0]),
    #     #  "active_energy" : str(data[5][0]),
    # }
    print("Data Dict : ",data_dict)
    try:
        serializer = SolarDataSerializer(data=data_dict)
        if serializer.is_valid():
            serializer.save()
            print("Data Saved Successfully")
        else:
            print("Error While saving  As : ",serializer.errors)
    except Exception as e:
        print("Error While Writing As : ",e)
        pass
