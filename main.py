from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Tesla Proxy Aktif!'

@app.route('/api/tesla')
def tesla():
    return 'Buraya Tesla API verisi gelir.'

if __name__ == '__main__':
    app.run()
