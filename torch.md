* pytorch相差太远的版本之间可能不兼容，如在1.7.0版本上save的模型在1.4上load报错

* 使用multiprocessing

```python
from torch.multiprocessing import Process, set_start_method


def train(model):
    pass


if __name__ == '__main__':
    set_start_method("spawn")
    model.share_memory()
    train(model)
```


* DP,DDP comparison

  | name                    | advantage                       | disadvantage                                            | applicable scene                                             |
  | ----------------------- | ------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------ |
  | DataParallel            | easy to use, only one more step | single-process multi_threads, may cause GIL contentions | single-machine multiple-gpus                                 |
  | DistributedDataParallel | one more step to DataParallel   |                                                         | single-machine multiple-gpus or multiple-machines multiple-gpus, and multi-gpu model |

* DP example
```python
import torch.nn as nn
import torch


def Model(nn.Model):
    def __init__(self):
        pass


model = Model()
model = nn.DataParallel(model)
device = torch.device("cuda:0")
model.to(device)
input = data.to(device)
output = model(input)
```

* contiguous \
torch.is_contiguous方法判断tensor在内存中是否连续存储
某些操作如torch.transpose, torch.permute, torch.narrow, torch.expand不改变tensor在内存中的物理存储，而是返回一个新的数组元信息，
记录数组的stride和shape等，这些操作虽然改变了tensor的形状，但是不产生新的维度也不减少维度。torch.view也是产生一个新的数组元信息，不改变数组
的物理存储方式，但是会改变维度。它要求数组的存储是连续的(主要是因为会改变维度，例如(3,2)的形状变成(6,)，stride变成一维，失去了原本的stride信息)。
因此view操作要求数组是连续的。torch.reshape操作相当于torch.contiguous.view。如果数组本身是连续的，则torch.contiguous不会执行操作，否则
返回一个新的连续存储的数组。
```python
import torch

t1 = torch.arange(12).reshape(3,4)  # t1的物理存储： [0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11]
t2 = torch.transpose(0, 1)          # t2与t1有相同的物理存储
t3 = torch.view(-1)                 # 会报错，即使不会报错，在物理上返回的是t1的存储，在逻辑上有错误
                                    # 而期望的物理存储是 [0,  4,  8,  1,  5,  9,  2,  6, 10,  3,  7, 11]
```
