from django.shortcuts import render

#  import APIView
from rest_framework.views import APIView
from .utils import *
from .models import *

#  impoer response
from rest_framework.response import Response
from .serializers import SolarDataSerializer
import datetime

# Create your views here.

class SaveData(APIView):

    def post(self , request):
        # print("Request Data : ",request.data["data"])

        try:
            data = request.data
            data = eval(list(data.keys())[0])
            # print("Eval Data : ",data)
            SlaveID = data['SlaveID']
            ReadingData = data['data']
            print("SlaveID : ",SlaveID)
            print("ReadingData : ",ReadingData)
            print("-"*30)


            if SlaveID == "1":
                data_for_ID_1(ReadingData)
            elif SlaveID == "2":
                data_for_ID_2(ReadingData)
            elif SlaveID == "3":
                data_for_ID_3(ReadingData)
            elif SlaveID == "4":
                data_for_ID_4(ReadingData)
            else:
                print("Invalid SlaveID")
                return Response("Invalid SlaveID")
                
            return Response("OK")
        
        except Exception as e:
            print("Error While Writing As : ",e)
            return Response("Error As : " + str(e))
    

    def get(self , request):
        from_date = request.GET.get('fromDate' , None)
        # print(datetime.datetime.now())
        to_date = request.GET.get('toDate' , None)
        slaveID = request.GET.get('slaveID' , None)

        if slaveID:
            data = SolarData.objects.filter(slaveId=slaveID)
        else:
            data = SolarData.objects.all()

        try:
            if from_date:
                from_date = datetime.datetime.strptime(from_date , "%d-%m-%Y")
                if to_date is None:
                    to_date = datetime.datetime.now().date()
                else:
                    to_date = datetime.datetime.strptime(to_date , "%d-%m-%Y %H:%M:%S")
                data = data.filter(Timestamp__gte=from_date , Timestamp__lte=to_date).order_by('-Timestamp')[:100]
                # data = SolarData.objects.filter(Timestamp__gte=from_date , Timestamp__lte=to_date).order_by('-Timestamp')[:1000]
            else:
                data = data.order_by('-Timestamp')[:1000]
                data = SolarData.objects.all().order_by('-Timestamp')[:100]
            serializer = SolarDataSerializer(data , many=True)
            return Response(serializer.data)
        
        except Exception as e:
            print("Error While Reading As : ",e)
            return Response("Error As : " + str(e))
