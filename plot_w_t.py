#-*- coding:utf-8 -*-
'''
程序说明（Introduce）：
引用（References）：
创建时间：’2015/9/6 22:02'
编写与修改：

'''
__author__ = 'WangYan'

import matplotlib.pyplot as plt

import numpy as np
import scipy as sp

from read_struct_file import  read_data

if __name__ == '__main__':
    all_data = read_data('save').ret_list()
    w_t = np.zeros([len(all_data),2])
    for i in range(len(all_data)):
        w_t[i,0] = all_data[i].sum/20.0
        w_t[i,1] = all_data[i].time
        #if w_t[i,0]<w_t[i-1,0]:
            #print w_t[i,1],w_t[i-1,1],w_t[i,1]-w_t[i-1,1]
    #w_t[:,1]= w_t[:,1]-min(w_t[:,1])

    plt.figure(1)
    print min(w_t[:,1]),max(w_t[:,1])
    plt.plot(w_t[:,1],w_t[:,0],'o-')
    plt.show()


