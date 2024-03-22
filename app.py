from flask import Flask, render_template,request
import requests
app = Flask(__name__)
API_KEY='16ae780eaaa9497dad2173549241903'
base_url='http://api.weatherapi.com/v1/current.json'
param={}

@app.route('/')
def hello_world():
    weather_data={}
    return render_template('home.html',weather_data=weather_data)


@app.route('/weather', methods = ['GET', 'POST'])
def weather():
    weather_data={}
    city=request.form.get('city')
    param={
        'key':API_KEY,
        'q':city
    }
    r=requests.get(base_url,params=param)
    data=r.json()
    if r.status_code==200:
        temperatute=data['current']['temp_c']
        pressure=data['current']['pressure_mb']
        wind_speed=data['current']['wind_kph']
        humidity=data['current']['humidity']
        cloud=data['current']['cloud']
        weather_type=data['current']['condition']['text']
        weather_data={
            'temp':temperatute,
            'pressure':pressure,
            'wind_speed':wind_speed,
            'humidity':humidity,
            'cloud':cloud,
            'weather_type':weather_type
        }
        return render_template('home.html', weather_data=weather_data,city=city)
    else:
        message="Please Enter A Valid City"
        return render_template('home.html', msg=message,weather_data=weather_data)







if __name__ == '__main__':
    app.run()
