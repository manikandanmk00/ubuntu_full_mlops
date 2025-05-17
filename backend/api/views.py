from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PredictView(APIView):
    def post(self, request):
        data = request.data
        # Call FastAPI service
        try:
            res = requests.post("http://fastapi:8000/predict", json=data)
            res.raise_for_status()
            prediction = res.json().get("predicted_price")
            return Response({"predicted_price": prediction})
        except requests.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
