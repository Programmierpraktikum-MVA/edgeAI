#!/bin/bash
# if ubuntu
yes | sudo apt-get install gcc python3-dev
yes | sudo nala install python3-dev git
yes | sudo nala install ffmpeg libsm6 libxext6
yes | sudo apt-get install python3-venv
git clone https://github.com/JetsonHacksNano/build_python.git
cd build_python
bash ./build_python3.sh

python3 -m venv base
source base/bin/activate
pip install Flask 
pip install ultralytics
pip install opencv-python --verbose

echo "Installation complete!"
