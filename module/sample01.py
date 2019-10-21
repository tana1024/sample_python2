import pytz
from datetime import datetime
import locale

print(datetime.now())
print(datetime.now(pytz.timezone('UTC')))
print(locale.getlocale(locale.LC_TIME))