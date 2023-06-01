import streamlit as st
import pandas as pd
import requests
# from bokeh.plotting import figure
# from bokeh.models import Col1umnDataSource
# import time

# Fetch data from API
api_url = 'http://13.127.238.203:8000/get-data/'
first_time = True

@st.cache_data(ttl=40)  # Cache the data for 60 seconds
def fetch_data():
    response = requests.get(api_url)
    data = response.json()
    return data

# Title and Subtitle
st.title('Dynamic Data Visualization')
st.subheader('Table of Measurements')

# Create empty placeholders for data and charts
data_placeholder = st.empty()
charts_placeholder = st.empty()

    # Fetch the latest data
data = fetch_data()

#  create refresh data button
if st.button('Refresh Data'):
    data = fetch_data()

# Dropdown for selecting SlaveID
col11 , col12 , col13 = st.columns(3)
col21 , col22 , col23 = st.columns(3)
# selected_slave_id = col11.selectbox('Select SlaveID',[1,2,3,4] , key='slave_id_dropdown')
#  get dlave id and set default value to 1
selected_slave_id = col11.selectbox('Select SlaveID',[1,2,3,4] , key='slave_id_dropdown' , index=0)
#  select parameter and set default value to voltage
selected_parameter = col12.selectbox('Select Parameter',['Voltage','Current','ActivePower','ReactivePower','ApperantPower'] , key='parameter_dropdown' , index=0)
#  button to load data in df
    

# get data for selected date range
from_date = col21.date_input('From Date' , key='from_date')
to_date = col22.date_input('To Date' , key='to_date')
# Convert the data to a DataFrame
rows = []
for item in data:
    if 'voltage' not in item or 'current' not in item or 'active_power' not in item or 'reactive_power' not in item or 'apperant_power' not in item or 'active_energy_export' not in item or 'active_energy_import' not in item:
        continue

    row = {
        # 'Timestamp': item.get('Timestamp'),
        #  Convert timestamp from UTC to IST and convert to YYYY-MM-DD
        'Timestamp': pd.to_datetime(item.get('Timestamp')) + pd.Timedelta(hours=5, minutes=30),
        # 'Timestamp': pd.to_datetime(item.get('Timestamp')) + pd.Timedelta(hours=5, minutes=30),
        'SlaveID': item.get('slaveId'),
        'Voltage_R': float(item['voltage'][0]) if item['voltage'] else None,
        'Voltage_Y': float(item['voltage'][1]) if item['voltage'] and len(item['voltage']) > 1 else None,
        'Voltage_B': float(item['voltage'][2]) if item['voltage'] and len(item['voltage']) > 2 else None,
        'Current_R': float(item['current'][0]) if item['current'] else None,
        'Current_Y': float(item['current'][1]) if item['current'] and len(item['current']) > 1 else None,
        'Current_B': float(item['current'][2]) if item['current'] and len(item['current']) > 2 else None,
        'ActivePower_R': float(item['active_power'][0]) if item['active_power'] else None,
        'ActivePower_Y': float(item['active_power'][1]) if item['active_power'] and len(item['active_power']) > 1 else None,
        'ActivePower_B': float(item['active_power'][2]) if item['active_power'] and len(item['active_power']) > 2 else None,
        'ReactivePower_R': float(item['reactive_power'][0]) if item['reactive_power'] else None,
        'ReactivePower_Y': float(item['reactive_power'][1]) if item['reactive_power'] and len(item['reactive_power']) > 1 else None,
        'ReactivePower_B': float(item['reactive_power'][2]) if item['reactive_power'] and len(item['reactive_power']) > 2 else None,
        'ApparentPower_R': float(item['apperant_power'][0]) if item['apperant_power'] else None,
        'ApparentPower_Y': float(item['apperant_power'][1]) if item['apperant_power'] and len(item['apperant_power']) > 1 else None,
        'ApparentPower_B': float(item['apperant_power'][2]) if item['apperant_power'] and len(item['apperant_power']) > 2 else None,
        'ActiveEnergyExport': float(item['active_energy_export'][0]) if item['active_energy_export'] else None,
        'ActiveEnergyImport': float(item['active_energy_import'][0]) if item['active_energy_import'] else None
    }
    rows.append(row)

# data with y axis as current_r and x axis as timestamp
if col13.button('Load Data') or first_time:
    first_time = False
    df = pd.DataFrame(rows)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df['Date'] = df['Timestamp'].dt.strftime('%Y-%m-%d')
    df.set_index('Timestamp', inplace=True)

    #  filter date column according to selected date range
    # df = df["Date"][from_date:to_date]


    try:
        #  get data for selected slave id
        
        df = df[df['SlaveID'] == selected_slave_id]
        #  get data for selected parameter with R Y B
        selected_parameter_list = []
        for i in ['R','Y','B']:
            selected_parameter_list.append(selected_parameter + '_' + i)

        #  get data for selected parameter
        df = df[selected_parameter_list]

        #  filter data by data range
        # df = df[from_date:to_date]


        #  remove null values
        df = df.dropna()


        st.dataframe(df)

        #  plot data using streamlit
        st.line_chart(df)

    except Exception as e:
        st.error(e)


# plot bar chart for ActiveEnergyExport and ActiveEnergyImport

#  get data for selected slave id

#  sidebar for charts
charts_placeholder = st.sidebar



df = pd.DataFrame(rows)
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df.set_index('Timestamp', inplace=True)


#  get data for selected slave id
df = df[df['SlaveID'] == selected_slave_id]


ActiveEnergyExport = df['ActiveEnergyExport'].sum()
ActiveEnergyImport = df['ActiveEnergyImport'].sum()
print(ActiveEnergyExport)
print(ActiveEnergyImport)

#  plot bar chart for ActiveEnergyExport and ActiveEnergyImport
charts_placeholder.bar_chart({'ActiveEnergyExport':ActiveEnergyExport , 'ActiveEnergyImport':ActiveEnergyImport})

#  plot line chart for ActiveEnergyExport and ActiveEnergyImport
charts_placeholder.line_chart({'ActiveEnergyExport':ActiveEnergyExport , 'ActiveEnergyImport':ActiveEnergyImport})

