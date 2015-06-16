# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 09:25:43 2015

@author: danaukes
"""

import pysftp
import PySide.QtGui as qg
import sys
import os

app = qg.QApplication(sys.argv)

class PutInfo(object):
    def __init__(self,host,directory,username,password):
        self.host = host
        self.directory = directory
        self.username = username
        self.password = password


class Dialog(qg.QDialog):
    def __init__(self,host = '',username = '',password = '',directory = ''):
        super(Dialog,self).__init__()        
        self.host = qg.QLineEdit()
        self.directory = qg.QLineEdit()
        self.username = qg.QLineEdit()
        self.password = qg.QLineEdit()
        self.password.setEchoMode(self.password.EchoMode.Password)

        self.host.setText(host)
        self.username.setText(username)
        self.password.setText(password)
        self.directory.setText(directory)
        
        button1 = qg.QPushButton('Ok')
        button2 = qg.QPushButton('Cancel')

        button1.pressed.connect(self.accept)
        button2.pressed.connect(self.reject)

        layout = qg.QGridLayout()
        layout.addWidget(qg.QLabel('host'),0,0)        
        layout.addWidget(qg.QLabel('directory'),1,0)        
        layout.addWidget(qg.QLabel('username'),2,0)        
        layout.addWidget(qg.QLabel('password'),3,0)        
        
        layout.addWidget(self.host,0,1)        
        layout.addWidget(self.directory,1,1)        
        layout.addWidget(self.username,2,1)        
        layout.addWidget(self.password,3,1)       
        layout.addWidget(button1,4,0)
        layout.addWidget(button2,4,1)

        self.setLayout(layout)

    def accept_data(self):
        return self.host.text(), self.username.text(), self.password.text(), self.directory.text()


def putfiles(putinfo,files):
    if putinfo.host=='' or putinfo.username=='' or putinfo.password=='' or putinfo.directory=='':
        d = Dialog(putinfo.host,putinfo.username,putinfo.password,putinfo.directory)
        ok = d.exec_()
        if ok:
            host,username,password,directory = d.accept_data()
            putinfo.host = host
            putinfo.username = username
            putinfo.password = password
            putinfo.directory = directory
            
    with pysftp.Connection(host = putinfo.host,username = putinfo.username,password = putinfo.password) as c:
        c.chdir(putinfo.directory)
        print('opened {}'.format(putinfo.host))
        for file in files:
            print('uploading {0} ...'.format(file))
            c.put(file)
        print('finished.')
        c.close()
    return putinfo


