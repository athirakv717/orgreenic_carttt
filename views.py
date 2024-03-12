from django.shortcuts import render,redirect
from django.views.generic import View, CreateView,FormView,TemplateView
from django.contrib.auth.models import AbstractUser
from app1.forms import SignUpForm,SignInForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login
from django.contrib import messages
from app1.models import Products,Categories,Cart
# Create your views here.
class Home(TemplateView):
     template_name="home.html"
     def get_context_data(self,**kwargs):
        # context data is used to retrieve data from database to view in template ie categories,products and images already added in database to shown in home page
        context=super().get_context_data(**kwargs)
        all_products=Products.objects.all()
        context["products"]=all_products
        return context


class SignUpView(CreateView):
    template_name='register.html'
    form_class=SignUpForm
    model=AbstractUser
    success_url=reverse_lazy('login') 



class SignInView(FormView):
    template_name='login.html'
    form_class=SignInForm 
    def post(self,request,*args,**kwargs):
        form=SignInForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get('username')
            passw=form.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=passw)
            if user:
                login(request,user)
                msg="login sucessful"
                messages.success(request,msg)
                return redirect("home")
            
            else:
              msg='invalid credentials'
              messages.error(request,msg)      
              return render(request,'login.html')    

class Seasonalfruits(TemplateView):     
   template_name='seasonalfruits.html'  

   def get_context_data(self, **kwargs): 
       context=super().get_context_data(**kwargs)
       all_products=Products.objects.all()
       context["products"]=all_products
       return context

class Importedfruits(TemplateView):     
   template_name='importedfruits.html'  

   def get_context_data(self, **kwargs): 
       context=super().get_context_data(**kwargs)
       all_products=Products.objects.all()
       context["products"]=all_products
       return context

class Tropicalfruits(TemplateView):     
   template_name='tropicalfruits.html'  

   def get_context_data(self, **kwargs): 
       context=super().get_context_data(**kwargs)
       all_products=Products.objects.all()
       context["products"]=all_products
       return context

class Dryfruits(TemplateView):     
   template_name='dryfruits.html'  

   def get_context_data(self, **kwargs): 
       context=super().get_context_data(**kwargs)
       all_products=Products.objects.all()
       context["products"]=all_products
       return context       


class Citrusfruits(TemplateView):     
   template_name='citrusfruits.html'  

   def get_context_data(self, **kwargs): 
       context=super().get_context_data(**kwargs)
       all_products=Products.objects.all()
       context["products"]=all_products
       return context  

class Berries(TemplateView):     
   template_name='berries.html'  

   def get_context_data(self, **kwargs): 
       context=super().get_context_data(**kwargs)
       all_products=Products.objects.all()
       context["products"]=all_products
       return context  

class Melons(TemplateView):     
   template_name='melons.html'  

   def get_context_data(self, **kwargs): 
       context=super().get_context_data(**kwargs)
       all_products=Products.objects.all()
       context["products"]=all_products
       return context        

class Leafy(TemplateView):     
   template_name='leafy.html'  

   def get_context_data(self, **kwargs): 
       context=super().get_context_data(**kwargs)
       all_products=Products.objects.all()
       context["products"]=all_products
       return context          
   

class Root(TemplateView):     
   template_name='root.html'  

   def get_context_data(self, **kwargs): 
       context=super().get_context_data(**kwargs)
       all_products=Products.objects.all()
       context["products"]=all_products
       return context     


class Pod(TemplateView):     
   template_name='pod.html'  

   def get_context_data(self, **kwargs): 
       context=super().get_context_data(**kwargs)
       all_products=Products.objects.all()
       context["products"]=all_products
       return context      
   
class Indoor(TemplateView):     
   template_name='indoorplants.html'  

   def get_context_data(self, **kwargs): 
       context=super().get_context_data(**kwargs)
       all_products=Products.objects.all()
       context["products"]=all_products
       return context    

class Cactus(TemplateView):     
   template_name='cactus.html'  

   def get_context_data(self, **kwargs): 
       context=super().get_context_data(**kwargs)
       all_products=Products.objects.all()
       context["products"]=all_products
       return context 

class Medicinal(TemplateView):     
   template_name='medicinalplants.html'  

   def get_context_data(self, **kwargs): 
       context=super().get_context_data(**kwargs)
       all_products=Products.objects.all()
       context["products"]=all_products
       return context            

class Fruitplants(TemplateView):     
   template_name='fruitplants.html'  

   def get_context_data(self, **kwargs): 
       context=super().get_context_data(**kwargs)
       all_products=Products.objects.all()
       context["products"]=all_products
       return context          

class Ornamentalplants(TemplateView):     
   template_name='ornamental.html'  

   def get_context_data(self, **kwargs): 
       context=super().get_context_data(**kwargs)
       all_products=Products.objects.all()
       context["products"]=all_products
       return context    

class Floweringplants(TemplateView):     
   template_name='flowerplant.html'  

   def get_context_data(self, **kwargs): 
       context=super().get_context_data(**kwargs)
       all_products=Products.objects.all()
       context["products"]=all_products
       return context         
   
class Organicfertiliser(TemplateView):     
   template_name='fertilisers.html'  

   def get_context_data(self, **kwargs): 
       context=super().get_context_data(**kwargs)
       all_products=Products.objects.all()
       context["products"]=all_products
       return context        
   

class Cocopeat(TemplateView):
    template_name='cocopeat.html'


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        all_products=Products.objects.all()
        context['products']=all_products
        return context