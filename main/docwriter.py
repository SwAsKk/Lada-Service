from docx import Document
from docxtpl import DocxTemplate

from shutil import copyfile
from copy import deepcopy
import os
import sys
from datetime import date


def direct_insert(doc_dest, doc_src):
    for p in doc_src.paragraphs:
        inserted_p = doc_dest._body._body._insert_p(p._p)
        if p._p.get_or_add_pPr().numPr:
            inserted_p.style = "ListNumber"

def doc_template_render(contract):
    day = date.today().strftime('%d')
    month = date.today().strftime('%m')
    year = date.today().strftime('%Y')
    
    client = contract.client
    consultant = contract.consultant
    car = contract.car
    
    data_d = {
        'day': day,
        'month': month,
        'year': year,
        'con_fullname': consultant.fullname,
        'con_address': consultant.branch.adress,
        'cli_fullname': client.fullname,
        'con_branch': consultant.branch.name,
        'cli_passport': client.passport,
        'car_brand': car.brand,
        'car_model': car.model,
        'car_year': car.year,
        'car_engnumber': car.enginenumber,
        'car_bdynumber': car.bodynumber,
        'car_price': car.price,
    }
    
    # Replace text from docx
    copyfile('main/ContractOffer.docx', 'media/Contract' + str(contract.id) + '.docx')
    doc_copy = DocxTemplate('media/Contract' + str(contract.id) + '.docx')
    doc_copy.render(data_d)
    doc_copy.save('media/Contract' + str(contract.id) + '.docx')
    
    return '/media/Contract' + str(contract.id) + '.docx'

