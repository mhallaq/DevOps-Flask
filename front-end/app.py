from flask import Flask,render_template,request
import requests
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
db=SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:user@mysql/mydb'

class weather_table(db.Model):
    id=db.Column(db.Integer, primary_key=True,autoincrement=True)
    lon=db.Column(db.Integer,nullable=False)
    lat=db.Column(db.Integer, nullable=False)
    temp=db.Column(db.String(10), nullable=False)
    feels_like=db.Column(db.String(10), nullable=False)
    weather_status=db.Column(db.String(100), nullable=False)

db.create_all()

@app.route('/')
def weather_dashboard():
    data=get_weather_results()
    lon=data['lon']
    lat=data['lat']
    temp=data["temp"]
    feels_like=data["feels_like"]
    weather=data["weather"]
    new_weather=weather_table(lon=lon,lat=lat,temp=temp+'°',feels_like=feels_like+'°',weather_status=weather)
    db.session.add(new_weather)
    db.session.commit()

    # location=data["name"]
    # return render_template('results.html',lat=lat,lon=lon,temp=temp,feels_like=feels_like,weather=weather)
    all_weather=weather_table.query.all()
    return render_template('day.html',all_weather=all_weather,lat=lat,lon=lon,temp=temp,feels_like=feels_like,weather=weather)

@app.route('/results',methods=['GET'])
def render_results():
   return 'None'


def get_weather_results():
    print('before api')
    api_url="http://back-end:5001/weather"
    print('after api')

    # print(api_url)
    r=requests.get(api_url)
    return r.json()


if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)




