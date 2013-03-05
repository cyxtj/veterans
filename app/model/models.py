#coding=utf-8

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:levis822@localhost:3306/dbo'
db = SQLAlchemy(app)


class ChineseDisease(db.Model):
    CDISid = db.Column(db.String(36), nullable=False, primary_key=True)
    code = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    parentcode = db.Column(db.String(20), nullable=False) #comment '无父节点,用-1代表'
    level = db.Column(db.SMALLINT, nullable=False) #comment '从1开始'
    isClassical = db.Column(db.Boolean, nullable=False, default=1) #comment '1:是标准的;0:非标准的'
    SPETid = db.Column(db.String(36), nullable=False, default=' ')
    illustration = db.Column(db.Text, nullable=False, default=' ')
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    state = db.Column(db.SMALLINT, nullable=False, default=0) #comment '0:正常;1:锁定'

    def __init__(self, CDISid, code, name, parentcode, level, isClassical, SPETid, illustration, createDay, optrid, state):
        self.CDISid = CDISid
        self.code = code
        self.name = name
        self.parentcode = parentcode
        self.level = level
        self.isClassical = isClassical
        self.SPETid = SPETid
        self.illustration = illustration
        self.createDay = createDay
        self.optrid = optrid
        self.state = state

    def __repr__(self):
        return self.CDISid

    @classmethod
    def data(self, CDISid=None):
        if CDISid:
            print CDISid
            return ChineseDisease.query.filter_by(CDISid=CDISid).first()
        else:
            return ChineseDisease.query.all()


class dCase(db.Model):
    CASEid = db.Column(db.String(36), nullable=False, primary_key=True)
    SPETid = db.Column(db.String(36), nullable=False, default=' ')
    DTMPid = db.Column(db.String(36), nullable=False, default=' ')
    code = db.Column(db.String(20), nullable=False)
    outpatientCode = db.Column(db.String(20), nullable=False)
    caseKind = db.Column(db.SMALLINT, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.SMALLINT, nullable=False)
    month = db.Column(db.SMALLINT, nullable=False, default=0)
    gender = db.Column(db.Boolean, nullable=False) #comment '0:男;1:女'
    nationality = db.Column(db.Boolean, nullable=False)
    personSort = db.Column(db.Boolean, nullable=False)
    afflication = db.Column(db.String(200), nullable=False, default=' ')
    job = db.Column(db.String(20), nullable=False, default=' ')
    tel = db.Column(db.String(20), nullable=False, default=' ')
    address = db.Column(db.String(200), nullable=False, default=' ')
    birthplace = db.Column(db.String(6), nullable=False)
    liveplace = db.Column(db.String(6), nullable=False)
    education = db.Column(db.Boolean, nullable=False)
    marriage = db.Column(db.Boolean, nullable=False)
    ohistory = db.Column(db.Text, nullable=False, default=' ')
    phistory = db.Column(db.Text, nullable=False, default=' ')
    fhistory = db.Column(db.Text, nullable=False, default=' ')
    allergy = db.Column(db.Text, nullable=False, default=' ')
    extraMed = db.Column(db.String(500), nullable=False, default=' ')
    nhistory = db.Column(db.Text, nullable=False, default=' ')
    mresult = db.Column(db.Boolean, nullable=False)
    vresult = db.Column(db.String(500), nullable=False)
    illustration = db.Column(db.Text, nullable=False, default=' ')
    state = db.Column(db.Boolean, nullable=False, default=0) #comment '0:正常;1:锁定'
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    hasFile = db.Column(db.Boolean, nullable=False, default=0) #comment '0:没有;1:有'
    preState = db.Column(db.Boolean, nullable=False)

    def __init__(self, CASEid, SPETid, DTMPid, code, outpatientCode, caseKind, name, age, month, gender, nationality, personSort, afflication, job, tel, address, birthplace, liveplace, education, marriage, ohistory, phistory, fhistory, allergy, extraMed, nhistory, mresult, vresult, illustration, state, createDay, optrid, hasFile, preState):
        self.CASEid = CASEid
        self.SPETid = SPETid
        self.DTMPid = DTMPid
        self.code = code
        self.outpatientCode = outpatientCode
        self.caseKind = caseKind
        self.name = name
        self.age = age
        self.month = month
        self.gender = gender
        self.nationality = nationality
        self.personSort = personSort
        self.afflication = afflication
        self.job = job
        self.tel = tel
        self.address = address
        self.birthplace = birthplace
        self.liveplace = liveplace
        self.education = education
        self.marriage = marriage
        self.ohistory = ohistory
        self.phistory = phistory
        self.fhistory = fhistory
        self.allergy = allergy
        self.extraMed = extraMed
        self.nhistory = nhistory
        self.mresult = mresult
        self.vresult = vresult
        self.illustration = illustration
        self.state = state
        self.createDay = createDay
        self.optrid = optrid
        self.hasFile = hasFile
        self.preState = preState


class dMethod(db.Model):
    DMETid = db.Column(db.String(36), nullable=False, primary_key=True)
    code = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    parentcode = db.Column(db.String(20), nullable=False) #comment '无父节点,用-1代表'
    level = db.Column(db.Boolean, nullable=False) #comment '从1开始'
    isClassical = db.Column(db.Boolean, nullable=False, default=1) #comment '1:是标准的;0:非标准的'
    SPETid = db.Column(db.String(36), nullable=False, default=' ')
    illustration = db.Column(db.Text, nullable=False, default=' ')
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    state = db.Column(db.Boolean, nullable=False, default=0) #comment '0:正常;1:锁定'

    def __init__(self, DMETid, code, name, parentcode, level, classical, SPETid, illustration, createDay, optrid, state):
        self.DMETid = DMETid
        self.code = code
        self.name = name
        self.parentcode = parentcode
        self.level = level
        self.isClassical = isClassical
        self.SPETid = SPETid
        self.illustration = illustration
        self.createDay = createDay
        self.optrid = optrid
        self.state = state


class dTemplate(db.Model):
    DTMPid = db.Column(db.String(36), nullable=False, primary_key=True)
    code = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    useClassCdis = db.Column(db.Boolean, nullable=False, default=0)
    useClassDmet = db.Column(db.Boolean, nullable=False, default=0)
    CDISid = db.Column(db.String(36), nullable=False, default=' ')
    WDISid = db.Column(db.String(36), nullable=False, default=' ')
    SEMCid = db.Column(db.String(36), nullable=False)
    DMETid = db.Column(db.String(36), nullable=False)
    takeWay = db.Column(db.Boolean, nullable=False)
    drugForm = db.Column(db.Boolean, nullable=False)
    SPETid = db.Column(db.String(36), nullable=False, default=' ')
    illustration = db.Column(db.Text, nullable=False, default=' ')
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    state = db.Column(db.Boolean, nullable=False, default=0) #comment '0:正常;1:锁定'

    def __init__(self, DTMPid, code, name, useClassCdis, useClassDmet, CDISid, WDISid, SEMCid, DMETid, takeWay, drugForm, SPETid, illustration, createDay, optrid, state):
        self.DTMPid = DTMPid
        self.code = code
        self.name = name
        self.useClassCdis = useClassCdis
        self.useClassDmet = useClassDmet
        self.CDISid = CDISid
        self.WDISid = WDISid
        self.SEMCid = SEMCid
        self.DMETid = DMETid
        self.takeWay = takeWay
        self.drugForm = drugForm
        self.SPETid = SPETid
        self.illustration = illustration
        self.createDay = createDay
        self.optrid = optrid
        self.state = state


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


class drug(db.Model):
    DRUGid = db.Column(db.String(36), nullable=False, primary_key=True)
    code = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    unit = db.Column(db.String(10), nullable=False)
    alias = db.Column(db.String(100), nullable=False, default=' ')
    py = db.Column(db.String(20), nullable=False, default=' ')
    wb = db.Column(db.String(20), nullable=False, default=' ')
    isClassical = db.Column(db.Boolean, nullable=False, default=1) #comment '1:是标准的;0:非标准的'
    SPETid = db.Column(db.String(36), nullable=False, default=' ')
    illustration = db.Column(db.Text, nullable=False, default=' ')
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    state = db.Column(db.Boolean, nullable=False, default=0) #comment '0:正常;1:锁定'

    def __init__(self, DRUGid, code, name, unit, alias, py, wb, classical, SPETid, illustration, createDay, optrid, state):
        self.DRUGid = DRUGid
        self.code = code
        self.name = name
        self.unit = unit
        self.alias = alias
        self.py = py
        self.wb = wb
        self.isClassical = isClassical
        self.SPETid = SPETid
        self.illustration = illustration
        self.createDay = createDay
        self.optrid = optrid
        self.state = state


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


class fixedrecipe(db.Model):
    FREPid = db.Column(db.String(36), nullable=False, primary_key=True)
    code = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    effect = db.Column(db.String(200), nullable=False, default=' ')
    py = db.Column(db.String(20), nullable=False, default=' ')
    wb = db.Column(db.String(20), nullable=False, default=' ')
    isClassical = db.Column(db.Boolean, nullable=False, default=1) #comment '1:是标准的;0:非标准的'
    SPETid = db.Column(db.String(36), nullable=False, default=' ')
    illustration = db.Column(db.Text, nullable=False, default=' ')
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    state = db.Column(db.Boolean, nullable=False, default=0) #comment '0:正常;1:锁定'

    def __init__(self, FREPid, code, name, effect, py, wb, classical, SPETid, illustration, createDay, optrid, state):
        self.FREPid = FREPid
        self.code = code
        self.name = name
        self.effect = effect
        self.py = py
        self.wb = wb
        self.isClassical = isClassical
        self.SPETid = SPETid
        self.illustration = illustration
        self.createDay = createDay
        self.optrid = optrid
        self.state = state


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


class semiotic(db.Model):
    SEMCid = db.Column(db.String(36), nullable=False, primary_key=True)
    CDISid = db.Column(db.String(36), db.ForeignKey('chinese_disease.CDISid'))
    code = db.Column(db.String(20), nullable=False)
    groupCode = db.Column(db.String(20), nullable=False, default=' ')
    name = db.Column(db.String(100), nullable=False)
    isClassical = db.Column(db.Boolean, nullable=False, default=1) #comment '1:是标准的;0:非标准的'
    SPETid = db.Column(db.String(36), nullable=False, default=' ')
    illustration = db.Column(db.Text, nullable=False, default=' ')
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    state = db.Column(db.Boolean, nullable=False, default=0) #comment '0:正常;1:锁定'
    
    def __init__(self, SEMCid, CDISid, code, groupCode, name, classical, SPETid, illustration, createDay, optrid, state):
        self.SEMCid = SEMCid
        self.CDISid = CDISid
        self.code = code
        self.groupCode = groupCode
        self.name = name
        self.isClassical = isClassical
        self.SPETid = SPETid
        self.illustration = illustration
        self.createDay = createDay
        self.optrid = optrid
        self.state = state


class symptom(db.Model):
    SYPMid = db.Column(db.String(36), nullable=False, primary_key=True)
    code = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    parentcode = db.Column(db.String(20), nullable=False) #comment '无父节点,用-1代表'
    level = db.Column(db.Boolean, nullable=False) #comment '从1开始'
    kind = db.Column(db.Boolean, nullable=False, default=0) #comment '分为 望、闻、问、切'
    sort = db.Column(db.Boolean, nullable=False, default=1) #comment '1:主症,2:兼症'
    valSort = db.Column(db.INT, nullable=False, default=0) #comment '0:字符串;-1:checkbox;其他:下拉选项'
    hasFile = db.Column(db.Boolean, nullable=False, default=0) #comment '0:没有;1:有'
    isClassical = db.Column(db.Boolean, nullable=False, default=1) #comment '1:是标准的;0:非标准的'
    SPETid = db.Column(db.String(36), nullable=False, default=' ')
    illustration = db.Column(db.Text, nullable=False, default=' ')
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    state = db.Column(db.Boolean, nullable=False, default=0) #comment '0:正常;1:锁定'

    def __init__(self, SYPMid, code, name, parentcode, level, kind, sort, valSort, hasFile, classical, SPETid, illustration, createDay, optrid, state):
        self.SYPMid = SYPMid
        self.code = code
        self.name = name
        self.parentcode = parentcode
        self.level = level
        self.kind = kind
        self.sort = sort
        self.valSort = valSort
        self.hasFile = hasFile
        self.isClassical = isClassical
        self.SPETid = SPETid
        self.illustration = illustration
        self.createDay = createDay
        self.optrid = optrid
        self.state = state


class WestenDisease(db.Model):
    WDISid = db.Column(db.String(36), nullable=False, primary_key=True)
    code = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    parentcode = db.Column(db.String(20), nullable=False) #comment '无父节点,用-1代表'
    level = db.Column(db.Boolean, nullable=False) #comment '从1开始'
    isClassical = db.Column(db.Boolean, nullable=False, default=1) #comment '1:是标准的;0:非标准的'
    SPETid = db.Column(db.String(36), nullable=False, default=' ')
    illustration = db.Column(db.Text, nullable=False, default=' ')
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    state = db.Column(db.Boolean, nullable=False, default=0) #comment '0:正常;1:锁定'

    def __init__(self, WDISid, code, name, parentcode, level, classical, SPETid, illustration, createDay, optrid, state):
        self.WDISid = WDISid
        self.code = code
        self.name = name
        self.parentcode = parentcode
        self.level = level
        self.isClassical = isClassical
        self.SPETid = SPETid
        self.illustration = illustration
        self.createDay = createDay
        self.optrid = optrid
        self.state = state


