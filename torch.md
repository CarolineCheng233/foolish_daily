使用multiprocessing

```python
from torch.multiprocessing import Process, set_start_method


def train(model):
    pass


if __name__ == '__main__':
    set_start_method("spawn")
    model.share_memory()
    train(model)
```