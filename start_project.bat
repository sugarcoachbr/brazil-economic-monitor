@echo off
title Palantir Projects - Thiago

echo ========================================
echo   PALANTIR PROJECTS - Thiago Parente
echo ========================================
echo.

cd /d C:\Users\Admin\OneDrive\Documentos\palantir-projects

echo Ativando ambiente virtual...
call venv\Scripts\activate.bat

echo Ambiente ativado com sucesso!
echo.
echo Comandos úteis:
echo   streamlit run dashboard.py          → Projeto 1
echo   streamlit run x_intelligence.py     → Projeto 2
echo.

cmd /k