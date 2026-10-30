
@echo off

REM Переход в корневую папку проекта
cd /d "%~dp0"

echo Running API tests...

REM Запуск Pytest с сохранением результатов для Allure
".venv\Scripts\python.exe" -m pytest -n 2 -v tests\test_store_order_httpx.py --alluredir=allure-results --clean-alluredir

REM Сохраняем код завершения Pytest
set "TEST_EXIT=%ERRORLEVEL%"

echo Generating Allure report...

REM Генерируем HTML-отчёт
call allure.cmd generate allure-results

REM Проверяем, удалось ли создать отчёт
if errorlevel 1 (
    echo Failed to generate Allure report.
    exit /b 2
)

echo.
echo Report generated: allure-report
echo Pytest exit code: %TEST_EXIT%

exit /b %TEST_EXIT%
