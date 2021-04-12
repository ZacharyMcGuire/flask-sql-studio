import os
import datetime
import io

from flask import Flask
from flask import session
from flask.helpers import flash, send_file
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
            session['df'] = df.to_csv(index=False, header=True)
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


@app.route('/download', methods=['GET'])
def download():
    try:
        csv = session['df']
        string_buffer = io.StringIO(csv)
        byte_buffer = io.BytesIO(string_buffer.read().encode('utf-8'))
        file_name = f'Exported Results {datetime.datetime.now()}.csv'

        return send_file(
            byte_buffer,
            mimetype='text/csv',
            as_attachment=True,
            attachment_filename=file_name
        )
    except Exception as e:
        print(e)
        flash('Unable to export resultset. Please try again.', 'alert-danger')
        return
