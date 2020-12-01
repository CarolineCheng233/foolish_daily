* #### 查看cuda runtime version

  nvcc --version

* #### 查看cuda driver version

  nvidia-smi

* #### cuda toolkit version要与cuda runtime version兼容

* #### cuda toolkit 与 cuda driver version的兼容性

![cuda_version](sup\cuda_version.PNG)

https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html

* #### cuda toolkit     pytorch    torchvision 通过pip/conda安装

conda install pytorch==1.5.0 torchvision==0.6.0 cudatoolkit==10.1 -c [source (e.g. conda-forge)]