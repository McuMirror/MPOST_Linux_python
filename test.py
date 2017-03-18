#!/usr/bin/python

import time
import glob
import mpost

def eventHandler(acceptor, event, value):
    print event
    if event == mpost.event.EscrowEvent:
	print acceptor.bill
        acceptor.escrowstack()

for f in glob.glob('/dev/ttyUSB*'):
    m = mpost.Acceptor(f)
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
