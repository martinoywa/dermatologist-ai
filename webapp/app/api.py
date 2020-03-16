from flask import Blueprint, render_template, request
from .model.inference import label


main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
		return render_template('index.html')
	else:
		print(request.files['image'])

		if 'image' not in request.files:
			print('No file uploaded')

		image = request.files['image'].read()
		#print(image)

		return render_template('result.html', prediction=label(image), image=image)