from django.shortcuts import render,redirect,reverse

from .models import careers,signups,telephone_tech_support,one_on_one_online_session,video_tech_support,QueryPages,JsonData,Online_Gd_For_Admin,Online_Gd_For_user
from django.conf import settings
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.


def videos(request):
    return render(request,'videos.html')

def about(request):
	return render(request,'about.html')

def signup(request):
    if request.method=="POST":
        username=request.POST.get("username")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        mobile_no=request.POST.get("mobile_no")
        email=request.POST.get("email")
        address=request.POST.get("address")
        country=request.POST.get("country")
        state=request.POST.get("state")
        Postal_code=request.POST.get("Postal_code")
        password=request.POST.get("password")
        cnf_password=request.POST.get("cnf_password")
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username Taken')
            return redirect('/signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email Id Taken')
            return redirect('/signup')
        elif password != cnf_password:
            messages.info(request,'Confirm Password not Match')
            return redirect('/signup')
        else:
            user=User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password)
            user.save()
            user_id=user.id
            data=signups(user_id=user_id,mobile_no=mobile_no,address=address,country=country,state=state,Postal_code=Postal_code)
            data.save()
            #messages.success(request,"Data Save Successfully")
            return redirect('/Welcome')

    else:
        return render(request,'signup.html')


def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credential')
            return redirect('/signin')
    else:
        return render(request,'signin.html')

def services(request):
    return render(request,'services.html')



def Work_withuss(request):
    if request.method=="POST":
        expert_name=request.POST.get("expert_name")
        expert_email=request.POST.get("expert_email")
        expert_phone_number=request.POST.get("expert_phone_number")
        resume_url=request.FILES['resume_url']

        #fs = FileSystemStorage(location='/media/resume/')
        #filename = fs.save(resume.name, resume)
        #resume_url = fs.url(filename)
        background=request.FILES['background']
        #background=request.FILES['background']
        #fs1 = FileSystemStorage(location='/media/background/')
        #filename1 = fs1.save(backgrond.name, background)
        #background_url = fs1.url(filename1)
        subject=request.POST.get("subject")
        description=request.POST.get("description")
        data=careers(expert_name=expert_name,expert_email=expert_email,expert_phone_number=expert_phone_number,resume_url=resume_url,background=background,subject=subject,description=description)
        data.save()
        return redirect("/")
    else:
        return render(request,'work_with_us.html')

def tech_support(request):
    if request.method=="POST":
        query=request.POST.get("query")
        slot=request.POST.get("slot")
        user_id = request.user.id
        print("user_id eygfygfhsgvdjhfdvgfhdvhjsdf",user_id)
        if user_id==None:
            messages.info(request,'Please Login First')
            return redirect('/tech_support')
        else:
            data=telephone_tech_support(user_id=user_id,slot=slot,query=query)
            data.save()
            messages.success(request,"Data Save Successfully")
            return redirect('/tech_support')
    else:
        return render(request,'services.html')
def video_tech(request):
    if request.method=="POST":
        query=request.POST.get("query")
        slot=request.POST.get("slot")
        user_id = request.user.id
        print("user_id eygfygfhsgvdjhfdvgfhdvhjsdf",user_id)
        if user_id==None:
            messages.info(request,'Please Login First')
            return redirect('/tech_support')
        else:
            data=video_tech_support(user_id=user_id,slot=slot,query=query)
            data.save()
            messages.success(request,"Data Save Successfully")
            return redirect('/tech_support')
def one_on_one_online(request):
    if request.method=="POST":
        query=request.POST.get("query")
        slot=request.POST.get("slot")
        user_id = request.user.id
        print("user_id eygfygfhsgvdjhfdvgfhdvhjsdf",user_id)
        if user_id==None:
            messages.info(request,'Please Login First')
            return redirect('/tech_support')
        else:
            data=one_on_one_online_session(user_id=user_id,slot=slot,query=query)
            data.save()
            messages.success(request,"Data Save Successfully")
            return redirect('/tech_support')
def online_g_d(request):
    if request.method=='POST':
        select_date_time=request.POST['select_date_time']
        user_id = request.user.id
        if user_id==None:
            messages.info(request,'Please Login First')
            return redirect('/online_g_d')
        else:
            data=Online_Gd_For_user(user_id=user_id,select_date_time=select_date_time)
            data.save()
            param = {'data': data}

            return redirect('/GD_success')
            '''messages.success(request,"Book Slot Successfully")
            return redirect('/online_g_d')'''
    else:
        data=Online_Gd_For_Admin.objects.all()
        param={'data':data}
        return render(request,'online_g_d.html',param)
def welcome(request):
    return render(request,"Welcome.html")

def GD_success(request):
    return render(request,"GD_success.html")

def create_query_page(request):
    if request.method=='POST':
        question=request.POST['question']
        answer_heading=request.POST['answer_heading']
        youtube_link=request.POST['youtube_link']
        article_link=request.POST['article_link']
        data=QueryPages(question=question,answer_heading=answer_heading,youtube_link=youtube_link,article_link=article_link)
        data.save()
        messages.success(request,"Data Save Successfully")
        return redirect("/create_query_page")
    else:
        return render(request,'create_query_page.html')

def logout(request):
    auth.logout(request)
    return redirect('/signin')
def home(request):
    return render(request,'home.html')
def search_view(request):
    queryString=request.GET['q']
    show=QueryPages.objects.filter(question__contains=queryString)
    return render(request,'home.html',{'show':show})





from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm



def process_payment(request):
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '200',
        'item_name': 'chandra',
        'invoice': '1',
        'notify_url': 'http://{}{}'.format("127.0.0.1:8000",
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format("127.0.0.1:8000",
                                           reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format("127.0.0.1:8000",
                                              reverse('payment_canceled')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    print("kjfvlfbdvkjdfbvkfdhvbfkhvbfdh",form)
    print("jkdsfghsdbfkdhfsjhdfd",paypal_dict)
    return render(request, 'process_payment.html', {'form': form})

def payment_done(request):
    return render(request, 'payment_done.html')


def payment_canceled(request):
    return render(request, 'payment_cancelled.html')
import razorpay
import json
import requests
razorpay_client = razorpay.Client(auth=("rzp_test_xcWqQEkxDTJU5o", "X34ywdQlXJNYTw58OWdxaLxx"))
from django.http import HttpResponse

def team(request):
    return render(request,'team.html')
def pay2(request):
    return render(request,'payment.html')
def pay1(request):
    try:
        if request.method=='POST':
            amount = 5100
            payment_id = request.POST['razorpay_payment_id']
            razorpay_client.payment.capture(payment_id, amount)
            all_data=json.dumps(razorpay_client.payment.fetch(payment_id))
            data=JsonData(all_data=all_data)
            data.save()
            return redirect('/signup')
    except:
        pass
















