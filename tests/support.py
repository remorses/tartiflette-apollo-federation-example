import json


pretty = lambda x: print(json.dumps(x, indent=4, default=str))

import pytest


