from django.shortcuts import render
def calculate(request):
    custlost = int(request.POST.get('price', '0'))
    initlost = int(request.POST.get('gst', '0'))
    bill = initlost + (initlost * custlost / 100) if request.method == 'POST' else 0
    print("initial customer =",initlost)
    print("customer lost =",custlost)
    print("churn rate =",bill)
    return render(request, 'myapp/math.html',{'initlost': initlost, 'custlost': custlost, 'bill': bill})