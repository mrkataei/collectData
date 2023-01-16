from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status



@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def candle(request):
    try:
        user = "hello world!"
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    return Response(user, status=status.HTTP_200_OK)