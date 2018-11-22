from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	holiday_tortoise=['https://i.pinimg.com/originals/20/ec/c3/20ecc3180e206bb1808d588ace9022cf.jpg','http://i1263.photobucket.com/albums/ii635/pokeymeg/IMG_1230.jpg','https://assets.heart.co.uk/2013/47/woolly-suits-for-tortoises--1385381144-view-1.jpg']
    return render_template('home.html',holiday_tortoise=holiday_tortoise)

if __name__ == '__main__':
    app.run(debug=True)

