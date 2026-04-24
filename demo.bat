@echo off
echo Running demo...

curl http://localhost:8080 > nul 2>&1

timeout /t 2 > nul

echo ---- Logs ----
type logs\access.log
echo --------------
echo Demo complete.