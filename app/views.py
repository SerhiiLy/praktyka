from flask import render_template, url_for, flash, redirect, request
from app import app, db, bcrypt
from app.forms import ScheduleForm
from app.models import Schedule

@app.route('/')
def index():
    schedules = Schedule.query.all()
    return render_template('index.html', schedules=schedules)


@app.route('/add-schedule', methods=['POST', 'GET'])
def add_schedule():
    form = ScheduleForm()
    if form.validate_on_submit():
        new_schedule = Schedule(flight_number=form.flight_number.data,
                                departure_time=form.departure_time.data,
                                day_week=form.days_week.data,
                                number_seats=form.number_seats.data,
                                route=form.route.data
                                )
        db.session.add(new_schedule)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add-schedule.html', form=form)