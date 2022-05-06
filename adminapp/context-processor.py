from http.client import HTTPResponse
from django.shortcuts import render , redirect 


def main_context(request):
    if 'permission' in request.session:
        permission = False
        if request.session['permission']['is_admin'] == True:
            permission = True
        return {
            'domain':request.META['HTTP_HOST'],
            'permission':permission
         }  
    else:
        return {
            'domain':request.META['HTTP_HOST'],
            'permission':''
        }     
