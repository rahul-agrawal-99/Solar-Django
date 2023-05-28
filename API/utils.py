import itertools
from .serializers import SolarDataSerializer


# Voltage
# Current
# Active Power 
# Reactive power
# Apparent power 
# Active current
# Reactive current

DB_COLUMNS = ["voltage" , "current" , "active_power" , "reactive_power"  , "apperant_power" , "active_energy_export" , "active_energy_import" ]

CURRENT_DATA1 = itertools.cycle(DB_COLUMNS.copy())
CURRENT_DATA2 = itertools.cycle(DB_COLUMNS.copy())
CURRENT_DATA3 = itertools.cycle(DB_COLUMNS.copy())
CURRENT_DATA4 = itertools.cycle(DB_COLUMNS.copy())


temp_data_2 = []
temp_data_3 = []
temp_data_4 = []
temp_data_1 = []
data_lock_1 = True
data_lock_2 = True
data_lock_3 = True
data_lock_4 = True


def data_for_ID_1(data):
    global data_lock_1
    if len(data) == 3 and any([True for i in data if (i > 220  and i < 260) ]) and data_lock_1:
        print("Voltage Data")
        data_lock_1 = False

    if not data_lock_1:
        # print("Data for 1: ",data)
        parameter = next(CURRENT_DATA1)
        # print("Current Temp Data : ",temp_data_1)
        if parameter == "voltage":
            if temp_data_1:
                save_to_db(temp_data_1 , 1)
                # print("Clearing Data")
                temp_data_1.clear()
            temp_data_1.extend([data])
        else:
            temp_data_1.append(data)
    

def data_for_ID_2(data):
    global data_lock_2
    if len(data) == 3 and any([True for i in data if (i > 220  and i < 260) ]) and data_lock_2:
        # print("Voltage Data")
        data_lock_2 = False

    if not data_lock_2:
        # print("Data for 2: ",data)
        parameter = next(CURRENT_DATA2)
        # print("Current Temp Data : ",temp_data_2)
        if parameter == "voltage":
            if temp_data_2:
                save_to_db(temp_data_2 , 2)
                # print("Clearing Data")
                temp_data_2.clear()
            temp_data_2.extend([data])
        else:
            temp_data_2.append(data)

def data_for_ID_3(data):
    global data_lock_3
    if len(data) == 3 and any([True for i in data if (i > 220  and i < 260) ]) and data_lock_3:
        # print("Voltage Data")
        data_lock_3 = False

    if not data_lock_3:
        # print("Data for 3: ",data)
        parameter = next(CURRENT_DATA3)
        # print("Current Temp Data : ",temp_data_3)
        if parameter == "voltage":
            if temp_data_3:
                save_to_db(temp_data_3 , 3)
                # print("Clearing Data")
                temp_data_3.clear()
            temp_data_3.extend([data])
        else:
            temp_data_3.append(data)


def data_for_ID_4(data):
    global data_lock_4
    if len(data) == 3 and any([True for i in data if (i > 220  and i < 260) ]) and data_lock_4:
        # print("Voltage Data")
        data_lock_4 = False

    if not data_lock_4:
        # print("Data for 4: ",data)
        parameter = next(CURRENT_DATA4)
        # print("Current Temp Data : ",temp_data_4)
        if parameter == "voltage":
            if temp_data_4:
                save_to_db(temp_data_4 , 4)
                # print("Clearing Data")
                temp_data_4.clear()
            temp_data_4.extend([data])
        else:
            temp_data_4.append(data)

def save_to_db(data , slaveId):
    # print("writing to database" , data)
    # print("length of data : ",len(data))

    data_dict = {}
    data_dict["slaveId"] = slaveId

    for index , value in enumerate(data):
        data_dict[DB_COLUMNS[index]] = value

    print("Data Dict : ",data_dict)
    try:
        serializer = SolarDataSerializer(data=data_dict)
        if serializer.is_valid():
            serializer.save()
            print("Data Saved Successfully")
        else:
            print("Error While saving with serializer  As : ",serializer.errors)
    except Exception as e:
        print("Exception Error  While Writing As : ",e)
        pass
