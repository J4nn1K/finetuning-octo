# Finetuning Octo to new a Observation/Action Space
![](https://github.com/J4nn1K/robot-learning/blob/main/media/eval_examples.gif)

## Installation

*The following instructions were tested on Ubuntu 22.04 and Linux 5.13.0 using Python 3.10*

Create a virtual environment using [Anaconda](https://docs.anaconda.com/free/anaconda/install/):
```
conda create -n robot-learning python=3.10
conda activate robot-learning
```
Clone and install [Octo](https://octo-models.github.io/):
```
git clone https://github.com/octo-models/octo.git
cd octo 
pip install -e .
pip install -r requirements.txt
```
Install [JAX](http://jax.readthedocs.io/) (GPU or TPU):
```
pip install --upgrade "jax[cuda11_pip]==0.4.20" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html
pip install --upgrade "jax[tpu]==0.4.20" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
```

Clone Tony Z. Zhao's [ACT (Action Chunking with Transformers)](https://tonyzhaozh.github.io/aloha/)  for its simulated ALOHA environment *Transfer Cube*:
```
git clone https://github.com/tonyzhaozh/act.git
pip3 install opencv-python modern_robotics pyrealsense2 h5py_cache pyquaternion pyyaml rospkg pexpect mujoco==2.3.3 dm_control==1.0.9 einops packaging h5py ipython
```
## Finetuning
Finetuning Octo to a new observation space and a new action space on [simulated ALOHA cube handover data](https://rail.eecs.berkeley.edu/datasets/example_sim_data.zip
).

Download and extract the dataset:
```
wget https://rail.eecs.berkeley.edu/datasets/example_sim_data.zip
unzip example_sim_data.zip
```
Run `scripts/finetune.py`:
```
python scripts/finetune.py \
--pretrained_path=hf://rail-berkeley/octo-small \
--data_dir=PATH/TO/aloha_sim_dataset  \
--save_dir=PATH/TO/CHECKPOINT/DIR
```
## Evaluation