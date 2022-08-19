from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Companies, Placements, Product, Order, Students
from .forms import ProductForm, OrderForm, StudentForm, PlacementForm, CompanyForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import auth_users, allowed_users
import pandas as pd
from django.core.paginator import Paginator
# Create your views here.


@login_required(login_url='user-login')
def index(request):
    placements = Placements.objects.all()
    placement_count = placements.count()
    students = Students.objects.all()
    student_count = students.count()
    companies = Companies.objects.all()
    company_count = companies.count()

    context = {
        'placement_count': placement_count,
        'student_count': student_count,
        'company_count': company_count,
    }
    return render(request, 'dashboard/index.html', context)


login_required(login_url='user-login')
def student(request):
    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Student has been added')
            return redirect('dashboard-customers')
    else:
        form = StudentForm()

    prompt = {
        'form': form
        }
    
    df = pd.read_excel('media/Students.xlsx')
    lst = []

    for i in range(len(df)):
        lst.append(df.iloc[i])

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
        # 'students': data,
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

    return render(request, 'dashboard/customers.html', prompt)


login_required(login_url='user-login')
def placement(request):
    if request.method == 'POST':
        form = PlacementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Student has been added')
            return redirect('dashboard-products')
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
    
    return render(request, 'dashboard/products.html', prompt)


login_required(login_url='user-login')
def company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Company has been added')
            return redirect('dashboard-order')
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
    
    return render(request, 'dashboard/order.html', prompt)









# @login_required(login_url='user-login')
# def products(request):
#     product = Product.objects.all()
#     product_count = product.count()
#     customer = User.objects.filter(groups=2)
#     customer_count = customer.count()
#     order = Order.objects.all()
#     order_count = order.count()
#     product_quantity = Product.objects.filter(name='')
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             product_name = form.cleaned_data.get('name')
#             messages.success(request, f'{product_name} has been added')
#             return redirect('dashboard-products')
#     else:
#         form = ProductForm()
#     context = {
#         'product': product,
#         'form': form,
#         'customer_count': customer_count,
#         'product_count': product_count,
#         'order_count': order_count,
#     }
#     return render(request, 'dashboard/products.html', context)


# @login_required(login_url='user-login')
# def product_detail(request, pk):
#     context = {

#     }
#     return render(request, 'dashboard/products_detail.html', context)


# @login_required(login_url='user-login')
# @allowed_users(allowed_roles=['Admin'])
# def customer_detail(request, pk):
#     customer = User.objects.filter(groups=2)
#     customer_count = customer.count()
#     product = Product.objects.all()
#     product_count = product.count()
#     order = Order.objects.all()
#     order_count = order.count()
#     customers = User.objects.get(id=pk)
#     context = {
#         'customers': customers,
#         'customer_count': customer_count,
#         'product_count': product_count,
#         'order_count': order_count,

#     }
#     return render(request, 'dashboard/customers_detail.html', context)


# @login_required(login_url='user-login')
# @allowed_users(allowed_roles=['Admin'])
# def product_edit(request, pk):
#     item = Product.objects.get(id=pk)
#     if request.method == 'POST':
#         form = ProductForm(request.POST, instance=item)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard-products')
#     else:
#         form = ProductForm(instance=item)
#     context = {
#         'form': form,
#     }
#     return render(request, 'dashboard/products_edit.html', context)


# @login_required(login_url='user-login')
# @allowed_users(allowed_roles=['Admin'])
# def product_delete(request, pk):
#     item = Product.objects.get(id=pk)
#     if request.method == 'POST':
#         item.delete()
#         return redirect('dashboard-products')
#     context = {
#         'item': item
#     }
#     return render(request, 'dashboard/products_delete.html', context)


# @login_required(login_url='user-login')
# def order(request):
#     order = Order.objects.all()
#     order_count = order.count()
#     customer = User.objects.filter(groups=2)
#     customer_count = customer.count()
#     product = Product.objects.all()
#     product_count = product.count()

#     context = {
#         'order': order,
#         'customer_count': customer_count,
#         'product_count': product_count,
#         'order_count': order_count,
#     }
#     return render(request, 'dashboard/order.html', context)