# Get Current time



**In this article, you will learn to get current time of your locale as well as different time zones in Python.**

There are a number of ways you can take to get current time in Python.

### Example 1: Current time using datetime object

```text
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
```

**Output**

```text
Current Time = 07:41:19
```

In the above example, we have imported `datetime` class from the [datetime](https://www.programiz.com/python-programming/datetime) module. Then, we used `now()` method to get a `datetime` object containing current date and time.

Using [datetime.strftime\(\)](https://www.programiz.com/python-programming/datetime/strftime) method, we then created a string representing current time.

If you need to create a `time` object containing current time, you can do something like this.

```text
from datetime import datetime

now = datetime.now().time() # time object

print("now =", now)
print("type(now) =", type(now))	
```

**Output**

```text
now = 07:43:37.457423
type(now) = <class 'datetime.time'>
```

### Example 2: Current time using time module

You can also get the current time using time module.

```text
import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)
```

**Output**

```text
07:46:58
```

### Example 3: Current time of a timezone

If you need to find current time of a certain timezone, you can use [pytZ module](http://pytz.sourceforge.net/).

```text
from datetime import datetime
import pytz

tz_NY = pytz.timezone('America/New_York') 
datetime_NY = datetime.now(tz_NY)
print("NY time:", datetime_NY.strftime("%H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London time:", datetime_London.strftime("%H:%M:%S"))
```

**Output**

```text
NY time: 03:45:16
London time: 08:45:16
```

