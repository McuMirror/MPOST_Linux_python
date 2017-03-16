#!/usr/bin/python

import time
import glob
import mpost

def eventHandler(event, value):
    print m.bill, event
    if event == mpost.event.EscrowEvent:
        time.sleep(1)
        m.escrowstack()

for f in glob.glob('/dev/ttyUSB*'):
    m = mpost.CAcceptor()
    m.open(f, mpost.powerup.A)
    # sleep after opening since it can take a while to get
    time.sleep(1)
    print 'm.devicestate: ',
    print m.devicestate

    for event in mpost.event.names.values():
        m.registercallback(eventHandler, event)

    m.escrowreturn()
    #m.autostack = True
    m.acceptbills = True
    print "device: ", m.deviceportname, m.devicetype, m.devicemodel, m.devicerevision, m.deviceserialnumber
    #print 'm.billtypes: ', m.billtypes
    #print 'm.billvalues: ', m.billvalues
    while True:
	time.sleep(60)
    m.autostack = False
    m.acceptbills = False
    m.close()
