from app import app
from flask import Flask, render_template, request, redirect, url_for, flash, session
from app.models.models import Listing
import requests
import json
from app.util.util import login_required, create_breadcrumb

@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        page=request.args.get('page', 1, type=int)
        listings=Listing.query.filter_by(approved=True).order_by(Listing.id.desc()).paginate(page=page,per_page=2)
        xmrprice=json.loads(requests.get("https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=BTC,USD,EUR").text)
        
        breadcrumb=create_breadcrumb(request.path)
        if listings:
            return render_template("index.html", listings=listings, xmrprice=xmrprice, breadcrumb=breadcrumb)
        else:
            flash("Couldn't fetch listings",'danger')
            return redirect(url_for('home',page=1))

