from unicodedata import category
from flask import render_template, request, redirect, url_for, flash, session, jsonify
from app.models.models import Listing,Review,User,db
from app import app
from app.util.util import login_required, admin_required, moderator_required, vendor_required, create_breadcrumb
from datetime import datetime

@login_required
@app.route("/listing", methods=['GET', 'POST'])
def listing():
    listingId=request.args.get('id',1)
    listing=Listing.query.filter_by(id=listingId).first_or_404()
    if request.method == 'GET':
        if listing:
            return render_template("listing.html", listing=listing,reviews=Review.query.filter_by(product_id=listingId).all(), breadcrumb=create_breadcrumb(request.path))
    elif request.method== 'POST':
        if listing:
            reviewContent=request.form.get('review')
            experience=request.form.get('experience')
            vendor=listing.vendor
            product_id=listing.id
            reviewByCurrentUser=Review.query.filter_by(user=session["username"], product_id=product_id).first()   #CHANGE USERNAME IN PRODUCTION
            if not reviewByCurrentUser:
                if reviewContent and experience:
                    vendor=User.query.filter_by(username=vendor).first()
                    if vendor:
                        if vendor.username!=session["username"]:
                            if experience=="good":
                                vendor.trustScore+=1
                                db.session.commit()
                            elif experience=="bad":
                                vendor.trustScore-=1
                                db.session.commit()
                            elif experience=="neutral":
                                pass
                            else:
                                flash("Please select a valid experience.", 'danger')
                                return redirect(url_for('listing', id=listingId))

                            review=Review(review=reviewContent, experience=experience, user=session["username"], vendor=vendor, product_id=product_id) #CHANGE USERNAME IN PRODUCTION
                            db.session.add(review)
                            db.session.commit()

                            flash("Review submitted",'success')
                            return redirect(url_for('listing', id=listingId))
                        else:
                            flash("You cannot review your own product.", 'danger')
                            return redirect(url_for('listing', id=listingId))
                    else:
                        flash("Vendor not found, review discarded",'danger')
                        return redirect(url_for('listing', id=listingId))
                else:
                    flash("There are some missing fields: review",'danger')
                    return redirect(url_for('listing', id=listingId))
            else:
                flash("You have already reviewed this product",'danger')
                return redirect(url_for('listing', id=listingId))   
        else:
            flash("There is no listing with this id",'danger')
            return redirect(url_for('listing'))

@app.route("/listing/create")
def create_listing():
    if request.method=="POST":
        title=request.form.get('title') 
        price=request.form.get('price')
        description=request.form.get('description')
        category=request.form.get('category')
        location=request.form.get('location')
        shipsTo=request.form.get('shipsTo')
        vendor=session["username"]
        if title and price and description and category and location and shipsTo:
            listing=Listing(title=title, price=price, description=description, category=category, location=location, shipsTo=shipsTo, vendor=vendor)
            db.session.add(listing)
            db.session.commit()
            flash("Listing created",'success')
            return redirect(url_for('listing', id=listing.id))
        else:
            flash("There are some missing fields",'danger')
            return redirect(url_for(f'user/{session["username"]}/', id=listing.id))
    if request.method=="GET":
        return render_template("create_listing.html", breadcrumb=create_breadcrumb(request.path))



