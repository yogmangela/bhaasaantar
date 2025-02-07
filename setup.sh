#!/bin/bash
set -xe

pyenv install 3.11.9

which python3
which pip3
python3 --version
pip3 --version
pip3 install -r requirements.txt
pip3 install flask

flask --version


pip3 install flask transformers sentencepiece sacremoses torch