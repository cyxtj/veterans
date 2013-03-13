#coding=utf-8

import json
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
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return self.name

    @classmethod
    def get_by_id(self, CDISid=None):
        print '_________________________'
        temp = ChineseDisease.query.filter_by(CDISid=CDISid).first()
        tempList = []
        tempList.append({})
        tempList[0]["CDISid"]=temp.CDISid
        tempList[0]["code"]=temp.code
        tempList[0]["name"]=temp.name
        tempList[0]["parentcode"]=temp.parentcode
        tempList[0]["level"]=temp.level
        tempList[0]["isClassical"]=temp.isClassical
        tempList[0]["SPETid"]=temp.SPETid
        tempList[0]["illustration"]=temp.illustration
        tempList[0]["createDay"]=temp.createDay
        tempList[0]["optrid"]=temp.optrid
        tempList[0]["state"]=temp.state
        return json.dumps(tempList)

    @classmethod
    def get_all(self):
        data = ChineseDisease.query.all()
        tempList = []
        print '_________________________'
        for (i, temp) in enumerate(data):
            tempList.append({})
            tempList[i]["CDISid"]=temp.CDISid
            tempList[i]["code"]=temp.code
            tempList[i]["name"]=temp.name
            tempList[i]["parentcode"]=temp.parentcode
            tempList[i]["level"]=temp.level
            tempList[i]["isClassical"]=temp.isClassical
            tempList[i]["SPETid"]=temp.SPETid
            tempList[i]["illustration"]=temp.illustration
            tempList[i]["createDay"]=temp.createDay
            tempList[i]["optrid"]=temp.optrid
            tempList[i]["state"]=temp.state
        return json.dumps(tempList)


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
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return self.name

    @classmethod 
    def get_by_id(selt, CASEid):
        print '_________________________'
        temp = dCase.query.filter_by(CASEid=CASEid).first()
        tempList = []
        tempList.append({})
        tempList[0]["CASEid"]=temp.CASEid
        tempList[0]["SPETid"]=temp.SPETid
        tempList[0]["DTMPid"]=temp.DTMPid
        tempList[0]["code"]=temp.code
        tempList[0]["outpatientCode"]=temp.outpatientCode
        tempList[0]["caseKind"]=temp.caseKind
        tempList[0]["name"]=temp.name
        tempList[0]["age"]=temp.age
        tempList[0]["month"]=temp.month
        tempList[0]["gender"]=temp.gender
        tempList[0]["nationality"]=temp.nationality
        tempList[0]["personSort"]=temp.personSort
        tempList[0]["afflication"]=temp.afflication
        tempList[0]["job"]=temp.job
        tempList[0]["tel"]=temp.tel
        tempList[0]["address"]=temp.address
        tempList[0]["birthplace"]=temp.birthplace
        tempList[0]["liveplace"]=temp.liveplace
        tempList[0]["education"]=temp.education
        tempList[0]["marriage"]=temp.marriage
        tempList[0]["ohistory"]=temp.ohistory
        tempList[0]["phistory"]=temp.phistory
        tempList[0]["fhistory"]=temp.fhistory
        tempList[0]["allergy"]=temp.allergy
        tempList[0]["extraMed"]=temp.extraMed
        tempList[0]["nhistory"]=temp.nhistory
        tempList[0]["mresult"]=temp.mresult
        tempList[0]["vresult"]=temp.vresult
        tempList[0]["illustration"]=temp.illustration
        tempList[0]["state"]=temp.state
        tempList[0]["createDay"]=temp.createDay
        tempList[0]["optrid"]=temp.optrid
        tempList[0]["hasFile"]=temp.hasFile
        tempList[0]["preState"]=temp.preState
        return json.dumps(tempList)

    @classmethod
    def get_all(self):
        data = dCase.query.all()
        tempList = []
        print '_________________________'
        for (i, temp) in enumerate(data):
            tempList.append({})
            tempList[i]["CASEid"]=temp.CASEid
            tempList[i]["SPETid"]=temp.SPETid
            tempList[i]["DTMPid"]=temp.DTMPid
            tempList[i]["code"]=temp.code
            tempList[i]["outpatientCode"]=temp.outpatientCode
            tempList[i]["caseKind"]=temp.caseKind
            tempList[i]["name"]=temp.name
            tempList[i]["age"]=temp.age
            tempList[i]["month"]=temp.month
            tempList[i]["gender"]=temp.gender
            tempList[i]["nationality"]=temp.nationality
            tempList[i]["personSort"]=temp.personSort
            tempList[i]["afflication"]=temp.afflication
            tempList[i]["job"]=temp.job
            tempList[i]["tel"]=temp.tel
            tempList[i]["address"]=temp.address
            tempList[i]["birthplace"]=temp.birthplace
            tempList[i]["liveplace"]=temp.liveplace
            tempList[i]["education"]=temp.education
            tempList[i]["marriage"]=temp.marriage
            tempList[i]["ohistory"]=temp.ohistory
            tempList[i]["phistory"]=temp.phistory
            tempList[i]["fhistory"]=temp.fhistory
            tempList[i]["allergy"]=temp.allergy
            tempList[i]["extraMed"]=temp.extraMed
            tempList[i]["nhistory"]=temp.nhistory
            tempList[i]["mresult"]=temp.mresult
            tempList[i]["vresult"]=temp.vresult
            tempList[i]["illustration"]=temp.illustration
            tempList[i]["state"]=temp.state
            tempList[i]["createDay"]=temp.createDay
            tempList[i]["optrid"]=temp.optrid
            tempList[i]["hasFile"]=temp.hasFile
            tempList[i]["preState"]=temp.preState
        return json.dumps(tempList)


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
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return self.name

    @classmethod
    def get_by_id(self, DMETid):
        print '_________________________'
        temp = dMethod.query.filter_by(DMETid=DMETid)
        tempList = []
        tempList.append({})
        tempList[0]["DMETid"] = temp.DMETid
        tempList[0]["code"] = temp.code
        tempList[0]["name"] = temp.name
        tempList[0]["parentcode"] = temp.parentcode
        tempList[0]["level"] = temp.level
        tempList[0]["isClassical"] = temp.isClassical
        tempList[0]["SPETid"] = temp.SPETid
        tempList[0]["illustration"] = temp.illustration
        tempList[0]["createDay"] = temp.createDay
        tempList[0]["optrid"] = temp.optrid
        tempList[0]["state"] = temp.state
        return json.dumps(tempList)

    @classmethod
    def get_all(self):
        data = dMethod.query.all()
        tempList = []
        print '_________________________'
        for (i, temp) in enumerate(data):
            tempList.append({})
            tempList[i]["DMETid"] = temp.DMETid
            tempList[i]["code"] = temp.code
            tempList[i]["name"] = temp.name
            tempList[i]["parentcode"] = temp.parentcode
            tempList[i]["level"] = temp.level
            tempList[i]["isClassical"] = temp.isClassical
            tempList[i]["SPETid"] = temp.SPETid
            tempList[i]["illustration"] = temp.illustration
            tempList[i]["createDay"] = temp.createDay
            tempList[i]["optrid"] = temp.optrid
            tempList[i]["state"] = temp.state
        return json.dumps(tempList)


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
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_id(self,DTMPid):
        print '_________________________'
        temp = dTemplate.query.filter_by(DTMPid=DTMPid)
        tempList = []
        tempList.append({})
        tempList[0]["DTMPid"] = temp.DTMPid
        tempList[0]["code"] = temp.code
        tempList[0]["name"] = temp.name
        tempList[0]["useClassCdis"] = temp.useClassCdis
        tempList[0]["useClassDmet"] = temp.useClassDmet
        tempList[0]["CDISid"] = temp.CDISid
        tempList[0]["WDISid"] = temp.WDISid
        tempList[0]["SEMCid"] = temp.SEMCid
        tempList[0]["DMETid"] = temp.DMETid
        tempList[0]["takeWay"] = temp.takeWay
        tempList[0]["drugForm"] = temp.drugForm
        tempList[0]["SPETid"] = temp.SPETid
        tempList[0]["illustration"] = temp.illustration
        tempList[0]["createDay"] = temp.createDay
        tempList[0]["optrid"] = temp.optrid
        tempList[0]["state"] = temp.state
        return json.dumps(tempList)

    @classmethod
    def get_all(self):
        data = dTemplate.query.all()
        tempList = []
        print '_________________________'
        for (i, temp) in enumerate(data):
            tempList.append({})
            tempList[i]["DTMPid"] = temp.DTMPid
            tempList[i]["code"] = temp.code
            tempList[i]["name"] = temp.name
            tempList[i]["useClassCdis"] = temp.useClassCdis
            tempList[i]["useClassDmet"] = temp.useClassDmet
            tempList[i]["CDISid"] = temp.CDISid
            tempList[i]["WDISid"] = temp.WDISid
            tempList[i]["SEMCid"] = temp.SEMCid
            tempList[i]["DMETid"] = temp.DMETid
            tempList[i]["takeWay"] = temp.takeWay
            tempList[i]["drugForm"] = temp.drugForm
            tempList[i]["SPETid"] = temp.SPETid
            tempList[i]["illustration"] = temp.illustration
            tempList[i]["createDay"] = temp.createDay
            tempList[i]["optrid"] = temp.optrid
            tempList[i]["state"] = temp.state
        return json.dumps(tempList)




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
        self.optrid = optrid
        self.state = state
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_id(self, DRUGid):
        print '_________________________'
        temp = drug.query.filter_by(DRUGid=DRUGid).first()
        tempList = []
        tempList.append({})
        tempList[0]["code"] = temp.code
        tempList[0]["name"] = temp.name
        tempList[0]["unit"] = temp.unit
        tempList[0]["alias"] = temp.alias
        tempList[0]["py"] = temp.py
        tempList[0]["wb"] = temp.wb
        tempList[0]["isClassical"] = temp.isClassical
        tempList[0]["SPETid"] = temp.SPETid
        tempList[0]["state"] = temp.state
        return json.dumps(tempList)

    @classmethod
    def get_all(self):
        data = drug.query.all()
        tempList = []
        print '____________________________________'
        for (i, temp) in enumerate(data):
            tempList.append({})
            tempList[i]["code"] = temp.code
            tempList[i]["name"] = temp.name
            tempList[i]["unit"] = temp.unit
            tempList[i]["alias"] = temp.alias
            tempList[i]["py"] = temp.py
            tempList[i]["wb"] = temp.wb
            tempList[i]["isClassical"] = temp.isClassical
            tempList[i]["SPETid"] = temp.SPETid
            tempList[i]["illustration"] = temp.illustration
            tempList[i]["state"] = temp.state
        return json.dumps(tempList)



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
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_id(self, FREPid):
        print '____________________________________'
        temp = fixedrecipe.query.filter_by(FREPid=FREPid).first()
        tempList = []
        tempList.append({})
        tempList[0]["code"] = temp.code
        tempList[0]["name"] = temp.name
        tempList[0]["effect"] = temp.effect
        tempList[0]["py"] = temp.py
        tempList[0]["wb"] = temp.wb
        tempList[0]["isClassical"] = temp.isClassical
        tempList[0]["SPETid"] = temp.SPETid
        tempList[0]["state"] = temp.state
        return json.dumps(tempList)

    @classmethod
    def get_all(self):
        data = fixedrecipe.query.all()
        tempList = []
        print '____________________________________'
        for (i, temp) in enumerate(data):
            tempList.append({})
            tempList[i]["code"] = temp.code
            tempList[i]["name"] = temp.name
            tempList[i]["effect"] = temp.effect
            tempList[i]["py"] = temp.py
            tempList[i]["wb"] = temp.wb
            tempList[i]["isClassical"] = temp.isClassical
            tempList[i]["SPETid"] = temp.SPETid
            tempList[i]["state"] = temp.state
        return json.dumps(tempList)



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
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_id(self, FREPid):
        print '____________________________________'
        temp = semiotic.query.filter_by(FREPid=FREPid).first()
        tempList = []
        tempList.append({})
        tempList[0]["SEMCid"] = temp.SEMCid
        tempList[0]["CDISid"] = temp.CDISid
        tempList[0]["code"] = temp.code
        tempList[0]["groupCode"] = temp.groupCode
        tempList[0]["name"] = temp.name
        tempList[0]["isClassical"] = temp.isClassical
        tempList[0]["SPETid"] = temp.SPETid
        tempList[0]["illustration"] = temp.illustration
        tempList[0]["createDay"] = temp.createDay
        tempList[0]["optrid"] = temp.optrid
        tempList[0]["state"] = temp.state
        return json.dumps(tempList)

    @classmethod
    def get_all(self):
        data = semiotic.query.all()
        tempList = []
        for (i, temp) in enumerate(data):
            print '____________________________________'
            tempList.append({})
            tempList[i]["SEMCid"] = temp.SEMCid
            tempList[i]["CDISid"] = temp.CDISid
            tempList[i]["code"] = temp.code
            tempList[i]["groupCode"] = temp.groupCode
            tempList[i]["name"] = temp.name
            tempList[i]["isClassical"] = temp.isClassical
            tempList[i]["SPETid"] = temp.SPETid
            tempList[i]["illustration"] = temp.illustration
            tempList[i]["createDay"] = temp.createDay
            tempList[i]["optrid"] = temp.optrid
            tempList[i]["state"] = temp.state
        return json.dumps(tempList)


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
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_id(self,SYPMid):
        print '____________________________________'
        temp = symptom.query.filter_by(SYPMid=SYPMid)
        tempList = []
        tempList.append({})
        tempList[0]["SYPMid"] = temp.SYPMid
        tempList[0]["code"] = temp.code
        tempList[0]["name"] = temp.name
        tempList[0]["parentcode"] = temp.parentcode
        tempList[0]["level"] = temp.level
        tempList[0]["kind"] = temp.kind
        tempList[0]["sort"] = temp.sort
        tempList[0]["valSort"] = temp.valSort
        tempList[0]["hasFile"] = temp.hasFile
        tempList[0]["isClassical"] = temp.isClassical
        tempList[0]["SPETid"] = temp.SPETid
        tempList[0]["illustration"] = temp.illustration
        tempList[0]["createDay"] = temp.createDay
        tempList[0]["optrid"] = temp.optrid
        tempList[0]["state"] = temp.state
        return json.dumps(tempList)

    @classmethod
    def get_all(self):
        data = temp.symptom.query.all()
        tempList = []
        print '____________________________________'
        for (i, temp) in enumerate(data):
            tempList.append({})
            tempList[i]["SYPMid"] = temp.SYPMid
            tempList[i]["code"] = temp.code
            tempList[i]["name"] = temp.name
            tempList[i]["parentcode"] = temp.parentcode
            tempList[i]["level"] = temp.level
            tempList[i]["kind"] = temp.kind
            tempList[i]["sort"] = temp.sort
            tempList[i]["valSort"] = temp.valSort
            tempList[i]["hasFile"] = temp.hasFile
            tempList[i]["isClassical"] = temp.isClassical
            tempList[i]["SPETid"] = temp.SPETid
            tempList[i]["illustration"] = temp.illustration
            tempList[i]["createDay"] = temp.createDay
            tempList[i]["optrid"] = temp.optrid
            tempList[i]["state"] = temp.state
        return json.dumps(tempList)


class WesternDisease(db.Model):
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
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_by_id(self,WDISid):
        temp = WesternDisease.query.filter_by(WDISid=WDISid)
        tempList = []
        tempList.append({})
        tempList[0]["WDISid"] = temp.WDISid
        tempList[0]["code"] = temp.code
        tempList[0]["name"] = temp.name
        tempList[0]["parentcode"] = temp.parentcode
        tempList[0]["level"] = temp.level
        tempList[0]["isClassical"] = temp.isClassical
        tempList[0]["SPETid"] = temp.SPETid
        tempList[0]["illustration"] = temp.illustration
        tempList[0]["createDay"] = temp.createDay
        tempList[0]["optrid"] = temp.optrid
        tempList[0]["state"] = temp.state
        return json.dumps(tempList)

    @classmethod
    def get_all(self):
        data = WesternDisease.query.all()
        tempList = []
        print '____________________________________'
        for (i, temp) in enumerate(data):
            tempList.append({})
            tempList[i]["WDISid"] = temp.WDISid
            tempList[i]["code"] = temp.code
            tempList[i]["name"] = temp.name
            tempList[i]["parentcode"] = temp.parentcode
            tempList[i]["level"] = temp.level
            tempList[i]["isClassical"] = temp.isClassical
            tempList[i]["SPETid"] = temp.SPETid
            tempList[i]["illustration"] = temp.illustration
            tempList[i]["createDay"] = temp.createDay
            tempList[i]["optrid"] = temp.optrid
            tempList[i]["state"] = temp.state
        return json.dumps(tempList)
