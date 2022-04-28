REM set variable="%~dp0src\programfiles\"
set variable=%~dp0
set PYTHONPATH=%PYTHONPATH%;%variable%
python3 src/programfiles/show_world_generation.py