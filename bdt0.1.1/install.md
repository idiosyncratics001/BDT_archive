#Installed Python 3.9.0
	python -m pip install --upgrade pip *elevated prompt
#Create virtual invironment for teams
	python -m pip install virtualenv  *elevated prompt
	python -m pip install --upgrade virtualenv
#The location will be the _env in the RDT root
	cd root location DT
	python -m venv _env
#activate and use the virtual env
	.\_env\Scripts\activate.bat
#test packages requirements.txt  
	pip freeze --local > requirements.txt   #  --local only uses installed packages, no globals
#display packages and versions
	pip list
#Install requirements.txt 
	python -m pip install -r requirements.txt
	#requirements.txt:
	# API framework
		fastapi
		uvicorn
		jinja2
		aiofiles
	# functions
		sqlalchemy
		pandas
		jupyterlab
	# ML & DL
#### https://webkul.com/blog/postgresql-windows-installation-problem-running-post-install-step-installation-may-not-complete-correctly/