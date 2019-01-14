from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now


class Agency(models.Model):
    # pass
    agency = models.CharField(max_length=254, unique=True, null=False)
    agencyAddress = models.CharField(max_length=254, blank=True)
    agencyTelephone = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.agency


class Department(models.Model):
    department = models.CharField(max_length=254, unique=True, blank=True)
    dptSpecification = models.CharField(max_length=254, blank=True)
    dptMinsalary = models.DecimalField(max_digits=25, decimal_places=2)
    dptPaymentRaise = models.IntegerField(blank=True)
    dpthourlySalary = models.DecimalField(max_digits=25, decimal_places=2)
    doc = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.department

    def save(self, *args, **kwargs):  # Function to overide default save method
        if self.doc is None:
            self.doc = now()
        super(Department, self).save(*args, **kwargs)


class Profile(models.Model):
    CEO = 1
    ADMIN = 2
    MANAGER = 3
    PURCHASE = 4
    CASHIER = 5
    AVARIS = 6
    HUMANRESOURCE = 7
    OPERATION = 8
    WAITRESS = 9

    ROLES = ((CEO, 'Ceo'), (ADMIN, 'Admin'), (MANAGER, 'Branch Manager'), (PURCHASE, 'Purchase Manager'),
             (CASHIER, 'Cashier'), (AVARIS, 'Avaris'), (HUMANRESOURCE, 'Human Resource'), (OPERATION, 'Operation'),
             (WAITRESS, 'Waitress'),)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, related_name='agencys')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    phone = models.CharField(max_length=254, unique=True, blank=True)
    address = models.CharField(max_length=254, blank=True)
    empCode = models.CharField(max_length=254, unique=True, blank=True)
    picture = models.ImageField(null=True, upload_to="%Y/%m/%d")
    birthDate = models.DateField(blank=True, null=True)
    birthPlace = models.CharField(max_length=254, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLES, blank=True, null=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clockIn = models.CharField(max_length=98, blank=True, null=True)
    clockinHr = models.CharField(max_length=98, blank=True, null=True)
    clockOut = models.CharField(max_length=98, blank=True, null=True)
    clockoutHr = models.CharField(max_length=98, blank=True, null=True)
    hours = models.IntegerField(blank=True, null=True)
    month = models.CharField(max_length=98, null=True, blank=True)
    actDate = models.CharField(max_length=98, null=True, blank=True)
    status = models.CharField(max_length=254, blank=True)

    # def save(self, *args, **kwargs):  # Function to overide default save method
    #     if self.clockIn is None:
    #         self.clockIn = now()
    #     if self.clockOut is None:
    #         self.clockOut = now()
    #     if self.hours is None:
    #         self.hours = 0
    #     if self.month is None:
    #         self.month = now()
    #     super(Attendance, self).save(*args, **kwargs)


class Bonus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=25, decimal_places=2)
    reason = models.CharField(max_length=254, blank=True)
    dateBonus = models.DateField(null=True, blank=True)
    empCode = models.CharField(max_length=254, blank=True)

    def save(self, *args, **kwargs):  # Function to overide default save method
        if self.dateBonus is None:
            self.dateBonus = now()
        super(Bonus, self).save(*args, **kwargs)


class Menu(models.Model):
    name = models.CharField(max_length=254, unique=True, blank=True)
    typeMenu = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    nameCat = models.CharField(max_length=254, unique=True, blank=True)
    status = models.CharField(max_length=254, blank=True)

    def save(self, *args, **kwargs):  # Function to overide default save method
        if self.status is None:
            self.status = "Active"
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.nameCat


class Deductions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=25, decimal_places=2)
    reason = models.CharField(max_length=254, blank=True)
    dateDeduction = models.DateField(null=True, blank=True)
    empCode = models.CharField(max_length=254, blank=True)

    def save(self, *args, **kwargs):  # Function to overide default save method
        if self.dateDeduction is None:
            self.dateDeduction = now()
        super(Deductions, self).save(*args, **kwargs)


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=25, decimal_places=2)
    reason = models.CharField(max_length=254, blank=True)
    dateExp = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):  # Function to overide default save method
        if self.dateExp is None:
            self.dateExp = now()
        super(Expense, self).save(*args, **kwargs)


class LogFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    logOperation = models.CharField(max_length=254, blank=True)
    dateO = models.DateField(null=True, blank=True)
    logResult = models.CharField(max_length=254, blank=True)

    def save(self, *args, **kwargs):  # Function to overide default save method
        if self.dateO is None:
            self.dateO = now()
        super(LogFile, self).save(*args, **kwargs)


class Loss(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=254, blank=True)
    quantity = models.IntegerField(blank=True)
    amount = models.DecimalField(max_digits=25, decimal_places=2, blank=True)
    reason = models.CharField(max_length=254, blank=True)
    dateOp = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):  # Function to overide default save method
        if self.dateOp is None:
            self.dateOp = now()
        super(Loss, self).save(*args, **kwargs)


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    namePdt = models.CharField(max_length=254, unique=True, blank=True)
    price = models.DecimalField(max_digits=25, decimal_places=2, blank=True)
    quantity = models.IntegerField(blank=True)
    minimum = models.IntegerField(blank=True)
    status = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.namePdt


class NumbersOrder(models.Model):
    number = models.IntegerField(null=False)

    def __str__(self):
        return self.number


class CodeEmployee(models.Model):
    code = models.IntegerField(null=False)

    def __str__(self):
        return self.code


class Tabs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    tableNum = models.CharField(max_length=254, blank=True, null=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    dateOp = models.DateTimeField(null=True, blank=True)
    orderNumber = models.CharField(max_length=254, null=True, blank=True)

    # total = models.DecimalField(max_digits=25, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.orderNumber


class OrderTotal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    orderNumber = models.CharField(max_length=254, null=True, blank=True)
    dateOp = models.DateTimeField(null=True, blank=True)
    total = models.DecimalField(max_digits=25, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.total


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    # tabs = models.ForeignKey(Tabs, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE, blank=True, null=True)
    orderNumber = models.CharField(max_length=254, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=25, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    dateOp = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.orderNumber

    @property
    def product_name(self):
        return self.product.namePdt


class PrintMsg(models.Model):
    orderNumber = models.CharField(max_length=254, null=True, blank=True)
    status = models.CharField(max_length=254, null=True, blank=True)
    dateOp = models.DateTimeField(null=True, blank=True)
    totalSale = models.DecimalField(max_digits=25, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.orderNumber


class Avaris(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True)
    reason = models.CharField(max_length=254, blank=True)
    dateOp = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):  # Function to overide default save method
        if self.dateOp is None:
            self.dateOp = now()
        super(Avaris, self).save(*args, **kwargs)


class Purchases(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True)
    amount = models.DecimalField(max_digits=25, decimal_places=2, blank=True)
    # justification = models.ImageField(null=True, upload_to="%Y/%m/%d")
    dateOp = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):  # Function to overide default save method
        if self.dateOp is None:
            self.dateOp = now()
        super(Purchases, self).save(*args, **kwargs)

    @property
    def product_name(self):
        return self.product.namePdt


class Sales(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    invoiceNumber = models.CharField(max_length=254, null=True, blank=True)
    amount = models.DecimalField(max_digits=25, null=True, decimal_places=2, blank=True)
    paid = models.DecimalField(max_digits=25, null=True, decimal_places=2)
    salesDate = models.DateTimeField(null=True, blank=True)
    # custmerSign = models.ImageField(null=True, blank=True, upload_to="%Y/%m/%d")
    customer = models.CharField(max_length=254, null=True, blank=True)
    # totalSale = models.DecimalField(max_digits=25, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.invoiceNumber


class Stock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product = models.CharField(max_length=254, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    stockType = models.CharField(max_length=254, blank=True)
    dateStock = models.DateTimeField(null=True, blank=True)

    # def save(self, *args, **kwargs):  # Function to overide default save method
    #     if self.dateStock is None:
    #         self.dateStock = now()
    #     super(Stock, self).save(*args, **kwargs)
