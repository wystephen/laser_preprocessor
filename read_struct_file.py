#-*- coding:utf-8 -*-
'''
程序说明（Introduce）：
引用（References）：
创建时间：’2015/9/6 19:52'
编写与修改：

'''
__author__ = 'WangYan'

import os
import sys



import numpy as np
import scipy as sp

class point_cloud(object):
    def __init__(self,dir,file):
        self.time = file

        f = open(str(dir+'/'+file))
        line_list = f.readlines()


        self.avg_v =float(line_list[0])
        self.sum = int(line_list[1])
        self.theta = float(line_list[2])
        self.data = np.zeros([len(line_list),4],dtype = float)

        for i in range(0,len(line_list)-3):
            index = i + 3
            line = line_list[index].split(',')
            self.data[i,:] = line




if __name__ == '__main__':
    file_list = os.listdir('save')
    #print file_list


    a = point_cloud('save',file_list[1])
    print a.data
    print a.avg_v
    print a.sum
    print a.theta
    print a.time
