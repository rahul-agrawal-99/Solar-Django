from django.shortcuts import render

#  import APIView
from rest_framework.views import APIView
from .utils import *
from .models import *

#  impoer response
from rest_framework.response import Response
from .serializers import SolarDataSerializer

# Create your views here.

class SaveData(APIView):

    def post(self , request):

        try:
            data = request.data
            data = eval(list(data.keys())[0])
            # print("Eval Data : ",data)
            SlaveID = data['SlaveID']
            ReadingData = data['data']


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
        all_data = request.GET.get('all' , None)

        if all_data is None:
            data = SolarData.objects.all().order_by('-Timestamp')[:2]
            
        else:
            data = SolarData.objects.all().order_by('Timestamp')
        serializer = SolarDataSerializer(data , many=True)
        return Response(serializer.data)
