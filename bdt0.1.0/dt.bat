@echo ================== 
@echo [Ryu's Data Tools]
@echo ------------------
@echo Starting DT.Server
@echo ==================
@echo off
uvicorn dt:app --host 11.69.67.2 --port 8000 --reload