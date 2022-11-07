import os 
from glob import glob
from natsort import natsorted
from os.path import join, abspath
import cv2

### 
paths={'Data':join('Data'),
'original':join('Data','original'),

'custom':join('Data','custom'),
'neg_custom':join('Data','custom','n'),

'custom_p':join('Data','custom','p'),
'custom_p_train':join('Data','custom','p','train'),
'custom_p_test':join('Data','Test','custom'),

'sample':join('Data','custom','sample'),

'public':join('Data','Public'),
'neg_public':join('Data','Public','Negative'),
'celeba':join('Data','Public','celeba'),
'public_p':join('Data','Public','p'),
'public_p_train':join('Data','Public','p','train'),
'public_p_test':join('Data','Test','public'),

'res': join('Result'),

'res_cus':join('Result','Custom'),
'res_pub':join('Result','Public'),


'src':join('src'),
'utils':join('utils'),
'turtorial':join('turtorial'),
}






team_members=['Akash','Bijay','Pradeep','Keshav']
samples_types=['p','n']


