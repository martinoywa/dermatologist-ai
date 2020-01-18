from flask import Blueprint, render_template, request


main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
		return render_template('index.html')
	else:
		print(request.files)

		if 'image' not in request.files:
			print('No file uploaded')

		image = request.files['image'].read()

		return render_template('result.html', image=image)