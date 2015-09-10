#-*- coding:utf-8 -*-
'''
程序说明（Introduce）：
引用（References）：
创建时间：’2015/9/10 22:29'
编写与修改：

'''
__author__ = 'WangYan'

import os
import  sys


import numpy as np

from read_struct_file import point_cloud

class pcd(object):
    def __init(self):
        self.file_name=''


    def save_to_file(self,file_name,data):
        '''

        :param file_name:
        :param data: 点云数据保存变量，(x,y,z)格式
        :return:
        '''

        pcd_file = open(file_name,'w')

        pcd_file.write('''# .PCD v.7 - Point Cloud Data file format
VERSION .7
FIELDS x y z
SIZE 4 4 4
TYPE F F F
COUNT 1 1 1 \n''')
        pcd_file.writelines('WIDTH '+str(data.shape[0])+'\n')
        pcd_file.writelines('HEIGHT 1\n')
        pcd_file.writelines('VIEWPOINT 0 0 0 1 0 0 0\n')
        pcd_file.writelines('POINTS '+str(data.shape[0])+'\n')
        pcd_file.writelines('DATA ascii\n')
        #print 'data shape1',data.shape[1]
        #print data
        for i in range(data.shape[0]):
            pcd_file.writelines(str(data[i,0])+' '+str(data[i,1])+' '+str(data[i,2])+'\n')
        pcd_file.close()

    def view_pointcloud(self,point_cloud):
        self.save_to_file(point_cloud.time+'.pcd',point_cloud.data[:,1:])
        os.system("pcd_viewer.exe "+point_cloud.time+'.pcd')



