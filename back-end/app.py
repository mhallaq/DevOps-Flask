from flask import Flask,request,jsonify
import requests
import configparser

app = Flask(__name__)

@app.route('/weather',methods=['GET'])
def weather():
    weather_data={}
    # temp= 'temp'
    # feels_like='feels_likes'
    # weather='weather'

    lon=requests.get("http://lon-service:5002/longitude").text
    lat=requests.get("http://lat-service:5003/latitude").text
    print('coordinates lat ',lat,'long',lon)
    # lat=request.form['latitude']
    api_key=get_api_key()
    data=get_weather_results(lon,lat,api_key)
    weather_data['temp']="{0:.2f}".format(data["main"]["temp"])
    weather_data['feels_like']="{0:.2f}".format(data["main"]["feels_like"])
    weather_data['weather']=data["weather"][0]["main"]
    weather_data['lon']=lon
    weather_data['lat']=lat
    
    # location=data["name"]
    return weather_data



def get_api_key():
    config=configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']

def get_weather_results(lon,lat,api_key):
    api_url="http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=metric&appid={}".format(lat,lon,api_key)
    # print(api_url)
    r=requests.get(api_url)
    return r.json()


if __name__=='__main__':
    app.run(host='0.0.0.0',port=5001)




