from flask import Flask, render_template

from scrapers.amazon import scrap_amazon_data

from scrapers.mutualfunds import scrap_mutualfund_data

from scrapers.yahoofinance import scrap_finance_data

from scrapers.collegedunia import scrap_college_data

from scrapers.goodreads import scrap_quotes_data

from scrapers.imdb import scrap_imdb_data

from scrapers.bbc import scrap_bbc_data

from scrapers.automationexercise import scrap_automationexercise_data

from scrapers.booking import scrap_booking_data

from scrapers.spotify import scrap_spotify_data

from scrapers.concurrency import scrape_concurrency_data

from scrapers.products import scrape_products_data

from scrapers.jikan import scrape_jikan_data

from scrapers.recipefinder import scrape_recipe_data

from scrapers.pokemon import scrape_pokemon_data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")

@app.route('/learnmore')
def learnmore():
    return render_template("learnMore.html")

@app.route('/scraping')
def scraping():
    return render_template("scraping.html")

@app.route('/staticscraping')
def staticscraping():
    return render_template("static.html")

@app.route('/amazon')
def amazon():
    products=scrap_amazon_data()
    return render_template("amazon.html",products=products)

@app.route('/mutualfunds')
def mutualfunds():
    funds=scrap_mutualfund_data() 
    return render_template("mutualfunds.html",funds= funds)

@app.route("/yahoofinance")
def yahoofinance():
    currencies = scrap_finance_data()
    return render_template("yahoofinance.html",currencies=currencies)


@app.route("/collegedunia")
def collegedunia():
    colleges = scrap_college_data()
    return render_template("collegedunia.html",colleges=colleges)


@app.route("/goodreads")
def goodreads():
    quotes = scrap_quotes_data()
    return render_template("goodreads.html",quotes=quotes)

@app.route("/dynamicscraping")
def dynamic_scraping():
    return render_template("dynamicscraping.html")

@app.route("/imdb")
def imdb():
    products = scrap_imdb_data()
    return render_template("imdb.html", products=products)

@app.route("/bbc")
def bbc():
    products = scrap_bbc_data()
    return render_template("bbc.html", products=products)

@app.route("/automationexercise")
def automationexercise():
    products = scrap_automationexercise_data()
    return render_template("automationexercise.html",products=products)

@app.route("/booking")
def booking():
    hotels = scrap_booking_data()
    return render_template("booking.html",hotels=hotels)

@app.route("/spotify")
def spotify():
    songs = scrap_spotify_data()
    return render_template("spotify.html",songs=songs)

@app.route("/api")
def api():
    return render_template("APIscraping.html")

@app.route("/concurrency")
def concurrency():
    products = scrape_concurrency_data()
    return render_template("concurrency.html", products=products)

@app.route("/products")
def products():
    products = scrape_products_data()
    return render_template("products.html",products=products)

@app.route("/jikan")
def jikan():
    anime = scrape_jikan_data()
    return render_template("jikan.html",anime=anime)

@app.route("/recipefinder")
def recipefinder():
    recipes = scrape_recipe_data()
    return render_template("recipefinder.html",recipes=recipes)

@app.route("/pokemon")
def pokemon():
    pokemon = scrape_pokemon_data()
    return render_template("pokemon.html",pokemon=pokemon)

@app.route("/Practicesheet")
def Practicesheet():
    return render_template("Practicesheet.html")

@app.route("/APIpokemon")
def APIpokemon():
    return render_template("notebooks/APIpokemon.html")

@app.route("/APIconcurrency")
def APIcurrency():
    return render_template("notebooks/APIconcurrency.html")

@app.route("/APIrecipefinder")
def APIrecipefinder():
    return render_template("notebooks/APIrecipefinder.html")

@app.route("/APIjikan")
def APIjikan():
    return render_template("notebooks/APIjikan.html")

@app.route("/APIproducts")
def APIproducts():
    return render_template("notebooks/APIproducts.html")

@app.route('/Staticamazon')
def Staticamazon():
    return render_template("notebooks/Staticamazon.html")


@app.route('/Staticgoodreads')
def Staticgoodreads():
    return render_template("notebooks/Staticgoodreads.html")


@app.route('/Staticmutualfunds')
def Staticmutualfunds():
    return render_template('notebooks/Staticmutualfunds.html')


@app.route('/Staticyahoofinance')
def Staticyahoofinance():
    return render_template("notebooks/Staticyahoofinance.html")


@app.route('/Staticcollegedunia')
def Staticcollegedunia():
    return render_template("notebooks/Staticcollegedunia.html")

@app.route('/dynamicspotify')
def dynamicspotify():
    return render_template("notebooks/dynamicspotify.html")

@app.route('/dynamicbooking')
def dynamicbooking():
    return render_template("notebooks/dynamicbooking.html")

@app.route('/dynamicbbc')
def dynamicbbc():
    return render_template("notebooks/dynamicbbc.html")

@app.route('/dynamicimdb')
def dynamicimdb():
    return render_template("notebooks/dynamicimdb.html")

@app.route('/dynamicecommerce')
def dynamicecommerce():
    return render_template("notebooks/dynamicecommerce.html")

@app.route("/internship")
def internship():
    return render_template("internship.html")


@app.route("/internshipweeks")
def internshipweeks():
    return render_template("internshipweeks.html")

@app.route("/motivation")
def motivation():
    return render_template("motivation.html")


@app.route("/experience")
def experience():
    return render_template("experience.html")

@app.route('/minorprojects')
def minorprojects():
    return render_template("minorprojects.html")


@app.route("/minorprojects2")
def minorprojects2():
    return render_template("minorprojects2.html")

@app.route("/week1")
def week1():
    return render_template("week1.html")


@app.route("/week2")
def week2():
    return render_template("week2.html")


@app.route("/week3")
def week3():

    return render_template("week3.html")

@app.route("/week4")
def week4():
    return render_template("week4.html")


@app.route("/week5")
def week5():
    return render_template("week5.html")

@app.route("/week6")
def week6():
    return render_template("week6.html")

if __name__ == "__main__":
    app.run(debug=True)