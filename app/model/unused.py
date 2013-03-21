#classes not used yet
class diagExam(db.Model):
    DIEXid = db.Column(db.String(36), nullable=False, primary_key=True)
    DIAGid = db.Column(db.String(36), db.ForeignKey('diagnose.DIAGid'))
    EXAMid = db.Column(db.String(36), db.ForeignKey('examination.EXAMid'))
    value = db.Column(db.String(200), nullable=False, default=' ')
    date = db.Column(db.DateTime)
    address = db.Column(db.String(100))
    illustration = db.Column(db.Text, nullable=False, default=' ')
    sequence = db.Column(db.INT, nullable=False, default=0)

    def __init__(self, DIEXid, DIAGid, EXAMid, value, date, address, illustration, sequence):
        self.DIEXid = DIEXid
        self.DIAGid = DIAGid
        self.EXAMid = EXAMid
        self.value = value
        self.date = date
        self.address = address
        self.illustration = illustration
        self.sequence = sequence
        db.session.add(self)
        db.session.commit()


    @classmethod
    def data(self, DIEXid=None):
        if DIEXid:
            print DIEXid
            return diagExam.query.filter_by(DIEXid=DIEXid).first()
        else:
            return diagExam.query.all()

class diagItem(db.Model):
    DIITid = db.Column(db.String(36), nullable=False, primary_key=True)
    DIREid = db.Column(db.String(36), db.ForeignKey('diag_recipe.DIREid'))
    dru_DRUGid = db.Column(db.String(36), db.ForeignKey('drug.DRUGid'))
    DRUGid = db.Column(db.String(36))
    quality = db.Column(db.DECIMAL(18,4), nullable=False, default=0)
    sequence = db.Column(db.INT, nullable=False, default=0)
    illustration = db.Column(db.Text, nullable=False, default=' ')

    def __init__(self, DIITid, DIREid, dru_DRUGid, DRUGid, quality, sequence, illustration):
        self.DIITid = DIITid
        self.DIREid = DIREid
        self.dru_DRUGid = dru_DRUGid
        self.DRUGid = DRUGid
        self.quality = quality
        self.sequence = sequence
        self.illustration = illustration
        db.session.add(self)
        db.session.commit()


class diagRecipe(db.Model):
    DIREid = db.Column(db.String(36), nullable=False, primary_key=True)
    DIAGid = db.Column(db.String(36), db.ForeignKey('diagnose.DIAGid'))
    FREPid = db.Column(db.String(36), db.ForeignKey('fixedrecipe.FREPid'))
    isCustomed = db.Column(db.Boolean, nullable=False, default=0)
    name = db.Column(db.String(36), nullable=False, default=' ')
    doctorAdvice = db.Column(db.Text, nullable=False, default=' ')
    drugForm = db.Column(db.Boolean, nullable=False)
    takeWay = db.Column(db.Boolean, nullable=False)
    quality = db.Column(db.SMALLINT, nullable=False)
    produceMethod = db.Column(db.String(100), nullable=False)
    usage = db.Column(db.String(100), nullable=False)

    def __init__(self, DIREid, DIAGid, FREPid, isCustomed, name, doctorAdvice, drugForm, takeWay, quality, produceMethod, usage):
        self.DIREid = DIREid
        self.DIAGid = DIAGid
        self.FREPid = FREPid
        self.isCustomed = isCustomed
        self.name = name
        self.doctorAdvice = doctorAdvice
        self.drugForm = drugForm
        self.takeWay = takeWay
        self.quality = quality
        self.produceMethod = produceMethod
        self.usage = usage
        db.session.add(self)
        db.session.commit()


class diagSymptom(db.Model):
    DISYid = db.Column(db.String(36), nullable=False, primary_key=True)
    SYPMid = db.Column(db.String(36), db.ForeignKey('symptom.SYPMid'))
    DIAGid = db.Column(db.String(36), db.ForeignKey('diagnose.DIAGid'))
    value = db.Column(db.String(200), nullable=False, default=' ')
    illustration = db.Column(db.Text, nullable=False, default=' ')
    sequence = db.Column(db.INT, nullable=False, default=0)

    def __init__(self, DISYid, SYPMid, DIAGid, value, illustration, sequence):
        self.DISYid = DISYid
        self.SYPMid = SYPMid
        self.DIAGid = DIAGid
        self.value = value
        self.illustration = illustration
        self.sequence = sequence
        db.session.add(self)
        db.session.commit()

class diagnose(db.Model):
    DIAGid = db.Column(db.String(36), nullable=False, primary_key=True)
    CASEid = db.Column(db.String(36), db.ForeignKey('d_case.CASEid'))
    CDISid = db.Column(db.String(36), nullable=False, default=' ')
    CDISid2 = db.Column(db.String(36), nullable=False, default=' ')
    WDISid = db.Column(db.String(36), nullable=False, default=' ')
    WDISid2 = db.Column(db.String(36), nullable=False, default=' ')
    SEMCid = db.Column(db.String(36), nullable=False)
    SEMCid2 = db.Column(db.String(36), nullable=False)
    SEMCid3 = db.Column(db.String(36), nullable=False)
    DMETid = db.Column(db.String(36), nullable=False)
    DMETid2 = db.Column(db.String(36), nullable=False)
    DMETid3 = db.Column(db.String(36), nullable=False)
    DIAGno = db.Column(db.Boolean, nullable=False, default=1)
    DIAGnum = db.Column(db.Boolean, nullable=False)
    DIAGday = db.Column(db.DateTime, nullable=False)
    lunarDay = db.Column(db.String(50), nullable=False, default=' ')
    solarTerm = db.Column(db.Boolean, nullable=False, default=0)
    DIAway = db.Column(db.Boolean, nullable=False, default=0)
    majorSue = db.Column(db.Text, nullable=False)
    illustration = db.Column(db.Text, nullable=False, default=' ')
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    westernMed = db.Column(db.Text, nullable=False, default=' ')
    other = db.Column(db.Text, nullable=False, default=' ')
    preSEMCid = db.Column(db.String(36), nullable=False)

    def __init__(self, DIAGid, CASEid, CDISid, CDISid2, WDISid, WDISid2, SEMCid, SEMCid2, SEMCid3, DMETid, DMETid2, DMETid3, DIAGno, DIAGnum, DIAGday, lunarDay, solarTerm, DIAway, majorSue, illustration, optrid, createDay, westernMed, other, preSEMCid):
        self.DIAGid = DIAGid
        self.CASEid = CASEid
        self.CDISid = CDISid
        self.CDISid2 = CDISid2
        self.WDISid = WDISid
        self.WDISid2 = WDISid2
        self.SEMCid = SEMCid
        self.SEMCid2 = SEMCid2
        self.SEMCid3 = SEMCid3
        self.DMETid = DMETid
        self.DMETid2 = DMETid2
        self.DMETid3 = DMETid3
        self.DIAGno = DIAGno
        self.DIAGnum = DIAGnum
        self.DIAGday = DIAGday
        self.lunarDay = lunarDay
        self.solarTerm = solarTerm
        self.DIAway = DIAway
        self.majorSue = majorSue
        self.illustration = illustration
        self.optrid = optrid
        self.createDay = createDay
        self.westernMed = westernMed
        self.other = other
        self.preSEMCid = preSEMCid
        db.session.add(self)
        db.session.commit()




class fixedrecipeItem(db.Model):
    FRITid = db.Column(db.String(36), nullable=False, primary_key=True)
    DRUGid = db.Column(db.String(36), db.ForeignKey('drug.DRUGid'))
    FREPid = db.Column(db.String(36), db.ForeignKey('fixedrecipe.FREPid'))
    quality = db.Column(db.DECIMAL(18,4), nullable=False, default=0)
    sequence = db.Column(db.INT, nullable=False, default=0)
    illustration = db.Column(db.Text, nullable=False, default=' ')

    def __init__(self, FRITid, DRUGid, FREPid, quality, sequence, illustration):
        self.FRITid = FRITid
        self.DRUGid = DRUGid
        self.FREPid = FREPid
        self.quality = quality
        self.sequence = sequence
        self.illustration = illustration
        db.session.add(self)
        db.session.commit()


class integratedSym(db.Model):
    INSYid = db.Column(db.String(36), nullable=False, primary_key=True)
    SYPMid = db.Column(db.String(36), db.ForeignKey('symptom.SYPMid'))
    name = db.Column(db.String(50), nullable=False)
    valSort = db.Column(db.INT, nullable=False)
    sequence = db.Column(db.INT, nullable=False)

    def __init__(self, INSYid, SYPMid, name, valSort, sequence):
        self.INSYid = INSYid
        self.SYPMid = SYPMid
        self.name = name
        self.valSort = valSort
        self.sequence = sequence
        db.session.add(self)
        db.session.commit()

class dtmpExamination(db.Model):
    DTEXid = db.Column(db.String(36), nullable=False, primary_key=True)
    DTMPid = db.Column(db.String(36), db.ForeignKey('d_template.DTMPid'))
    EXAMid = db.Column(db.String(36), db.ForeignKey('examination.EXAMid'))
    sequence = db.Column(db.INT, nullable=False)
    illustration = db.Column(db.Text, nullable=False)

    def __init__(self, DTEXid, DTMPid, EXAMid, sequence, illustration):
        self.DTEXid = DTEXid
        self.DTMPid = DTMPid
        self.EXAMid = EXAMid
        self.sequence = sequence
        self.illustration = illustration
        db.session.add(self)
        db.session.commit()


class dtmpSymptom(db.Model):
    DTSYid = db.Column(db.String(36), nullable=False, primary_key=True)
    DTMPid = db.Column(db.String(36), db.ForeignKey('d_template.DTMPid'))
    SYPMid = db.Column(db.String(36), db.ForeignKey('symptom.SYPMid'))
    isFirst = db.Column(db.Boolean, nullable=False, default=1)
    sequence = db.Column(db.INT, nullable=False, default=0)
    illustration = db.Column(db.Text, nullable=False, default=' ')

    def __init__(self, DTSYid, DTMPid, SYPMid, isFirst, sequence, illustration):
        self.DTSYid = DTSYid
        self.DTMPid = DTMPid
        self.SYPMid = SYPMid
        self.isFirst = isFirst
        self.sequence = sequence
        self.illustration = illustration
        db.session.add(self)
        db.session.commit()


class examination(db.Model):
    EXAMid = db.Column(db.String(36), nullable=False, primary_key=True)
    code = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    abbreviation = db.Column(db.String(50), nullable=False, default=' ')
    kind = db.Column(db.Boolean, nullable=False, default=0)
    normalValue = db.Column(db.String(200), nullable=False, default=' ')
    hasFile = db.Column(db.Boolean, nullable=False, default=0) #comment '0:没有;1:有'
    isClassical = db.Column(db.Boolean, nullable=False, default=1) #comment '1:是标准的;0:非标准的'
    SPETid = db.Column(db.String(36), nullable=False, default=' ')
    illustration = db.Column(db.Text, nullable=False, default=' ')
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    state = db.Column(db.Boolean, nullable=False, default=0) #comment '0:正常;1:锁定'

    def __init__(self, EXAMid, code, name, abbreviation, kind, normalValue, hasFile, classical, SPETid, illustration, createDay, optrid, state):
        self.EXAMid = EXAMid
        self.code = code
        self.name = name
        self.abbreviation = abbreviation
        self.kind = kind
        self.normalValue = normalValue
        self.hasFile = hasFile
        self.isClassical = isClassical
        self.SPETid = SPETid
        self.illustration = illustration
        self.createDay = createDay
        self.optrid = optrid
        self.state = state
        db.session.add(self)
        db.session.commit()
