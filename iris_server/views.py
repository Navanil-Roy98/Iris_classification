from django.http import HttpResponse
from django.shortcuts import render
from machine_learning.data_prediction import predict


def home(request):
    # If Post: 1. take inputs (4) 2. call fuction, get o/p, 3. Display o/p
    # else: Display home page
    if request.method == 'POST':
        sw = request.POST['sw'].strip()
        sl = request.POST['sl'].strip()
        pw = request.POST['pw'].strip()
        pl = request.POST['pl'].strip()
        try:
            sw = float(sw)
            sl = float(sl)
            pw = float(pw)
            pl = float(pl)
        except:
            return HttpResponse('<center>'
                        '   <h2> ERROR </h2>'
                        '   <h1> INVALID INPUTS </h1>'
                        '   <h3> return to <a href="http://127.0.0.1:8000"> Home </a> and enter correctly! </h3>'
                        '</center>')
            
        iris_species = {
            0: 'IRIS-SETOSA',
            1: 'IRIS-VERSICOLOR',
            2: 'IRIS-VIRGINICA',
        }
        score, acc = predict(sl, sw, pl, pw)
        if score != -1:
            dic = {
                'sl' : sl,
                'sw' : sw,
                'pl' : pl,
                'pw' : pw,
                'ta' : score,
                'tr' : iris_species[acc[0]],
            }
            return render(request, 'output.html', dic)
        else:
            # error
            return HttpResponse('<center>'
                        '   <h1> INTERNAL ERROR </h1>'
                        '   <h3> return to <a href="http://127.0.0.1:8000"> Home </a> and enter correctly! </h3>'
                        '</center>')

    else:
        return render(request, 'home.html')


def error(request):
    return HttpResponse('<center>'
                        '   <h2> 404 </h2>'
                        '   <h1> PAGE NOT FOUND </h1>'
                        '   <h3> return to <a href="http://127.0.0.1:8000"> Home </a> </h3>'
                        '</center>')
