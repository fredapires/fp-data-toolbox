# %% ||| Append parent file path to sys.path (for lib imports)
import sys
import os

# module_path = os.path.abspath(os.path.join(os.pardir))
module_path = os.path.abspath(os.path.join(os.pardir, os.pardir))
# module_path = os.path.abspath(os.path.join(os.pardir, os.pardir, os.pardir))
if module_path not in sys.path:
    sys.path.append(module_path)
