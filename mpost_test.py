#!/usr/bin/python

import time
import glob
import mpost

def eventHandler(event, value):
    print m.bill, event, value

for f in glob.glob('/dev/ttyUSB*'):
    m = mpost.CAcceptor()
    m.open(f, mpost.powerup.A)
    # sleep after opening since it can take a while to get
    time.sleep(1)
    print 'm.devicestate: ',
    print m.devicestate
    m.registercallback(eventHandler, mpost.event.StackedEvent)
    m.autostack = True
    m.acceptbills = True
    print "device: ",
    print m.deviceportname
    print m.devicemodel
    print m.devicetype
    print m.devicerevision
    print 'm.bill: ',
    print m.bill
    print 'm.billtypes: ',
    print m.billtypes
    print 'm.billvalues: ',
    print m.billvalues
    setbillvalues = []
    while True:
	time.sleep(60)
    m.autostack = False
    m.acceptbills = False
    m.close()
