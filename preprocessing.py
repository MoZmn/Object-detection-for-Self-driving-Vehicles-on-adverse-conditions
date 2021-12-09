"""
@author: zamanm16
"""

import sys
sys.path.append('D:\\Courses\\05- Deep and Neural\\788\\Final project\\LAST ORIG\\final project')
from convert_to_kitti import convert_kitti
from arrange_dataset_tf2 import arrange_data

if __name__=='__main__':
    core_number = 2
    convert_kitti(core_number)
    arrange_data()