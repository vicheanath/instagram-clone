up: 
	docker-compose -f docker-compose.dev.yml up

down:
	docker-compose -f docker-compose.dev.yml down

build:
	docker-compose -f docker-compose.dev.yml build

exec:
	docker exec -it instagram.app bash