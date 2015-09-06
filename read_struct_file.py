#-*- coding:utf-8 -*-
'''
程序说明（Introduce）：读取loam_tools fast_transfor 生成的中间数据文件。
引用（References）：
创建时间：’2015/9/6 19:52'
编写与修改：
1，连数据一起保存了~

'''
__author__ = 'WangYan'

import os
import sys



import numpy as np
import scipy as sp

class point_cloud(object):
    def __init__(self,dir,file):
        self.time = file.split('.')[0]+file.split('.')[1]

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

class read_data(object):
    def __init__(self,dir):
        self.pointclout_list = list()
        file_list = os.listdir(dir)
        for file_name in file_list:
            self.pointclout_list.append(point_cloud(dir,file_name))
    def ret_list(self):
        return self.pointclout_list

if __name__ == '__main__':
    file_list = os.listdir('save')
    #print file_list


    a = point_cloud('save',file_list[1])
    print a.data
    print a.avg_v
    print a.sum
    print a.theta
    print a.time
