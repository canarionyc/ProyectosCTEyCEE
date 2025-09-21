# %% setup
import sys
print(sys.path)

import numpy as np
import matplotlib.pyplot as plt

from pyCTE import ureg, Quantity

# Create quantities using the shared registry
temperature = Quantity(20, 'degC')
area = Quantity(50, 'm^2')

# Or use the registry directly
pressure = ureg.Quantity(101.325, 'kPa')