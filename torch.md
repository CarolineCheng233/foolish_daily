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