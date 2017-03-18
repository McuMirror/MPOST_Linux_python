from _mpost import *

_acceptor = Acceptor

def Acceptor(port = None, powerup = powerup.A):
    if port is None:
    	return _acceptor()
    else:
    	m = _acceptor()
    	m.open(port,powerup)
    	return m

_acceptor.getauditlifetimetotals = lambda self: dict(zip(['datamapid','hours','motorstarts','escrows','recognised','validated'],self._auditlifetimetotals()))

_acceptor.getauditperformance = lambda self: dict(zip(['ch0rejects','ch1rejects','totaljams','recoveryattempts','rejectattempts','stackerjams','jamswithoutrecovery','outofserviceevents','outoforderevents','hours','toolongevents','tooshortevents','failedescrows','calibrations','resets','flashdownloads','cassettefullevents','cassetteremovedevents'],self._auditperformance()))

_acceptor.getauditqp = lambda self: dict(zip(['last100acceptrate','motorstarts','docsstacked','escrows','recognised','validated','recognizerrejects','securityrejects','orientationrejects','disabledrejects','fastfeedrejects','feedattemptswhiledisabled','hostreturndocrejections','barcodesdecoded'],self._auditqp()))

