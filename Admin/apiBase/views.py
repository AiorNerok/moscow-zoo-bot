from rest_framework.decorators import api_view

from django.shortcuts import render

# Create your views here.


@api_view(['Get'])
def Some():
    return {
        'ping': 'pong'
    }