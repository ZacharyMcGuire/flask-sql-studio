import os

from flask import Flask
from flask.helpers import flash
from flask.templating import render_template
import pandas as pd

from forms import QueryForm
from db import engine

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

if not app.config['SECRET_KEY']:
    raise ValueError('No SECRET_KEY environment variable set')


@app.route('/', methods=('GET', 'POST'))
def index():
    form = QueryForm()
    if form.validate_on_submit():
        query = form.sql.data
        try:
            df = pd.read_sql(query, engine)
        except Exception as e:
            flash('{}'.format(e), 'alert-danger')
        else:
            return render_template(
                'index.html',
                form=form,
                table=df.to_html(classes='table table-striped table-bordered',
                                 header='true', index=False, justify="left",
                                 show_dimensions=True)
            )
    return render_template('index.html', form=form)
