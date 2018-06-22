from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from .models import Transaction
from .models import Wfdata

# Create your views here.
def index(request):
    #if 'action' in request.GET:
    #    action = request.GET['action']
    #    if action == 'load' :
    #        return HttpResponse('{"id1":{ "ttype": "ttype-1", "icode": "BDE43B34BE3", "desc": "Great Britain  adfasdfasdfadfasd", "bcode":"135670"}, "id2":{ "ttype": "ttype-2", "icode": "2343423ERWER", "desc": "Great Britain2 asdfadfasdfasdf", "bcode":"235670"}, "id3":{ "ttype": "ttype-3", "icode": "FGFG343434", "desc": "asdfadfasdf Great Britain3", "bcode":"345670"}, "id4":{ "ttype": "ttype-4", "icode": "_____FGFG343434", "desc": "___ Great Britain3 ___", "bcode":"345670"}}')
    #    elif action == 'save' :
    #        return HttpResponse('ok')
    #else:
    t_list = Wfdata.objects.all()
    output = "{"
    for tt in t_list:
        output += tt.getJSON()
    return HttpResponse(output)


def getTransactions(request):
    output = "{"
    try:
        transactions = Transaction.objects.order_by('iid')
        for t in transactions:
            output += t.getJSON() + ","
        output += "}"
    except Transaction.DoesNotExist:
        raise Http404("Question does not exist")
    return HttpResponse(output)

def saveData(request):
    _ttype = request.GET['ttype']
    _bcode = request.GET['bcode']
    _quantity = request.GET['quantity']
    t = Transaction.objects.get(ttype=_ttype)

    wfdatas = Wfdata.objects.all()
    id_list = [d.getID() for d in wfdatas]
    max_iid = -1
    if len(id_list) > 0:
        max_iid = max(id_list)
    w = Wfdata(iid=max_iid + 1, t_id=t.getID(), barcode=_bcode, quantity=_quantity)
    w.save()
    return HttpResponse('ok')