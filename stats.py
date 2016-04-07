class Stats:
    def __init__(self, ws, bs, s, t, w, i, a, ld, sv, ss):
        self.ws = ws
        self.bs = bs
        self.s = s
        self.t = t
        self.w = w
        self.i = i
        self.a = a
        self.ld = ld
        self.sv = sv
        self.ss = ss

    pass

    def __str__(self):
        return 'WS\tBS\tS\tT\tW\tI\tA\tLd\tSv\tSS\n' + str(self.ws) + '\t' + str(self.bs) + '\t' + str(self.s) + '\t'\
            + str(self.t) + '\t' + str(self.w) + '\t' + str(self.i) + '\t' + str(self.a) + '\t' + str(self.ld) + '\t'\
            + str(self.sv) + '+\t' + str(self.ss) + '+\n'
    
    def __eq__(self, other):
        return self.ws == other.ws and self.bs == other.bs and self.s == other.s and self.t == other.t and \
               self.w == other.w and self.i == other.i and self.a == other.a and self.ld == other.ld and \
               self.sv == other.sv and self.ss == other.ss

