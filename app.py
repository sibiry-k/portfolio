from flask import Flask, render_template

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')

@app.route('/')
def index():
    return render_template('index.pug')


if __name__ == '__main__':
    app.run()