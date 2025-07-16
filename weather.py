from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "9cd9ba6c57c1b7e6f1450217ec210a8f"

@app.route('/', methods=['GET','POST'])

def index():
    weather = None
    if request.method == 'POST':
        city = request.form['city']
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                'city': city,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon']
            }

        else:
            weather = {'error': 'City not found!'}
    return render_template('index.html', weather = weather)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # 5000 for local, dynamic in Render
    app.run(host='0.0.0.0', port=port)

