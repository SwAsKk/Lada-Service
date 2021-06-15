from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Branch(models.Model):
    # br name
    # br inn
    # br commandor
    # br adress
    # br phone 
    # br parking
    
    name = models.CharField(
        # Название на русском Для админки и лэйблов
        verbose_name = 'Название',
        
        # Макс. длина
        max_length = 50,
        
        # NOT NULL
        null = False,
        blank = False,
    )
    
    commandor = models.CharField(
        verbose_name = 'Руководитель',
        max_length = 50,
        null = False,
        blank = False,
    )
    
    inn = models.CharField(
        verbose_name = 'ИНН',
        max_length = 17,
        null = False,
        blank = False,
    )
    
    adress = models.CharField(
        verbose_name = 'Адресс',
        max_length = 50,
        null = False,
        blank = False,
    )
    
    phone = models.CharField(
        verbose_name = 'Телефон',
        max_length = 11,
        null = False,
        blank = False,
    )
    
    parking = models.IntegerField(
        verbose_name = 'Парк.места',
        default = 100,
        null = False,
        blank = False,
    )

    def get_absolute_url(self):
	    return reverse('branch_details_url', kwargs = {'id': self.id})

    def get_update_url(self):
	    return reverse('branch_edit_url', kwargs = {'id': self.id})

    def get_delete_url(self):
        return reverse('branch_delete_url', kwargs = {'id':self.id})
		
    
    # Если надо представить в виде строки
    def __str__(self):
        return '{} - {}'.format(self.id, self.name, self.commandor)
        
    class Meta:
        # Название на русском для админки для целого класса
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'

class Client(models.Model):
    # cl fullname
    # cl passport
    # cl bank 
    # cl banknumber
    # cl sign
    
    fullname = models.CharField(
        verbose_name = 'ПолноеИмя', 
        max_length = 50,
        null = False, 
        blank = False,
        default = '',
    )
    
    
    passport = models.CharField(
        verbose_name = 'Паспорт',
        max_length = 10,
        null = False, 
        blank = False,
        default = '',
    )
    
    bankname = models.CharField(
        verbose_name = 'Банк',
        max_length = 25,
        null = False, 
        blank = False,
        default = '',
    )
    
    
    
    banknumber = models.CharField(
        verbose_name = 'БанковскийСчёт',
        max_length = 20,
        null = False, 
        blank = False,
        default = '', 
    )
    
    sign = models.CharField(
        verbose_name = 'ЮридическийПризнак',
        max_length = 10,
        null = False, 
        blank = False,
        default = '',
    )
    
    
    def get_absolute_url(self):
	    return reverse('client_details_url', kwargs = {'id': self.id})

    def get_update_url(self):
	    return reverse('client_edit_url', kwargs = {'id': self.id})

    def get_delete_url(self):
        return reverse('client_delete_url', kwargs = {'id':self.id})


    def __str__(self):
        return '{} - {}'.format(self.fullname, self.passport)

    
        
    class Meta:
        # Название на русском для админки для целого класса
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class Consultant(models.Model):
    #co fullname 
    #co dateofbirth
    #co branchid
    
    branch = models.ForeignKey(
        to = Branch,
        on_delete = models.CASCADE,
        verbose_name = 'Номер филиала',
        null = False,
    )
    
    fullname = models.CharField(
        verbose_name = 'Полное имя',
        max_length = 50, 
        null = False, 
        blank = False, 
        default = '',
    )
    
    dateofbirth  = models.DateField( 
        verbose_name = 'Дата рождения',
        null = False, 
        blank = False,
    )
    def get_absolute_url(self):
	    return reverse('consultant_details_url', kwargs = {'id': self.id})

    def get_update_url(self):
	    return reverse('consultant_edit_url', kwargs = {'id': self.id})

    def get_delete_url(self):
        return reverse('consultant_delete_url', kwargs = {'id':self.id})
		
    def __str__(self):
        return '{} - {}'.format(self.fullname, self.dateofbirth)
        
    class Meta:
        # Название на русском для админки для целого класса
        verbose_name = 'Консультант'
        verbose_name_plural = 'Консультанты'
 
class Car(models.Model):
#cr Brand (CharField, 20)
#cr Model (CharField, 20)
#cr BodyModel (CharField, 20)
#cr WheelPosition (CharField, 10)
#cr DriveBool (CharField, 5)
#cr Type (CharField, 8)
#cr BodyType (CharField, 20)
#cr BodyNumber (IntegerField)
#cr EngineNumber(IntegerField)
#cr EngineVolume(IntegerField)
#cr EnginePower(IntegerField)
#cr Price(IntegerField)
#cr Year(IntegerField)
#cr mileage (IntegerField)


    brand = models.CharField(
        verbose_name = 'Бренд',
        max_length = 20,
        null = False, 
        blank = False, 
        default = '',
    )
    
    model = models.CharField(
        verbose_name = 'Модель',
        max_length = 20,
        null = False, 
        blank = False, 
        default = '',
    )
    
    bodymodel = models.CharField(
        verbose_name = 'Модель кузова',
        max_length = 20,
        null = False, 
        blank = False, 
        default = '',
    )
    
    wheelposition = models.CharField(
        verbose_name = 'Позиция руля',
        max_length = 10, 
        null = False,
        blank = False, 
        default = '',
    )
    drivebool = models.CharField(
        verbose_name = 'Полный привод',
        max_length = 5,
        null = False, 
        blank = False,
        default = '',
    )
    type = models.CharField(
        verbose_name = 'Тип',
        max_length = 8,
        null = False, 
        blank = False, 
        default = '',
    )
    bodytype = models.CharField(
        verbose_name = 'Тип кузова',
        max_length = 20, 
        null = False, 
        blank = False, 
        default = '',
    )
    
    bodynumber = models.IntegerField(
        verbose_name = 'Номер кузова',
        null = False, 
        blank = False,
    )
    
    enginenumber = models.IntegerField(
        verbose_name = 'Номер двигателя',
        null = False,
        blank = False,
    )
    enginevolume = models.IntegerField(
        verbose_name = 'Объём двигателя',
        null = False,
        blank = False,
    )
    enginepower = models.IntegerField(
        verbose_name = 'Мощность двигателя',
        null = False, 
        blank = False,
    )
    price = models.IntegerField(
        verbose_name = 'Цена',
        null = False,
        blank = False,
    )
    year = models.IntegerField(
        verbose_name = 'Год выпуска',
        null = False, 
        blank = False,
    )
    mileage = models.IntegerField(
        verbose_name = 'Милиаж',
        null = False, 
        blank = False,
    )

    def get_absolute_url(self):
	    return reverse('car_details_url', kwargs = {'id': self.id})

    def get_update_url(self):
	    return reverse('car_edit_url', kwargs = {'id': self.id})

    def get_delete_url(self):
        return reverse('car_delete_url', kwargs = {'id':self.id})

    def __str__(self):
        return '{}. {} - {}'.format(self.id, self.brand, self.model)
        
	
	
    class Meta:
        # Название на русском для админки для целого класса
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
    
class Contract(models.Model):
#consultantid
#clientid
#branchid
#carid

    client = models.ForeignKey(
        to = Client,
        on_delete = models.CASCADE,
        verbose_name = 'Номер клиента',
        null = False,
    )
	
    consultant = models.ForeignKey(
        to = Consultant, 
        on_delete = models.CASCADE, 
        verbose_name = 'Номер консультанта',
        null = False,
    )
	
    branch = models.ForeignKey(
        to = Branch, 
        on_delete = models.CASCADE,
        verbose_name = 'Номер филиала',
        null = False,
    )
	
    car = models.ForeignKey(
        to = Car,
        on_delete = models.CASCADE,
        verbose_name = 'Номер машины',
        null = False,
    )

    
    def get_absolute_url(self):
	    return reverse('contract_details_url', kwargs = {'id': self.id})

    def get_update_url(self):
	    return reverse('contract_edit_url', kwargs = {'id': self.id})

    def get_delete_url(self):
        return reverse('contract_delete_url', kwargs = {'id':self.id})

    def get_print_url(self):
        return reverse('print_contract_url', kwargs = {'id':self.id})

    def __str__(self):
        return '{} - {}'.format(self.brand, self.model)
        

    

    class Meta:
        verbose_name = 'Контракт'
        verbose_name_plural = 'Контракты'










 