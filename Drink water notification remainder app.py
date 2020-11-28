
# coding: utf-8

# In[3]:


##install plyer library

import time 
from plyer import notification
#time.sleep() wil make the command to sleep for the given seconds 

if __name__ == '__main__':
    while True:
        notification.notify(title = 'DRINK WATER',
                            message='ALERT WEIGHT INCREASING: Drink water and run upstairs',
                            timeout = 5)
        time.sleep(30*60)#run every 30 minutes

