* #### 查看cuda runtime version
```shell script
   nvcc --version
```
  
* #### 查看cuda driver version
```shell script
   nvidia-smi
```


* #### cuda toolkit version要与cuda runtime version相同

* #### cuda toolkit 与 cuda driver version的兼容性

![cuda_version](sup/cuda_version.PNG)

https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html

* #### 安装pytorch with cuda support
```shell script
   conda install pytorch==1.5.0 torchvision==0.6.0 cudatoolkit=10.1 -c [source (e.g. pytorch)]
```
手动下载whl安装: 到网页 https://download.pytorch.org/whl/torch_stable.html  找到合适的版本(pytorch版本与toolkit对应版本关系见下面)
下载了torchvision和pytorch之后，先pip install torchvision，然后安装pytorch


pytorch与cudatoolkit对应版本\
https://pytorch.org/get-started/previous-versions/

验证是否安装成功：

```python
import torch
print(torch.cuda.is_available())
```

如果使用的时候出现以下情况则cuda不可用：\
No CUDA runtime is found, using CUDA_HOME='...'
