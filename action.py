import os
from datetime import datetime
from pytz import timezone

print('time zone is {0:s}/{1:s}'.format(os.environ['INPUT_TZ1'], os.environ['INPUT_TZ2']))

fmt = "%Y%m%d_%H%M%S_%Z%z"
now_utc = datetime.now(timezone('{0:s}/{1:s}'.format(os.environ['INPUT_TZ1'], os.environ['INPUT_TZ2'])))
str_temp = now_utc.strftime(fmt)

if None != str_temp:
    command = 'echo ::set-output name=datetime_str::{0:s}'.format(str_temp)
    print(command)
    print(os.popen(command).read())


