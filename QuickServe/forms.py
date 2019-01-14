from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from QuickServe.models import Attendance, Agency, Department, Profile, Menu, Category, Product, Expense, Loss, Bonus, \
    Deductions, Purchases, Avaris, Stock, Orders, Tabs, Sales


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ('user', 'clockIn', 'clockinHr', 'clockoutHr', 'clockOut', 'hours', 'month', 'actDate', 'status',)


class AgencyForm(forms.ModelForm):
    # pass
    class Meta:
        model = Agency
        fields = ('agency', 'agencyAddress', 'agencyTelephone',)


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('department', 'dptSpecification', 'dptMinsalary', 'dptPaymentRaise', 'dpthourlySalary', 'doc',)


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class ExtraForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('agency', 'department', 'phone', 'address', 'empCode', 'birthDate', 'birthPlace', 'role', 'picture',)


class MenuForm(forms.ModelForm):
    # pass
    class Meta:
        model = Menu
        fields = ('name', 'typeMenu',)


class CategoryForm(forms.ModelForm):
    # pass
    class Meta:
        model = Category
        fields = ('user', 'menu', 'nameCat', 'status',)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('user', 'category', 'namePdt', 'price', 'quantity', 'minimum', 'status',)


class PdtUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('id',)


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('user', 'amount', 'dateExp', 'reason',)


class LossForm(forms.ModelForm):
    class Meta:
        model = Loss
        fields = ('user', 'reason', 'amount', 'dateOp', 'item', 'quantity')


class BonusForm(forms.ModelForm):
    class Meta:
        model = Bonus
        fields = ('user', 'amount', 'reason', 'dateBonus', 'empCode')


class DeductionsForm(forms.ModelForm):
    class Meta:
        model = Deductions
        fields = ('user', 'empCode', 'reason', 'amount', 'dateDeduction')


class PurchasesForm(forms.ModelForm):
    # justification = forms.ImageField()

    class Meta:
        model = Purchases
        fields = ('user', 'product', 'quantity', 'amount', 'dateOp',)


class AvarisForm(forms.ModelForm):
    class Meta:
        model = Avaris
        fields = ('user', 'product', 'quantity', 'reason', 'dateOp')


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ('user', 'product', 'quantity', 'stockType', 'dateStock')


class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('user', 'product', 'orderNumber', 'quantity', 'amount', 'status', 'dateOp')


class TabsForm(forms.ModelForm):
    class Meta:
        model = Tabs
        fields = ('user', 'tableNum', 'orderNumber', 'status', 'dateOp')


class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ('user', 'amount', 'paid', 'invoiceNumber', 'customer', 'status', 'salesDate')
