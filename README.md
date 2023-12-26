# Robot Learning

## Installation
Create a virtual environment (Python 3.10, to minimize compatability issues):
```
python -m venv robot-learning
source robot-learning/bin/activate
```
Tony Z. Zhao's ACT (Action Chunking with Transformers):
```
git clone https://github.com/tonyzhaozh/act.git
```
Octo: 
```
git clone https://github.com/octo-models/octo.git
cd octo
pip install -e .
pip install -r requirements.txt
pip install --upgrade "jax[cuda11_pip]==0.4.20" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html
```