from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status






class PredictView(APIView):
    def post(self, request):
        try:
            data = request.data
            response = requests.post("http://localhost:5000/predict", json=data)
            return Response(response.json())
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
