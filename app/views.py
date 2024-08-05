# -*- coding: utf-8 -*-

from flask import Flask, flash, render_template, redirect, request, url_for
from datetime import datetime

from app.models import Strain, TestFood, SampleFood
from app.forms import StrainForm, TestFoodForm, SampleFoodForm
from app import constants as C
from app import app, db  # นำเข้า app และ db จาก __init__.py


@app.route('/')
def index():
    strains = Strain.query.order_by(db.text('category asc, id asc'))
    test_foods = TestFood.query.order_by(db.text('id asc'))
    return render_template('index.html', strains=strains, test_foods=test_foods)


@app.route('/strain/add', methods=['POST'])
def strain_add():
    form = StrainForm(request.form)
    if form.validate_on_submit():
        strain = Strain(name=form.name.data.strip(),
                        category=form.category.data,
                        test_result=form.test_result.data.strip())
        db.session.add(strain)
        db.session.commit()
        flash(u'Added strain &ndash; {}'.format(strain.name))
    return redirect(url_for('settings'))


@app.route('/strain/<id>', methods=['GET', 'POST'])
def strain_edit(id):
    strain = Strain.query.get(id)
    test_foods = TestFood.query.order_by(db.text('id asc'))
    form = StrainForm(request.form, obj=strain)
    if form.validate_on_submit():
        strain.name = form.name.data.strip()
        strain.category = form.category.data
        strain.test_result = form.test_result.data.strip()
        db.session.commit()
        flash(u'Updated strain &ndash; {}'.format(strain.name))
        return redirect(url_for('settings'))
    return render_template('strain_edit.html',
        strain=strain, test_foods=test_foods, form=form)


@app.route('/strain/<id>/delete', methods=['POST'])
def strain_delete(id):
    strain = Strain.query.get(id)
    flash(u'Removed strain &ndash; {}'.format(strain.name))
    db.session.delete(strain)
    db.session.commit()
    return redirect(url_for('settings'))


@app.route('/test_food/add', methods=['POST'])
def test_food_add():
    form = TestFoodForm(request.form)
    form.name.data = form.name.data.strip().upper()
    if form.validate_on_submit():
        test_food = TestFood(name=form.name.data)
        db.session.add(test_food)
        db.session.commit()
        flash(u'Added test food &ndash; {}'.format(test_food.name))
    return redirect(url_for('settings'))


@app.route('/test_food/<id>/delete', methods=['POST'])
def test_food_delete(id):
    test_food = TestFood.query.get(id)
    flash(u'Removed test food &ndash; {}'.format(test_food.name))
    db.session.delete(test_food)
    db.session.commit()
    return redirect(url_for('settings'))


@app.route('/record')
def record():
    sample_foods = SampleFood.query.filter_by(deleted_at=None).order_by(db.text('id desc'))
    return render_template('record.html', sample_foods=sample_foods)


@app.route('/record/<id>')
def record_view(id):
   sample_food = SampleFood.query.get(id)
   test_foods = TestFood.query.order_by(db.text('id asc'))
   return render_template('record_view.html',
       sample_food=sample_food, test_foods=test_foods)


@app.route('/record/<id>/delete', methods=['POST'])
def record_delete(id):
    sample_food = SampleFood.query.get(id)
    sample_food.deleted_at = datetime.now()
    flash(u'Removed record &ndash; {}'.format(sample_food.name or '(Unnamed)'))
    db.session.commit()
    return redirect(url_for('record'))


@app.route('/analysis', methods=['GET', 'POST'])
def analysis():
    test_foods = TestFood.query.order_by(db.text('id asc'))
    form = SampleFoodForm(request.form)
    if form.validate_on_submit():
        name = form.name.data.strip()
        test_result = form.test_result.data
        sample_food = SampleFood(name=name, test_result=test_result)
        db.session.add(sample_food)
        db.session.commit()
        flash(u'Success')
        return redirect(url_for('record_view', id=sample_food.id))
    for field, error in form.errors.items():
        flash(error, 'error')
    return render_template('analysis.html', test_foods=test_foods, form=form)


@app.route('/settings')
def settings():
    strain_form = StrainForm()
    test_food_form = TestFoodForm()
    strains = Strain.query.order_by(db.text('category asc, id asc'))
    test_foods = TestFood.query.order_by(db.text('id asc'))
    return render_template('settings.html',
        strain_form=strain_form, test_food_form=test_food_form,
        strains=strains, test_foods=test_foods)
