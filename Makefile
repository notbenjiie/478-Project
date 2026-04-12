# CECS 478 Honeypot Project Makefile

.PHONY: bootstrap run stop clean

bootstrap:
	@echo "Setting up project environment..."
	mkdir -p logs
	docker-compose build
	@echo "Bootstrap complete. Run 'make run' to start the trap."

run:
	docker-compose up -d
	@echo "Honeypot is live on http://localhost:8080"
	@echo "Monitoring logs..."
	docker-compose logs -f

stop:
	docker-compose down

clean:
	docker-compose down
	rm -rf logs/*
	@echo "Environment cleaned."
