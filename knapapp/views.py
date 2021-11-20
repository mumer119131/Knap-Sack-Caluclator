from django.shortcuts import render, redirect
from . import cal
from django.http import HttpResponse
import json
# Create your views here.


no_of_values = int()


def home(request):
    context = dict()

    if request.method == 'POST':
        if 'no_of_values' in request.POST:
            no_of_values = int(request.POST['no_of_values'])
            if no_of_values != '':
                values_str = str()
                for i in range(no_of_values):
                    values_str += '1'
                context['no_of_values'] = values_str

    return render(request, 'knapapp/home.html', context)


def calculate(request):
    data = list()
    if request.method == 'POST':
        no_values = int((len(request.POST)-3)/2)+1

        sackweight = request.POST['sackweight']
        if sackweight == '':
            return HttpResponse('Recheck the Sack Weight')
        for i in range(1, no_values):
            try:
                weight = request.POST['w'+str(i)]
                profit = request.POST['p'+str(i)]
                ratio = int(profit)/int(weight)
                data.append([int(weight), int(profit), ratio])
            except:
                return HttpResponse(f'Recheck the p or w {i}th fields')
        print(request.POST.get('type'))
        if request.POST.get('type') == "Fractional KnapSack":
            total_profit, total_weight = cal.fractional(data, int(sackweight))
        else:
            total_profit, total_weight = cal.knapsnack0_1(
                data, int(sackweight))
        message = f'Total Profit is {total_profit} and Total Weight is {total_weight}'
        return HttpResponse(message)

    return render(request, 'knapapp/home.html')
