from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import joblib
from .forms import ContactModelForm, ResultModelForm, Result2ModelForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'home.html')


@login_required
def predict(request):
    if request.method == "POST":
        form = Result2ModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        raise Exception('Invalid Input')
    else:
        form = Result2ModelForm()
        return render(request, 'predict.html', {'form':form})


def result(request):
    cls = joblib.load('model.sav')
    lis = []

    lis.append(request.POST['age'])
    lis.append(request.POST['sex'])
    lis.append(request.POST['cp'])
    lis.append(request.POST['trestbps'])
    lis.append(request.POST['chol'])
    lis.append(request.POST['fbs'])
    lis.append(request.POST['restecg'])
    lis.append(request.POST['thalach'])
    lis.append(request.POST['exang'])
    lis.append(request.POST['oldpeak'])
    lis.append(request.POST['slope'])
    lis.append(request.POST['ca'])
    lis.append(request.POST['thal'])
    print(lis)

   
    ans = round(cls.predict_proba([lis])[0][1]*100)
    

    return render(request, 'result.html', {'ans':ans})


def about(request):
    return render(request,'about.html')


def contact(request):
    if request.method == "GET":
        form = ContactModelForm()
        return render(request,'contact.html', {'form':form})
    else:   
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            message = form.cleaned_data['description']
            from_email = form.cleaned_data['mail']
            phone = form.cleaned_data['phone']
            message = message+str(phone)
            try:
                send_mail(
                    'Contact us form message',
                    message,
                    
                    from_email,
                    ['dpsystem99@gmail.com'],
                    fail_silently=False,
                )
                
            except Exception as e:
                print(str(e))
            messages.success(request, 'Successfully sent you message to HPS in gmail')
            
            return redirect('home')
            
            
    


