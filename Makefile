# CECS 478 Honeypot Project Makefile

.PHONY: up demo down clean logs

up:
	@echo "Starting system..."
	mkdir -p logs artifacts/release/logs artifacts/release/pcaps
	docker compose up -d --build
	@echo "System running on http://localhost:8080"

demo:
	@echo "Running demo..."
	curl http://localhost:8080 || true
	sleep 2
	@echo "---- Logs ----"
	cat logs/access.log
	@echo "--------------"
	python src/generate_metrics.py
	@echo "Demo complete."

logs:
	docker compose logs

down:
	docker compose down

clean:
	docker compose down
	rm -rf logs artifacts
	@echo "Cleaned."
