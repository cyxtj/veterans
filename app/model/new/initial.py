#coding=utf-8

import json
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import flask.ext.restless

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:levis822@localhost:3306/dbo2'
db = SQLAlchemy(app)


class MissionAlgor(db.Model):
    MIALid = db.Column(db.String(36), nullable=False, primary_key=True)
    LEMIid = db.Column(db.String(36), db.ForeignKey('learn_mission.LEMIid'))
    ALGOid = db.Column(db.String(36), db.ForeignKey('algorithm.ALGOid'))
    code = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    type = db.Column(db.SMALLINT, nullable=False)
    sequence = db.Column(db.Integer, nullable=False)
    #primary key(MIALid)

    def __init__(self, MIALid, LEMIid, ALGOid, code, name, type, sequence):
        self.MIALid = MIALid 
        self.LEMIid = LEMIid 
        self.ALGOid = ALGOid 
        self.code = code 
        self.name = name 
        self.type = type 
        self.sequence = sequence 


class MissionPar(db.Model):
    MIPAid = db.Column(db.String(36), nullable=False, primary_key=True)
    MIALid = db.Column(db.String(36), db.ForeignKey('mission_algor.MIALid'))
    code = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    value = db.Column(db.String(100), nullable=False)
    illustration = db.Column(db.String(200), nullable=False, default=' ')
    #primary key(MIPAid)

    def __init__(self, MIPAid, MIALid, code, name, value, illustration):

        self.MIPAid = MIPAid 
        self.MIALid = MIALid 
        self.code = code 
        self.name = name 
        self.value = value 
        self.illustration = illustration 


class accessory(db.Model):
    ACCEid = db.Column(db.String(36), nullable=False, primary_key=True)
    ownerid = db.Column(db.String(36), nullable=False)
    realFilename = db.Column(db.String(100), nullable=False, default=' ')
    filename = db.Column(db.String(100), nullable=False, default=' ')
    filetype = db.Column(db.String(50), nullable=False, default=' ')
    path = db.Column(db.String(200), nullable=False, default=' ')
    illustration = db.Column(db.Text, nullable=False, default=' ')
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    #primary key(ACCEid)

    def __init__(self, ACCEid, ownerid, realFilename, filename, filetype, path, illustration, createDay, optrid):

        self.ACCEid = ACCEid 
        self.ownerid = ownerid 
        self.realFilename = realFilename 
        self.filename = filename 
        self.filetype = filetype 
        self.path = path 
        self.illustration = illustration 
        self.createDay = createDay 
        self.optrid = optrid 


class algorithm(db.Model):
    ALGOid = db.Column(db.String(36), nullable=False, primary_key=True)
    code = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    type = db.Column(db.SMALLINT, nullable=False)
    illustration = db.Column(db.String(300), nullable=False, default=' ')
    #primary key(ALGOid)

    def __init__(self, ALGOid, code, name, type, illustration):

        self.ALGOid = ALGOid 
        self.code = code 
        self.name = name 
        self.type = type 
        self.illustration = illustration 


class algorithmPar(db.Model):
    ALPAid = db.Column(db.String(36), nullable=False, primary_key=True)
    ALGOid = db.Column(db.String(36), db.ForeignKey('algorithm.ALGOid'))
    code = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    value = db.Column(db.String(100), nullable=False)
    illustration = db.Column(db.String(200), nullable=False, default=' ')
    #primary key(ALPAid)

    def __init__(self, ALPAid, ALGOid, code, name, value, illustration):

        self.ALPAid = ALPAid 
        self.ALGOid = ALGOid 
        self.code = code 
        self.name = name 
        self.value = value 
        self.illustration = illustration 


class ancientBook(db.Model):
    ANBOid = db.Column(db.String(36), nullable=False, primary_key=True)
    REBOid = db.Column(db.String(36), db.ForeignKey('read_book.REBOid'))
    literature_name = db.Column(db.String(20), nullable=False, default=' ')
    pubType = db.Column(db.String(10), nullable=False, default=' ')
    benefit = db.Column(db.String(100), nullable=False, default=' ')
    #primary key(ANBOid)

    def __init__(self, ANBOid, REBOid, literature_name, pubType, benefit):

        self.ANBOid = ANBOid 
        self.REBOid = REBOid 
        self.literature_name = literature_name 
        self.pubType = pubType 
        self.benefit = benefit 


class ancientSpecialist(db.Model):
    ANSPid = db.Column(db.String(36), nullable=False, primary_key=True)
    REBOid = db.Column(db.String(36), db.ForeignKey('read_book.REBOid'))
    name = db.Column(db.String(20), nullable=False)
    major = db.Column(db.String(100), nullable=False)
    #primary key(ANSPid)

    def __init__(self, ANSPid, REBOid, name, major):

        self.ANSPid = ANSPid 
        self.REBOid = REBOid 
        self.name = name 
        self.major = major 


class background(db.Model):
    BACKid = db.Column(db.String(36), nullable=False, primary_key=True)
    STSTid = db.Column(db.String(36), db.ForeignKey('study_story.STSTid'))
    sport = db.Column(db.String(300), nullable=False)
    literature = db.Column(db.String(300), nullable=False)
    health = db.Column(db.String(300), nullable=False)
    tour = db.Column(db.String(300), nullable=False)
    other_hobby = db.Column(db.String(300), nullable=False)
    smoke = db.Column(db.String(300), nullable=False)
    coffee = db.Column(db.String(300), nullable=False)
    alcohol = db.Column(db.String(300), nullable=False)
    tea = db.Column(db.String(300), nullable=False)
    movie = db.Column(db.String(300), nullable=False)
    other_habit = db.Column(db.String(300), nullable=False)
    chinese = db.Column(db.String(300), nullable=False)
    philosophy = db.Column(db.String(300), nullable=False)
    art = db.Column(db.String(300), nullable=False)
    custom = db.Column(db.String(300), nullable=False)
    belief = db.Column(db.String(300), nullable=False)
    other_culture = db.Column(db.String(300), nullable=False)
    other_experience = db.Column(db.Text, nullable=False, default=' ')
    tiptop_duty = db.Column(db.String(300), nullable=False)
    years = db.Column(db.String(10), nullable=False)
    organization = db.Column(db.String(300), nullable=False)
    parttime_duty = db.Column(db.String(300), nullable=False)
    glory = db.Column(db.String(300), nullable=False)
    acquire_time = db.Column(db.String(10), nullable=False)
    #primary key(BACKid)

    def __init__(self, BACKid, STSTid, sport, literature, health, tour, other_hobby, smoke, coffee, alcohol, tea, movie, other_habit, chinese, philosophy, art, custom, belief, other_culture, other_experience, tiptop_duty, years, organization, parttime_duty, glory, acquire_time):

        self.BACKid = BACKid 
        self.STSTid = STSTid 
        self.sport = sport 
        self.literature = literature 
        self.health = health 
        self.tour = tour 
        self.other_hobby = other_hobby 
        self.smoke = smoke 
        self.coffee = coffee 
        self.alcohol = alcohol 
        self.tea = tea 
        self.movie = movie 
        self.other_habit = other_habit 
        self.chinese = chinese 
        self.philosophy = philosophy 
        self.art = art 
        self.custom = custom 
        self.belief = belief 
        self.other_culture = other_culture 
        self.other_experience = other_experience 
        self.tiptop_duty = tiptop_duty 
        self.years = years 
        self.organization = organization 
        self.parttime_duty = parttime_duty 
        self.glory = glory 
        self.acquire_time = acquire_time 


class badInstance(db.Model):
    BAINid = db.Column(db.String(36), nullable=False, primary_key=True)
    REBOid = db.Column(db.String(36), db.ForeignKey('read_book.REBOid'))
    content = db.Column(db.Text, nullable=False, default=' ')
    #primary key(BAINid)

    def __init__(self, BAINid, REBOid, content):

        self.BAINid = BAINid 
        self.REBOid = REBOid 
        self.content = content 


class basicinformation(db.Model):
    Num = db.Column(db.String(50), nullable=False)
    Name = db.Column(db.String(50), nullable=False)
    Gender = db.Column(db.String(50), nullable=False)
    Age = db.Column(db.String(50), nullable=False)
    Diploma = db.Column(db.String(50), nullable=False)
    Dgree = db.Column(db.String(50), nullable=False)
    Rank = db.Column(db.String(50))
    PromotionTime = db.Column(db.String(50))
    Duty = db.Column(db.Text)
    HashId = db.Column(db.String(36), nullable=False, primary_key=True)
    State = db.Column(db.SMALLINT)
    SpecialisId = db.Column(db.String(36), db.ForeignKey('specialist.SPETid'))
    OperatorId = db.Column(db.String(36))
    CreateDate = db.Column(db.DateTime)
    #primary key(HashId)

    def __init__(self, Num, Name, Gender, Age, Diploma, Dgree, Rank, PromotionTime, Duty, HashId, State, SpecialisId, OperatorId, CreateDate):

        self.Num = Num 
        self.Name = Name 
        self.Gender = Gender 
        self.Age = Age 
        self.Diploma = Diploma 
        self.Dgree = Dgree 
        self.Rank = Rank 
        self.PromotionTime = PromotionTime 
        self.Duty = Duty 
        self.HashId = HashId 
        self.State = State 
        self.SpecialisId = SpecialisId 
        self.OperatorId = OperatorId 
        self.CreateDate = CreateDate 


class bookResult(db.Model):
    Num = db.Column(db.String(50))
    Title = db.Column(db.String(50))
    Author = db.Column(db.String(50))
    AuthorAffiliation = db.Column(db.String(50))
    Abstract = db.Column(db.Text)
    Source = db.Column(db.String(50))
    Files = db.Column(db.String(50))
    SpecialistId = db.Column(db.String(36), db.ForeignKey('specialist.SPETid'))
    OperatorId = db.Column(db.String(36))
    HashId = db.Column(db.String(36), nullable=False, primary_key=True)
    State = db.Column(db.SMALLINT)
    #primary key(HashId)

    def __init__(self, Num, Title, Author, AuthorAffiliation, Abstract, Source, Files, SpecialistId, OperatorId, HashId, State):

        self.Num = Num 
        self.Title = Title 
        self.Author = Author 
        self.AuthorAffiliation = AuthorAffiliation 
        self.Abstract = Abstract 
        self.Source = Source 
        self.Files = Files 
        self.SpecialistId = SpecialistId 
        self.OperatorId = OperatorId 
        self.HashId = HashId 
        self.State = State 


class ChineseDisease(db.Model):
    CDISid = db.Column(db.String(36), nullable=False, primary_key=True)
    code = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    parentcode = db.Column(db.String(20), nullable=False)
    level = db.Column(db.SMALLINT, nullable=False)
    isClassical = db.Column(db.Boolean, nullable=False, default=1)
    SPETid = db.Column(db.String(36), nullable=False, default=' ')
    illustration = db.Column(db.Text, nullable=False, default=' ')
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    state = db.Column(db.SMALLINT, nullable=False, default=0)
    #primary key(CDISid))
    #key = db.Column(AK_CDISEASE_PK_CODE_CDISEASE (code)

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


class caseAnalysis(db.Model):
    CAANid = db.Column(db.String(36), nullable=False, primary_key=True)
    SPETid = db.Column(db.String(36), db.ForeignKey('specialist.SPETid'))
    CASEid = db.Column(db.String(36), nullable=False)
    diagnose_mode = db.Column(db.SMALLINT, nullable=False, default=0)
    diagnose_method = db.Column(db.SMALLINT, nullable=False, default=0)
    look_body = db.Column(db.String(50), nullable=False)
    illustration = db.Column(db.Text, nullable=False)
    tongue = db.Column(db.SMALLINT, nullable=False, default=0)
    tongue1 = db.Column(db.String(50), nullable=False)
    look_place = db.Column(db.String(50), nullable=False)
    sound = db.Column(db.String(50), nullable=False)
    taste = db.Column(db.String(50), nullable=False)
    question_answer = db.Column(db.String(200), nullable=False)
    question_content = db.Column(db.Text, nullable=False)
    special_question = db.Column(db.String(200), nullable=False)
    feel_diagnose = db.Column(db.String(200), nullable=False)
    habit_dmethod = db.Column(db.String(200), nullable=False)
    important_question = db.Column(db.String(500), nullable=False)
    information_select = db.Column(db.String(200), nullable=False)
    analysis_way = db.Column(db.String(500), nullable=False)
    analysis_method = db.Column(db.SMALLINT, nullable=False, default=0)
    other_method = db.Column(db.String(200), nullable=False)
    analysis_evidence = db.Column(db.String(200), nullable=False)
    reason_evidence = db.Column(db.String(200), nullable=False)
    character_evidence = db.Column(db.String(200), nullable=False)
    place_evidence = db.Column(db.String(200), nullable=False)
    situation_evidence = db.Column(db.String(200), nullable=False)
    semiotics = db.Column(db.String(50), nullable=False)
    recipe_name = db.Column(db.String(50), nullable=False)
    produce_method = db.Column(db.String(200), nullable=False)
    takedrug_way = db.Column(db.String(200), nullable=False)
    doctor_advice = db.Column(db.Text, nullable=False)
    experience = db.Column(db.String(500), nullable=False)
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    state = db.Column(db.SMALLINT, nullable=False, default=0)
    #primary key(CAANid)

    def __init__(self, CAANid, SPETid, CASEid, diagnose_mode, diagnose_method, look_body, illustration, tongue, tongue1, look_place, sound, taste, question_answer, question_content, special_question, feel_diagnose, habit_dmethod, important_question, information_select, analysis_way, analysis_method, other_method, analysis_evidence, reason_evidence, character_evidence, place_evidence, situation_evidence, semiotics, recipe_name, produce_method, takedrug_way, doctor_advice, experience, createDay, optrid, state):

        self.CAANid = CAANid 
        self.SPETid = SPETid 
        self.CASEid = CASEid 
        self.diagnose_mode = diagnose_mode 
        self.diagnose_method = diagnose_method 
        self.look_body = look_body 
        self.illustration = illustration 
        self.tongue = tongue 
        self.tongue1 = tongue1 
        self.look_place = look_place 
        self.sound = sound 
        self.taste = taste 
        self.question_answer = question_answer 
        self.question_content = question_content 
        self.special_question = special_question 
        self.feel_diagnose = feel_diagnose 
        self.habit_dmethod = habit_dmethod 
        self.important_question = important_question 
        self.information_select = information_select 
        self.analysis_way = analysis_way 
        self.analysis_method = analysis_method 
        self.other_method = other_method 
        self.analysis_evidence = analysis_evidence 
        self.reason_evidence = reason_evidence 
        self.character_evidence = character_evidence 
        self.place_evidence = place_evidence 
        self.situation_evidence = situation_evidence 
        self.semiotics = semiotics 
        self.recipe_name = recipe_name 
        self.produce_method = produce_method 
        self.takedrug_way = takedrug_way 
        self.doctor_advice = doctor_advice 
        self.experience = experience 
        self.createDay = createDay 
        self.optrid = optrid 
        self.state = state 


class classicCase(db.Model):
    clcaid = db.Column(db.String(36), nullable=False, primary_key=True)
    operatorId = db.Column(db.String(36))
    SPETid = db.Column(db.String(36), db.ForeignKey('specialist.SPETid'))
    state = db.Column(db.SMALLINT)
    diagnosisNo = db.Column(db.String(50))
    creatDate = db.Column(db.DateTime)
    num = db.Column(db.String(36), nullable=False)
    title = db.Column(db.String(50))
    source = db.Column(db.SMALLINT)
    caseNum = db.Column(db.String(50))
    name = db.Column(db.String(50))
    gender = db.Column(db.String(50))
    birthday = db.Column(db.String(50))
    people = db.Column(db.String(50))
    job = db.Column(db.String(50))
    hometown = db.Column(db.String(50))
    married = db.Column(db.String(50))
    address = db.Column(db.String(50))
    postcode = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    presentIll = db.Column(db.Text)
    pastIll = db.Column(db.Text)
    familyIll = db.Column(db.Text)
    personalIll = db.Column(db.Text)
    visit = db.Column(db.Text)
    note = db.Column(db.Text)
    remark = db.Column(db.Text)
    collectPerson = db.Column(db.String(50))
    collectTime = db.Column(db.String(50))
    verifyOpinion = db.Column(db.Text)
    verifyName = db.Column(db.String(50))
    verifyTime = db.Column(db.String(50))
    diagTime1 = db.Column(db.String(50))
    mainDisease1 = db.Column(db.Text)
    caseAbstract1 = db.Column(db.Text)
    zhengKeys1 = db.Column(db.Text)
    westdisease1 = db.Column(db.String(50))
    tcmdisease1 = db.Column(db.String(50))
    tcmsyndrome1 = db.Column(db.String(50))
    therapy1 = db.Column(db.Text)
    fangYao1 = db.Column(db.Text)
    otherCure1 = db.Column(db.Text)
    doctorAdvice1 = db.Column(db.Text)
    efficacy1 = db.Column(db.String(50))
    diagTime2 = db.Column(db.String(50))
    mainDisease2 = db.Column(db.Text)
    caseAbstract2 = db.Column(db.Text)
    zhengKeys2 = db.Column(db.Text)
    westdisease2 = db.Column(db.String(50))
    tcmdisease2 = db.Column(db.String(50))
    tcmsyndrome2 = db.Column(db.String(50))
    therapy2 = db.Column(db.Text)
    fangYao2 = db.Column(db.Text)
    otherCure2 = db.Column(db.Text)
    doctorAdvice2 = db.Column(db.Text)
    efficacy2 = db.Column(db.String(50))
    diagTime3 = db.Column(db.String(50))
    mainDisease3 = db.Column(db.Text)
    caseAbstract3 = db.Column(db.Text)
    zhengKeys3 = db.Column(db.Text)
    westdisease3 = db.Column(db.String(50))
    tcmdisease3 = db.Column(db.String(50))
    tcmsyndrome3 = db.Column(db.String(50))
    therapy3 = db.Column(db.Text)
    fangYao3 = db.Column(db.Text)
    otherCure3 = db.Column(db.Text)
    doctorAdvice3 = db.Column(db.Text)
    efficacy3 = db.Column(db.String(50))
    diagTime4 = db.Column(db.String(50))
    mainDisease4 = db.Column(db.Text)
    caseAbstract4 = db.Column(db.Text)
    zhengKeys4 = db.Column(db.Text)
    westdisease4 = db.Column(db.String(50))
    tcmdisease4 = db.Column(db.String(50))
    tcmsyndrome4 = db.Column(db.String(50))
    therapy4 = db.Column(db.Text)
    fangYao4 = db.Column(db.Text)
    otherCure4 = db.Column(db.Text)
    doctorAdvice4 = db.Column(db.Text)
    efficacy4 = db.Column(db.String(50))
    diagTime5 = db.Column(db.String(50))
    mainDisease5 = db.Column(db.Text)
    caseAbstract5 = db.Column(db.Text)
    zhengKeys5 = db.Column(db.Text)
    westdisease5 = db.Column(db.String(50))
    tcmdisease5 = db.Column(db.String(50))
    tcmsyndrome5 = db.Column(db.String(50))
    therapy5 = db.Column(db.Text)
    fangYao5 = db.Column(db.Text)
    otherCure5 = db.Column(db.Text)
    doctorAdvice5 = db.Column(db.Text)
    efficacy5 = db.Column(db.String(50))
    diagTime6 = db.Column(db.String(50))
    mainDisease6 = db.Column(db.Text)
    caseAbstract6 = db.Column(db.Text)
    zhengKeys6 = db.Column(db.Text)
    westdisease6 = db.Column(db.String(50))
    tcmdisease6 = db.Column(db.String(50))
    tcmsyndrome6 = db.Column(db.String(50))
    therapy6 = db.Column(db.Text)
    fangYao6 = db.Column(db.Text)
    otherCure6 = db.Column(db.Text)
    doctorAdvice6 = db.Column(db.Text)
    efficacy6 = db.Column(db.String(50))
    diagTime7 = db.Column(db.String(50))
    mainDisease7 = db.Column(db.Text)
    caseAbstract7 = db.Column(db.Text)
    zhengKeys7 = db.Column(db.Text)
    westdisease7 = db.Column(db.String(50))
    tcmdisease7 = db.Column(db.String(50))
    tcmsyndrome7 = db.Column(db.String(50))
    therapy7 = db.Column(db.Text)
    fangYao7 = db.Column(db.Text)
    otherCure7 = db.Column(db.Text)
    doctorAdvice7 = db.Column(db.Text)
    efficacy7 = db.Column(db.String(50))
    diagTime8 = db.Column(db.String(50))
    mainDisease8 = db.Column(db.Text)
    caseAbstract8 = db.Column(db.Text)
    zhengKeys8 = db.Column(db.Text)
    westdisease8 = db.Column(db.String(50))
    tcmdisease8 = db.Column(db.String(50))
    tcmsyndrome8 = db.Column(db.String(50))
    therapy8 = db.Column(db.Text)
    fangYao8 = db.Column(db.Text)
    otherCure8 = db.Column(db.Text)
    doctorAdvice8 = db.Column(db.Text)
    efficacy8 = db.Column(db.String(50))
    diagTime9 = db.Column(db.String(50))
    mainDisease9 = db.Column(db.Text)
    caseAbstract9 = db.Column(db.Text)
    zhengKeys9 = db.Column(db.Text)
    westdisease9 = db.Column(db.String(50))
    tcmdisease9 = db.Column(db.String(50))
    tcmsyndrome9 = db.Column(db.String(50))
    therapy9 = db.Column(db.Text)
    fangYao9 = db.Column(db.Text)
    otherCure9 = db.Column(db.Text)
    doctorAdvice9 = db.Column(db.Text)
    efficacy9 = db.Column(db.String(50))
    diagTime10 = db.Column(db.String(50))
    mainDisease10 = db.Column(db.Text)
    caseAbstract10 = db.Column(db.Text)
    zhengKeys10 = db.Column(db.Text)
    westdisease10 = db.Column(db.String(50))
    tcmdisease10 = db.Column(db.String(50))
    tcmsyndrome10 = db.Column(db.String(50))
    therapy10 = db.Column(db.Text)
    fangYao10 = db.Column(db.Text)
    otherCure10 = db.Column(db.Text)
    doctorAdvice10 = db.Column(db.Text)
    efficacy10 = db.Column(db.String(50))
    diagTime11 = db.Column(db.String(50))
    mainDisease11 = db.Column(db.Text)
    caseAbstract11 = db.Column(db.Text)
    zhengKeys11 = db.Column(db.Text)
    westdisease11 = db.Column(db.String(50))
    tcmdisease11 = db.Column(db.String(50))
    tcmsyndrome11 = db.Column(db.String(50))
    therapy11 = db.Column(db.Text)
    fangYao11 = db.Column(db.Text)
    otherCure11 = db.Column(db.Text)
    doctorAdvice11 = db.Column(db.Text)
    efficacy11 = db.Column(db.String(50))
    diagTime12 = db.Column(db.String(50))
    mainDisease12 = db.Column(db.Text)
    caseAbstract12 = db.Column(db.Text)
    zhengKeys12 = db.Column(db.Text)
    westdisease12 = db.Column(db.String(50))
    tcmdisease12 = db.Column(db.String(50))
    tcmsyndrome12 = db.Column(db.String(50))
    therapy12 = db.Column(db.Text)
    fangYao12 = db.Column(db.Text)
    otherCure12 = db.Column(db.Text)
    doctorAdvice12 = db.Column(db.Text)
    efficacy12 = db.Column(db.String(50))
    diagTime13 = db.Column(db.String(50))
    mainDisease13 = db.Column(db.Text)
    caseAbstract13 = db.Column(db.Text)
    zhengKeys13 = db.Column(db.Text)
    westdisease13 = db.Column(db.String(50))
    tcmdisease13 = db.Column(db.String(50))
    tcmsyndrome13 = db.Column(db.String(50))
    therapy13 = db.Column(db.Text)
    fangYao13 = db.Column(db.Text)
    otherCure13 = db.Column(db.Text)
    doctorAdvice13 = db.Column(db.Text)
    efficacy13 = db.Column(db.String(50))
    diagTime14 = db.Column(db.String(50))
    mainDisease14 = db.Column(db.Text)
    caseAbstract14 = db.Column(db.Text)
    zhengKeys14 = db.Column(db.Text)
    westdisease14 = db.Column(db.String(50))
    tcmdisease14 = db.Column(db.String(50))
    tcmsyndrome14 = db.Column(db.String(50))
    therapy14 = db.Column(db.Text)
    fangYao14 = db.Column(db.Text)
    otherCure14 = db.Column(db.Text)
    doctorAdvice14 = db.Column(db.Text)
    efficacy14 = db.Column(db.String(50))
    diagTime15 = db.Column(db.String(50))
    mainDisease15 = db.Column(db.Text)
    caseAbstract15 = db.Column(db.Text)
    zhengKeys15 = db.Column(db.Text)
    westdisease15 = db.Column(db.String(50))
    tcmdisease15 = db.Column(db.String(50))
    tcmsyndrome15 = db.Column(db.String(50))
    therapy15 = db.Column(db.Text)
    fangYao15 = db.Column(db.Text)
    otherCure15 = db.Column(db.Text)
    doctorAdvice15 = db.Column(db.Text)
    efficacy15 = db.Column(db.String(50))
    diagTime16 = db.Column(db.String(50))
    mainDisease16 = db.Column(db.Text)
    caseAbstract16 = db.Column(db.Text)
    zhengKeys16 = db.Column(db.Text)
    westdisease16 = db.Column(db.String(50))
    tcmdisease16 = db.Column(db.String(50))
    tcmsyndrome16 = db.Column(db.String(50))
    therapy16 = db.Column(db.Text)
    fangYao16 = db.Column(db.Text)
    otherCure16 = db.Column(db.Text)
    doctorAdvice16 = db.Column(db.Text)
    efficacy16 = db.Column(db.String(50))
    diagTime17 = db.Column(db.String(50))
    mainDisease17 = db.Column(db.Text)
    caseAbstract17 = db.Column(db.Text)
    zhengKeys17 = db.Column(db.Text)
    westdisease17 = db.Column(db.String(50))
    tcmdisease17 = db.Column(db.String(50))
    tcmsyndrome17 = db.Column(db.String(50))
    therapy17 = db.Column(db.Text)
    fangYao17 = db.Column(db.Text)
    otherCure17 = db.Column(db.Text)
    doctorAdvice17 = db.Column(db.Text)
    efficacy17 = db.Column(db.String(50))
    diagTime18 = db.Column(db.String(50))
    mainDisease18 = db.Column(db.Text)
    caseAbstract18 = db.Column(db.Text)
    zhengKeys18 = db.Column(db.Text)
    westdisease18 = db.Column(db.String(50))
    tcmdisease18 = db.Column(db.String(50))
    tcmsyndrome18 = db.Column(db.String(50))
    therapy18 = db.Column(db.Text)
    fangYao18 = db.Column(db.Text)
    otherCure18 = db.Column(db.Text)
    doctorAdvice18 = db.Column(db.Text)
    efficacy18 = db.Column(db.String(50))
    #primary key(clcaid)

    def __init__(self, clcaid, operatorId, SPETid, state, diagnosisNo, creatDate, num, title, source, caseNum, name, gender, birthday, people, job, hometown, married, address, postcode, phone, presentIll, pastIll, familyIll, personalIll, visit, note, remark, collectPerson, collectTime, verifyOpinion, verifyName, verifyTime, diagTime1, mainDisease1, caseAbstract1, zhengKeys1, westdisease1, tcmdisease1, tcmsyndrome1, therapy1, fangYao1, otherCure1, doctorAdvice1, efficacy1, diagTime2, mainDisease2, caseAbstract2, zhengKeys2, westdisease2, tcmdisease2, tcmsyndrome2, therapy2, fangYao2, otherCure2, doctorAdvice2, efficacy2, diagTime3, mainDisease3, caseAbstract3, zhengKeys3, westdisease3, tcmdisease3, tcmsyndrome3, therapy3, fangYao3, otherCure3, doctorAdvice3, efficacy3, diagTime4, mainDisease4, caseAbstract4, zhengKeys4, westdisease4, tcmdisease4, tcmsyndrome4, therapy4, fangYao4, otherCure4, doctorAdvice4, efficacy4, diagTime5, mainDisease5, caseAbstract5, zhengKeys5, westdisease5, tcmdisease5, tcmsyndrome5, therapy5, fangYao5, otherCure5, doctorAdvice5, efficacy5, diagTime6, mainDisease6, caseAbstract6, zhengKeys6, westdisease6, tcmdisease6, tcmsyndrome6, therapy6, fangYao6, otherCure6, doctorAdvice6, efficacy6, diagTime7, mainDisease7, caseAbstract7, zhengKeys7, westdisease7, tcmdisease7, tcmsyndrome7, therapy7, fangYao7, otherCure7, doctorAdvice7, efficacy7, diagTime8, mainDisease8, caseAbstract8, zhengKeys8, westdisease8, tcmdisease8, tcmsyndrome8, therapy8, fangYao8, otherCure8, doctorAdvice8, efficacy8, diagTime9, mainDisease9, caseAbstract9, zhengKeys9, westdisease9, tcmdisease9, tcmsyndrome9, therapy9, fangYao9, otherCure9, doctorAdvice9, efficacy9, diagTime10, mainDisease10, caseAbstract10, zhengKeys10, westdisease10, tcmdisease10, tcmsyndrome10, therapy10, fangYao10, otherCure10, doctorAdvice10, efficacy10, diagTime11, mainDisease11, caseAbstract11, zhengKeys11, westdisease11, tcmdisease11, tcmsyndrome11, therapy11, fangYao11, otherCure11, doctorAdvice11, efficacy11, diagTime12, mainDisease12, caseAbstract12, zhengKeys12, westdisease12, tcmdisease12, tcmsyndrome12, therapy12, fangYao12, otherCure12, doctorAdvice12, efficacy12, diagTime13, mainDisease13, caseAbstract13, zhengKeys13, westdisease13, tcmdisease13, tcmsyndrome13, therapy13, fangYao13, otherCure13, doctorAdvice13, efficacy13, diagTime14, mainDisease14, caseAbstract14, zhengKeys14, westdisease14, tcmdisease14, tcmsyndrome14, therapy14, fangYao14, otherCure14, doctorAdvice14, efficacy14, diagTime15, mainDisease15, caseAbstract15, zhengKeys15, westdisease15, tcmdisease15, tcmsyndrome15, therapy15, fangYao15, otherCure15, doctorAdvice15, efficacy15, diagTime16, mainDisease16, caseAbstract16, zhengKeys16, westdisease16, tcmdisease16, tcmsyndrome16, therapy16, fangYao16, otherCure16, doctorAdvice16, efficacy16, diagTime17, mainDisease17, caseAbstract17, zhengKeys17, westdisease17, tcmdisease17, tcmsyndrome17, therapy17, fangYao17, otherCure17, doctorAdvice17, efficacy17, diagTime18, mainDisease18, caseAbstract18, zhengKeys18, westdisease18, tcmdisease18, tcmsyndrome18, therapy18, fangYao18, otherCure18, doctorAdvice18, efficacy18):

        self.clcaid = clcaid 
        self.operatorId = operatorId 
        self.SPETid = SPETid 
        self.state = state 
        self.diagnosisNo = diagnosisNo 
        self.creatDate = creatDate 
        self.num = num 
        self.title = title 
        self.source = source 
        self.caseNum = caseNum 
        self.name = name 
        self.gender = gender 
        self.birthday = birthday 
        self.people = people 
        self.job = job 
        self.hometown = hometown 
        self.married = married 
        self.address = address 
        self.postcode = postcode 
        self.phone = phone 
        self.presentIll = presentIll 
        self.pastIll = pastIll 
        self.familyIll = familyIll 
        self.personalIll = personalIll 
        self.visit = visit 
        self.note = note 
        self.remark = remark 
        self.collectPerson = collectPerson 
        self.collectTime = collectTime 
        self.verifyOpinion = verifyOpinion 
        self.verifyName = verifyName 
        self.verifyTime = verifyTime 
        self.diagTime1 = diagTime1 
        self.mainDisease1 = mainDisease1 
        self.caseAbstract1 = caseAbstract1 
        self.zhengKeys1 = zhengKeys1 
        self.westdisease1 = westdisease1 
        self.tcmdisease1 = tcmdisease1 
        self.tcmsyndrome1 = tcmsyndrome1 
        self.therapy1 = therapy1 
        self.fangYao1 = fangYao1 
        self.otherCure1 = otherCure1 
        self.doctorAdvice1 = doctorAdvice1 
        self.efficacy1 = efficacy1 
        self.diagTime2 = diagTime2 
        self.mainDisease2 = mainDisease2 
        self.caseAbstract2 = caseAbstract2 
        self.zhengKeys2 = zhengKeys2 
        self.westdisease2 = westdisease2 
        self.tcmdisease2 = tcmdisease2 
        self.tcmsyndrome2 = tcmsyndrome2 
        self.therapy2 = therapy2 
        self.fangYao2 = fangYao2 
        self.otherCure2 = otherCure2 
        self.doctorAdvice2 = doctorAdvice2 
        self.efficacy2 = efficacy2 
        self.diagTime3 = diagTime3 
        self.mainDisease3 = mainDisease3 
        self.caseAbstract3 = caseAbstract3 
        self.zhengKeys3 = zhengKeys3 
        self.westdisease3 = westdisease3 
        self.tcmdisease3 = tcmdisease3 
        self.tcmsyndrome3 = tcmsyndrome3 
        self.therapy3 = therapy3 
        self.fangYao3 = fangYao3 
        self.otherCure3 = otherCure3 
        self.doctorAdvice3 = doctorAdvice3 
        self.efficacy3 = efficacy3 
        self.diagTime4 = diagTime4 
        self.mainDisease4 = mainDisease4 
        self.caseAbstract4 = caseAbstract4 
        self.zhengKeys4 = zhengKeys4 
        self.westdisease4 = westdisease4 
        self.tcmdisease4 = tcmdisease4 
        self.tcmsyndrome4 = tcmsyndrome4 
        self.therapy4 = therapy4 
        self.fangYao4 = fangYao4 
        self.otherCure4 = otherCure4 
        self.doctorAdvice4 = doctorAdvice4 
        self.efficacy4 = efficacy4 
        self.diagTime5 = diagTime5 
        self.mainDisease5 = mainDisease5 
        self.caseAbstract5 = caseAbstract5 
        self.zhengKeys5 = zhengKeys5 
        self.westdisease5 = westdisease5 
        self.tcmdisease5 = tcmdisease5 
        self.tcmsyndrome5 = tcmsyndrome5 
        self.therapy5 = therapy5 
        self.fangYao5 = fangYao5 
        self.otherCure5 = otherCure5 
        self.doctorAdvice5 = doctorAdvice5 
        self.efficacy5 = efficacy5 
        self.diagTime6 = diagTime6 
        self.mainDisease6 = mainDisease6 
        self.caseAbstract6 = caseAbstract6 
        self.zhengKeys6 = zhengKeys6 
        self.westdisease6 = westdisease6 
        self.tcmdisease6 = tcmdisease6 
        self.tcmsyndrome6 = tcmsyndrome6 
        self.therapy6 = therapy6 
        self.fangYao6 = fangYao6 
        self.otherCure6 = otherCure6 
        self.doctorAdvice6 = doctorAdvice6 
        self.efficacy6 = efficacy6 
        self.diagTime7 = diagTime7 
        self.mainDisease7 = mainDisease7 
        self.caseAbstract7 = caseAbstract7 
        self.zhengKeys7 = zhengKeys7 
        self.westdisease7 = westdisease7 
        self.tcmdisease7 = tcmdisease7 
        self.tcmsyndrome7 = tcmsyndrome7 
        self.therapy7 = therapy7 
        self.fangYao7 = fangYao7 
        self.otherCure7 = otherCure7 
        self.doctorAdvice7 = doctorAdvice7 
        self.efficacy7 = efficacy7 
        self.diagTime8 = diagTime8 
        self.mainDisease8 = mainDisease8 
        self.caseAbstract8 = caseAbstract8 
        self.zhengKeys8 = zhengKeys8 
        self.westdisease8 = westdisease8 
        self.tcmdisease8 = tcmdisease8 
        self.tcmsyndrome8 = tcmsyndrome8 
        self.therapy8 = therapy8 
        self.fangYao8 = fangYao8 
        self.otherCure8 = otherCure8 
        self.doctorAdvice8 = doctorAdvice8 
        self.efficacy8 = efficacy8 
        self.diagTime9 = diagTime9 
        self.mainDisease9 = mainDisease9 
        self.caseAbstract9 = caseAbstract9 
        self.zhengKeys9 = zhengKeys9 
        self.westdisease9 = westdisease9 
        self.tcmdisease9 = tcmdisease9 
        self.tcmsyndrome9 = tcmsyndrome9 
        self.therapy9 = therapy9 
        self.fangYao9 = fangYao9 
        self.otherCure9 = otherCure9 
        self.doctorAdvice9 = doctorAdvice9 
        self.efficacy9 = efficacy9 
        self.diagTime10 = diagTime10 
        self.mainDisease10 = mainDisease10 
        self.caseAbstract10 = caseAbstract10 
        self.zhengKeys10 = zhengKeys10 
        self.westdisease10 = westdisease10 
        self.tcmdisease10 = tcmdisease10 
        self.tcmsyndrome10 = tcmsyndrome10 
        self.therapy10 = therapy10 
        self.fangYao10 = fangYao10 
        self.otherCure10 = otherCure10 
        self.doctorAdvice10 = doctorAdvice10 
        self.efficacy10 = efficacy10 
        self.diagTime11 = diagTime11 
        self.mainDisease11 = mainDisease11 
        self.caseAbstract11 = caseAbstract11 
        self.zhengKeys11 = zhengKeys11 
        self.westdisease11 = westdisease11 
        self.tcmdisease11 = tcmdisease11 
        self.tcmsyndrome11 = tcmsyndrome11 
        self.therapy11 = therapy11 
        self.fangYao11 = fangYao11 
        self.otherCure11 = otherCure11 
        self.doctorAdvice11 = doctorAdvice11 
        self.efficacy11 = efficacy11 
        self.diagTime12 = diagTime12 
        self.mainDisease12 = mainDisease12 
        self.caseAbstract12 = caseAbstract12 
        self.zhengKeys12 = zhengKeys12 
        self.westdisease12 = westdisease12 
        self.tcmdisease12 = tcmdisease12 
        self.tcmsyndrome12 = tcmsyndrome12 
        self.therapy12 = therapy12 
        self.fangYao12 = fangYao12 
        self.otherCure12 = otherCure12 
        self.doctorAdvice12 = doctorAdvice12 
        self.efficacy12 = efficacy12 
        self.diagTime13 = diagTime13 
        self.mainDisease13 = mainDisease13 
        self.caseAbstract13 = caseAbstract13 
        self.zhengKeys13 = zhengKeys13 
        self.westdisease13 = westdisease13 
        self.tcmdisease13 = tcmdisease13 
        self.tcmsyndrome13 = tcmsyndrome13 
        self.therapy13 = therapy13 
        self.fangYao13 = fangYao13 
        self.otherCure13 = otherCure13 
        self.doctorAdvice13 = doctorAdvice13 
        self.efficacy13 = efficacy13 
        self.diagTime14 = diagTime14 
        self.mainDisease14 = mainDisease14 
        self.caseAbstract14 = caseAbstract14 
        self.zhengKeys14 = zhengKeys14 
        self.westdisease14 = westdisease14 
        self.tcmdisease14 = tcmdisease14 
        self.tcmsyndrome14 = tcmsyndrome14 
        self.therapy14 = therapy14 
        self.fangYao14 = fangYao14 
        self.otherCure14 = otherCure14 
        self.doctorAdvice14 = doctorAdvice14 
        self.efficacy14 = efficacy14 
        self.diagTime15 = diagTime15 
        self.mainDisease15 = mainDisease15 
        self.caseAbstract15 = caseAbstract15 
        self.zhengKeys15 = zhengKeys15 
        self.westdisease15 = westdisease15 
        self.tcmdisease15 = tcmdisease15 
        self.tcmsyndrome15 = tcmsyndrome15 
        self.therapy15 = therapy15 
        self.fangYao15 = fangYao15 
        self.otherCure15 = otherCure15 
        self.doctorAdvice15 = doctorAdvice15 
        self.efficacy15 = efficacy15 
        self.diagTime16 = diagTime16 
        self.mainDisease16 = mainDisease16 
        self.caseAbstract16 = caseAbstract16 
        self.zhengKeys16 = zhengKeys16 
        self.westdisease16 = westdisease16 
        self.tcmdisease16 = tcmdisease16 
        self.tcmsyndrome16 = tcmsyndrome16 
        self.therapy16 = therapy16 
        self.fangYao16 = fangYao16 
        self.otherCure16 = otherCure16 
        self.doctorAdvice16 = doctorAdvice16 
        self.efficacy16 = efficacy16 
        self.diagTime17 = diagTime17 
        self.mainDisease17 = mainDisease17 
        self.caseAbstract17 = caseAbstract17 
        self.zhengKeys17 = zhengKeys17 
        self.westdisease17 = westdisease17 
        self.tcmdisease17 = tcmdisease17 
        self.tcmsyndrome17 = tcmsyndrome17 
        self.therapy17 = therapy17 
        self.fangYao17 = fangYao17 
        self.otherCure17 = otherCure17 
        self.doctorAdvice17 = doctorAdvice17 
        self.efficacy17 = efficacy17 
        self.diagTime18 = diagTime18 
        self.mainDisease18 = mainDisease18 
        self.caseAbstract18 = caseAbstract18 
        self.zhengKeys18 = zhengKeys18 
        self.westdisease18 = westdisease18 
        self.tcmdisease18 = tcmdisease18 
        self.tcmsyndrome18 = tcmsyndrome18 
        self.therapy18 = therapy18 
        self.fangYao18 = fangYao18 
        self.otherCure18 = otherCure18 
        self.doctorAdvice18 = doctorAdvice18 
        self.efficacy18 = efficacy18 


class classicCaseDiagnosis(db.Model):
    clcaid = db.Column(db.String(36), nullable=False, primary_key=True)
    caseNum = db.Column(db.String(50))
    diagnosisNum = db.Column(db.String(50))
    diagTime = db.Column(db.String(50))
    mainDisease = db.Column(db.Text)
    caseAbstract = db.Column(db.Text)
    zhengKeys = db.Column(db.Text)
    westdisease = db.Column(db.String(50))
    tcmdisease = db.Column(db.String(50))
    tcmsyndrome = db.Column(db.String(50))
    therapy = db.Column(db.Text)
    fangYao = db.Column(db.Text)
    otherCure = db.Column(db.Text)
    doctorAdvice = db.Column(db.Text)
    efficacy = db.Column(db.String(50))
    #primary key(clcaid)

    def __init__(self, clcaid, caseNum, diagnosisNum, diagTime, mainDisease, caseAbstract, zhengKeys, westdisease, tcmdisease, tcmsyndrome, therapy, fangYao, otherCure, doctorAdvice, efficacy):

        self.clcaid = clcaid 
        self.caseNum = caseNum 
        self.diagnosisNum = diagnosisNum 
        self.diagTime = diagTime 
        self.mainDisease = mainDisease 
        self.caseAbstract = caseAbstract 
        self.zhengKeys = zhengKeys 
        self.westdisease = westdisease 
        self.tcmdisease = tcmdisease 
        self.tcmsyndrome = tcmsyndrome 
        self.therapy = therapy 
        self.fangYao = fangYao 
        self.otherCure = otherCure 
        self.doctorAdvice = doctorAdvice 
        self.efficacy = efficacy 


class continuingeducation(db.Model):
    Participent = db.Column(db.String(50))
    TrainingName = db.Column(db.String(50))
    Category = db.Column(db.String(50))
    TrainingDate = db.Column(db.String(50))
    Hours = db.Column(db.String(50))
    CreditHour = db.Column(db.String(50))
    HashId = db.Column(db.String(36), nullable=False, primary_key=True)
    SpecialisId = db.Column(db.String(36), db.ForeignKey('specialist.SPETid'))
    State = db.Column(db.SMALLINT)
    OperatorId = db.Column(db.String(36))
    CreateDate = db.Column(db.DateTime)
    #primary key(HashId)

    def __init__(self, Participent, TrainingName, Category, TrainingDate, Hours, CreditHour, HashId, SpecialisId, State, OperatorId, CreateDate):

        self.Participent = Participent 
        self.TrainingName = TrainingName 
        self.Category = Category 
        self.TrainingDate = TrainingDate 
        self.Hours = Hours 
        self.CreditHour = CreditHour 
        self.HashId = HashId 
        self.SpecialisId = SpecialisId 
        self.State = State 
        self.OperatorId = OperatorId 
        self.CreateDate = CreateDate 


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
    gender = db.Column(db.SMALLINT, nullable=False)
    nationality = db.Column(db.SMALLINT, nullable=False)
    personSort = db.Column(db.SMALLINT, nullable=False)
    afflication = db.Column(db.String(200), nullable=False, default=' ')
    job = db.Column(db.String(20), nullable=False, default=' ')
    tel = db.Column(db.String(20), nullable=False, default=' ')
    address = db.Column(db.String(200), nullable=False, default=' ')
    birthplace = db.Column(db.String(6), nullable=False)
    liveplace = db.Column(db.String(6), nullable=False)
    education = db.Column(db.SMALLINT, nullable=False)
    marriage = db.Column(db.SMALLINT, nullable=False)
    ohistory = db.Column(db.Text, nullable=False, default=' ')
    phistory = db.Column(db.Text, nullable=False, default=' ')
    fhistory = db.Column(db.Text, nullable=False, default=' ')
    allergy = db.Column(db.Text, nullable=False, default=' ')
    extraMed = db.Column(db.String(500), nullable=False, default=' ')
    nhistory = db.Column(db.Text, nullable=False, default=' ')
    mresult = db.Column(db.SMALLINT, nullable=False)
    vresult = db.Column(db.String(500), nullable=False)
    illustration = db.Column(db.Text, nullable=False, default=' ')
    state = db.Column(db.SMALLINT, nullable=False, default=0)
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    hasFile = db.Column(db.Boolean, nullable=False, default=0)
    preState = db.Column(db.SMALLINT, nullable=False, default=0)
    #primary key(CASEid))
    #########check = db.Column(([age] >= 0 and [age] <= 999))

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
    parentcode = db.Column(db.String(20), nullable=False)
    level = db.Column(db.SMALLINT, nullable=False)
    isClassical = db.Column(db.Boolean, nullable=False, default=1)
    SPETid = db.Column(db.String(36), nullable=False, default=' ')
    illustration = db.Column(db.Text, nullable=False, default=' ')
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    state = db.Column(db.SMALLINT, nullable=False, default=0)
    #primary key(DMETid))
    #key = db.Column(AK_DMETHOD_PK_CODE_DMETHOD (code)

    def __init__(self, DMETid, code, name, parentcode, level, isClassical, SPETid, illustration, createDay, optrid, state):

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
    takeWay = db.Column(db.SMALLINT, nullable=False)
    drugForm = db.Column(db.SMALLINT, nullable=False)
    SPETid = db.Column(db.String(36), nullable=False, default=' ')
    illustration = db.Column(db.Text, nullable=False, default=' ')
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    useClassWdis = db.Column(db.Boolean, nullable=False, default=0)
    state = db.Column(db.SMALLINT, nullable=False, default=0)
    #primary key(DTMPid))
    #key = db.Column(AK_DTEMPLATE_PK_CODE_DTEMPLAT (code)

    def __init__(self, DTMPid, code, name, useClassCdis, useClassDmet, CDISid, WDISid, SEMCid, DMETid, takeWay, drugForm, SPETid, illustration, createDay, optrid, useClassWdis, state):

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
        self.useClassWdis = useClassWdis 
        self.state = state 


class dataSet(db.Model):
    DASEid = db.Column(db.String(36), nullable=False, primary_key=True)
    DTMPid = db.Column(db.String(36), nullable=False)
    code = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    missionType = db.Column(db.SMALLINT, nullable=False)
    sampleNum = db.Column(db.Integer, nullable=False, default=0)
    attributeNum = db.Column(db.Integer, nullable=False, default=0)
    state = db.Column(db.SMALLINT, nullable=False, default=0)
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    #primary key(DASEid)

    def __init__(self, DASEid, DTMPid, code, name, missionType, sampleNum, attributeNum, state, createDay, optrid):

        self.DASEid = DASEid 
        self.DTMPid = DTMPid 
        self.code = code 
        self.name = name 
        self.missionType = missionType 
        self.sampleNum = sampleNum 
        self.attributeNum = attributeNum 
        self.state = state 
        self.createDay = createDay 
        self.optrid = optrid 


class diagExam(db.Model):
    DIEXid = db.Column(db.String(36), nullable=False, primary_key=True)
    DIAGid = db.Column(db.String(36), db.ForeignKey('diagnose.DIAGid'))
    EXAMid = db.Column(db.String(36), db.ForeignKey('examination.EXAMid'))
    value = db.Column(db.String(200), nullable=False, default=' ')
    illustration = db.Column(db.Text, nullable=False, default=' ')
    date = db.Column(db.DateTime)
    sequence = db.Column(db.Integer, default=0)
    address = db.Column(db.String(100))
    #primary key(DIEXid)

    def __init__(self, DIEXid, DIAGid, EXAMid, value, illustration, date, sequence, address):

        self.DIEXid = DIEXid 
        self.DIAGid = DIAGid 
        self.EXAMid = EXAMid 
        self.value = value 
        self.illustration = illustration 
        self.date = date 
        self.sequence = sequence 
        self.address = address 


class diagItem(db.Model):
    DIITid = db.Column(db.String(36), nullable=False, primary_key=True)
    DIREid = db.Column(db.String(36), db.ForeignKey('diag_recipe.DIREid'))
    dru_DRUGid = db.Column(db.String(36))
    DRUGid = db.Column(db.String(36), db.ForeignKey('drug.DRUGid'))
    quality = db.Column(db.DECIMAL(18,4), nullable=False, default=0)
    sequence = db.Column(db.Integer, nullable=False, default=0)
    illustration = db.Column(db.Text, nullable=False, default=' ')
    #primary key(DIITid)

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
    drugForm = db.Column(db.SMALLINT, nullable=False)
    takeWay = db.Column(db.SMALLINT, nullable=False)
    quality = db.Column(db.SMALLINT, nullable=False)
    produceMethod = db.Column(db.String(100), nullable=False)
    usage = db.Column(db.String(100), nullable=False)
    #primary key(DIREid)

    def __init__(self, DIREid, DIAGid, FREPid, isCustomed, name, doctorAdvice, drugForm, takeWay, quality, produceMethod):

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


class diagSymptom(db.Model):
    DISYid = db.Column(db.String(36), nullable=False, primary_key=True)
    SYPMid = db.Column(db.String(36), db.ForeignKey('symptom.SYPMid'))
    DIAGid = db.Column(db.String(36), db.ForeignKey('diagnose.DIAGid'))
    value = db.Column(db.String(200), nullable=False, default=' ')
    illustration = db.Column(db.Text, nullable=False, default=' ')
    sequence = db.Column(db.Integer, default=0)
    #primary key(DISYid)

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
    DIAGno = db.Column(db.SMALLINT, nullable=False, default=1)
    DIAGnum = db.Column(db.SMALLINT, nullable=False)
    DIAGday = db.Column(db.DateTime, nullable=False)
    lunarDay = db.Column(db.String(50), nullable=False, default=' ')
    solarTerm = db.Column(db.SMALLINT, nullable=False, default=0)
    DIAway = db.Column(db.SMALLINT, nullable=False, default=0)
    majorSue = db.Column(db.Text, nullable=False)
    illustration = db.Column(db.Text, nullable=False, default=' ')
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    westernMed = db.Column(db.Text, nullable=False, default=' ')
    other = db.Column(db.Text, nullable=False, default=' ')
    preSEMCid = db.Column(db.String(36))
    #primary key(DIAGid)

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


class district(db.Model):
    DISTid = db.Column(db.String(36), nullable=False, primary_key=True)
    code = db.Column(db.String(20), nullable=False)
    parentcode = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    level = db.Column(db.SMALLINT, nullable=False)
    py = db.Column(db.String(20), nullable=False, default=' ')
    wb = db.Column(db.String(20), nullable=False, default=' ')
    illustration = db.Column(db.Text, nullable=False, default=' ')
    #primary key(DISTid))
    #key = db.Column(AK_DISTRICT_PK_CODE_DISTRICT (code)

    def __init__(self, DISTid, code, parentcode, name, level, py, wb, illustration):

        self.DISTid = DISTid 
        self.code = code 
        self.parentcode = parentcode 
        self.name = name 
        self.level = level 
        self.py = py 
        self.wb = wb 
        self.illustration = illustration 


class drug(db.Model):
    DRUGid = db.Column(db.String(36), nullable=False, primary_key=True)
    code = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    unit = db.Column(db.String(10), nullable=False)
    alias = db.Column(db.String(100), nullable=False, default=' ')
    py = db.Column(db.String(20), nullable=False, default=' ')
    wb = db.Column(db.String(20), nullable=False, default=' ')
    isClassical = db.Column(db.Boolean, nullable=False, default=1)
    SPETid = db.Column(db.String(36), nullable=False, default=' ')
    illustration = db.Column(db.Text, nullable=False, default=' ')
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    state = db.Column(db.SMALLINT, nullable=False, default=0)
    #primary key(DRUGid))
    #key = db.Column(AK_DRUG_PK_CODE_DRUG (code)

    def __init__(self, DRUGid, code, name, unit, alias, py, wb, isClassical, SPETid, illustration, createDay, optrid, state):

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
    sequence = db.Column(db.Integer, nullable=False)
    illustration = db.Column(db.Text, nullable=False)
    #primary key(DTEXid)

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
    sequence = db.Column(db.Integer, nullable=False, default=0)
    illustration = db.Column(db.Text, nullable=False, default=' ')
    #primary key(DTSYid)

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
    kind = db.Column(db.SMALLINT, nullable=False, default=0)
    normalValue = db.Column(db.String(200), nullable=False, default=' ')
    hasFile = db.Column(db.Boolean, nullable=False, default=0)
    isClassical = db.Column(db.Boolean, nullable=False, default=1)
    SPETid = db.Column(db.String(36), nullable=False, default=' ')
    illustration = db.Column(db.Text, nullable=False, default=' ')
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    state = db.Column(db.SMALLINT, nullable=False, default=0)
    #primary key(EXAMid))
    #key = db.Column(AK_EXAMINATION_PK_COD_EXAMINAT (code)

    def __init__(self, EXAMid, code, name, abbreviation, kind, normalValue, hasFile, isClassical, SPETid, illustration, createDay, optrid, state):

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


class feature(db.Model):
    FEATid = db.Column(db.String(36), nullable=False, primary_key=True)
    DASEid = db.Column(db.String(36), db.ForeignKey('data_set.DASEid'))
    code = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    featType = db.Column(db.SMALLINT, nullable=False)
    valSort = db.Column(db.SMALLINT, nullable=False, default=0)
    sequence = db.Column(db.Integer, nullable=False)
    #primary key(FEATid)

    def __init__(self, FEATid, DASEid, code, name, featType, valSort, sequence):

        self.FEATid = FEATid 
        self.DASEid = DASEid 
        self.code = code 
        self.name = name 
        self.featType = featType 
        self.valSort = valSort 
        self.sequence = sequence 


class fileinfo(db.Model):
    FIlEINFOid = db.Column(db.String(36), nullable=False, primary_key=True)
    code = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    SPETid = db.Column(db.String(36), nullable=False)
    illustration = db.Column(db.Text, nullable=False, default=' ')
    createDay = db.Column(db.DateTime, nullable=False)
    optrid = db.Column(db.String(36), nullable=False)
    state = db.Column(db.SMALLINT, nullable=False)
    fileinfoType = db.Column(db.SMALLINT, nullable=False)
    #primary key(FIlEINFOid)

    def __init__(self, FIlEINFOid, code, name, SPETid, illustration, createDay, optrid, state, fileinfoType):

        self.FIlEINFOid = FIlEINFOid 
        self.code = code 
        self.name = name 
        self.SPETid = SPETid 
        self.illustration = illustration 
        self.createDay = createDay 
        self.optrid = optrid 
        self.state = state 
        self.fileinfoType = fileinfoType 


class fixedrecipe(db.Model):
    FREPid = db.Column(db.String(36), nullable=False, primary_key=True)
    code = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    effect = db.Column(db.String(200), nullable=False, default=' ')
    py = db.Column(db.String(20), nullable=False, default=' ')
    wb = db.Column(db.String(20), nullable=False, default=' ')
    isClassical = db.Column(db.Boolean, nullable=False, default=1)
    SPETid = db.Column(db.String(36), nullable=False, default=' ')
    illustration = db.Column(db.Text, nullable=False, default=' ')
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    state = db.Column(db.SMALLINT, nullable=False, default=0)
    #primary key(FREPid))
    #key = db.Column(AK_FIXEDRECIPE_PK_COD_FIXEDREC (code)

    def __init__(self, FREPid, code, name, effect, py, wb, isClassical, SPETid, illustration, createDay, optrid, state):

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
    sequence = db.Column(db.Integer, nullable=False, default=0)
    illustration = db.Column(db.Text, nullable=False, default=' ')
    #primary key(FRITid)

    def __init__(self, FRITid, DRUGid, FREPid, quality, sequence, illustration):

        self.FRITid = FRITid 
        self.DRUGid = DRUGid 
        self.FREPid = FREPid 
        self.quality = quality 
        self.sequence = sequence 
        self.illustration = illustration 


class genre(db.Model):
    GENRid = db.Column(db.String(36), nullable=False, primary_key=True)
    INSTid = db.Column(db.String(36), db.ForeignKey('inherit_study.INSTid'))
    main_specialist = db.Column(db.String(20), nullable=False, default=' ')
    genre_name = db.Column(db.String(20), nullable=False, default=' ')
    achievement = db.Column(db.String(100), nullable=False, default=' ')
    #primary key(GENRid)

    def __init__(self, GENRid, INSTid, main_specialist, genre_name, achievement):

        self.GENRid = GENRid 
        self.INSTid = INSTid 
        self.main_specialist = main_specialist 
        self.genre_name = genre_name 
        self.achievement = achievement 


class goodInstance(db.Model):
    GOINid = db.Column(db.String(36), nullable=False, primary_key=True)
    REBOid = db.Column(db.String(36), db.ForeignKey('read_book.REBOid'))
    content = db.Column(db.Text, nullable=False, default=' ')
    #primary key(GOINid)

    def __init__(self, GOINid, REBOid, content):

        self.GOINid = GOINid 
        self.REBOid = REBOid 
        self.content = content 


class inherit(db.Model):
    INHEid = db.Column(db.String(36), nullable=False, primary_key=True)
    INSTid = db.Column(db.String(36), db.ForeignKey('inherit_study.INSTid'))
    name = db.Column(db.String(20), nullable=False)
    start_date = db.Column(db.String(16), nullable=False, default='1900-1-1')
    end_date = db.Column(db.String(16), nullable=False, default='1900-1-1')
    theoretics = db.Column(db.String(100), nullable=False, default=' ')
    introduction = db.Column(db.Text, nullable=False, default=' ')
    #key = db.Column(db.String(100), nullable=False, default=' ')
    #primary key(INHEid)

    def __init__(self, INHEid, INSTid, name, start_date, end_date, theoretics, introduction):

        self.INHEid = INHEid 
        self.INSTid = INSTid 
        self.name = name 
        self.start_date = start_date 
        self.end_date = end_date 
        self.theoretics = theoretics 
        self.introduction = introduction 


class inheritStudy(db.Model):
    INSTid = db.Column(db.String(36), nullable=False, primary_key=True)
    SPETid = db.Column(db.String(36), db.ForeignKey('specialist.SPETid'))
    enlighten_teacher = db.Column(db.String(20), nullable=False)
    work_place = db.Column(db.String(50), nullable=False)
    major = db.Column(db.String(50), nullable=False)
    early_degree = db.Column(db.Text, nullable=False, default=' ')
    textbook_type = db.Column(db.SMALLINT, nullable=False)
    textbook = db.Column(db.Text, nullable=False, default=' ')
    other_book = db.Column(db.Text, nullable=False, default=' ')
    study_time = db.Column(db.Text, nullable=False, default=' ')
    wisdom = db.Column(db.Text, nullable=False, default=' ')
    aphorism = db.Column(db.Text, nullable=False, default=' ')
    ideal = db.Column(db.Text, nullable=False, default=' ')
    point = db.Column(db.Text, nullable=False, default=' ')
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    state = db.Column(db.SMALLINT, nullable=False, default=0)
    #primary key(INSTid)

    def __init__(self, INSTid, SPETid, enlighten_teacher, work_place, major, early_degree, textbook_type, textbook, other_book, study_time, wisdom, aphorism, ideal, point, createDay, optrid, state):

        self.INSTid = INSTid 
        self.SPETid = SPETid 
        self.enlighten_teacher = enlighten_teacher 
        self.work_place = work_place 
        self.major = major 
        self.early_degree = early_degree 
        self.textbook_type = textbook_type 
        self.textbook = textbook 
        self.other_book = other_book 
        self.study_time = study_time 
        self.wisdom = wisdom 
        self.aphorism = aphorism 
        self.ideal = ideal 
        self.point = point 
        self.createDay = createDay 
        self.optrid = optrid 
        self.state = state 


class integratedSym(db.Model):
    INSYid = db.Column(db.String(36), nullable=False, primary_key=True)
    SYPMid = db.Column(db.String(36), db.ForeignKey('symptom.SYPMid'))
    name = db.Column(db.String(50), nullable=False)
    valSort = db.Column(db.Integer, nullable=False)
    sequence = db.Column(db.Integer, nullable=False)
    #primary key(INSYid)

    def __init__(self, INSYid, SYPMid, name, valSort, sequence):

        self.INSYid = INSYid 
        self.SYPMid = SYPMid 
        self.name = name 
        self.valSort = valSort 
        self.sequence = sequence 


class learnMission(db.Model):
    LEMIid = db.Column(db.String(36), nullable=False, primary_key=True)
    DASEid = db.Column(db.String(36), db.ForeignKey('data_set.DASEid'))
    DTMPid = db.Column(db.String(36), nullable=False)
    code = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    missionType = db.Column(db.SMALLINT, nullable=False)
    testType = db.Column(db.SMALLINT, nullable=False)
    testPar = db.Column(db.DECIMAL(4,1), nullable=False)
    illustration = db.Column(db.Text, nullable=False, default=' ')
    state = db.Column(db.SMALLINT, nullable=False, default=0)
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    #primary key(LEMIid)

    def __init__(self, LEMIid, DASEid, DTMPid, code, name, missionType, testType, testPar, illustration, state, createDay, optrid):

        self.LEMIid = LEMIid 
        self.DASEid = DASEid 
        self.DTMPid = DTMPid 
        self.code = code 
        self.name = name 
        self.missionType = missionType 
        self.testType = testType 
        self.testPar = testPar 
        self.illustration = illustration 
        self.state = state 
        self.createDay = createDay 
        self.optrid = optrid 


class literature(db.Model):
    LITEid = db.Column(db.String(36), nullable=False, primary_key=True)
    SCIEid = db.Column(db.String(36), db.ForeignKey('science.SCIEid'))
    literature = db.Column(db.String(20), nullable=False, default=' ')
    pubType = db.Column(db.String(10), nullable=False, default=' ')
    publishing_date = db.Column(db.String(16), nullable=False, default='1900-1-1')
    publishing_company = db.Column(db.String(30), nullable=False, default=' ')
    paper = db.Column(db.String(30), nullable=False, default=' ')
    magazine = db.Column(db.String(30), nullable=False, default=' ')
    #primary key(LITEid)

    def __init__(self, LITEid, SCIEid, literature, pubType, publishing_date, publishing_company, paper, magazine):

        self.LITEid = LITEid 
        self.SCIEid = SCIEid 
        self.literature = literature 
        self.pubType = pubType 
        self.publishing_date = publishing_date 
        self.publishing_company = publishing_company 
        self.paper = paper 
        self.magazine = magazine 


class mainBook(db.Model):
    MABOid = db.Column(db.String(36), nullable=False, primary_key=True)
    INSTid = db.Column(db.String(36), db.ForeignKey('inherit_study.INSTid'))
    literature_name = db.Column(db.String(20), nullable=False, default=' ')
    pubType = db.Column(db.String(10), nullable=False, default=' ')
    publishing_date = db.Column(db.String(16), nullable=False, default='1900-1-1')
    edition = db.Column(db.String(30), nullable=False, default=' ')
    publishing_company = db.Column(db.String(30), nullable=False, default=' ')
    #primary key(MABOid)

    def __init__(self, MABOid, INSTid, literature_name, pubType, publishing_date, edition, publishing_company):

        self.MABOid = MABOid 
        self.INSTid = INSTid 
        self.literature_name = literature_name 
        self.pubType = pubType 
        self.publishing_date = publishing_date 
        self.edition = edition 
        self.publishing_company = publishing_company 


class mediaInfo(db.Model):
    Num = db.Column(db.String(50))
    Name = db.Column(db.String(50))
    Category = db.Column(db.String(50))
    Abs = db.Column(db.Text)
    ProducedTime = db.Column(db.String(50))
    Maker = db.Column(db.String(50))
    FileName = db.Column(db.String(50))
    Longth = db.Column(db.String(50))
    DataFormat = db.Column(db.String(50))
    SpecialistId = db.Column(db.String(36), db.ForeignKey('specialist.SPETid'))
    OperatorId = db.Column(db.String(36))
    HashId = db.Column(db.String(36), nullable=False, primary_key=True)
    State = db.Column(db.SMALLINT)
    CreateDate = db.Column(db.DateTime)
    #primary key(HashId)

    def __init__(self, Num, Name, Category, Abs, ProducedTime, Maker, FileName, Longth, DataFormat, SpecialistId, OperatorId, HashId, State, CreateDate):

        self.Num = Num 
        self.Name = Name 
        self.Category = Category 
        self.Abs = Abs 
        self.ProducedTime = ProducedTime 
        self.Maker = Maker 
        self.FileName = FileName 
        self.Longth = Longth 
        self.DataFormat = DataFormat 
        self.SpecialistId = SpecialistId 
        self.OperatorId = OperatorId 
        self.HashId = HashId 
        self.State = State 
        self.CreateDate = CreateDate 


class message(db.Model):
    MESGid = db.Column(db.String(36), nullable=False, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(256), nullable=False)
    sender = db.Column(db.String(36), nullable=False)
    receivor = db.Column(db.String(36), nullable=False)
    readed = db.Column(db.Boolean, nullable=False)
    msgDate = db.Column(db.DateTime, nullable=False)
    sysMsg = db.Column(db.Boolean, nullable=False)
    #primary key(MESGid)

    def __init__(self, MESGid, title, content, sender, receivor, readed, msgDate, sysMsg):

        self.MESGid = MESGid 
        self.title = title 
        self.content = content 
        self.sender = sender 
        self.receivor = receivor 
        self.readed = readed 
        self.msgDate = msgDate 
        self.sysMsg = sysMsg 


class modernBook(db.Model):
    MOBOid = db.Column(db.String(36), nullable=False, primary_key=True)
    REBOid = db.Column(db.String(36), db.ForeignKey('read_book.REBOid'))
    literature_name = db.Column(db.String(20), nullable=False, default=' ')
    pubType = db.Column(db.String(10), nullable=False, default=' ')
    benefit = db.Column(db.String(100), nullable=False, default=' ')
    #primary key(MOBOid)

    def __init__(self, MOBOid, REBOid, literature_name, pubType, benefit):

        self.MOBOid = MOBOid 
        self.REBOid = REBOid 
        self.literature_name = literature_name 
        self.pubType = pubType 
        self.benefit = benefit 


class modernSpecialist(db.Model):
    MOSPid = db.Column(db.String(36), nullable=False, primary_key=True)
    REBOid = db.Column(db.String(36), db.ForeignKey('read_book.REBOid'))
    name = db.Column(db.String(20), nullable=False)
    isprofession = db.Column(db.Boolean, nullable=False, default=0)
    afflication = db.Column(db.String(100), nullable=False)
    major = db.Column(db.String(100), nullable=False)
    #primary key(MOSPid)

    def __init__(self, MOSPid, REBOid, name, isprofession, afflication, major):

        self.MOSPid = MOSPid 
        self.REBOid = REBOid 
        self.name = name 
        self.isprofession = isprofession 
        self.afflication = afflication 
        self.major = major 


class newDTechnology(db.Model):
    OperatorId = db.Column(db.String(36))
    Num = db.Column(db.String(50))
    Name = db.Column(db.String(50))
    Content = db.Column(db.Text)
    FormationTime = db.Column(db.String(50))
    DevelopingPeople = db.Column(db.String(50))
    Possessor = db.Column(db.String(50))
    Bearer = db.Column(db.String(50))
    DevelopmentAffiliation = db.Column(db.Text)
    PossesionAffiliation = db.Column(db.Text)
    ApplicationAffiliation = db.Column(db.Text)
    ApplicationStartingTime = db.Column(db.String(50))
    Files = db.Column(db.String(50))
    SpecialisId = db.Column(db.String(36), db.ForeignKey('specialist.SPETid'))
    HashId = db.Column(db.String(36), nullable=False, primary_key=True)
    State = db.Column(db.SMALLINT)
    CreateDate = db.Column(db.DateTime)
    #primary key(HashId)

    def __init__(self, OperatorId, Num, Name, Content, FormationTime, DevelopingPeople, Possessor, Bearer, DevelopmentAffiliation, PossesionAffiliation, ApplicationAffiliation, ApplicationStartingTime, Files, SpecialisId, HashId, State, CreateDate):

        self.OperatorId = OperatorId 
        self.Num = Num 
        self.Name = Name 
        self.Content = Content 
        self.FormationTime = FormationTime 
        self.DevelopingPeople = DevelopingPeople 
        self.Possessor = Possessor 
        self.Bearer = Bearer 
        self.DevelopmentAffiliation = DevelopmentAffiliation 
        self.PossesionAffiliation = PossesionAffiliation 
        self.ApplicationAffiliation = ApplicationAffiliation 
        self.ApplicationStartingTime = ApplicationStartingTime 
        self.Files = Files 
        self.SpecialisId = SpecialisId 
        self.HashId = HashId 
        self.State = State 
        self.CreateDate = CreateDate 


class operator(db.Model):
    OPTRid = db.Column(db.String(36), nullable=False, primary_key=True)
    #ROLEid = db.Column(db.String(36), nullable=False, db.ForeignKey('userrole.ROLEid'))
    ROLEid = db.Column(db.String(36), db.ForeignKey('userrole.ROLEid'))
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    realname = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.SMALLINT, nullable=False, default=0)
    part = db.Column(db.String(100), nullable=False, default=' ')
    SPETid = db.Column(db.CHAR(36), nullable=False, default=' ')
    illustration = db.Column(db.Text, nullable=False, default=' ')
    insertLock = db.Column(db.Boolean, nullable=False, default=0)
    editLock = db.Column(db.Boolean, nullable=False, default=0)
    deleteLock = db.Column(db.Boolean, nullable=False, default=0)
    state = db.Column(db.SMALLINT, nullable=False, default=0)
    #primary key(OPTRid))
    #key = db.Column(AK_OPERATOR_PK_USERNA_OPERATOR (username)

    def __init__(self, OPTRid, ROLEid, username, password, realname, gender, part, SPETid, illustration, insertLock, editLock, deleteLock, state):

        self.OPTRid = OPTRid 
        self.ROLEid = ROLEid 
        self.username = username 
        self.password = password 
        self.realname = realname 
        self.gender = gender 
        self.part = part 
        self.SPETid = SPETid 
        self.illustration = illustration 
        self.insertLock = insertLock 
        self.editLock = editLock 
        self.deleteLock = deleteLock 
        self.state = state 


class operatorfun(db.Model):
    OPTRid = db.Column(db.String(36), primary_key=True)
    #OPTRid = db.Column(db.String(36), nullable=False, primary_key=True, db.ForeignKey('operator.OPTRid'))
    SFUNid = db.Column(db.String(36), db.ForeignKey('sysfun.SFUNid'))
    #SFUNid = db.Column(db.String(36), nullable=False, db.ForeignKey('sysfun.SFUNid'))
    #primary key(OPTRid, SFUNid)

    def __init__(self, OPTRid, SFUNid):

        self.OPTRid = OPTRid 
        self.SFUNid = SFUNid 


class otherBook(db.Model):
    OTBOid = db.Column(db.String(36), nullable=False, primary_key=True)
    BACKid = db.Column(db.String(36), db.ForeignKey('background.BACKid'))
    literature_name = db.Column(db.String(20), nullable=False, default=' ')
    pubType = db.Column(db.String(10), nullable=False, default=' ')
    benefit = db.Column(db.String(100), nullable=False, default=' ')
    #primary key(OTBOid)

    def __init__(self, OTBOid, BACKid, literature_name, pubType, benefit):

        self.OTBOid = OTBOid 
        self.BACKid = BACKid 
        self.literature_name = literature_name 
        self.pubType = pubType 
        self.benefit = benefit 


class otherInformation(db.Model):
    OTINid = db.Column(db.String(36), nullable=False, primary_key=True)
    INSTid = db.Column(db.String(36), db.ForeignKey('inherit_study.INSTid'))
    literature_name = db.Column(db.String(20), nullable=False, default=' ')
    publishing_name = db.Column(db.String(16), nullable=False, default='1900-1-1')
    edition = db.Column(db.String(30), nullable=False, default=' ')
    publishing_company = db.Column(db.String(30), nullable=False, default=' ')
    magazine = db.Column(db.String(30), nullable=False, default=' ')
    entrepreneur = db.Column(db.String(30), nullable=False, default=' ')
    #primary key(OTINid)

    def __init__(self, OTINid, INSTid, literature_name, publishing_name, edition, publishing_company, magazine, entrepreneur):

        self.OTINid = OTINid 
        self.INSTid = INSTid 
        self.literature_name = literature_name 
        self.publishing_name = publishing_name 
        self.edition = edition 
        self.publishing_company = publishing_company 
        self.magazine = magazine 
        self.entrepreneur = entrepreneur 


class paperResult(db.Model):
    num = db.Column(db.String(50))
    Title = db.Column(db.String(150))
    Author = db.Column(db.String(50))
    AuthorAffiliation = db.Column(db.String(50))
    Abstract = db.Column(db.Text)
    Source = db.Column(db.String(50))
    Files = db.Column(db.String(50))
    SpeicalistId = db.Column(db.String(36), db.ForeignKey('specialist.SPETid'))
    OperatorId = db.Column(db.String(36))
    HashId = db.Column(db.String(36), nullable=False, primary_key=True)
    State = db.Column(db.SMALLINT)
    CreateDate = db.Column(db.DateTime)
    #primary key(HashId)

    def __init__(self, num, Title, Author, AuthorAffiliation, Abstract, Source, Files, SpeicalistId, OperatorId, HashId, State, CreateDate):

        self.num = num 
        self.Title = Title 
        self.Author = Author 
        self.AuthorAffiliation = AuthorAffiliation 
        self.Abstract = Abstract 
        self.Source = Source 
        self.Files = Files 
        self.SpeicalistId = SpeicalistId 
        self.OperatorId = OperatorId 
        self.HashId = HashId 
        self.State = State 
        self.CreateDate = CreateDate 


class patentResult(db.Model):
    Num = db.Column(db.String(50))
    Name = db.Column(db.String(50))
    ApplicationNum = db.Column(db.String(50))
    PatentNum = db.Column(db.String(50))
    PatentMandate = db.Column(db.String(50))
    Inventor = db.Column(db.String(50))
    Patentee = db.Column(db.String(50))
    Files = db.Column(db.String(50))
    SpecialistId = db.Column(db.String(36), db.ForeignKey('specialist.SPETid'))
    OperatorId = db.Column(db.String(36))
    HashId = db.Column(db.String(36), nullable=False, primary_key=True)
    State = db.Column(db.SMALLINT)
    createDate = db.Column(db.DateTime)
    #primary key(HashId)

    def __init__(self, Num, Name, ApplicationNum, PatentNum, PatentMandate, Inventor, Patentee, Files, SpecialistId, OperatorId, HashId, State, createDate):

        self.Num = Num 
        self.Name = Name 
        self.ApplicationNum = ApplicationNum 
        self.PatentNum = PatentNum 
        self.PatentMandate = PatentMandate 
        self.Inventor = Inventor 
        self.Patentee = Patentee 
        self.Files = Files 
        self.SpecialistId = SpecialistId 
        self.OperatorId = OperatorId 
        self.HashId = HashId 
        self.State = State 
        self.createDate = createDate 


class pullulation(db.Model):
    PULLid = db.Column(db.String(36), nullable=False, primary_key=True)
    STSTid = db.Column(db.String(36), db.ForeignKey('study_story.STSTid'))
    famous = db.Column(db.String(100), nullable=False, default=' ')
    famous_date = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    famous_age = db.Column(db.SMALLINT, nullable=False)
    famous_reason = db.Column(db.String(50), nullable=False, default=' ')
    famous_achievement = db.Column(db.String(50), nullable=False, default=' ')
    revelation = db.Column(db.String(50), nullable=False, default=' ')
    experience = db.Column(db.Text, nullable=False)
    aphorism = db.Column(db.String(100), nullable=False, default=' ')
    advice = db.Column(db.String(100), nullable=False)
    credendum = db.Column(db.String(100), nullable=False)
    hope = db.Column(db.String(100), nullable=False)
    other_advice = db.Column(db.String(100), nullable=False)
    all_clinic_time = db.Column(db.SMALLINT, nullable=False)
    old_clinic_time = db.Column(db.SMALLINT, nullable=False)
    last_clinic_time = db.Column(db.SMALLINT, nullable=False)
    clinic_regard = db.Column(db.Text, nullable=False, default=' ')
    diagnose_custom = db.Column(db.Text, nullable=False, default=' ')
    #primary key(PULLid)

    def __init__(self, PULLid, STSTid, famous, famous_date, famous_age, famous_reason, famous_achievement, revelation, experience, aphorism, advice, credendum, hope, other_advice, all_clinic_time, old_clinic_time, last_clinic_time, clinic_regard, diagnose_custom):

        self.PULLid = PULLid 
        self.STSTid = STSTid 
        self.famous = famous 
        self.famous_date = famous_date 
        self.famous_age = famous_age 
        self.famous_reason = famous_reason 
        self.famous_achievement = famous_achievement 
        self.revelation = revelation 
        self.experience = experience 
        self.aphorism = aphorism 
        self.advice = advice 
        self.credendum = credendum 
        self.hope = hope 
        self.other_advice = other_advice 
        self.all_clinic_time = all_clinic_time 
        self.old_clinic_time = old_clinic_time 
        self.last_clinic_time = last_clinic_time 
        self.clinic_regard = clinic_regard 
        self.diagnose_custom = diagnose_custom 


class readBook(db.Model):
    REBOid = db.Column(db.String(36), nullable=False, primary_key=True)
    STSTid = db.Column(db.String(36), db.ForeignKey('study_story.STSTid'))
    sequence = db.Column(db.String(300), nullable=False)
    study_emphases = db.Column(db.SMALLINT, nullable=False)
    emphases_reason = db.Column(db.Text, nullable=False)
    study_advice = db.Column(db.SMALLINT, nullable=False)
    advice_reason = db.Column(db.Text, nullable=False)
    con_book = db.Column(db.Text, nullable=False)
    extensive_book = db.Column(db.Text, nullable=False)
    bad_book = db.Column(db.Text, nullable=False)
    classic_opinion = db.Column(db.Text, nullable=False)
    genre_attitude = db.Column(db.Text, nullable=False)
    relation_option = db.Column(db.SMALLINT, nullable=False)
    opinion_reason = db.Column(db.Text, nullable=False)
    special_book = db.Column(db.String(500), nullable=False)
    ratio = db.Column(db.String(100), nullable=False)
    #primary key(REBOid)

    def __init__(self, REBOid, STSTid, sequence, study_emphases, emphases_reason, study_advice, advice_reason, con_book, extensive_book, bad_book, classic_opinion, genre_attitude, relation_option, opinion_reason, special_book, ratio):

        self.REBOid = REBOid 
        self.STSTid = STSTid 
        self.sequence = sequence 
        self.study_emphases = study_emphases 
        self.emphases_reason = emphases_reason 
        self.study_advice = study_advice 
        self.advice_reason = advice_reason 
        self.con_book = con_book 
        self.extensive_book = extensive_book 
        self.bad_book = bad_book 
        self.classic_opinion = classic_opinion 
        self.genre_attitude = genre_attitude 
        self.relation_option = relation_option 
        self.opinion_reason = opinion_reason 
        self.special_book = special_book 
        self.ratio = ratio 


class rediagnose(db.Model):
    RDIAid = db.Column(db.String(36), nullable=False, primary_key=True)
    CAANid = db.Column(db.String(36), db.ForeignKey('case_analysis.CAANid'))
    RDIAno = db.Column(db.SMALLINT, nullable=False)
    disease_state = db.Column(db.String(200), nullable=False)
    tongue = db.Column(db.SMALLINT, nullable=False, default=0)
    tongue1 = db.Column(db.String(50), nullable=False)
    artery = db.Column(db.String(50), nullable=False)
    other_artery = db.Column(db.String(200), nullable=False)
    rediagnose_analysis = db.Column(db.Text, nullable=False)
    #primary key(RDIAid)

    def __init__(self, RDIAid, CAANid, RDIAno, disease_state, tongue, tongue1, artery, other_artery, rediagnose_analysis):

        self.RDIAid = RDIAid 
        self.CAANid = CAANid 
        self.RDIAno = RDIAno 
        self.disease_state = disease_state 
        self.tongue = tongue 
        self.tongue1 = tongue1 
        self.artery = artery 
        self.other_artery = other_artery 
        self.rediagnose_analysis = rediagnose_analysis 


class researchItem(db.Model):
    Name = db.Column(db.String(50))
    Leval = db.Column(db.String(50))
    Princial = db.Column(db.String(50))
    Participent = db.Column(db.String(50))
    Affiliation = db.Column(db.Text)
    Duration = db.Column(db.String(50))
    Source = db.Column(db.Text)
    Abstruct = db.Column(db.String(50))
    HashId = db.Column(db.String(36), nullable=False, primary_key=True)
    SpecialisId = db.Column(db.String(36), db.ForeignKey('specialist.SPETid'))
    State = db.Column(db.SMALLINT)
    OperationId = db.Column(db.String(36))
    Category = db.Column(db.String(50))
    CreateDate = db.Column(db.DateTime)
    #primary key(HashId)

    def __init__(self, Name, Leval, Princial, Participent, Affiliation, Duration, Source, Abstruct, HashId, SpecialisId, State, OperationId, Category, CreateDate):

        self.Name = Name 
        self.Leval = Leval 
        self.Princial = Princial 
        self.Participent = Participent 
        self.Affiliation = Affiliation 
        self.Duration = Duration 
        self.Source = Source 
        self.Abstruct = Abstruct 
        self.HashId = HashId 
        self.SpecialisId = SpecialisId 
        self.State = State 
        self.OperationId = OperationId 
        self.Category = Category 
        self.CreateDate = CreateDate 


class resultReward(db.Model):
    Num = db.Column(db.String(50))
    ResultName = db.Column(db.String(50))
    Author = db.Column(db.String(50))
    AuthorAffiliation = db.Column(db.String(50))
    RewardName = db.Column(db.String(50))
    Leval = db.Column(db.String(50))
    RewardDate = db.Column(db.String(50))
    LicensingGroup = db.Column(db.String(50))
    Files = db.Column(db.String(50))
    SpecialistId = db.Column(db.String(36), db.ForeignKey('specialist.SPETid'))
    OperatorId = db.Column(db.String(36))
    State = db.Column(db.SMALLINT)
    HashId = db.Column(db.String(36), nullable=False, primary_key=True)
    CreateDate = db.Column(db.DateTime)
    #primary key(HashId)

    def __init__(self, Num, ResultName, Author, AuthorAffiliation, RewardName, Leval, RewardDate, LicensingGroup, Files, SpecialistId, OperatorId, State, HashId, CreateDate):

        self.Num = Num 
        self.ResultName = ResultName 
        self.Author = Author 
        self.AuthorAffiliation = AuthorAffiliation 
        self.RewardName = RewardName 
        self.Leval = Leval 
        self.RewardDate = RewardDate 
        self.LicensingGroup = LicensingGroup 
        self.Files = Files 
        self.SpecialistId = SpecialistId 
        self.OperatorId = OperatorId 
        self.State = State 
        self.HashId = HashId 
        self.CreateDate = CreateDate 


class science(db.Model):
    SCIEid = db.Column(db.String(36), nullable=False, primary_key=True)
    SPETid = db.Column(db.String(36), db.ForeignKey('specialist.SPETid'))
    recipe_description = db.Column(db.Text, nullable=False, default=' ')
    drugs = db.Column(db.Text, nullable=False)
    technique = db.Column(db.Text, nullable=False, default=' ')
    recipes = db.Column(db.Text, nullable=False, default=' ')
    study_opinion = db.Column(db.Text, nullable=False, default=' ')
    study_advice = db.Column(db.Text, nullable=False, default=' ')
    reports = db.Column(db.Text, nullable=False, default=' ')
    contents = db.Column(db.Text, nullable=False, default=' ')
    reference = db.Column(db.Text, nullable=False, default=' ')
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    state = db.Column(db.SMALLINT, nullable=False, default=0)
    #primary key(SCIEid)

    def __init__(self, SCIEid, SPETid, recipe_description, drugs, technique, recipes, study_opinion, study_advice, reports, contents, reference, createDay, optrid, state):

        self.SCIEid = SCIEid 
        self.SPETid = SPETid 
        self.recipe_description = recipe_description 
        self.drugs = drugs 
        self.technique = technique 
        self.recipes = recipes 
        self.study_opinion = study_opinion 
        self.study_advice = study_advice 
        self.reports = reports 
        self.contents = contents 
        self.reference = reference 
        self.createDay = createDay 
        self.optrid = optrid 
        self.state = state 


class semiotic(db.Model):
    SEMCid = db.Column(db.String(36), nullable=False, primary_key=True)
    CDISid = db.Column(db.String(36), db.ForeignKey('chinese_disease.CDISid'))
    code = db.Column(db.String(20), nullable=False)
    groupCode = db.Column(db.String(20), nullable=False, default=' ')
    name = db.Column(db.String(100), nullable=False)
    isClassical = db.Column(db.Boolean, nullable=False, default=1)
    SPETid = db.Column(db.String(36), nullable=False, default=' ')
    illustration = db.Column(db.Text, nullable=False, default=' ')
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    state = db.Column(db.SMALLINT, nullable=False, default=0)
    #primary key(SEMCid))
    #key = db.Column(AK_SEMIOTIC_PK_CODE_SEMIOTIC (code)

    def __init__(self, SEMCid, CDISid, code, groupCode, name, isClassical, SPETid, illustration, createDay, optrid, state):

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


class sourceTechnology(db.Model):
    OperatorId = db.Column(db.String(36))
    Num = db.Column(db.String(50))
    Name = db.Column(db.String(50))
    Content = db.Column(db.Text)
    FormationTime = db.Column(db.String(50))
    Possessor = db.Column(db.String(50))
    Bearer = db.Column(db.String(50))
    PossetionAffiliation = db.Column(db.Text)
    ApplicaionAffiliation = db.Column(db.Text)
    Duration = db.Column(db.String(50))
    Files = db.Column(db.String(50))
    SpecialisId = db.Column(db.String(36), db.ForeignKey('specialist.SPETid'))
    HashId = db.Column(db.String(36), nullable=False, primary_key=True)
    State = db.Column(db.SMALLINT)
    CreateDate = db.Column(db.DateTime)
    #primary key(HashId)

    def __init__(self, OperatorId, Num, Name, Content, FormationTime, Possessor, Bearer, PossetionAffiliation, ApplicaionAffiliation, Duration, Files, SpecialisId, HashId, State, CreateDate):

        self.OperatorId = OperatorId 
        self.Num = Num 
        self.Name = Name 
        self.Content = Content 
        self.FormationTime = FormationTime 
        self.Possessor = Possessor 
        self.Bearer = Bearer 
        self.PossetionAffiliation = PossetionAffiliation 
        self.ApplicaionAffiliation = ApplicaionAffiliation 
        self.Duration = Duration 
        self.Files = Files 
        self.SpecialisId = SpecialisId 
        self.HashId = HashId 
        self.State = State 
        self.CreateDate = CreateDate 


class specialist(db.Model):
    SPETid = db.Column(db.String(36), nullable=False, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    code = db.Column(db.String(20))
    birthday = db.Column(db.DateTime, nullable=False)
    nationality = db.Column(db.SMALLINT, nullable=False)
    native_place = db.Column(db.String(6), nullable=False)
    gender = db.Column(db.SMALLINT, nullable=False)
    afflication = db.Column(db.String(100), nullable=False)
    telephone = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    postalcode = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(100), nullable=False)
    principalship = db.Column(db.String(100), nullable=False)
    major = db.Column(db.String(100), nullable=False)
    social_status = db.Column(db.Text, nullable=False)
    school_degree = db.Column(db.String(100), nullable=False)
    school = db.Column(db.String(100), nullable=False)
    graduation_date = db.Column(db.DateTime, nullable=False)
    other_degree = db.Column(db.String(100), nullable=False)
    learning_date = db.Column(db.DateTime, nullable=False)
    work_date = db.Column(db.DateTime, nullable=False)
    motivation = db.Column(db.String(100), nullable=False)
    mode = db.Column(db.String(100), nullable=False)
    resume = db.Column(db.Text, nullable=False)
    contribution = db.Column(db.Text, nullable=False)
    health_info = db.Column(db.String(50), nullable=False)
    clinic_info = db.Column(db.String(50), nullable=False)
    reseach_disease = db.Column(db.Text, nullable=False)
    recips = db.Column(db.Text, nullable=False)
    drugs = db.Column(db.Text, nullable=False)
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    state = db.Column(db.SMALLINT, nullable=False, default=0)
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    #primary key(SPETid)

    def __init__(self, SPETid, name, code, birthday, nationality, native_place, gender, afflication, telephone, address, postalcode, status, principalship, major, social_status, school_degree, school, graduation_date, other_degree, learning_date, work_date, motivation, mode, resume, contribution, health_info, clinic_info, reseach_disease, recips, drugs, optrid, state, createDay):

        self.SPETid = SPETid 
        self.name = name 
        self.code = code 
        self.birthday = birthday 
        self.nationality = nationality 
        self.native_place = native_place 
        self.gender = gender 
        self.afflication = afflication 
        self.telephone = telephone 
        self.address = address 
        self.postalcode = postalcode 
        self.status = status 
        self.principalship = principalship 
        self.major = major 
        self.social_status = social_status 
        self.school_degree = school_degree 
        self.school = school 
        self.graduation_date = graduation_date 
        self.other_degree = other_degree 
        self.learning_date = learning_date 
        self.work_date = work_date 
        self.motivation = motivation 
        self.mode = mode 
        self.resume = resume 
        self.contribution = contribution 
        self.health_info = health_info 
        self.clinic_info = clinic_info 
        self.reseach_disease = reseach_disease 
        self.recips = recips 
        self.drugs = drugs 
        self.optrid = optrid 
        self.state = state 
        self.createDay = createDay 


class student(db.Model):
    STUDid = db.Column(db.String(36), nullable=False, primary_key=True)
    TEEXid = db.Column(db.String(36), db.ForeignKey('teach_experience.TEEXid'))
    name = db.Column(db.String(20), nullable=False)
    years = db.Column(db.String(20), nullable=False, default=' ')
    major = db.Column(db.String(100), nullable=False)
    domain = db.Column(db.String(30), nullable=False, default=' ')
    achievement = db.Column(db.String(100), nullable=False, default=' ')
    #primary key(STUDid)

    def __init__(self, STUDid, TEEXid, name, years, major, domain, achievement):

        self.STUDid = STUDid 
        self.TEEXid = TEEXid 
        self.name = name 
        self.years = years 
        self.major = major 
        self.domain = domain 
        self.achievement = achievement 


class studyRelation(db.Model):
    STRLid = db.Column(db.String(36), nullable=False, primary_key=True)
    PULLid = db.Column(db.String(36), db.ForeignKey('pullulation.PULLid'))
    name = db.Column(db.String(20), nullable=False)
    afflication = db.Column(db.String(100), nullable=False)
    reason = db.Column(db.String(100), nullable=False, default=' ')
    #primary key(STRLid)

    def __init__(self, STRLid, PULLid, name, afflication, reason):

        self.STRLid = STRLid 
        self.PULLid = PULLid 
        self.name = name 
        self.afflication = afflication 
        self.reason = reason 


class studyStory(db.Model):
    STSTid = db.Column(db.String(36), nullable=False, primary_key=True)
    SPETid = db.Column(db.String(36), db.ForeignKey('specialist.SPETid'))
    study_start_date = db.Column(db.DateTime, nullable=False)
    start_age = db.Column(db.SMALLINT, nullable=False, default=0)
    read_day = db.Column(db.SMALLINT, nullable=False, default=0)
    read_week = db.Column(db.SMALLINT, nullable=False, default=0)
    practice_day = db.Column(db.SMALLINT, nullable=False, default=0)
    practice_week = db.Column(db.SMALLINT, nullable=False, default=0)
    study_end_date = db.Column(db.DateTime, nullable=False)
    end_age = db.Column(db.SMALLINT, nullable=False, default=0)
    matter_type = db.Column(db.SMALLINT, nullable=False)
    matter = db.Column(db.Text, nullable=False, default=' ')
    work_start_date = db.Column(db.DateTime, nullable=False)
    work_age = db.Column(db.SMALLINT, nullable=False, default=0)
    clinic_day = db.Column(db.SMALLINT, nullable=False, default=0)
    clinic_week = db.Column(db.SMALLINT, nullable=False, default=0)
    study_day = db.Column(db.SMALLINT, nullable=False, default=0)
    study_week = db.Column(db.SMALLINT, nullable=False, default=0)
    clinic_years = db.Column(db.SMALLINT, nullable=False, default=0)
    root_years = db.Column(db.SMALLINT, nullable=False, default=0)
    root_place = db.Column(db.String(50), nullable=False)
    work_start = db.Column(db.String(20), nullable=False)
    work_middle = db.Column(db.String(20), nullable=False)
    work_end = db.Column(db.String(20), nullable=False)
    work_mode = db.Column(db.String(50), nullable=False)
    study_key = db.Column(db.String(50), nullable=False, default=' ')
    other_situation = db.Column(db.Text, nullable=False, default=' ')
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    state = db.Column(db.SMALLINT, nullable=False, default=0)
    #primary key(STSTid)

    def __init__(self, STSTid, SPETid, study_start_date, start_age, read_day, read_week, practice_day, practice_week, study_end_date, end_age, matter_type, matter, work_start_date, work_age, clinic_day, clinic_week, study_day, study_week, clinic_years, root_years, root_place, work_start, work_middle, work_end, work_mode, study_key, other_situation, createDay, optrid, state):

        self.STSTid = STSTid 
        self.SPETid = SPETid 
        self.study_start_date = study_start_date 
        self.start_age = start_age 
        self.read_day = read_day 
        self.read_week = read_week 
        self.practice_day = practice_day 
        self.practice_week = practice_week 
        self.study_end_date = study_end_date 
        self.end_age = end_age 
        self.matter_type = matter_type 
        self.matter = matter 
        self.work_start_date = work_start_date 
        self.work_age = work_age 
        self.clinic_day = clinic_day 
        self.clinic_week = clinic_week 
        self.study_day = study_day 
        self.study_week = study_week 
        self.clinic_years = clinic_years 
        self.root_years = root_years 
        self.root_place = root_place 
        self.work_start = work_start 
        self.work_middle = work_middle 
        self.work_end = work_end 
        self.work_mode = work_mode 
        self.study_key = study_key 
        self.other_situation = other_situation 
        self.createDay = createDay 
        self.optrid = optrid 
        self.state = state 


class symptom(db.Model):
    SYPMid = db.Column(db.String(36), nullable=False, primary_key=True)
    code = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    parentcode = db.Column(db.String(20), nullable=False)
    level = db.Column(db.SMALLINT, nullable=False)
    kind = db.Column(db.SMALLINT, nullable=False, default=0)
    sort = db.Column(db.SMALLINT, nullable=False, default=1)
    valSort = db.Column(db.Integer, nullable=False, default=0)
    hasFile = db.Column(db.Boolean, nullable=False, default=0)
    isClassical = db.Column(db.Boolean, nullable=False, default=1)
    SPETid = db.Column(db.String(36), nullable=False, default=' ')
    illustration = db.Column(db.Text, nullable=False, default=' ')
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    state = db.Column(db.SMALLINT, nullable=False, default=0)
    #primary key(SYPMid))
    #key = db.Column(AK_SYMPTOM_PK_CODE_SYMPTOM (code)

    def __init__(self, SYPMid, code, name, parentcode, level, kind, sort, valSort, hasFile, isClassical, SPETid, illustration, createDay, optrid, state):

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


class syscode(db.Model):
    CODEid = db.Column(db.String(36), nullable=False, primary_key=True)
    no = db.Column(db.Integer, nullable=False)
    code = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(50), nullable=False, default=' ')
    illustration = db.Column(db.Text, nullable=False, default=' ')
    #primary key(CODEid))
    #key = db.Column(AK_SYSCODE_PK_CODE_SYSCODE (code))
    #key = db.Column(AK_SYSCODE_PK_NO_SYSCODE (no)

    def __init__(self, CODEid, no, code, name, illustration):

        self.CODEid = CODEid 
        self.no = no 
        self.code = code 
        self.name = name 
        self.illustration = illustration 


class syscodeValue(db.Model):
    SVALid = db.Column(db.String(36), nullable=False, primary_key=True)
    CODEid = db.Column(db.String(36), nullable=False, default=' ')
    subno = db.Column(db.Integer, nullable=False)
    subcode = db.Column(db.String(20), nullable=False)
    truevalue = db.Column(db.String(100))
    py = db.Column(db.String(20), default=' ')
    wb = db.Column(db.String(20), default=' ')
    illustration = db.Column(db.Text, default=' ')
    #primary key(SVALid)

    def __init__(self, SVALid, CODEid, subno, subcode, truevalue, py, wb, illustration):

        self.SVALid = SVALid 
        self.CODEid = CODEid 
        self.subno = subno 
        self.subcode = subcode 
        self.truevalue = truevalue 
        self.py = py 
        self.wb = wb 
        self.illustration = illustration 


class sysfun(db.Model):
    SFUNid = db.Column(db.String(36), nullable=False, primary_key=True)
    code = db.Column(db.String(20), nullable=False)
    parentcode = db.Column(db.String(20), nullable=False, default='-1')
    level = db.Column(db.SMALLINT, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    href = db.Column(db.String(200), nullable=False, default=' ')
    targetFrame = db.Column(db.String(100), nullable=False, default=' ')
    illustration = db.Column(db.Text, nullable=False, default=' ')
    state = db.Column(db.SMALLINT, nullable=False, default=0)
    #primary key(SFUNid))
    #key = db.Column(AK_SYSFUN_PK_CODE_SYSFUN (code)

    def __init__(self, SFUNid, code, parentcode, level, name, href, targetFrame, illustration, state):

        self.SFUNid = SFUNid 
        self.code = code 
        self.parentcode = parentcode 
        self.level = level 
        self.name = name 
        self.href = href 
        self.targetFrame = targetFrame 
        self.illustration = illustration 
        self.state = state 


class table(db.Model):
    id = db.Column(db.CHAR(10), nullable=False, primary_key=True)
    name = db.Column(db.CHAR(10))
    #primary key(id)

    def __init__(self, id, name):

        self.id = id 
        self.name = name 


class talentreward(db.Model):
    OperatorId = db.Column(db.String(36))
    Name = db.Column(db.String(50))
    Category = db.Column(db.String(50))
    Leval = db.Column(db.String(50))
    Principal = db.Column(db.String(50))
    Participent = db.Column(db.String(50))
    Affiliation = db.Column(db.Text)
    StaringTime = db.Column(db.String(50))
    Source = db.Column(db.Text)
    Absturct = db.Column(db.Text)
    SpecialisId = db.Column(db.String(36), db.ForeignKey('specialist.SPETid'))
    HashId = db.Column(db.String(36), nullable=False, primary_key=True)
    State = db.Column(db.SMALLINT)
    CreateDate = db.Column(db.DateTime)
    #primary key(HashId)

    def __init__(self, OperatorId, Name, Category, Leval, Principal, Participent, Affiliation, StaringTime, Source, Absturct, SpecialisId, HashId, State, CreateDate):

        self.OperatorId = OperatorId 
        self.Name = Name 
        self.Category = Category 
        self.Leval = Leval 
        self.Principal = Principal 
        self.Participent = Participent 
        self.Affiliation = Affiliation 
        self.StaringTime = StaringTime 
        self.Source = Source 
        self.Absturct = Absturct 
        self.SpecialisId = SpecialisId 
        self.HashId = HashId 
        self.State = State 
        self.CreateDate = CreateDate 


class teachExperience(db.Model):
    TEEXid = db.Column(db.String(36), nullable=False, primary_key=True)
    STSTid = db.Column(db.String(36), db.ForeignKey('study_story.STSTid'))
    study_gist = db.Column(db.String(300), nullable=False)
    clinic_gist = db.Column(db.String(300), nullable=False)
    other_gist = db.Column(db.String(300), nullable=False)
    schoolage_request = db.Column(db.String(300), nullable=False)
    knowledge_request = db.Column(db.String(300), nullable=False)
    moral_request = db.Column(db.String(300), nullable=False)
    other_request = db.Column(db.String(300), nullable=False)
    school_opinion = db.Column(db.Text, nullable=False)
    course_ratio = db.Column(db.String(300), nullable=False)
    period_ratio = db.Column(db.String(300), nullable=False)
    textbook = db.Column(db.Text, nullable=False)
    inherit_mode = db.Column(db.Text, nullable=False)
    teach_opinion = db.Column(db.Text, nullable=False)
    combine_opinion = db.Column(db.Text, nullable=False)
    system_opinion = db.Column(db.Text, nullable=False)
    department_opinion = db.Column(db.Text, nullable=False)
    research_opinion = db.Column(db.Text, nullable=False)
    support_opinion = db.Column(db.Text, nullable=False)
    #primary key(TEEXid)

    def __init__(self, TEEXid, STSTid, study_gist, clinic_gist, other_gist, schoolage_request, knowledge_request, moral_request, other_request, school_opinion, course_ratio, period_ratio, textbook, inherit_mode, teach_opinion, combine_opinion, system_opinion, department_opinion, research_opinion, support_opinion):

        self.TEEXid = TEEXid 
        self.STSTid = STSTid 
        self.study_gist = study_gist 
        self.clinic_gist = clinic_gist 
        self.other_gist = other_gist 
        self.schoolage_request = schoolage_request 
        self.knowledge_request = knowledge_request 
        self.moral_request = moral_request 
        self.other_request = other_request 
        self.school_opinion = school_opinion 
        self.course_ratio = course_ratio 
        self.period_ratio = period_ratio 
        self.textbook = textbook 
        self.inherit_mode = inherit_mode 
        self.teach_opinion = teach_opinion 
        self.combine_opinion = combine_opinion 
        self.system_opinion = system_opinion 
        self.department_opinion = department_opinion 
        self.research_opinion = research_opinion 
        self.support_opinion = support_opinion 


class teaching(db.Model):
    TEACid = db.Column(db.String(36), nullable=False, primary_key=True)
    PULLid = db.Column(db.String(36), db.ForeignKey('pullulation.PULLid'))
    start_date = db.Column(db.String(16), nullable=False, default='1900-1-1')
    end_date = db.Column(db.String(16), nullable=False, default='1900-1-1')
    teach_place = db.Column(db.String(100), nullable=False, default=' ')
    major = db.Column(db.String(100), nullable=False)
    #primary key(TEACid)

    def __init__(self, TEACid, PULLid, start_date, end_date, teach_place, major):

        self.TEACid = TEACid 
        self.PULLid = PULLid 
        self.start_date = start_date 
        self.end_date = end_date 
        self.teach_place = teach_place 
        self.major = major 


class techCreative(db.Model):
    Num = db.Column(db.String(50))
    Name = db.Column(db.Text)
    Conent = db.Column(db.Text)
    FormationTime = db.Column(db.String(50))
    Author = db.Column(db.String(50))
    Files = db.Column(db.String(50))
    HashId = db.Column(db.String(36), nullable=False, primary_key=True)
    State = db.Column(db.SMALLINT)
    SpecialisId = db.Column(db.String(36), db.ForeignKey('specialist.SPETid'))
    CreateDate = db.Column(db.DateTime)
    OperatorId = db.Column(db.String(36))
    #primary key(HashId)

    def __init__(self, Num, Name, Conent, FormationTime, Author, Files, HashId, State, SpecialisId, CreateDate, OperatorId):

        self.Num = Num 
        self.Name = Name 
        self.Conent = Conent 
        self.FormationTime = FormationTime 
        self.Author = Author 
        self.Files = Files 
        self.HashId = HashId 
        self.State = State 
        self.SpecialisId = SpecialisId 
        self.CreateDate = CreateDate 
        self.OperatorId = OperatorId 


class technologyapplication(db.Model):
    OperatorId = db.Column(db.String(36))
    Num = db.Column(db.String(50))
    Name = db.Column(db.String(50))
    Disease = db.Column(db.String(50))
    Department = db.Column(db.String(50))
    Author = db.Column(db.String(50))
    Affiliation = db.Column(db.Text)
    Percentage = db.Column(db.String(50))
    Beneficiary = db.Column(db.Text)
    EfficacyAssement = db.Column(db.Text)
    HealthEconomics = db.Column(db.Text)
    SpecialisId = db.Column(db.String(36), db.ForeignKey('specialist.SPETid'))
    HashId = db.Column(db.String(36), nullable=False, primary_key=True)
    State = db.Column(db.SMALLINT)
    CreateDate = db.Column(db.DateTime)
    #primary key(HashId)

    def __init__(self, OperatorId, Num, Name, Disease, Department, Author, Affiliation, Percentage, Beneficiary, EfficacyAssement, HealthEconomics, SpecialisId, HashId, State, CreateDate):

        self.OperatorId = OperatorId 
        self.Num = Num 
        self.Name = Name 
        self.Disease = Disease 
        self.Department = Department 
        self.Author = Author 
        self.Affiliation = Affiliation 
        self.Percentage = Percentage 
        self.Beneficiary = Beneficiary 
        self.EfficacyAssement = EfficacyAssement 
        self.HealthEconomics = HealthEconomics 
        self.SpecialisId = SpecialisId 
        self.HashId = HashId 
        self.State = State 
        self.CreateDate = CreateDate 


class technologycase(db.Model):
    OperatorId = db.Column(db.String(36))
    Num = db.Column(db.String(50))
    Name = db.Column(db.String(50))
    Possessor = db.Column(db.String(50))
    PossesstionAffilation = db.Column(db.String(50))
    specialisId = db.Column(db.String(36), db.ForeignKey('specialist.SPETid'))
    HashId = db.Column(db.String(36), nullable=False, primary_key=True)
    State = db.Column(db.SMALLINT)
    CreateDate = db.Column(db.DateTime)
    #primary key(HashId)

    def __init__(self, OperatorId, Num, Name, Possessor, PossesstionAffilation, specialisId, HashId, State, CreateDate):

        self.OperatorId = OperatorId 
        self.Num = Num 
        self.Name = Name 
        self.Possessor = Possessor 
        self.PossesstionAffilation = PossesstionAffilation 
        self.specialisId = specialisId 
        self.HashId = HashId 
        self.State = State 
        self.CreateDate = CreateDate 


class userrole(db.Model):
    ROLEid = db.Column(db.String(36), nullable=False, primary_key=True)
    code = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    illustration = db.Column(db.Text, nullable=False, default=' ')
    state = db.Column(db.SMALLINT, nullable=False, default=0)
    #primary key(ROLEid))
    #key = db.Column(AK_USERROLE_PK_CODE_USERROLE (code)

    def __init__(self, ROLEid, code, name, illustration, state):

        self.ROLEid = ROLEid 
        self.code = code 
        self.name = name 
        self.illustration = illustration 
        self.state = state 


class userrolefun(db.Model):
    ROLEid = db.Column(db.String(36), primary_key=True)
    #ROLEid = db.Column(db.String(36), nullable=False, primary_key=True, db.ForeignKey('userrole.ROLEid'))
    SFUNid = db.Column(db.String(36), db.ForeignKey('sysfun.SFUNid'))
    #SFUNid = db.Column(db.String(36), nullable=False, db.ForeignKey('sysfun.SFUNid'))
    #primary key(ROLEid, SFUNid)

    def __init__(self, ROLEid, SFUNid):

        self.ROLEid = ROLEid 
        self.SFUNid = SFUNid 


class WesternDisease(db.Model):
    WDISid = db.Column(db.String(36), nullable=False, primary_key=True)
    code = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    parentcode = db.Column(db.String(20), nullable=False)
    level = db.Column(db.SMALLINT, nullable=False)
    isClassical = db.Column(db.Boolean, nullable=False, default=1)
    SPETid = db.Column(db.String(36), nullable=False, default=' ')
    illustration = db.Column(db.Text, nullable=False, default=' ')
    createDay = db.Column(db.DateTime, nullable=False, default='1900-1-1')
    optrid = db.Column(db.String(36), nullable=False, default=' ')
    state = db.Column(db.SMALLINT, nullable=False, default=0)
    #primary key(WDISid))
    #key = db.Column(AK_WDISEASE_PK_CODE_WDISEASE (code)

    def __init__(self, WDISid, code, name, parentcode, level, isClassical, SPETid, illustration, createDay, optrid, state):

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


class wisdom(db.Model):
    WISDid = db.Column(db.String(36), nullable=False, primary_key=True)
    REBOid = db.Column(db.String(36), db.ForeignKey('read_book.REBOid'))
    content = db.Column(db.Text, nullable=False, default=' ')
    #primary key(WISDid)

    def __init__(self, WISDid, REBOid, content):

        WISDid = db.Column(db.String(36), nullable=False, primary_key=True)
        REBOid = db.Column(db.String(36), db.ForeignKey('read_book.REBOid'))
    content = db.Column(db.Text, nullable=False, default=' ')
        #primary key(WISDid)

