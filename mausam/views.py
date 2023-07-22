from django.shortcuts import render,HttpResponse
import json
import urllib.request
import datetime
# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        
        try:
            res = urllib.request.urlopen(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=5ae1b89bcd78a7e9adfca23934c572ce")
            json_data = json.loads(res.read().decode('utf-8'))
            data = {
                "city": city,
                "country_code": json_data['sys']['country'],
                "weather_main": json_data['weather'][0]['main'],
                "weather_description": json_data['weather'][0]['description'],
                "temperature": json_data['main']['temp'],
                "feels_like": json_data['main']['feels_like'],
                "humidity": json_data['main']['humidity'],
                "wind_speed": json_data['wind']['speed'],
                "icon_code": json_data['weather'][0]['icon'],
                "pressure": json_data['main']['pressure'],
                "sunrise": datetime.datetime.fromtimestamp(json_data['sys']['sunrise']), # convert timestamp to time
                "sunset": datetime.datetime.fromtimestamp(json_data['sys']['sunset']),
            }
            return render(request, "index.html", {"data": data})
        except Exception as e:
            # API errors here
            error = "No Such City Found."
            return render(request,'index.html',{'error':error})
        
    return render(request,'index.html')