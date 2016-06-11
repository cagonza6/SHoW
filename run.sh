find . -name "*.pyc" -exec rm -rf {} \;
sh makeGui.sh
python -B Main.py
