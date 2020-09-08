dev:
	docker build -t custom-gunicorn -f docker/Dockerfile .
	docker run -d --name dev-gunicorn -p 8888:5000 -v $(PWD)/logs:/app/logs custom-gunicorn

prod:
	NETWORK_MODE=bridge docker-compose up -d


