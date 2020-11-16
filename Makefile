run:
	python3 manage.py runserver 8002

docker_build:
	docker build -t proyect_2 .

docker_run:
	docker run -d -p 8000:8000 proyect_2