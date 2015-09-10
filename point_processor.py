#-*- coding:utf-8 -*-
'''
程序说明（Introduce）：
引用（References）：
创建时间：’2015/9/7 14:27'
编写与修改：

'''
__author__ = 'WangYan'
import time

import numpy as np
import scipy as sp

import os
import sys

from read_struct_file import read_data,point_cloud

import matplotlib.pyplot as plt
from mayavi import mlab
#from OpenGL.GL import *
#from OpenGL.GLU import *
#from OpenGL.GLUT import *


if __name__ == '__main__':
    all_data = read_data('save').ret_list()#read list

    #glutInit()
   # glutInitDisplayMode(GLUT_RGBA|GLUT_SINGLE)
   # glutInitWindowSize(400,400)
   # glutCreateWindow("first")
    for data_t in all_data:

        print data_t.data
        import pcd_manage
        t_f = pcd_manage.pcd()
        print data_t.data[:,1:3].shape[0]
        print data_t.data[10,1]
        print data_t.data[10,2]
        print data_t.data[10,3]
        #t_f.save_to_file(str('pcd_file/')+data_t.time+str('.pcd'),data_t.data[:,1:])
        t_f.view_pointcloud(data_t)
        break












