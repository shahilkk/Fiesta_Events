from django.shortcuts import  redirect,render

def admin_login_required(fun):
    def wrap(request,*args,**kwargs):
        if 'permission' in request.session:
            return fun(request,*args,**kwargs)    
        else:
            return render(request,'login.html') 
            # return redirect('userapp:login')
    return wrap        