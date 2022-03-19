# tensor-print
a print helper for printing information of a tensor or ndarray


## Usage
```
from tensor_print import tpr
import numpy as np 
import torch

a = np.random.randn(1, 2, 3)
b = torch.randn(2, 3, 4)

tpr(a)
tpr(b)
```

output:
```
>>>
a | ndarray | [1, 2, 3] | max:1.04e+00 | min:-1.04e+00 | mean:9.88e-02 | std:7.21e-01 
<<<
>>>
b | Tensor | cpu | [2, 3, 4] | max:1.93e+00 | min:-1.96e+00 | mean:-3.30e-01 | std:9.39e-01 
<<<
```
