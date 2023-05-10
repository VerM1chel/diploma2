
class Configuration:
    cpu = None
    cooler = None
    motherboard = None
    ram = None
    gpu = None
    ssd = None
    hdd = None
    power = None
    casePC = None
    def __init__(self, cpu=None, cooler=None, motherboard=None, ram=None, gpu=None, ssd=None, hdd=None, power=None, casePC=None):
        self.cpu = cpu
        self.cooler = cooler
        self.motherboard = motherboard
        self.ram = ram
        self.gpu = gpu
        self.ssd = ssd
        self.hdd = hdd
        self.power = power
        self.casePC = casePC