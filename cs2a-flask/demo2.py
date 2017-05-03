import csv
from flask import Flask, render_template, request
app = Flask(__name__)


sales = list(csv.DictReader(open('RE.csv')))
zips = list({x['zip'] for x in sales})

lines = open('romeo_and_juliet.txt').read().splitlines()

def convert_to_list(dict):
	return [dict[k] for k in dict];


@app.route('/',methods=['GET','POST'])
def r2():
	if request.method == 'POST':
		n = request.form['zip']
		house_list = [convert_to_list(x) for x in sales if x['zip']==n]
		return render_template("zip.html",zip=n,zips=zips,house_list=house_list)
	else:
		return render_template("zip.html",zip='00000',zips=zips,house_list=[])


if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
