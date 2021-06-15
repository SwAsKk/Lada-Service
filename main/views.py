from django.shortcuts import render

from main.models import *
from main.forms import *
from django.views import View
from django.http import HttpResponseRedirect
from main.docwriter import doc_template_render

# Create your views here.

# Функции - просмотра страниц


def base_context(request):
    context = dict()
    context['user'] = request.user
    return context

def index(request):
    """ Функция покааза первой странички"""
    c = base_context(request)
    c['title'] = 'LADA Service'
    
    return render(request, 'index.html', c)


def print_contract(request, id):
    con = Contract.objects.get(id=id)
    return HttpResponseRedirect(doc_template_render(con))


def branches(request):
    c = base_context(request)
    
    
    br = Branch.objects.all()
    
    c['branch_list'] = br

    return render(request, 'branch/branches.html', c)
    
def clients(request):
    c = base_context(request)
    
    
    cl = Client.objects.all()
    
    c['client_list'] = cl 
    
    return render(request, 'client/clients.html', c)
    
def consultants(request):
    c = base_context(request)
    
    co = Consultant.objects.all()
    
    c['consultant_list'] = co
    
    return render(request, 'consultant/consultants.html', c)

def contracts(request):
	c = base_context(request)
	
	con = Contract.objects.all()
	c['contract_list'] = con
	return render(request, 'contract/contracts.html', c)
	
def cars(request):
    c = base_context(request)
    
    cr = Car.objects.all()
    c['car_list'] = cr
    return render(request, 'car/cars.html', c)


class ContractAdd(View):
	def get(self,request):
		contract = CreateContractForm()
		c = base_context(request)
		
		c['contract_add'] = contract
		return render(request, 'contract/contract-add.html', c)
		
	def post(self,request):
		contract = CreateContractForm(request.POST)
		
		c = base_context(request)
		
		c['contract-add'] = contract
		
		if contract.is_valid():
			new_contract = contract.save()
			return HttpResponseRedirect('/contracts/')
		return render(request, 'contract/contract-add.html', c)
           
class BranchAdd(View):
    def get(self,request):
        branch = CreateBranchForm()
        c = base_context(request)
        
        c['branch_add'] = branch
        return render(request, 'branch/branch-add.html', c)
       
        
    def post(self,request):
        branch = CreateBranchForm(request.POST)
        
        c = base_context(request)
        
        c['branch_add'] = branch
        
        if branch.is_valid():
            new_branch = branch.save()
            return HttpResponseRedirect('/branches/')
            
        return render(request, 'branch/branch-add.html', c)   
        
class CarAdd(View):
    def get(self,request):
        car = CreateCarForm()
        c = base_context(request)
        
        c['car_add'] = car
        return render(request, 'car/car-add.html', c)
        
    def post(self,request):
        car = CreateCarForm(request.POST)
        c = base_context(request)
        
        c['car_add'] = car 
        
        if car.is_valid():
            new_car = car.save()
            return HttpResponseRedirect('/cars/')
        return render(request, 'car/car-add.html', c) 
        
class ClientAdd(View):
    def get(self,request):
        client = CreateClientForm()
        c = base_context(request)
        
        c['client_add'] = client
        return render(request, 'client/client-add.html', c)
        
    def post(self,request):
        client = CreateClientForm(request.POST)
        c = base_context(request)
        
        c['client_add'] = client
        
        if client.is_valid():
            new_client = client.save()
            return HttpResponseRedirect('/clients/')
        return render (request, 'client/client-add.html', c)
		
class ConsultantAdd(View):
	def get(self,request):
		consultant = CreateConsultantForm()
		c = base_context(request)
		
		c['consultant_add'] = consultant
		return render(request, 'consultant/consultant-add.html', c)
		
	def post(self,request):
		consultant = CreateConsultantForm(request.POST)
		c = base_context(request)
		
		c['consultant_add'] = consultant
		
		if consultant.is_valid():
			new_consultant = consultant.save()
			return HttpResponseRedirect('/consultants/')
		return render(request, 'consultant/consultant-add.html', c)
		
        
class ConsultantDetails(View):
	def get(self,request,id):
		consultant = Consultant.objects.get(id = id)
		return render(request, 'consultant/consultant-details.html', context={'consultant': consultant})

class ConsultantUpdate(View):
    def get(self, request, id):
        cons = Consultant.objects.get(id = id)
        initial_dict = {
            'branch': cons.branch,
            'fullname': cons.fullname,
            'dateofbirth': cons.dateofbirth,
        }
        form = CreateConsultantForm(initial = initial_dict)
        return render(request, 'consultant/consultant-edit.html', context={'consultant_add':form, 'consultant':cons})
    def post(self,request,id):
        cons = Consultant.objects.get(id = id)
        form = CreateConsultantForm(request.POST)

        if form.is_valid():
            update_cons = form.update(cons)
            return HttpResponseRedirect('/consultants/') 
        return render(request, 'consultant/consultant-edit.html', context={'consultant_add':form, 'consultant':cons})

class ConsultantDelete(View):
    def get(self,request,id):
        Consultant.objects.get(id = id).delete()
        return HttpResponseRedirect('/consultants/')


class BranchDetails(View):
    def get(self,request,id):
        branch = Branch.objects.get(id = id)
        return render(request, 'branch/branch-details.html', context={'branch':branch})

class BranchUpdate(View):
    def get(self, request, id):
        br = Branch.objects.get(id = id)
        initial_dict = {
            'name': br.name,
            'commandor': br.commandor,
            'inn': br.inn,
            'adress': br.adress,
            'phone': br.phone,
            'parking': br.parking,
        }
        form = CreateBranchForm(initial = initial_dict)
        return render(request, 'branch/branch-edit.html', context={'branch_add':form, 'branch':br})
    def post(self,request,id):
        br = Branch.objects.get(id = id)
        form = CreateBranchForm(request.POST)

        if form.is_valid():
            update_br = form.update(br)
            return HttpResponseRedirect('/branches/') 
        return render(request, 'branch/branch-edit.html', context={'branch_add':form, 'branch':br})

class BranchDelete(View):
    def get(self,request,id):
        Branch.objects.get(id = id).delete()
        return HttpResponseRedirect('/branches/')    


class ClientDetails(View):
    def get(self,request,id):
        client = Client.objects.get(id = id)
        return render(request, 'client/client-details.html', context={'client':client})

class ClientUpdate(View):
    def get(self, request, id):
        cl = Client.objects.get(id = id)
        initial_dict = {
            'fullname': cl.fullname,
            'passport': cl.passport,
            'bankname': cl.bankname,
            'banknumber': cl.banknumber,
            'sign': cl.sign
        }
        form = CreateClientForm(initial=initial_dict)
        return render(request, 'client/client-edit.html', context={'client_add':form, 'client':cl})
    def post(self,request,id):
        cl = Client.objects.get(id = id)
        form = CreateClientForm(request.POST)

        if form.is_valid():
            update_cl = form.update(cl)
            return HttpResponseRedirect('/clients/') 
        return render(request, 'client/client-edit.html', context={'client_add':form, 'client':cl})

class ClientDelete(View):
    def get(self,request,id):
        Client.objects.get(id = id).delete()
        return HttpResponseRedirect('/clients/')  


class CarDetails(View):
    def get(self,request,id):
        car = Car.objects.get(id = id)
        return render(request, 'car/car-details.html', context={'car':car})

class CarUpdate(View):
    def get(self, request, id):
        cr = Car.objects.get(id = id)
        initial_dict = {
            'brand': cr.brand,
            'model': cr.model,
            'bodymodel': cr.bodymodel,
            'wheelposition': cr.wheelposition,
            'drivebool': cr.drivebool,
            'type': cr.type,
            'bodytype': cr.bodytype,
            'bodynumber': cr.bodynumber,
            'enginenumber': cr.enginenumber,
            'enginevolume': cr.enginevolume,
            'enginepower': cr.enginepower,
            'price': cr.price,
            'year': cr.year,
            'mileage': cr.mileage
        }
        form = CreateCarForm(initial=initial_dict)
        return render(request, 'car/car-edit.html', context={'car_add':form, 'car':cr})
    def post(self,request,id):
        cr = Car.objects.get(id = id)
        form = CreateCarForm(request.POST)

        if form.is_valid():
            update_cr = form.update(cr)
            return HttpResponseRedirect('/cars/') 
        return render(request, 'car/car-edit.html', context={'car_add':form, 'car':cr})

class CarDelete(View):
    def get(self,request,id):
        Car.objects.get(id = id).delete()
        return HttpResponseRedirect('/cars/')  


class ContractDetails(View):
    def get(self,request,id):
        contract = Contract.objects.get(id = id)
        return render(request, 'contract/contract-details.html', context={'contract':contract})

class ContractUpdate(View):
    def get(self, request, id):
        cn = Contract.objects.get(id = id)
        initial_dict = {
            'client': cn.client,
            'consultant': cn.consultant,
            'branch': cn.branch,
            'car': cn.car,
        }
        form = CreateContractForm(initial=initial_dict)
        return render(request, 'contract/contract-edit.html', context={'contract_add':form, 'contract':cn})
    def post(self,request,id):
        cn = Contract.objects.get(id = id)
        form = CreateContractForm(request.POST)

        if form.is_valid():
            update_cn = form.update(cn)
            return HttpResponseRedirect('/contracts/') 
        return render(request, 'contract/contract-edit.html', context={'contract_add':form, 'contract':cn})

class ContractDelete(View):
    def get(self,request,id):
        Contract.objects.get(id = id).delete()
        return HttpResponseRedirect('/contracts/')  

