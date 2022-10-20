@echo off
echo "link start !"

powershell -command "cd D:\BOT\GIT\LittlePaimon"

powershell -command "sleep 1"

powershell -command ".\bot.py"

pause
