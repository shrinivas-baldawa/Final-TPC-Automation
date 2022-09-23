from django.shortcuts import render, redirect
from .models import Companies, Placements, Students, Bulletin
from .forms import StudentForm, PlacementForm, CompanyForm, BulletinForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import pandas as pd
from django.core.paginator import Paginator
from django.views.generic import View, ListView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from django.views.decorators.csrf import csrf_protect

# Create your views here.


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard/index.html')

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format = None):

        df1 = pd.read_excel('media/Companies.xlsx')
        # df2 = pd.read_excel('media/Placements.xlsx')

        labels = df1['Company']
        chartLabel = "Company Salaries"
        chartdata = df1['Salary']

        data = {
            "labels":labels,
            "chartLabel":chartLabel,
            "chartdata":chartdata,
        }
        return Response(data)

@login_required(login_url='user-login')
def index(request):
    placements = Placements.objects.all()
    placement_count = placements.count()
    students = Students.objects.all()
    student_count = students.count()
    companies = Companies.objects.all()
    company_count = companies.count()

    lst = []

    data = Bulletin.objects.all()

    p = Paginator(data,50)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)

    context = {
        'placement_count': placement_count,
        'student_count': student_count,
        'company_count': company_count,
        'page_obj': page_obj,
    }

    for column in lst:
        _, created = Bulletin.objects.update_or_create(
            notice = column[0],
        )

    return render(request, 'dashboard/index.html', context)


login_required(login_url='user-login')
def student(request):
    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Student has been added')
            return redirect('dashboard-students')
    else:
        form = StudentForm()


    df = pd.read_excel('media/Students.xlsx')
    lst = []

    # for i in range(len(df)):
    #     lst.append(df.iloc[i])

    data = Students.objects.all()

    p = Paginator(data,50)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)

    prompt = {
        'page_obj': page_obj,
        'form': form
        }

    for column in lst:
        _, created = Students.objects.update_or_create(
            prn = column[0],
            name = column[1],
            branch = column[2],
            dob = column[3],
            email_id1 = column[4],
            email_id2 = column[5],
            phone1 = column[6],
            phone2 = column[7],
            address = column[8],
            tenth_board = column[9],
            tenth_perc = column[10],
            tenth_year = column[11],
            twelth_board = column[12],
            twelth_perc = column[13],
            twelth_year =  column[14],
            diploma_board = column[15],
            diploma_perc = column[16],
            diploma_year = column[17],
            sem1 = column[18],
            sem2 = column[19],
            sem3 = column[20],
            sem4 = column[21],
            sem5 = column[22],
            sem6 = column[23],
            cgpi = column[24],
            perc = column[25],
            live_kts = column[26],
            dead_kts = column[27],
            choice =  column[28],
        )

    return render(request, 'dashboard/students.html', prompt)


login_required(login_url='user-login')
def placement(request):
    if request.method == 'POST':
        form = PlacementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Student has been added')
            return redirect('dashboard-placements')
    else:
        form = PlacementForm()

    #START FROM HERE
    df = pd.read_excel('media/Placements.xlsx')
    lst = []

    for i in range(len(df)):
        lst.append(df.iloc[i])

    data = Placements.objects.all()

    p = Paginator(data,50)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)

    prompt = {
        # 'students': data,
        'page_obj': page_obj,
        'form': form
        }

    for column in lst:
        _, created = Placements.objects.update_or_create(
            prn = column[0],
            name = column[1],
            offer1 = column[2],
            offer2 = column[3],
            offer3 = column[4],
            batch = column[5]
        )
    
    return render(request, 'dashboard/placements.html', prompt)


login_required(login_url='user-login')
def company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Company has been added')
            return redirect('dashboard-companies')
    else:
        form = CompanyForm()

    #START FROM HERE
    df = pd.read_excel('media/Companies.xlsx')
    lst = []

    for i in range(len(df)):
        lst.append(df.iloc[i])

    data = Companies.objects.all()

    p = Paginator(data,50)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)

    prompt = {
        # 'students': data,
        'page_obj': page_obj,
        'form': form
        }

    for column in lst:
        _, created = Companies.objects.update_or_create(
            company = column[0],
            salary = column[1]
        )
    
    return render(request, 'dashboard/companies.html', prompt)


login_required(login_url='user-login')
def bulletin(request):
    if request.method == 'POST':
        form = BulletinForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Notice has been added')
            return redirect('dashboard-bulletin')
    else:
        form = BulletinForm()

    #START FROM HERE
    lst = []

    data = Bulletin.objects.all()

    p = Paginator(data,50)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)

    prompt = {
        # 'students': data,
        'page_obj': page_obj,
        'form': form
        }

    for column in lst:
        _, created = Bulletin.objects.update_or_create(
            notice = column[0],
        )
    
    return render(request, 'dashboard/bulletin.html', prompt)


@login_required(login_url='user-login')
def product_delete(request, notice):
    item = Bulletin.objects.get(notice = notice)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-bulletin')
    context = {
        'item': item
    }
    return render(request, 'dashboard/products_delete.html', context)


class SearchResultsView(ListView):
    model = Students
    template_name = 'dashboard/search.html'

    def get_queryset(self):  # new
        query_name = self.request.GET.get("name")
        query_branch = self.request.GET.getlist("branch")
        query_cgpi = self.request.GET.get("cgpi")
        query_kt = self.request.GET.get("kt")
        query_choice = self.request.GET.get("choice")
        object_list = Students.objects.all()
        print(query_branch)

        if query_name:
            object_list = object_list.filter(Q(name__icontains=query_name))
        if query_branch:
            object_list = object_list.filter(Q(branch__icontains=query_branch[0]))
            length = len(query_branch)
            if length>1:
                for i in range(1,length):
                    object_list = object_list | object_list.filter(Q(branch__icontains=query_branch[i]))
        if query_cgpi:
            object_list = object_list.filter(Q(cgpi__range=(query_cgpi,10)))
        if query_kt:
            object_list = object_list.filter(Q(live_kts__range=(0,query_kt)))
        if query_choice:
            object_list = object_list.filter(Q(choice__icontains=query_choice))
        
        return object_list


class SearchResultsView1(ListView):
    model = Placements
    template_name = 'dashboard/search1.html'

    def get_queryset(self):  # new
        query_name = self.request.GET.get("name")
        query_offer = self.request.GET.get("offer")
        query_batch = self.request.GET.get("batch")
        object_list = Placements.objects.all()

        if query_name:
            object_list = object_list.filter(Q(name__icontains=query_name))
        if query_offer:
            object_list = object_list.filter(Q(offer1__icontains=query_offer)) | object_list.filter(Q(offer2__icontains=query_offer)) | object_list.filter(Q(offer3__icontains=query_offer))

        if query_batch:
            object_list = object_list.filter(Q(batch__icontains=query_batch))

        return object_list

@csrf_protect
def sendMail(request):
    if request.method == 'POST':
        var = request.POST.get('checkall')
        mylst = var.split(',')
        if mylst[0] == 'on':
            mylst = mylst[1:]

        
    return render(request, 'dashboard/students.html')