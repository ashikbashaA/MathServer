# Ex.03 Design a Website for Server Side Processing
## Date: 10-11-2026

## AIM:
To create a web page to calculate Churn Rate using server-side scripts.

## FORMULA:
Churn Rate = (CustLost / InitCust) * 100
<br> InitCust --> Initial Customers Count
<br> CustLost --> Customers Lost Count

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the Result using the given formula.

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
```
ashik.html

<html>
     <head>
        <title>Churn Rate Calculator </title>
     </head>
     <body >
         <center><i><h1>Churn Rate Calculator</h1></i></center>
         <center><i><h2>ashik(26018692)</h2></i></center>
     <form method="post">
        {% csrf_token %}<br>
            <label>CustLost:</label>
            <input type="text" name="{{cust_lost}}"><br><br>
            <label>InitCut:</label>
            <input type="text" name="{{init_cut}}"><br><br>
            <input type="submit" value="Calculate"><br><br>
            <label>Churn Rate:</label>
            <input type="text" value="{{churn_rate}}"><br><br>
     </form>
     </body>
</html>

views.py

from django.shortcuts import render
def calculate(request):
    custlost = int(request.POST.get('price', '0'))
    initlost = int(request.POST.get('gst', '0'))
    bill = initlost + (initlost * custlost / 100) if request.method == 'POST' else 0
    print("initial customer =",initlost)
    print("customer lost =",custlost)
    print("churn rate =",bill)
    return render(request, 'myapp/math.html',{'initlost': initlost, 'custlost': custlost, 'bill': bill})

urls.py

from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [path('', views.calculate, name='calculate'),]

```



## OUTPUT - SERVER SIDE:
![alt text](<Screenshot 2026-11-13 140310.png>)


## OUTPUT - WEBPAGE:
![alt text](<Screenshot 2026-11-13 140225.png>)


## RESULT:
The the web page to calculate Churn Rate using server-side scripts is created successfully.
