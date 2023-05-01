from django.shortcuts import render

#  import APIView
from rest_framework.views import APIView
from .utils import *

#  impoer response
from rest_framework.response import Response

# Create your views here.

class SaveData(APIView):

    def post(self , request):

        try:
            #  d = [('{"TS" : "1669442071", "D": "26/11/2022 05:54:31", "SlaveID": "1","voltage": "[239.590286,238.094696,240.652374]"}', '')]
            data = request.data
            # print("Eval Data : ",data)
            data = eval(list(data.keys())[0])
            print("Eval Data : ",data)
            SlaveID = data['SlaveID']
            ReadingData = data['data']


            if SlaveID == "1":
                print("Modbus ID 1 : ",ReadingData)
                data_for_ID_1(ReadingData)
            elif SlaveID == "2":
                print("Modbus ID 2 : ",ReadingData)
                data_for_ID_2(ReadingData)
            elif SlaveID == "3":
                print("Modbus ID 3 : ",ReadingData)
                data_for_ID_3(ReadingData)
            elif SlaveID == "4":
                print("Modbus ID 4 : ",ReadingData)
                data_for_ID_4(ReadingData)
            else:
                print("Invalid Modbus ID")
                return Response("Invalid Modbus ID")
                
            return Response("OK")
        
        except Exception as e:
            print("Error While Writing As : ",e)
            return Response("Error As : " + str(e))
    


