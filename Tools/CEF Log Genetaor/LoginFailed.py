#!/usr/bin/python
# Python script designed to write to the local Syslog file in CEF format on an Azure Ubuntu 18.04 VM.
# Laraib Khan Nov 2022

# Importing the libraries used in the script
import random
import syslog
import time
from datetime import datetime

# Simple list that contains usernames that will be randomly selected and then otput to the "duser" CEF field.
usernames = ['Frank', 'John', 'Joe', 'Tony', 'Mario', 'James', 'Chris', 'Mary', 'Rose', 'Jennifer', 'Amanda', 'Andrea', 'Lina']
outcomes = ['success', 'failure']

dhost = 'scals.securiment.com'
#Device Time
now = datetime.now()
current_time = now.strftime("%H:%M:%S")


# Endless loop that will run the below every five minutes.
while True:

    # Assigning a random value from the above lists to the two variables that will be used to write to the Syslog file.
    selected_user = random.choice(usernames)
    event_outcome = random.choice(outcomes)

# Assigning a random integer value from 1-255 that will be appended to the IP addresses written to the Syslog file.
    ip = str(random.randint(1,255))
    ip2 = str(random.randint(1,255))

# The User Authentication Failed Syslog message that will be written.
    syslog_message7 = "CEF:0|Securiment|SCALS|1.0|1006|User Authentication Failed |10|src=10.0.10.1 dst=10.0.0.19 duser=farhan Outcome=failure cat=Application Generic act=LoginFailure dhost=scals.securiment.com rt=" + current_time + " dvc=10.1.1.19 dtz=utc dvchost=scals.securiment.com spriv=User"

# Writing the event to the Syslog file.
    syslog.openlog(facility=syslog.LOG_LOCAL7)
    syslog.syslog(syslog.LOG_INFO, syslog_message7)


# Pausing the loop for 6 minute.
    time.sleep(10)

# End of script