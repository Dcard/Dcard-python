# Dcard-python

This module solve the problem of annoying CSRF problem.

So you can write scripts by simply `import dcard`.

### Installation:
* `pip install dcard` (What an awesome name!)

### Usage:
```
from dcard import Dcard
d = Dcard('<USERNAME>', '<PASSWORD>')

# get info about yourself
data = d.session.get('https://www.dcard.tw/api/member/status').json()
```
