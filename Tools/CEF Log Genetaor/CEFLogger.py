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

# The Account Created Syslog message that will be written.
    syslog_message1 = "CEF:0|Securiment|SCALS|1.0|1000|User Account Created|10|src=167.0.0." + ip + " dst=10.0.0." + ip + " duser=" + selected_user + " act=AccountCreated dhost=scals.securiment.com rt=" + current_time + " dvc=10.1.1.19 dtz=utc dvchost=scals.securiment.com suser=faiq suid=10"

# Writing the event to the Syslog file.
    syslog.openlog(facility=syslog.LOG_LOCAL7)
    syslog.syslog(syslog.LOG_INFO, syslog_message1)

# The Account Deleted Syslog message that will be written.
    syslog_message2 = "CEF:0|Securiment|SCALS|1.0|1001|User Account Deleted|10|src=167.0.0." + ip + " dst=10.0.0." + ip + " duser=" + selected_user + " act=AccountDeleted dhost=scals.securiment.com rt=" + current_time + " dvc=10.1.1.19 dtz=utc dvchost=scals.securiment.com suser=faiq suid=10"

# Writing the event to the Syslog file.
    syslog.openlog(facility=syslog.LOG_LOCAL7)
    syslog.syslog(syslog.LOG_INFO, syslog_message2)

# The User Account Disabling Syslog message that will be written.
    syslog_message3 = "CEF:0|Securiment|SCALS|1.0|1002|User Account Disabled|10|src=167.0.0." + ip + " dst=10.0.0." + ip + " duser=" + selected_user + " EventOutcome=" + event_outcome + " cat=Application Generic act=AccountDisabled dhost=scals.securiment.com rt=" + current_time + " dvc=10.1.1.19 dtz=utc dvchost=scals.securiment.com cs2Label=Reason cs2= User inactive for 30 days spriv=Administrator"

# Writing the event to the Syslog file.
    syslog.openlog(facility=syslog.LOG_LOCAL7)
    syslog.syslog(syslog.LOG_INFO, syslog_message3)

# The User Account Enabling Syslog message that will be written.
    syslog_message4 = "CEF:0|Securiment|SCALS|1.0|1003|User Account Enabled|10|src=167.0.0." + ip + " dst=10.0.0." + ip + " duser=" + selected_user + " EventOutcome=" + event_outcome + " cat=Application Generic act=AccountEnabled dhost=scals.securiment.com rt=" + current_time + " dvc=10.1.1.19 dtz=utc dvchost=scals.securiment.com cs2Label=Reason cs2=User is now active spriv=Administrator"

# Writing the event to the Syslog file.
    syslog.openlog(facility=syslog.LOG_LOCAL7)
    syslog.syslog(syslog.LOG_INFO, syslog_message4)

# The User Account Modified Syslog message that will be written.
    syslog_message5 = "CEF:0|Securiment|SCALS|1.0|1004|User Account Modified|10|src=167.0.0." + ip + " dst=10.0.0.19 duser=" + selected_user + " EventOutcome=" + event_outcome + " cat=Application Generic act=AccountModified dhost=scals.securiment.com rt=" + current_time + " dvc=10.1.1.19 dtz=utc dvchost=scals.securiment.com cs2Label=Reason cs2=User permissions changed spriv=User"

# Writing the event to the Syslog file.
    syslog.openlog(facility=syslog.LOG_LOCAL7)
    syslog.syslog(syslog.LOG_INFO, syslog_message5)

# The User Authentication Succeeded Syslog message that will be written.
    syslog_message6 = "CEF:0|Securiment|SCALS|1.0|1005|User Authentication Succeeded|10|src=167.0.0." + ip + " dst=10.0.0.19 duser=" + selected_user + " EventOutcome=success cat=Application Generic act=LoginSuccess dhost=scals.securiment.com rt=" + current_time + " dvc=10.1.1.19 dtz=utc dvchost=scals.securiment.com"

# Writing the event to the Syslog file.
    syslog.openlog(facility=syslog.LOG_LOCAL7)
    syslog.syslog(syslog.LOG_INFO, syslog_message6)

# The User Authentication Failed Syslog message that will be written.
    syslog_message7 = "CEF:0|Securiment|SCALS|1.0|1006|User Authentication Failed |10|src=167.0.0." + ip + " dst=10.0.0.19 duser=" + selected_user + " EventOutcome=failure cat=Application Generic act=LoginFailure dhost=scals.securiment.com rt=" + current_time + " dvc=10.1.1.19 dtz=utc dvchost=scals.securiment.com cs2Label=Reason cs2=Bad Password spriv=User"

# Writing the event to the Syslog file.
    syslog.openlog(facility=syslog.LOG_LOCAL7)
    syslog.syslog(syslog.LOG_INFO, syslog_message7)

# The User Log out Syslog message that will be written.
    syslog_message8 = "CEF:0|Securiment|SCALS|1.0|1007|Logout|10|src=167.0.0." + ip + " dst=10.0.0.19 duser=" + selected_user + " EventOutcome=success cat=Application Generic act=Logout dhost=scals.securiment.com rt=" + current_time + " dvc=10.1.1.19 dtz=utc dvchost=scals.securiment.com"

# Writing the event to the Syslog file.
    syslog.openlog(facility=syslog.LOG_LOCAL7)
    syslog.syslog(syslog.LOG_INFO, syslog_message8)

# The Password Reset Syslog message that will be written.
    syslog_message9 = "CEF:0|Securiment|SCALS|1.0|1008|Password Reset|10|src=167.0.0." + ip + " dst=10.1.1.19 duser=Hal duid=18 EventOutcome=success cat=Application Generic act=PasswordReset dhost=scals.securiment.com rt=" + current_time + " dvc=10.1.1.19 dtz=utc dvchost=scals.securiment.com cs2Label=Reason cs2=User permissions changed spriv=User"

# Writing the event to the Syslog file.
    syslog.openlog(facility=syslog.LOG_LOCAL7)
    syslog.syslog(syslog.LOG_INFO, syslog_message9)

# The User Group Added Syslog message that will be written.
    syslog_message10 = "CEF:0|Securiment|SCALS|1.0|1009|User Group Added|10|src=167.0.0." + ip + " dst=10.1.1.19 EventOutcome=success cat=Application Generic act=UserGroupDeleted dhost=scals.securiment.com rt=" + current_time + " dvc=10.1.1.19 dtz=utc dvchost=scals.securiment.com spriv=Administrator cs1Label=User Group Name cs1=Information Security cs2Label=Group Attributes Old cs2= Application Access Control cs3Label=Group Attributes New cs3=Information Security Management"

# Writing the event to the Syslog file.
    syslog.openlog(facility=syslog.LOG_LOCAL7)
    syslog.syslog(syslog.LOG_INFO, syslog_message10)

# The User Group Deleted Syslog message that will be written.
    syslog_message11 = "CEF:0|Securiment|SCALS|1.0|1010|User Group Deleted|10|src=167.0.0." + ip + " dst=10.1.1.19 EventOutcome=success cat=Application Generic act=UserGroupDeleted dhost=scals.securiment.com rt=" + current_time + " dvc=10.1.1.19 dtz=utc dvchost=scals.securiment.com spriv=Administrator cs1Label=User Group Name cs1=Information Security cs2Label=Group Attributes Old cs2= Application Access Control cs3Label=Group Attributes New cs3=Information Security Management"

# Writing the event to the Syslog file.
    syslog.openlog(facility=syslog.LOG_LOCAL7)
    syslog.syslog(syslog.LOG_INFO, syslog_message11)

# The User Group Modified Syslog message that will be written.
    syslog_message12 = "CEF:0|Securiment|SCALS|1.0|1011|User Group Modified|10|src=167.0.0." + ip + " dst=10.1.1.19 EventOutcome=success cat=Application Generic act=UserGroupModified dhost=scals.securiment.com rt=" + current_time + " dvc=10.1.1.19 dtz=utc dvchost=scals.securiment.com spriv=Administrator cs1Label=User Group Name cs1=Information Security cs2Label=Group Attributes Old cs2= Application Access Control cs3Label=Group Attributes New cs3=Information Security Management"

# Writing the event to the Syslog file.
    syslog.openlog(facility=syslog.LOG_LOCAL7)
    syslog.syslog(syslog.LOG_INFO, syslog_message12)

# The User Added to Group Syslog message that will be written.
    syslog_message13 = "CEF:0|Securiment|SCALS|1.0|1012|User Added to Group|10|src=167.0.0." + ip + " dst=10.1.1.19 duser=Aida duid=8 EventOutcome=success cat=Application Generic act=UserAddedToGroup dhost=scals.securiment.com rt=" + current_time + " dvc=10.1.1.19 dtz=utc dvchost=scals.securiment.com spriv=Administrator cs1Label=User Group Name cs1=Information Security cs2Label=Old Groups cs2= Information Technology, Application cs3Label=New Groups cs3=Information Security"

# Writing the event to the Syslog file.
    syslog.openlog(facility=syslog.LOG_LOCAL7)
    syslog.syslog(syslog.LOG_INFO, syslog_message13)

# The User Removed from Group Syslog message that will be written.
    syslog_message14 = "CEF:0|Securiment|SCALS|1.0|1013|User Removed from Group|10|src=167.0.0." + ip + " dst=10.1.1.19 duser=Haris duid=5 EventOutcome=success cat=Application Generic act=UserRemovedFromGroup dhost=scals.securiment.com rt=" + current_time + " dvc=10.1.1.19 dtz=utc dvchost=scals.securiment.com spriv=Administrator cs1Label=User Group Name cs1=Information Security cs2Label=Old Groups cs2= Information Technology, Application cs3Label=New Groups cs3=Information Security"

# Writing the event to the Syslog file.
    syslog.openlog(facility=syslog.LOG_LOCAL7)
    syslog.syslog(syslog.LOG_INFO, syslog_message14)

# The Audit Log Cleared Syslog message that will be written.
    syslog_message15 = "CEF:0|Securiment|SCALS|1.0|1014|Audit Log Cleared|10|src=167.0.0." + ip + " dst=10.1.1.19 EventOutcome=" + event_outcome + " cat=Application Generic act=AuditLogCleared dhost=scals.securiment.com rt=" + current_time + " dvc=10.1.1.19 dtz=utc dvchost=scals.securiment.com spriv=User"

# Writing the event to the Syslog file.
    syslog.openlog(facility=syslog.LOG_LOCAL7)
    syslog.syslog(syslog.LOG_INFO, syslog_message15)

# The Log Level Changed Syslog message that will be written.
    syslog_message16 = "CEF:0|Securiment|SCALS|1.0|1015|Log Level Changed|10|src=167.0.0." + ip + " dst=10.1.1.19 EventOutcome=success cat=Application Generic act=LogLevelChanged dhost=scals.securiment.com rt=" + current_time + " dvc=10.1.1.19 dtz=utc dvchost=scals.securiment.com cs2Label=Old Log Level cs2=INFO cs3Label=New Log Level cs3=WARNING spriv=Administrator suser=hadi suid=12"

# Writing the event to the Syslog file.
    syslog.openlog(facility=syslog.LOG_LOCAL7)
    syslog.syslog(syslog.LOG_INFO, syslog_message16)

# The Logging Turned Off Syslog message that will be written.
    syslog_message17 = "CEF:0|Securiment|SCALS|1.0|1016|Logging Turned Off|10|src=167.0.0." + ip + " dst=10.1.1.19 EventOutcome=success cat=Application Generic act=LoggingTurnedOff dhost=scals.securiment.com rt=" + current_time + " dvc=10.1.1.19 dtz=utc dvchost=scals.securiment.com spriv=Administrator user=hadi suid=12"

# Writing the event to the Syslog file.
    syslog.openlog(facility=syslog.LOG_LOCAL7)
    syslog.syslog(syslog.LOG_INFO, syslog_message17)

# The Authentication Mode Changed Syslog message that will be written.
    syslog_message18 = "CEF:0|Securiment|SCALS|1.0|1017|Authentication Mode Changed|10|src=167.0.0." + ip + " dst=10.1.1.19 duser=" + selected_user + " EventOutcome=" + event_outcome + " cat=Application Generic act=AuthenticationModeChanged dhost=scals.securiment.com rt=" + current_time + " dvc=10.1.1.19 dtz=utc dvchost=scals.securiment.com cs2Label=Old Authentication cs2=Single-Factor cs3Label=New Authentication cs3=Multi-Factor spriv=Administrator suser=faiq suid=10"

# Writing the event to the Syslog file.
    syslog.openlog(facility=syslog.LOG_LOCAL7)
    syslog.syslog(syslog.LOG_INFO, syslog_message18)

# The Application Command name message that will be written.
    syslog_message19 = "CEF:0|Securiment|SCALS|1.0|1018|Application Command Executed|10|src=167.0.0." + ip + " dst=10.1.1.19 EventOutcome=success cat=Application Generic act=CommandExecuted dhost=scals.securiment.com rt=" + current_time + " dvc=10.1.1.19 dtz=utc dvchost=scals.securiment.com spriv=Administrator cs5Label=Command Executed cs5=service httpd restart cs4Label=CommandMode cs4=Root =faiq suid=10"

# Writing the event to the Syslog file.
    syslog.openlog(facility=syslog.LOG_LOCAL7)
    syslog.syslog(syslog.LOG_INFO, syslog_message19)

# Pausing the loop for 6 minute.
    time.sleep(60)

# End of script