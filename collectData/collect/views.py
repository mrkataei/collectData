from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import requests



BASE_URL = 'https://api-pub.bitfinex.com'

@api_view(['GET'])
@permission_classes((AllowAny,))
def candle(request):
    try:
        symbol = request.query_params['symbol']
        timeframe = request.query_params['timeframe']

        candles = requests.get(url = BASE_URL + f'/v2/candles/trade:{timeframe}:{symbol}/hist?limit=100').text

    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(candles, status=status.HTTP_200_OK)