from django import forms

from main.models import *
from django.core.exceptions import ValidationError, ObjectDoesNotExist


class CreateBranchForm(forms.Form):
    name = forms.CharField(max_length=50)
    commandor = forms.CharField(max_length=50)
    inn = forms.CharField(max_length=17)
    adress = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=11)
    parking = forms.IntegerField()

    def clean_name(self):
        new_name = self.cleaned_data['name']
        if len(new_name) == 0:
            raise ValidationError('Имя не может быть пустым')
        elif len(new_name) >= 50:
            raise ValidationError('Имя не может быть больше 50')
        return new_name

    def clean_commandor(self):
        new_commandor = self.cleaned_data['commandor']
        if len(new_commandor) == 0:
            raise ValidationError('Имя руководителя не может быть пустым')
        elif len(new_commandor) >= 50:
            raise ValidationError('Имя руководителя не может быть больше 50')
        return new_commandor

    def clean_inn(self):
        new_inn = self.cleaned_data['inn']

        is_clean = True
        for c in new_inn:
            if not c.isdigit():
                is_clean = False
        if not is_clean:
            raise ValidationError('ИНН не может содержать букв')
        elif len(new_inn) == 0:
            raise ValidationError('ИНН не может быть пустым')
        elif len(new_inn) >= 17:
            raise ValidationError('ИНН не может быть больше 17 знаков')

        return new_inn

    def clean_adress(self):
        new_adress = self.cleaned_data['adress']
        if len(new_adress) == 0:
            raise ValidationError('Адрес не может быть пустым')
        elif len(new_adress) >= 50:
            raise ValidationError('Адрес не может быть больше 50 символов')
        return new_adress

    def clean_phone(self):
        new_phone = self.cleaned_data['phone']

        is_clean = True
        for h in new_phone:
            if not h.isdigit():
                is_clean = False
        if not is_clean:
            raise ValidationError('Номер не может содержать букв')
        elif len(new_phone) == 0:
            raise ValidationError('Номер не может быть пустым')
        elif len(new_phone) >= 12:
            raise ValidationError('Номер не может быть больше 11 символов')
        return new_phone

    def clean_parking(self):
        new_parking = self.cleaned_data['parking']

        if new_parking >= 5000:
            raise ValidationError('Число парковочных мест не может быть больше 5000!')
        elif new_parking <= 0:
            raise ValidationError('Число парковочных мест не может быть меньше нуля!)')
        return new_parking

    def save(self):
        new_branch = Branch.objects.create(
        name=self.cleaned_data['name'],
        commandor=self.cleaned_data['commandor'],
        inn=self.cleaned_data['inn'],
        adress=self.cleaned_data['adress'],
        phone=self.cleaned_data['phone'],
        parking=self.cleaned_data['parking'],
        )
        return new_branch

    def update(self,model):
        model.name = self.cleaned_data['name']
        model.commandor = self.cleaned_data['commandor']
        model.inn = self.cleaned_data['inn']
        model.adress = self.cleaned_data['adress']
        model.phone = self.cleaned_data['phone']
        model.parking = self.cleaned_data['parking']
        model.save()

    def delete(self,model):
        model.delete()


class CreateClientForm(forms.Form):
    fullname = forms.CharField(max_length=50)
    passport = forms.CharField(max_length=10)
    bankname = forms.CharField(max_length=25)
    banknumber = forms.CharField(max_length=20)
    sign = forms.CharField(max_length=10)

    def clean_fullname(self):
        new_fullname = self.cleaned_data['fullname']
        if len(new_fullname) == 0:
            raise ValidationError('Имя не может быть пустым!')
        elif len(new_fullname) >= 50:
            raise ValidationError('Имя не может быть больше 50 знаков!')
        return new_fullname

    def clean_passport(self):
        new_passport = self.cleaned_data['passport']

        is_clean = True
        for g in new_passport:
            if not g.isdigit():
                is_clean = False
            if not is_clean:
                raise ValidationError('Паспорт не может содержать букв')
            elif len(new_passport) == 0:
                raise ValidationError('Номер паспорта не может быть пустым!')
            elif len(new_passport) >= 11:
                raise ValidationError('Номер паспорта не может превышать 10 символов')
            return new_passport

    def clean_bankname(self):
        new_bankname = self.cleaned_data['bankname']
        if len(new_bankname) == 0:
            raise ValidationError('Название банка не может быть пустым')
        elif len(new_bankname) >= 25:
            raise ValidationError('Название банка не может быть больше 25 символов')
        return new_bankname

    def clean_banknumber(self):
        new_banknumber = self.cleaned_data['banknumber']

        is_clean = True
        for k in new_banknumber:
            if not k.isdigit():
                is_clean = False
            if not is_clean:
                raise ValidationError('Номер банковского счёта не может содержать буквы')
            elif len(new_banknumber) == 0:
                raise ValidationError('Номер банковского счёта не может быть пустым')
            elif len(new_banknumber) >= 20:
                raise ValidationError('Номер банковского счёта не может содержать больше 20 символов')
            return new_banknumber

    def clean_sign(self):
        new_sign = self.cleaned_data['sign']
        if len(new_sign) == 0:
            raise ValidationError('Юридический признак не может быть пустым')
        elif len(new_sign) >= 10:
            raise ValidationError('Юридический признак не может содержать больше 10 символов')
        return new_sign

    def save(self):
        new_client = Client.objects.create(
        fullname=self.cleaned_data['fullname'],
        passport=self.cleaned_data['passport'],
        bankname=self.cleaned_data['bankname'],
        banknumber=self.cleaned_data['banknumber'],
        sign=self.cleaned_data['sign']
        )
        return new_client

    def update(self,model):
        model.fullname = self.cleaned_data['fullname']
        model.passport = self.cleaned_data['passport']
        model.bankname = self.cleaned_data['bankname']
        model.banknumber = self.cleaned_data['banknumber']
        model.sign = self.cleaned_data['sign']
        model.save()

    def delete(self,model):
        model.delete()


class CreateCarForm(forms.Form):
    brand = forms.CharField(max_length=20)
    model = forms.CharField(max_length=20)
    bodymodel = forms.CharField(max_length=20)
    wheelposition = forms.CharField(max_length=10)
    drivebool = forms.CharField(max_length=5)
    type = forms.CharField(max_length=8)
    bodytype = forms.CharField(max_length=20)

    bodynumber = forms.IntegerField()
    enginenumber = forms.IntegerField()
    enginevolume = forms.IntegerField()
    enginepower = forms.IntegerField()
    price = forms.IntegerField()
    year = forms.IntegerField()
    mileage = forms.IntegerField()

    def clean_brand(self):
        new_brand = self.cleaned_data['brand']
        is_clean = True
        for a in new_brand:
            if not a.isalpha():
                is_clean = False
            if not is_clean:
                raise ValidationError('Бренд не может содержать цифр')
        if len(new_brand) == 0:
            raise ValidationError('Название бренда не может быть пустым')
        elif len(new_brand) >= 20:
            raise ValidationError('Название бренда не может содержать больше 20 знаков')
        return new_brand

    def clean_model(self):
        new_model = self.cleaned_data['model']
        if len(new_model) == 0:
            raise ValidationError('Название модели не может быть пустым')
        elif len(new_model) >= 20:
            raise ValidationError('Название модели не может содержать больше 20 символов')
        return new_model

    def clean_bodymodel(self):
        new_bodymodel = self.cleaned_data['bodymodel']
        if len(new_bodymodel) == 0:
            raise ValidationError('Модель кузова не может быть пустой!')
        elif len(new_bodymodel) >= 20:
            raise ValidationError('Модель кузова не может содержать больше 20 знаков')
        return new_bodymodel

    def clean_wheelposition(self):
        new_wheelposition = self.cleaned_data['wheelposition']
        is_clean = True
        for v in new_wheelposition:
            if not v.isalpha():
                is_clean = False
            if not is_clean:
                raise ValidationError('Позиия руля не может содержать цифры')
        if len(new_wheelposition) == 0:
            raise ValidationError('Позиция руля не может быть пустой')
        elif len(new_wheelposition) >= 10:
            raise ValidationError('Позиция руля не может содрежать больше 10 знаков')
        return new_wheelposition

    def clean_drivebool(self):
        new_drivebool = self.cleaned_data['drivebool']
        is_clean = True
        for y in new_drivebool:
            if not y.isalpha():
                is_clean = False
            if not is_clean:
                raise ValidationError('Наличие полного привода не может содержать цифр, у нас тут не единицы и нолики')
            if len(new_drivebool) == 0:
                raise ValidationError('Данный параметр не может быть пустым')
            elif len(new_drivebool) >= 5:
                raise ValidationError('Данный параметр не может превышать 5 символов (выбрать да\нет)')
            return new_drivebool

    def clean_type(self):
        new_type = self.cleaned_data['type']
        is_clean = True
        for s in new_type:
            if not s.isalpha():
                is_clean = False
            if not is_clean:
                raise ValidationError('Тип машины не может содержать цифр, ты что, робот?')
            if len(new_type) == 0:
                raise ValidationError('Тип машины не может быть пустым')
            elif len(new_type) >= 8:
                raise ValidationError('Тип машины не может быть больше 8 символов, или вы пишете роман в поле для ввода?')
            return new_type

    def clean_bodytype(self):
        new_bodytype = self.cleaned_data['bodytype']
        is_clean = True
        for t in new_bodytype:
            if not t.isalpha():
                is_clean = False
            if not is_clean:
                raise ValidationError('Робот, кажется ты начал захват планеты не с того места, тут не должно быть цифр')
            if len(new_bodytype) == 0:
                raise ValidationError('Тип кузова не может быть пустым!')
            elif len(new_bodytype) >= 20:
                raise ValidationError('Тип кузова не может содержать больше 20 символов')
            return new_bodytype

    def save(self):
        new_car = Car.objects.create(
        brand=self.cleaned_data['brand'],
        model=self.cleaned_data['model'],
        bodymodel=self.cleaned_data['bodymodel'],
        wheelposition=self.cleaned_data['wheelposition'],
        drivebool=self.cleaned_data['drivebool'],
        type=self.cleaned_data['type'],
        bodytype=self.cleaned_data['bodytype'],
        bodynumber=self.cleaned_data['bodynumber'],
        enginenumber=self.cleaned_data['enginenumber'],
        enginevolume=self.cleaned_data['enginevolume'],
        enginepower=self.cleaned_data['enginepower'],
        price=self.cleaned_data['price'],
        year=self.cleaned_data['year'],
        mileage=self.cleaned_data['mileage']
        )
        return new_car

    def update(self,model):
        model.brand = self.cleaned_data['brand']
        model.model = self.cleaned_data['model']
        model.bodymodel = self.cleaned_data['bodymodel']
        model.wheelposition = self.cleaned_data['wheelposition']
        model.drivebool = self.cleaned_data['drivebool']
        model.type = self.cleaned_data['type']
        model.bodytype = self.cleaned_data['bodytype']
        model.bodynumber = self.cleaned_data['bodynumber']
        model.enginenumber = self.cleaned_data['enginenumber']
        model.enginevolume = self.cleaned_data['enginevolume']
        model.enginepower = self.cleaned_data['enginepower']
        model.price = self.cleaned_data['price']
        model.year = self.cleaned_data['year']
        model.mileage = self.cleaned_data['mileage']
        model.save()

    def delete(self,model):
        model.delete()


class CreateConsultantForm(forms.Form):
    branch = forms.ModelChoiceField(queryset=Branch.objects.all())
    fullname = forms.CharField(max_length=50)
    dateofbirth = forms.DateField()

    def clean_fullname(self):
        new_fullname = self.cleaned_data['fullname']
        is_clean = True
        for h in new_fullname:
            if not h.isalpha():
                is_clean = False
            if not is_clean:
                raise ValidationError('Тут не может быть цифр, ты что, робот?')
            if len(new_fullname) == 0:
                raise ValidationError('Имя консультанта не может быть пустым!')
            elif len(new_fullname) >= 50:
                raise ValidationError('Имя консультанта не может содержать больше 50 символов')
            return new_fullname

	# Я сделал через ModelChoiceField
	# На заметку: вы пытались искать по имени, но надо потом не .objects.get(), там Queryset будет, достаточно просто .first()

    def save(self):
        branch = self.cleaned_data['branch']
        new_consultant = Consultant.objects.create(
        branch=branch,
        fullname=self.cleaned_data['fullname'],
        dateofbirth=self.cleaned_data['dateofbirth']
        )
        return new_consultant
    def update(self,model):
        model.branch = self.cleaned_data['branch']
        model.fullname = self.cleaned_data['fullname']
        model.dateofbirth = self.cleaned_data['dateofbirth']
        model.save()

    def delete(self,model):
        model.delete()


class CreateContractForm(forms.Form):
    client = forms.ModelChoiceField(queryset=Client.objects.all())
    consultant = forms.ModelChoiceField(queryset=Consultant.objects.all())
    branch = forms.ModelChoiceField(queryset=Branch.objects.all())
    car = forms.ModelChoiceField(queryset=Car.objects.all())
	
    def save(self):
        client = self.cleaned_data['client']
        consultant = self.cleaned_data['consultant']
        branch = self.cleaned_data['branch']
        car = self.cleaned_data['car']
        new_contract = Contract.objects.create(
        client = client,
        consultant = consultant,
        branch = branch,
        car = car
	    )
        return new_contract

    def update(self,model):
        model.client = self.cleaned_data['client']
        model.consultant = self.cleaned_data['consultant']
        model.branch = self.cleaned_data['branch']
        model.car = self.cleaned_data['car']
        model.save()

    def delete(self,model):
        model.delete()
         









    
    
