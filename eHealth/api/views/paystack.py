from  django.conf import settings
from requests.api import head
from rest_framework.views import APIView
from rest_framework.response import Response
import requests


class Paystack(APIView):

  def get(self, response):
    res_url = f'https://api.paystack.co/bank/resolve?account_number=0142651862&bank_code=058'
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {settings.PAYSTACK_PUBLIC_KEY}'}
    res = requests.get(res_url, headers=headers).json()
    print(res)
    return Response(res)


