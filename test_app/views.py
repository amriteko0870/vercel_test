from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def index(request):
    res = {
            'status':True,
            'message':'Success'
          }
    return Response(res)