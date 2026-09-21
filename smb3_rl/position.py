"""Conservative quarantine for the reproduced single-frame RAM page anomaly."""
class PositionGuard:
    def __init__(self,x):
        self.last=int(x)
        self.pending=False
        self.samples_quarantined=0
    def observe(self,x):
        x=int(x);delta=x-self.last
        if self.pending:
            self.pending=False
            if abs(delta)>16:return self.last,False,True
            self.last=x
            return x,True,False
        if abs(delta)<=16:
            self.last=x
            return x,True,False
        if abs(abs(delta)-256)<=16:
            self.pending=True
            self.samples_quarantined+=1
            return self.last,False,False
        return self.last,False,True
