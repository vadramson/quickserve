from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import User
from django.core.paginator import Paginator
from django.db import transaction
from django.db.models import Count, Min, Sum, Avg
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.timezone import now
from httplib2 import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer, UserSerializer, TabsSerializer, OrdersSerializer, ProfileSerializer, \
     SalesSerializer, LossSerializer, ExpenseSerializer, AvarisSerializer, PurchasesSerializer, AttendanceSerializer\

from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token


from QuickServe.forms import AttendanceForm, AgencyForm, DepartmentForm, ExtraForm, SignUpForm, MenuForm, CategoryForm, \
    ProductForm, ExpenseForm, LossForm, BonusForm, DeductionsForm, PurchasesForm, AvarisForm, StockForm, OrdersForm, \
    TabsForm, SalesForm
from QuickServe.models import Agency, Department, Menu, Category, Product, Expense, Loss, Bonus, Profile, Deductions, \
    Purchases, Avaris, Stock, Orders, NumbersOrder, Tabs, Sales, PrintMsg, Attendance, OrderTotal
# from .utils import render_to_pdf


# from Accounts.forms import SignUpForm, EditProfileForm, ProfileData

# API VIEWS Start


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated,)


class ProductAll(APIView):
    def post(self, request):
        tken = request.data.get("user_id")
        print(tken)
        stat = 'Active'
        product = Product.objects.filter(status__exact=stat, quantity__gt=0).order_by('-id')
        serializer = ProductSerializer(product, many=True)
        return Response({"prod": serializer.data})


@api_view(["POST"])
def my_drf_login(request):
    # data = dict()
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if not user:
        return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    urs = get_object_or_404(User, pk=token.user_id)
    prof = get_object_or_404(Profile, user=urs)
    # serializer = UserSerializer(urs)
    # car_serializer = CarSerializer(car, context={"request": request})
    # serializer = ProfileSerializer(prof)
    # return Response(serializer.data)
    # data = dict()
    # data = {"user": urs}
    # return JsonResponse(data)
    return Response(
        {"token": token.key, "user_id": token.user_id, "Username": urs.username, "Name": urs.get_full_name(),
         "picture": urs.profile.picture.url, "Role": urs.profile.role})


# {"token": token.key, "user_id": token.user_id, "Username": urs.username, "Name": urs.get_full_name(),
#  "picture": urs.profile.picture.url, "Role": urs.profile.role}


@api_view(["POST"])
def my_drf_logout(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if not user:
        return Response({"error": "Unknown User"}, status=HTTP_401_UNAUTHORIZED)
    logout(request)
    return Response({"Respond": "Logout"})


# TABS API VIEWS HERE

@api_view(["GET"])
def get_tabs(request, self):
    permission_classes = (IsAuthenticated,)
    user = self.request.user
    print(user.pk)
    tab = Tabs.objects.filter(user=user)
    serializer = TabsSerializer(tab, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def get_all_my_open_tabs(request):
    toke = request.data.get("token")
    tokeen = get_object_or_404(Token, key=toke)
    print(tokeen.key)
    urs = get_object_or_404(User, pk=tokeen.user_id)
    tab = Tabs.objects.filter(user=urs, status__exact='Open').order_by('-id')
    serializer = TabsSerializer(tab, many=True)
    return Response({"myTabs": serializer.data})


@api_view(["POST"])
def my_open_tabs(request):
    tken = request.data.get("user_id")
    print(tken)
    tokeen = get_object_or_404(Token, user_id=tken)
    print(tokeen.key)
    urs = get_object_or_404(User, pk=tken)
    tab = Tabs.objects.filter(user=urs, status__exact='Open').order_by('-id')
    serializer = TabsSerializer(tab, many=True)
    return Response({"myTabs": serializer.data})


@api_view(["POST"])
def my_closed_tabs(request):
    tken = request.data.get("user_id")
    print(tken)
    tokeen = get_object_or_404(Token, user_id=tken)
    print(tokeen.key)
    urs = get_object_or_404(User, pk=tken)
    tab = Tabs.objects.filter(user=urs, status__exact='Closed').order_by('-id')
    serializer = TabsSerializer(tab, many=True)
    return Response({"myTabs": serializer.data})


class TabsGetOpen(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = self.request.user
        tab = Tabs.objects.filter(user=user, status__exact='Open').order_by('-id')
        serializer = TabsSerializer(tab, many=True)
        return Response(serializer.data)


class TabsGetClosed(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = self.request.user
        tab = Tabs.objects.filter(user__exact=user, status__exact='Closed').order_by('-id')
        serializer = TabsSerializer(tab, many=True)
        return Response(serializer.data)


class TabsAdd(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = TabsSerializer(data=request.data)
        if serializer.is_valid():
            tken = request.data.get("user_id")
            print(tken)
            tokeen = get_object_or_404(Token, user_id=tken)
            print(tokeen.key)
            urs = get_object_or_404(User, pk=tken)
            tab = Tabs()
            ordNum = NumbersOrder.objects.get()
            user = self.request.user
            stat = 'Open'
            tab.tableNum = request.data.get("tableNum")
            tab.status = stat
            tab.dateOp = now()
            tab.orderNumber = ordNum.number
            num = ordNum.number
            tab.user = urs
            ordNum.number += 1
            tab.save()
            ordNum.save()
            tabs = Tabs.objects.filter(user=urs, status__exact='Open', orderNumber__exact=num).order_by('-id')
            serializer = TabsSerializer(tabs, many=True)
            return Response({"tabCreate": serializer.data})
        return Response({"tabCreate": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class TabsDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        user = self.request.user
        print(user.pk)
        tab = Tabs.objects.filter(user=user.pk)
        serializer = TabsSerializer(tab, many=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        tabs = get_object_or_404(Tabs, pk=pk)
        tabs.delete()
        return Response('Deleted', status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        serializer = TabsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

            # def get_queryset(self):
            #     user = self.request.user
            #     # serializer = Tabs.objects.filter(user__exact=user)
            #     permission_classes = (IsAuthenticated,)
            #     # return Response(serializer.data)
            #     return Tabs.objects.filter(user__exact=user)


# ORDERS API VIEWS HERE

class OrdersGet(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = self.request.user
        # tab = Tabs.objects.filter(user=user, status__exact='Open')
        order = Orders.objects.all().order_by('-id')
        serializer = OrdersSerializer(order, many=True)
        return Response(serializer.data)


class OrdersGetParticular(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        # user = self.request.user
        orderNumber = request.data.get("orderNumber")
        order = Orders.objects.filter(orderNumber__exact=orderNumber).order_by('-id')
        serializer = OrdersSerializer(order, many=True)
        total_amt = Orders.objects.filter(orderNumber__exact=orderNumber).aggregate(sum=Sum('amount'))['sum']
        return Response({"orderParticular":serializer.data, "totalAmt": total_amt})


class OrdersAdd(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = OrdersSerializer(data=request.data)
        if serializer.is_valid():
            print("valid")
            order = Orders()
            pdt = request.data.get("product")
            qty = request.data.get("quantity")
            tken = request.data.get("user_id")
            print(tken)
            tokeen = get_object_or_404(Token, user_id=tken)
            print(tokeen.key)
            urs = get_object_or_404(User, pk=tken)
            print(qty)
            ordNum = request.data.get("orderNumber")
            product = get_object_or_404(Product, pk=pdt)
            # tab = get_object_or_404(Tabs, orderNumber=ordNum)
            print("datas")
            if int(qty) <= product.quantity:
                print("ok to save")
                # user = self.request.user
                product.quantity -= int(qty)
                amount = int(qty) * product.price
                # tat = tab.total + amount
                # print(tat)
                order.dateOp = now()
                order.product = product
                order.quantity = int(qty)
                order.orderNumber = ordNum
                order.amount = amount
                order.status = "Open"
                order.user = urs
                order.save()
                product.save()
                # tab.save()
                # orders = Orders.objects.filter(user__exact=user)
                orders = Orders.objects.filter(orderNumber__exact=ordNum).order_by('-id')
                serializer = OrdersSerializer(orders, many=True)
                total_amt = Orders.objects.filter(orderNumber__exact=ordNum).aggregate(sum=Sum('amount'))['sum']
                return Response({"orders": serializer.data, "total": total_amt})
            else:
                return Response({"insuff": "Insufficient Product in Stock"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrdersDel(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = TabsSerializer(data=request.data)
        if serializer.is_valid():
            idOrder = request.data.get("id")
            order = get_object_or_404(Orders, pk=idOrder)
            product = get_object_or_404(Product, namePdt=order.product)
            product.quantity += order.quantity
            product.save()
            order.delete()
            orders = Orders.objects.filter(orderNumber__exact=order.orderNumber).order_by('-id')
            serializer = OrdersSerializer(orders, many=True)
            return Response({"delOrd": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ATTENDANCE API VIEWS HERE

class ClockIn(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            tken = request.data.get("user")
            print(tken)
            tokeen = get_object_or_404(Token, user_id=tken)
            print(tokeen.key)
            urs = get_object_or_404(User, pk=tken)
            attend = Attendance()
            attend.actDate = now().today().date()
            chk = Attendance.objects.filter(user__exact=urs, actDate__exact=attend.actDate)
            if chk:
                return Response({"Clockin": "You have already Clocked in for Today"})
            attend.user = urs
            attend.actDate = now().today().date()
            attend.month = now().month
            attend.clockIn = now().hour
            attend.clockinHr = now().minute
            attend.status = 'Clocked In'
            attend.save()
            return Response({"Clockin": "You are now clocked in for the day"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClockOut(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            tken = request.data.get("user")
            print(tken)
            tokeen = get_object_or_404(Token, user_id=tken)
            print(tokeen.key)
            urs = get_object_or_404(User, pk=tken)
            attend = Attendance()
            attend.actDate = now().today().date()
            chk = get_object_or_404(Attendance, user__exact=urs, actDate__exact=attend.actDate)
            if not chk:
                return Response({"ClockOut": "You are not yet Clocked in for the day"})
            else:
                if chk.status == 'Clocked In':
                    chk.clockOut = now().hour
                    chk.clockoutHr = now().minute
                    chk.status = 'Clocked In Clocked Out'
                    ck = Attendance.objects.filter(user__exact=urs, actDate__exact=attend.actDate)
                    minutes = (int(chk.clockoutHr) - int(chk.clockinHr)) / 60
                    hours = int(chk.clockOut) - int(chk.clockIn)
                    chk.hours = minutes + hours
                    chk.save()
                    return Response({"ClockOut": "You are now clocked OUT for the day"})
                elif chk.status == 'Clocked In Clocked Out':
                    return Response({"ClockOut": "You are already CLOCKED OUT for the DAY"})
        return Response({"": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# SALES API VIEWS HERE

class Sale(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = SalesSerializer(data=request.data)
        if serializer.is_valid():
            tken = request.data.get("user_id")
            # print(tken)
            tokeen = get_object_or_404(Token, user_id=tken)
            print(tokeen.key)
            urs = get_object_or_404(User, pk=tken)
            msg = PrintMsg()
            sales = Sales()
            invNum = request.data.get("orderNumber")
            tab = get_object_or_404(Tabs, orderNumber=invNum)
            order = Orders.objects.filter(orderNumber=tab.orderNumber)
            orders = Orders()
            user = self.request.user
            if order:
                tab.status = 'Closed'
                tab.tableNum = tab.tableNum
                orders = order.filter(orderNumber__exact=tab.orderNumber)
                msg.status = 'Waiting'
                msg.orderNumber = tab.orderNumber
                msg.dateOp = now()
                sales.status = 'Closed'
                sales.user = urs
                sales.salesDate = now()
                sales.customer = request.data.get("customer")
                sales.paid = request.data.get("totalSale")
                sales.amount = request.data.get("totalSale")
                sales.invoiceNumber = tab.orderNumber
                # sales.custmerSign = request.data.get("custmerSign")
                sales.save()
                msg.totalSale = request.data.get("totalSale")
                msg.save()
                for ord in orders:
                    ord.status = 'Closed'
                    ord.save()
                tab.save()
            return Response({"Sale": "Sale Validated Successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# API VIEWS End


@login_required
def home(request):
    pdt = Product.objects.all()
    pdtCount = Product.objects.aggregate(countt=Count('id'))['countt']
    print(pdtCount)
    pdtLess = Product.objects.filter(quantity__lt=20).order_by('-id')
    # product = Product.objects.filter(status__exact=stat, quantity__gt=0).order_by('-id')
    # print(pdtLess.namePdt)
    return render(request, 'homep/home.html', {"pdtCount": pdtCount, "pdtLess": pdtLess})

@login_required
def pdtAlert(request):
    pdtCount = Product.objects.aggregate(countt=Count(quantity__lt=20))['countt']
    print(pdtCount)
    pdtLess = Product.objects.filter(quantity__lt=1000).order_by('-id')
    return render(request, 'index.html', {"pdtCount": pdtCount, "pdtLess": pdtLess})


@login_required
def agency_list(request):
    # agencys = Agency.objects.all().order_by("id") # to order in ascending order
    agencys = Agency.objects.all().order_by("-id")  # to order in descending order
    return render(request, 'agencys/agency_list.html', {'agencys': agencys})


@login_required
def user_list(request):
    # agencys = Agency.objects.all().order_by("id") # to order in ascending order
    users = User.objects.all().order_by("id")  # to order in descending order
    return render(request, 'profiles/user_profile_list.html', {'users': users})


# AGENCY VIEWS

@login_required
def save_agency_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():

            form.save()
            data['form_is_valid'] = True
            agencys = Agency.objects.all().order_by("-id")
            paginator = Paginator(agencys, 12)
            data['html_agency_list'] = render_to_string('agencys/includes/partial_agency_list.html',
                                                        {'agencys': agencys})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


@login_required
def agency_create(request):
    if request.method == 'POST':
        form = AgencyForm(request.POST)
    else:
        form = AgencyForm()
    return save_agency_form(request, form, 'agencys/includes/partial_agency_create.html')


@login_required
def agency_update(request, pk):
    agency = get_object_or_404(Agency, pk=pk)
    if request.method == 'POST':
        form = AgencyForm(request.POST, instance=agency)
    else:
        form = AgencyForm(instance=agency)
    return save_agency_form(request, form, 'agencys/includes/partial_subject_update.html')


@login_required
def agency_delete(request, pk):
    agency = get_object_or_404(Agency, pk=pk)
    data = dict()
    if request.method == 'POST':
        agency.delete()
        data['form_is_valid'] = True
        agencys = Agency.objects.all().order_by("-id")
        paginator = Paginator(agencys, 12)
        data['html_agency_list'] = render_to_string('agencys/includes/partial_agency_list.html', {'agencys': agencys})
    else:
        context = {'agency': agency}
        data['html_form'] = render_to_string('agencys/includes/partial_agency_delete.html', context, request=request)
    return JsonResponse(data)


# Department Views


@login_required
def department_list(request):
    # departments = Department.objects.all().order_by("id") # to order in ascending order
    departments = Department.objects.all().order_by("-id")  # to order in descending order
    return render(request, 'departments/department_list.html', {'departments': departments})


# DEPARTMENT VIEWS

@login_required
def save_department_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():

            form.save()
            data['form_is_valid'] = True
            departments = Department.objects.all().order_by("-id")
            paginator = Paginator(departments, 12)
            data['html_department_list'] = render_to_string('departments/includes/partial_department_list.html',
                                                            {'departments': departments})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


@login_required
def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
    else:
        form = DepartmentForm()
    return save_department_form(request, form, 'departments/includes/partial_department_create.html')


@login_required
def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
    else:
        form = DepartmentForm(instance=department)
    return save_department_form(request, form, 'departments/includes/partial_department_update.html')


@login_required
def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    data = dict()
    if request.method == 'POST':
        department.delete()
        data['form_is_valid'] = True
        departments = Department.objects.all().order_by("-id")
        paginator = Paginator(departments, 12)
        data['html_department_list'] = render_to_string('departments/includes/partial_department_list.html',
                                                        {'departments': departments})
    else:
        context = {'department': department}
        data['html_form'] = render_to_string('departments/includes/partial_department_delete.html', context,
                                             request=request)
    return JsonResponse(data)


@login_required
def profile_list(request):
    # profiles = Profile.objects.all().order_by("id") # to order in ascending order
    users = User.objects.all().order_by("-id")  # to order in descending order
    return render(request, 'profiles/profile_list.html', {'users': users})


# USER CREATION VIEWS

@transaction.atomic
def createUser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        extra = ExtraForm(request.POST, request.FILES)
        if form.is_valid() and extra.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            extra = ExtraForm(request.POST, request.FILES,
                              instance=user.profile)  # Reload the profile form with the profile instance
            extra.full_clean()  # Manually clean the form this time. It is implicitly called by "is_valid()" method
            extra.save()  # Gracefully save the form
            messages.success(request, 'New User Added Successfuly!', extra_tags='alert')
        else:
            return redirect('home')
    else:
        form = SignUpForm()
        extra = ExtraForm()
    return render(request, 'profiles/createUser.html', {'form': form, 'extra': extra})


# MENU VIEWS

@login_required
def menu_list(request):
    # menus = Menu.objects.all().order_by("id") # to order in ascending order
    menus = Menu.objects.all().order_by("-id")  # to order in descending order
    return render(request, 'menus/menu_list.html', {'menus': menus})


@login_required
def save_menu_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():

            form.save()
            messages.success(request, 'Menu Saved !', extra_tags='alert')
            data['form_is_valid'] = True
            menus = Menu.objects.all().order_by("-id")
            paginator = Paginator(menus, 12)
            data['html_menu_list'] = render_to_string('menus/includes/partial_menu_list.html', {'menus': menus})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


@login_required
def menu_create(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
    else:
        form = MenuForm()
    return save_menu_form(request, form, 'menus/includes/partial_menu_create.html')


@login_required
def menu_update(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
    else:
        form = MenuForm(instance=menu)
    return save_menu_form(request, form, 'menus/includes/partial_menu_update.html')


@login_required
def menu_delete(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    data = dict()
    if request.method == 'POST':
        menu.delete()
        data['form_is_valid'] = True
        menus = Menu.objects.all().order_by("-id")
        paginator = Paginator(menus, 12)
        data['html_menu_list'] = render_to_string('menus/includes/partial_menu_list.html', {'menus': menus})
    else:
        context = {'menu': menu}
        data['html_form'] = render_to_string('menus/includes/partial_menu_delete.html', context, request=request)
    return JsonResponse(data)


# CATEGORY VIEWS

@login_required
def category_list(request):
    # categorys = Category.objects.all().order_by("id") # to order in ascending order
    categorys = Category.objects.all().order_by("-id")  # to order in descending order
    return render(request, 'categorys/category_list.html', {'categorys': categorys})


@login_required
def save_category_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():

            form.save()
            data['save_category'] = True
            data['form_is_valid'] = True
            categorys = Category.objects.all().order_by("-id")
            paginator = Paginator(categorys, 12)
            data['html_category_list'] = render_to_string('categorys/includes/partial_category_list.html',
                                                          {'categorys': categorys})
        else:
            data['save_category_error'] = True
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
    else:
        form = CategoryForm()
    return save_category_form(request, form, 'categorys/includes/partial_category_create.html')


@login_required
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
    else:
        form = CategoryForm(instance=category)
    return save_category_form(request, form, 'categorys/includes/partial_category_update.html')


@login_required
def category_activate(request, pk):
    category = get_object_or_404(Category, pk=pk)
    data = dict()
    if request.method == 'POST':
        category.status = 'Active'
        category.save()
        data['form_is_valid'] = True
        data['category_activate'] = True
        categorys = Category.objects.all().order_by("-id")
        paginator = Paginator(categorys, 12)
        data['html_category_list'] = render_to_string('categorys/includes/partial_category_list.html',
                                                      {'categorys': categorys})
    else:
        context = {'category': category}
        data['html_form'] = render_to_string('categorys/includes/partial_category_activate.html', context,
                                             request=request)
    return JsonResponse(data)


@login_required
def category_deactivate(request, pk):
    category = get_object_or_404(Category, pk=pk)
    data = dict()
    if request.method == 'POST':
        category.status = 'Deactivate'
        category.save()
        data['form_is_valid'] = True
        data['category_deactivate'] = True
        categorys = Category.objects.all().order_by("-id")
        paginator = Paginator(categorys, 12)
        data['html_category_list'] = render_to_string('categorys/includes/partial_category_list.html',
                                                      {'categorys': categorys})
    else:
        context = {'category': category}
        data['html_form'] = render_to_string('categorys/includes/partial_category_deactivate.html', context,
                                             request=request)
    return JsonResponse(data)


@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    data = dict()
    if request.method == 'POST':
        category.delete()
        data['form_is_valid'] = True
        categorys = Category.objects.all().order_by("-id")
        paginator = Paginator(categorys, 12)
        data['html_category_list'] = render_to_string('categorys/includes/partial_category_list.html',
                                                      {'categorys': categorys})
    else:
        context = {'category': category}
        data['html_form'] = render_to_string('categorys/includes/partial_category_activate.html', context,
                                             request=request)
    return JsonResponse(data)


# Product VIEWS

@login_required
def product_list(request):
    # products = Product.objects.all().order_by("id") # to order in ascending order
    products = Product.objects.all().order_by("-id")  # to order in descending order
    return render(request, 'products/product_list.html', {'products': products})


@login_required
def save_product_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            products = Product.objects.all().order_by("-id")
            paginator = Paginator(products, 12)
            data['html_product_list'] = render_to_string('products/includes/partial_product_list.html',
                                                         {'products': products})
        else:
            data['form_is_valid'] = False
            data['form_error'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
    else:
        form = ProductForm()
    return save_product_form(request, form, 'products/includes/partial_product_create.html')


@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
    else:
        form = ProductForm(instance=product)
    return save_product_form(request, form, 'products/includes/partial_product_update.html')


@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    data = dict()
    if request.method == 'POST':
        product.delete()
        data['form_is_valid'] = True
        products = Product.objects.all().order_by("-id")
        paginator = Paginator(products, 12)
        data['html_product_list'] = render_to_string('products/includes/partial_product_list.html',
                                                     {'products': products})
    else:
        context = {'product': product}
        data['html_form'] = render_to_string('products/includes/partial_product_deactivate.html', context,
                                             request=request)
    return JsonResponse(data)


@login_required
def product_activate(request, pk):
    product = get_object_or_404(Product, pk=pk)
    data = dict()
    if request.method == 'POST':
        product.status = 'Active'
        product.save()
        data['form_is_valid'] = True
        data['product_activate'] = True
        products = Product.objects.all().order_by("-id")
        paginator = Paginator(products, 12)
        data['html_product_list'] = render_to_string('products/includes/partial_product_list.html',
                                                     {'products': products})
    else:
        context = {'product': product}
        data['html_form'] = render_to_string('products/includes/partial_product_activate.html', context,
                                             request=request)
    return JsonResponse(data)


@login_required
def product_deactivate(request, pk):
    product = get_object_or_404(Product, pk=pk)
    data = dict()
    if request.method == 'POST':
        product.status = 'Deactivate'
        product.save()
        data['form_is_valid'] = True
        data['product_deactivate'] = True
        products = Product.objects.all().order_by("-id")
        paginator = Paginator(products, 12)
        data['html_product_list'] = render_to_string('products/includes/partial_product_list.html',
                                                     {'products': products})
    else:
        context = {'product': product}
        data['html_form'] = render_to_string('products/includes/partial_product_deactivate.html', context,
                                             request=request)
    return JsonResponse(data)


# Expense VIEWS

@login_required
def expense_list(request):
    # expenses = Expense.objects.all().order_by("id") # to order in ascending order
    expenses = Expense.objects.all().order_by("-id")  # to order in descending order
    return render(request, 'expenses/expense_list.html', {'expenses': expenses})


@login_required
def save_expense_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():

            form.save()
            data['form_is_valid'] = True
            expenses = Expense.objects.all().order_by("-id")
            paginator = Paginator(expenses, 12)
            data['html_expense_list'] = render_to_string('expenses/includes/partial_expense_list.html',
                                                         {'expenses': expenses})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


@login_required
def expense_create(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
    else:
        form = ExpenseForm()
    return save_expense_form(request, form, 'expenses/includes/partial_expense_create.html')


@login_required
def expense_update(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
    else:
        form = ExpenseForm(instance=expense)
    return save_expense_form(request, form, 'expenses/includes/partial_expense_update.html')


@login_required
def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    data = dict()
    if request.method == 'POST':
        expense.delete()
        data['form_is_valid'] = True
        expenses = Expense.objects.all().order_by("-id")
        paginator = Paginator(expenses, 12)
        data['html_expense_list'] = render_to_string('expenses/includes/partial_expense_list.html',
                                                     {'expenses': expenses})
    else:
        context = {'expense': expense}
        data['html_form'] = render_to_string('expenses/includes/partial_expense_delete.html', context, request=request)
    return JsonResponse(data)


# Loss VIEWS

@login_required
def loss_list(request):
    # losss = Loss.objects.all().order_by("id") # to order in ascending order
    losss = Loss.objects.all().order_by("-id")  # to order in descending order
    return render(request, 'losss/loss_list.html', {'losss': losss})


@login_required
def save_loss_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():

            form.save()
            data['form_is_valid'] = True
            losss = Loss.objects.all().order_by("-id")
            paginator = Paginator(losss, 12)
            data['html_loss_list'] = render_to_string('losss/includes/partial_loss_list.html', {'losss': losss})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


@login_required
def loss_create(request):
    if request.method == 'POST':
        form = LossForm(request.POST)
    else:
        form = LossForm()
    return save_loss_form(request, form, 'losss/includes/partial_loss_create.html')


@login_required
def loss_update(request, pk):
    loss = get_object_or_404(Loss, pk=pk)
    if request.method == 'POST':
        form = LossForm(request.POST, instance=loss)
    else:
        form = LossForm(instance=loss)
    return save_loss_form(request, form, 'losss/includes/partial_loss_update.html')


@login_required
def loss_delete(request, pk):
    loss = get_object_or_404(Loss, pk=pk)
    data = dict()
    if request.method == 'POST':
        loss.delete()
        data['form_is_valid'] = True
        losss = Loss.objects.all().order_by("-id")
        paginator = Paginator(losss, 12)
        data['html_loss_list'] = render_to_string('losss/includes/partial_loss_list.html', {'losss': losss})
    else:
        context = {'loss': loss}
        data['html_form'] = render_to_string('losss/includes/partial_loss_delete.html', context, request=request)
    return JsonResponse(data)


# Bonus VIEWS

@login_required
def bonus_list(request):
    # bonuss = Bonus.objects.all().order_by("id") # to order in ascending order
    bonuss = Bonus.objects.all().order_by("-id")  # to order in descending order
    return render(request, 'bonuss/bonus_list.html', {'bonuss': bonuss})


@login_required
def save_bonus_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            code = form.cleaned_data['empCode']
            print(code)
            bonus = Profile.objects.filter(empCode=code)
            if bonus:
                print("Exist")
                form.save()
                # messages.success(request, 'Bonus Saved !', extra_tags='alert')
                data['form_is_valid'] = True
                bonuss = Bonus.objects.all().order_by("-id")
                paginator = Paginator(bonuss, 12)
                data['html_bonus_list'] = render_to_string('bonuss/includes/partial_bonus_list.html',
                                                           {'bonuss': bonuss})
            else:
                data['form_is_valid'] = False
                bonuss = Bonus.objects.all().order_by("-id")
                paginator = Paginator(bonuss, 12)
                data['html_bonus_list'] = render_to_string('bonuss/includes/partial_bonus_list.html',
                                                           {'bonuss': bonuss})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


@login_required
def bonus_create(request):
    if request.method == 'POST':
        form = BonusForm(request.POST)
    else:
        form = BonusForm()
    return save_bonus_form(request, form, 'bonuss/includes/partial_bonus_create.html')


@login_required
def bonus_update(request, pk):
    bonus = get_object_or_404(Bonus, pk=pk)
    if request.method == 'POST':
        form = BonusForm(request.POST, instance=bonus)
        # data['bonus_update'] = True
    else:
        form = BonusForm(instance=bonus)
    return save_bonus_form(request, form, 'bonuss/includes/partial_bonus_update.html')


@login_required
def bonus_delete(request, pk):
    bonus = get_object_or_404(Bonus, pk=pk)
    data = dict()
    if request.method == 'POST':
        bonus.delete()
        data['form_is_valid'] = True
        data['bonus_delete'] = True
        bonuss = Bonus.objects.all().order_by("-id")
        paginator = Paginator(bonuss, 12)
        data['html_bonus_list'] = render_to_string('bonuss/includes/partial_bonus_list.html', {'bonuss': bonuss, })
    else:
        context = {'bonus': bonus}
        data['html_form'] = render_to_string('bonuss/includes/partial_bonus_delete.html', context, request=request)
    return JsonResponse(data)


# Deductions VIEWS

@login_required
def deduction_list(request):
    # deductions = Deductions.objects.all().order_by("id") # to order in ascending order
    deductions = Deductions.objects.all().order_by("-id")  # to order in descending order
    return render(request, 'deductions/deduction_list.html', {'deductions': deductions})


@login_required
def save_deduction_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            code = form.cleaned_data['empCode']
            print(code)
            deduction = Profile.objects.filter(empCode=code)
            if deduction:
                print("Exist")
                form.save()
                # messages.success(request, 'Deductions Saved !', extra_tags='alert')
                data['form_is_valid'] = True
                deductions = Deductions.objects.all().order_by("-id")
                paginator = Paginator(deductions, 12)
                data['html_deduction_list'] = render_to_string('deductions/includes/partial_deduction_list.html',
                                                               {'deductions': deductions})
            else:
                data['form_is_valid'] = False
                deductions = Deductions.objects.all().order_by("-id")
                paginator = Paginator(deductions, 12)
                data['html_deduction_list'] = render_to_string('deductions/includes/partial_deduction_list.html',
                                                               {'deductions': deductions})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


@login_required
def deduction_create(request):
    if request.method == 'POST':
        form = DeductionsForm(request.POST)
    else:
        form = DeductionsForm()
    return save_deduction_form(request, form, 'deductions/includes/partial_deduction_create.html')


@login_required
def deduction_update(request, pk):
    deduction = get_object_or_404(Deductions, pk=pk)
    if request.method == 'POST':
        form = DeductionsForm(request.POST, instance=deduction)
        # data['deduction_update'] = True
    else:
        form = DeductionsForm(instance=deduction)
    return save_deduction_form(request, form, 'deductions/includes/partial_deduction_update.html')


@login_required
def deduction_delete(request, pk):
    deduction = get_object_or_404(Deductions, pk=pk)
    data = dict()
    if request.method == 'POST':
        deduction.delete()
        data['form_is_valid'] = True
        data['deduction_delete'] = True
        deductions = Deductions.objects.all().order_by("-id")
        paginator = Paginator(deductions, 12)
        data['html_deduction_list'] = render_to_string('deductions/includes/partial_deduction_list.html',
                                                       {'deductions': deductions, })
    else:
        context = {'deduction': deduction}
        data['html_form'] = render_to_string('deductions/includes/partial_deduction_delete.html', context,
                                             request=request)
    return JsonResponse(data)


# PURCHASES VIEWS

@login_required
def purchase_list(request):
    purchases = Purchases.objects.all().order_by("-id")  # to order in descending order
    return render(request, 'purchases/purchase_list.html', {'purchases': purchases})


@login_required
def save_purchase_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            print("Hello")
            product = form.cleaned_data['product']
            quantity = form.cleaned_data['quantity']
            print(product)
            purchase = get_object_or_404(Product, namePdt=product)
            print(purchase)
            # form.save()
            if purchase:
                print(purchase.quantity)
                purchase.quantity += quantity
                form.save()
                purchase.save()
                # messages.success(request, 'Purchases Saved !', extra_tags='alert')
            data['form_is_valid'] = True
            purchases = Purchases.objects.all().order_by("-id")
            paginator = Paginator(purchases, 12)
            data['html_purchase_list'] = render_to_string('purchases/includes/partial_purchase_list.html',
                                                          {'purchases': purchases})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


@login_required
def purchase_create(request):
    if request.method == 'POST':
        form = PurchasesForm(request.POST, request.FILES)
    else:
        form = PurchasesForm()
    return save_purchase_form(request, form, 'purchases/includes/partial_purchase_create.html')


@login_required
def save_purchase_update_form(request, form, pk, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            sentPdt = form.cleaned_data['product']
            purQty = form.cleaned_data['quantity']
            print('the Pk')
            print(sentPdt)
            purchase = get_object_or_404(Purchases, pk=pk)
            product = get_object_or_404(Product, namePdt=purchase.product)
            productDiff = get_object_or_404(Product, namePdt=sentPdt)
            if sentPdt == purchase.product:
                if purQty >= purchase.quantity:
                    print(purchase.quantity)
                    newQty = purQty - purchase.quantity
                    product.quantity += newQty
                    print(product.quantity)
                    # print(product)
                    form.save()
                    product.save()
                else:
                    print(purchase.quantity)
                    newQty = purchase.quantity - purQty
                    product.quantity -= newQty
                    print(product.quantity)
                    # print(product)
                    form.save()
                    product.save()
            else:
                product.quantity -= purchase.quantity
                product.save()
                productDiff.quantity += purQty
                productDiff.save()
                form.save()
            data['form_is_valid'] = True
            purchases = Purchases.objects.all().order_by("-id")
            data['html_purchase_list'] = render_to_string('purchases/includes/partial_purchase_list.html',
                                                          {'purchases': purchases})

        else:
            data['purchase_update'] = False
            data['form_error'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


@login_required
def purchase_update(request, pk):
    purchase = get_object_or_404(Purchases, pk=pk)
    purPdt = purchase.product
    purQty = purchase.quantity
    idPur = purchase.id
    print(idPur)
    if request.method == 'POST':
        data = dict()
        product = get_object_or_404(Product, namePdt=purPdt)
        print(purchase.quantity)
        print(product)

        form = PurchasesForm(request.POST, request.FILES, instance=purchase)
    else:
        form = PurchasesForm(instance=purchase)
    return save_purchase_update_form(request, form, pk, 'purchases/includes/partial_purchase_update.html')


# AVARIS VIEWS

@login_required
def avaris_list(request):
    avariss = Avaris.objects.all().order_by("-id")  # to order in descending order
    return render(request, 'avariss/avaris_list.html', {'avariss': avariss})


@login_required
def save_avaris_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            print("Hello")
            product = form.cleaned_data['product']
            quantity = form.cleaned_data['quantity']
            print(product)
            avaris = get_object_or_404(Product, namePdt=product)
            print(avaris)
            # form.save()
            if avaris:
                print(avaris.quantity)
                avaris.quantity -= quantity
                form.save()
                avaris.save()
                # messages.success(request, 'Avaris Saved !', extra_tags='alert')
            data['form_is_valid'] = True
            avariss = Avaris.objects.all().order_by("-id")
            paginator = Paginator(avariss, 12)
            data['html_avaris_list'] = render_to_string('avariss/includes/partial_avaris_list.html',
                                                        {'avariss': avariss})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


@login_required
def avaris_create(request):
    if request.method == 'POST':
        form = AvarisForm(request.POST, request.FILES)
    else:
        form = AvarisForm()
    return save_avaris_form(request, form, 'avariss/includes/partial_avaris_create.html')


@login_required
def save_avaris_update_form(request, form, pk, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            sentPdt = form.cleaned_data['product']
            purQty = form.cleaned_data['quantity']
            print('the Pk')
            print(sentPdt)
            avaris = get_object_or_404(Avaris, pk=pk)
            product = get_object_or_404(Product, namePdt=avaris.product)
            productDiff = get_object_or_404(Product, namePdt=sentPdt)
            if sentPdt == avaris.product:
                if purQty >= avaris.quantity:
                    print(avaris.quantity)
                    newQty = purQty - avaris.quantity
                    product.quantity -= newQty
                    print(product.quantity)
                    # print(product)
                    form.save()
                    product.save()
                else:
                    print(avaris.quantity)
                    newQty = avaris.quantity - purQty
                    product.quantity += newQty
                    print(product.quantity)
                    # print(product)
                    form.save()
                    product.save()
            else:
                product.quantity += avaris.quantity
                product.save()
                productDiff.quantity -= purQty
                productDiff.save()
                form.save()
            data['form_is_valid'] = True
            avariss = Avaris.objects.all().order_by("-id")
            data['html_avaris_list'] = render_to_string('avariss/includes/partial_avaris_list.html',
                                                        {'avariss': avariss})

        else:
            data['avaris_update'] = False
            data['form_error'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


@login_required
def avaris_update(request, pk):
    avaris = get_object_or_404(Avaris, pk=pk)
    purPdt = avaris.product
    purQty = avaris.quantity
    idPur = avaris.id
    print(idPur)
    if request.method == 'POST':
        data = dict()
        product = get_object_or_404(Product, namePdt=purPdt)
        print(avaris.quantity)
        print(product)

        form = AvarisForm(request.POST, request.FILES, instance=avaris)
    else:
        form = AvarisForm(instance=avaris)
    return save_avaris_update_form(request, form, pk, 'avariss/includes/partial_avaris_update.html')


# STOCK VIEWS

@login_required
def stock_list(request):
    # stocks = Profile.objects.all().order_by("id") # to order in ascending order
    stocks = Stock.objects.all().order_by("-id")  # to order in descending order
    return render(request, 'stocks/stock_list.html', {'stocks': stocks})


@login_required
def product_list_Stokc(request):
    # stocks = Profile.objects.all().order_by("id") # to order in ascending order
    pdts = Product.objects.all().first()  # to order in descending order
    return render(request, 'stocks/includes/partial_stock_form.html', {'pdts': pdts})


@login_required
def save_stock_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            products = Product.objects.all()
            # ct = products.count()
            # print(ct)
            stock = Stock()
            i = 1
            for pdt in products:
                stock.user = form.cleaned_data['user']
                stock.dateStock = now()
                stock.product = pdt.namePdt
                stock.stockType = form.cleaned_data['stockType']
                stock.quantity = pdt.quantity
                # print(stock.product)
                # print(stock.user)
                stock.save()
            data['save_stock'] = True
            data['form_is_valid'] = True
            stocks = Stock.objects.all().order_by("-id")
            paginator = Paginator(stocks, 12)
            data['html_stocks_list'] = render_to_string('stocks/includes/partial_stock_list.html', {'stocks': stocks})
        else:
            data['save_stock_error'] = True
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


@login_required
def stock_create(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
    else:
        form = StockForm()
    return save_stock_form(request, form, 'stocks/includes/partial_stock_create.html')


# TABS VIEWS

@login_required
def tab_list_closed(request, urs):
    # tabs = Tabs.objects.all().order_by("id") # to order in ascending order
    clo = 'Closed'
    tabs = Tabs.objects.filter(status__exact=clo, user__exact=urs).order_by("-id")  # to order in descending order
    # tabs = Tabs.objects.all().order_by("-id")  # to order in descending order
    return render(request, 'tabs/tab_list_closed.html', {'tabs': tabs})


@login_required
def tab_list(request, urs):
    # tabs = Tabs.objects.all().order_by("id") # to order in ascending order
    op = 'Open'
    tab = Tabs.objects.filter(status__exact=op, user__exact=urs).order_by("-id")  # to order in descending order
    tabs = tab.distinct().order_by('-id')
    # tabs = Tabs.objects.all().order_by("-id")  # to order in descending order
    return render(request, 'tabs/tab_list.html', {'tabs': tabs})


@login_required
def save_tab_form(request, form, urs, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            tab = Tabs()
            ordNum = NumbersOrder.objects.get()
            tab.user = form.cleaned_data['user']
            tab.dateOp = now()
            tab.orderNumber = ordNum.number
            tab.tableNum = form.cleaned_data['tableNum']
            tab.status = form.cleaned_data['status']
            ordNum.number += 1
            # tab.total = 0
            tab.save()
            ordNum.save()
            data['form_is_valid'] = True
            tabs = Tabs.objects.filter(user__exact=urs).order_by("-id")
            paginator = Paginator(tabs, 12)
            data['html_tab_list'] = render_to_string('tabs/includes/partial_tab_list.html', {'tabs': tabs})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


@login_required
def tab_create(request, urs):
    if request.method == 'POST':
        form = TabsForm(request.POST)
    else:
        form = TabsForm()
    return save_tab_form(request, form, urs, 'tabs/includes/partial_tab_create.html')


# Orders VIEWS

@login_required
def order_list_closed(request, pk, urs):
    # orders = Orders.objects.all().order_by("id") # to order in ascending order
    # print(pk)
    tab = get_object_or_404(Tabs, pk=pk)
    orders = Orders.objects.filter(orderNumber__exact=tab.orderNumber, user__exact=urs).order_by(
        '-id')  # to order in descending order
    total = orders.aggregate(total=Sum('amount'))
    print(total)

    print()
    return render(request, 'orders/order_list_closed.html', {'orders': orders, 'pk': pk, 'total': total})


@login_required
def order_list(request, pk, urs):
    # orders = Orders.objects.all().order_by("id") # to order in ascending order
    # print(pk)
    tab = get_object_or_404(Tabs, pk=pk)
    orders = Orders.objects.filter(orderNumber__exact=tab.orderNumber, user__exact=urs)  # to order in descending order
    print(tab.orderNumber)
    return render(request, 'orders/order_list.html', {'orders': orders, 'pk': pk})


@login_required
def save_order_form(request, form, pk, template_name):
    global ammt, amt
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            print('Pk from save is ' + pk)
            order = Orders()
            pdt = form.cleaned_data['product']
            qty = form.cleaned_data['quantity']
            tab = get_object_or_404(Tabs, pk=pk)
            product = get_object_or_404(Product, namePdt=pdt)
            if qty <= product.quantity:
                product.quantity -= qty
                print(tab.orderNumber)
                amount = qty * product.price
                # tot = tab.total + amount
                # tab.total = tot
                order.dateOp = now()
                order.product = pdt
                order.quantity = qty
                order.orderNumber = tab.orderNumber
                order.amount = amount
                order.status = form.cleaned_data['status']
                order.user = form.cleaned_data['user']
                order.save()
                product.save()
                # tab.save()
                data['form_is_valid'] = True
                tab = get_object_or_404(Tabs, pk=pk)
                orders = Orders.objects.filter(orderNumber=tab.orderNumber)  # to order in descending order
                # ct = count(order)
                # print(ct)
                # total = sum(order.amount, ct)
                # print(ct)
                # print(total)
                ammt = order.amount
                print(tab.orderNumber)
                paginator = Paginator(orders, 12)
                data['html_order_list'] = render_to_string('orders/includes/partial_order_list.html',
                                                           {'orders': orders, 'ammt': ammt})
            else:
                data['insufficient_product'] = True
                tab = get_object_or_404(Tabs, pk=pk)
                orders = Orders.objects.filter(orderNumber=tab.orderNumber)  # to order in descending order
                print(tab.orderNumber)
                print('insufficient Product')
                paginator = Paginator(orders, 12)
                data['html_order_list'] = render_to_string('orders/includes/partial_order_list.html',
                                                           {'orders': orders})
        else:
            data['form_is_valid'] = False
            data['form_error'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


@login_required
def order_create(request, pk):
    tab = get_object_or_404(Tabs, pk=pk)
    print('Tabs id ' + pk + ' ')
    print(tab)
    if request.method == 'POST':
        form = OrdersForm(request.POST, instance=tab)
    else:
        form = OrdersForm(instance=tab)
    return save_order_form(request, form, pk, 'orders/includes/partial_order_create.html')


@login_required
def order_delete(request, pk):
    order = get_object_or_404(Orders, pk=pk)
    data = dict()
    if request.method == 'POST':
        product = get_object_or_404(Product, namePdt=order.product)
        product.quantity += order.quantity
        product.save()
        order.delete()
        data['order_delete'] = True
        orders = Orders.objects.filter(orderNumber=order.orderNumber)
        paginator = Paginator(orders, 12)
        data['html_order_list'] = render_to_string('orders/includes/partial_order_list.html', {'orders': orders})
    else:
        context = {'order': order}
        data['html_form'] = render_to_string('orders/includes/partial_order_delete.html', context, request=request)
    return JsonResponse(data)


# Sales VIEWS

@login_required
def sale_list(request, pk):
    tab = get_object_or_404(Tabs, pk=pk)  # to order in ascending order
    saless = Orders.objects.filter(orderNumber=tab.orderNumber)  # to order in descending order
    return render(request, 'sales/sale_list.html', {'saless': saless, 'pk': pk})


@login_required
def save_sales_form(request, form, pk, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            msg = PrintMsg()
            sales = Sales()
            tab = get_object_or_404(Tabs, pk=pk)
            tabs = Tabs.objects.filter(pk=pk)
            order = Orders.objects.filter(orderNumber=tab.orderNumber)
            orders = Orders()
            if order:
                print("Exist")
                tab.status = 'Closed'
                tab.tableNum = tab.tableNum
                orders = order.filter(orderNumber__exact=tab.orderNumber)
                msg.status = 'Waiting'
                msg.orderNumber = tab.orderNumber
                msg.dateOp = now()
                sales.status = form.cleaned_data['status']
                sales.user = form.cleaned_data['user']
                sales.salesDate = now()
                sales.customer = form.cleaned_data['customer']
                sales.paid = form.cleaned_data['paid']
                sales.amount = form.cleaned_data['paid']
                sales.invoiceNumber = tab.orderNumber
                # sales.custmerSign = form.cleaned_data['custmerSign']
                sales.save()
                msg.save()
                for ord in orders:
                    ord.status = 'Closed'
                    ord.save()
                tab.save()

                # form.save()
                # messages.success(request, 'Sales Saved !', extra_tags='alert')
                data['form_is_valid'] = True
                saless = Sales.objects.all().order_by("-id")
                paginator = Paginator(saless, 12)
                data['html_sales_list'] = render_to_string('sales/includes/partial_sales_list.html', {'saless': saless})
            else:
                data['form_is_valid'] = False
                saless = Sales.objects.all().order_by("-id")
                paginator = Paginator(saless, 12)
                data['html_sales_list'] = render_to_string('sales/includes/partial_sales_list.html', {'saless': saless})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


@login_required
def sale_create(request, pk):
    tab = get_object_or_404(Tabs, pk=pk)
    print(pk)
    if request.method == 'POST':
        form = SalesForm(request.POST, request.FILES, instance=tab)
    else:
        form = SalesForm(instance=tab)
    return save_sales_form(request, form, pk, 'sales/includes/partial_sale_create.html')


@login_required
def sale_update(request, pk):
    sales = get_object_or_404(Sales, pk=pk)
    if request.method == 'POST':
        form = SalesForm(request.POST, instance=sales)
        # data['sales_update'] = True
    else:
        form = SalesForm(instance=sales)
    return save_sales_form(request, form, 'sales/includes/partial_sale_update.html')


@login_required
def print_list(request):
    # profiles = Profile.objects.all().order_by("id") # to order in ascending order
    op = 'Waiting'
    prints = PrintMsg.objects.filter(status__exact=op).order_by("-id")  # to order in descending order
    return render(request, 'prints/print_list.html', {'prints': prints})


@login_required
def printed_list_msg(request):
    # profiles = Profile.objects.all().order_by("id") # to order in ascending order
    op = 'Printed'
    prints = PrintMsg.objects.filter(status__exact=op).order_by("-id")  # to order in descending order
    return render(request, 'prints/print_list_printed.html', {'prints': prints})


# @login_required
# def print_list_pdf(request, pk, *args, **kwargs):
#     # orders = Orders.objects.all().order_by("id") # to order in ascending order
#     orders = Orders.objects.filter(orderNumber__exact=pk).annotate(money=Sum('amount'))  # to order in descending order
#     sales = Sales.objects.filter(invoiceNumber__exact=pk)
#     total = orders.annotate(money=Sum('amount'))
#     prtMsg = get_object_or_404(PrintMsg, orderNumber__exact=pk)
#     prtMsg.status = 'Printed'
#     prtMsg.save()
#     html = render(request, 'prints/includes/partial_print_waiting.html',
#                   {'orders': orders, 'pk': pk, 'sales': sales, 'total': total})
#     pdf = render_to_pdf('prints/includes/partial_print_waiting.html',
#                         {'orders': orders, 'pk': pk, 'sales': sales, 'total': total})
#     return HttpResponse(pdf, content_type='application/pdf')

@login_required
def print_list_pdf(request, pk):
    orders = Orders.objects.filter(orderNumber__exact=pk).order_by('-id')  # to order in descending order
    sales = Sales.objects.filter(invoiceNumber__exact=pk)
    total = Orders.objects.filter(orderNumber__exact=pk).aggregate(sum=Sum('amount'))['sum']
    prtMsg = get_object_or_404(PrintMsg, orderNumber__exact=pk)
    prtMsg.status = 'Printed'
    prtMsg.save()
    return render(request, 'prints/includes/partial_print_waiting.html', {'orders': orders, 'pk': pk, 'sales': sales, 'total': total})
    # return Response({"orders": serializer.data, "total": total_amt})


# @login_required
# def printed_list_pdf(request, pk, *args, **kwargs):
#     orders = Orders.objects.filter(orderNumber__exact=pk).annotate(money=Sum('amount'))  # to order in descending order
#     sales = Sales.objects.filter(invoiceNumber__exact=pk)
#     total = orders.annotate(money=Sum('amount'))
#     html = render(request, 'prints/includes/partial_print_waiting.html',
#                   {'orders': orders, 'pk': pk, 'sales': sales, 'total': total})
#     pdf = render_to_pdf('prints/includes/partial_print_waiting.html',
#                         {'orders': orders, 'pk': pk, 'sales': sales, 'total': total})
#     return HttpResponse(pdf, content_type='application/pdf')


@login_required
def printed_list_pdf(request, pk):
    orders = Orders.objects.filter(orderNumber__exact=pk).order_by('-id')  # to order in descending order
    sales = Sales.objects.filter(invoiceNumber__exact=pk)
    total = Orders.objects.filter(orderNumber__exact=pk).aggregate(sum=Sum('amount'))['sum']
    return render(request, 'prints/includes/partial_print_waiting.html', {'orders': orders, 'pk': pk, 'sales': sales, 'total': total})
    # return Response({"orders": serializer.data, "total": total_amt})



# Attendance VIEWS

@login_required
def attendance_list(request):
    attendances = Attendance.objects.all().order_by("-id")  # to order in descending order
    return render(request, 'attendances/attendance_list.html', {'attendances': attendances})


@login_required
def clock_in_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            print("Hello")
            data['form_is_valid'] = True
            attend = Attendance()
            attend.user = form.cleaned_data['user']
            attend.actDate = now().today().date()
            chk = Attendance.objects.filter(user__exact=attend.user, actDate__exact=attend.actDate)
            if chk:
                data['attendance_clockin_err'] = True
                data['html_attendance_list'] = render_to_string('homep/home.html')
            else:
                attend.user = form.cleaned_data['user']
                attend.actDate = now().today().date()
                attend.month = now().month
                attend.clockIn = now().hour
                attend.clockinHr = now().minute
                attend.status = 'Clocked In'
                attend.save()
                data['attendance_clockin'] = True
                data['html_attendance_list'] = render_to_string('homep/home.html')

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


@login_required
def attendance_clockin(request):
    months = now().month
    hrs = now().hour
    minu = now().minute
    day = now().today().date()
    print(months)
    print(day)
    print(hrs)
    print(minu)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, request.FILES)
    else:
        form = AttendanceForm()
    return clock_in_form(request, form, 'attendances/includes/partial_attendance_clockin.html')


@login_required
def clock_out_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            print("Hello")
            data['form_is_valid'] = True
            attend = Attendance()
            attend.user = form.cleaned_data['user']
            attend.actDate = now().today().date()
            chk = get_object_or_404(Attendance, user__exact=attend.user, actDate__exact=attend.actDate)
            if chk:
                chk.clockOut = now().hour
                chk.clockoutHr = now().minute
                chk.status = 'Clocked In Clocked Out'
                minutes = int(chk.clockoutHr - chk.clockinHr) / 60
                hours = chk.clockOut - chk.clockIn
                chk.hours = minutes + hours
                attend.save()
                data['attendance_clockout'] = True
                data['html_attendance_list'] = render_to_string('homep/home.html')

            else:
                data['attendance_clockout_err'] = True
                data['html_attendance_list'] = render_to_string('homep/home.html')

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


@login_required
def attendance_clockout(request):
    months = now().month
    hrs = now().hour
    minu = now().minute
    day = now().today().date()
    print(months)
    print(day)
    print(hrs)
    print(minu)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, request.FILES)
    else:
        form = AttendanceForm()
    return clock_in_form(request, form, 'attendances/includes/partial_attendance_clockin.html')


@login_required
def profile_list(request):
    # profiles = Profile.objects.all().order_by("id") # to order in ascending order
    users = User.objects.all().order_by("-id")  # to order in descending order
    return render(request, 'profiles/profile_list.html', {'users': users})


# Charts For Report

@login_required
def reports(request):
    # departments = Department.objects.all().order_by("id") # to order in ascending order
    departments = Department.objects.all().order_by("-id")  # to order in descending order
    return render(request, 'reports/reports_list.html', {'departments': departments})


@login_required
def product_report(request):
    return render(request, 'reports/product_reports.html')


class ProductStats(APIView):
    def get(self, request, format=None):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)


@login_required
def cash_out_stat(request):
    return render(request, 'reports/cash_out_flows_reports.html')


class CashOutStats(APIView):
    def get(self, request, format=None):
        loss = Loss.objects.all()
        # expense = Expense.objects.all()
        # serializer1 = ExpenseSerializer(expense, many=True)
        serializer = LossSerializer(loss, many=True)
        # return JsonResponse({"serializer ":serializer.data, "serializer1 ": serializer1.data}, safe=False)
        return JsonResponse(serializer.data, safe=False)


class ExpenseStats(APIView):
    def get(self, request, format=None):
        loss = Loss.objects.all()
        expense = Expense.objects.all()
        serializer = ExpenseSerializer(expense, many=True)
        return JsonResponse(serializer.data, safe=False)


class AvarisStats(APIView):
    def get(self, request, format=None):
        avaris = Avaris.objects.all()
        serializer = AvarisSerializer(avaris, many=True)
        return JsonResponse(serializer.data, safe=False)


@login_required
def purchase_statistic(request):
    return render(request, 'reports/purchase_reports.html')


class PurchasesStats(APIView):
    def get(self, request, format=None):
        user = self.request.user
        purchases = Purchases.objects.all()
        serializer = PurchasesSerializer(purchases, many=True)
        return JsonResponse(serializer.data, safe=False)


class AttendStats(APIView):
    def get(self, request, format=None):
        user = self.request.user
        attend = Attendance.objects.filter(user=user).order_by('-id')
        serializer = AttendanceSerializer(attend, many=True)
        return JsonResponse(serializer.data, safe=False)