from django.shortcuts import  redirect

def admin_login_required(fun):
    def wrap(request,*args,**kwargs):
        if 'permission' in request.session:
            return fun(request,*args,**kwargs)    
        else:
            return redirect('/user/login')
    return wrap        