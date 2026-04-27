# CECS 478 Honeypot Project Makefile

.PHONY: up demo down clean logs

up:
	@echo "Starting system..."
	mkdir -p logs artifacts/release/logs artifacts/release/pcaps
	docker compose up -d --build
	@echo "System running on http://localhost:8080"

demo:
	@echo "Running demo..."
	sleep 5
	curl http://localhost:8080 || true
	curl http://localhost:8080/admin || true
	curl http://localhost:8080/test || true
	sleep 2
	@echo "---- Logs ----"
	cat logs/access.log || true
	@echo "--------------"
	python3 src/generate_metrics.py || python src/generate_metrics.py
	@echo "Demo complete."

logs:
	docker compose logs

down:
	docker compose down

clean:
	docker compose down
	rm -rf logs artifacts
	@echo "Cleaned."
