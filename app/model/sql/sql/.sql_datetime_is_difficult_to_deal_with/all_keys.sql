
table MissionAlgor add constraint FK_MISSIONA_RELATIONS_ALGORITH foreign key (ALGOid)
      references algorithm (ALGOid);

table MissionAlgor add constraint FK_MISSIONA_RELATIONS_LEARNMIS foreign key (LEMIid)
      references learnMission (LEMIid);

table MissionPar add constraint FK_MISSIONP_RELATIONS_MISSIONA foreign key (MIALid)
      references MissionAlgor (MIALid);

table algorithmPar add constraint FK_ALGORITH_RELATIONS_ALGORITH foreign key (ALGOid)
      references algorithm (ALGOid);

table ancientBook add constraint FK_ANCIENTB_RELATIONS_READBOOK foreign key (REBOid)
      references readBook (REBOid);

table ancientSpecialist add constraint FK_ANCIENTS_RELATIONS_READBOOK foreign key (REBOid)
      references readBook (REBOid);

table background add constraint FK_BACKGROU_RELATIONS_STUDYSTO foreign key (STSTid)
      references studyStory (STSTid);

table badInstance add constraint FK_BADINSTA_RELATIONS_READBOOK foreign key (REBOid)
      references readBook (REBOid);

table basicinformation add constraint FK_basicinformation_specialist foreign key (SpecialisId)
      references specialist (SPETid);

table bookResult add constraint FK_bookResult_specialist foreign key (SpecialistId)
      references specialist (SPETid);

table caseAnalysis add constraint FK_CASEANAL_RELATIONS_SPECIALI foreign key (SPETid)
      references specialist (SPETid);

table classicCase add constraint FK_classicCase_specialist foreign key (SPETid)
      references specialist (SPETid);

table continuingeducation add constraint FK_continuingeducation_specialist foreign key (SpecialisId)
      references specialist (SPETid);

table diagExam add constraint FK_DIAGEXAM_RELATIONS_DIAGNOSE foreign key (DIAGid)
      references diagnose (DIAGid);

table diagExam add constraint FK_DIAGEXAM_RELATIONS_EXAMINAT foreign key (EXAMid)
      references examination (EXAMid);

table diagItem add constraint FK_DIAGITEM_RELATIONS_DIAGRECI foreign key (DIREid)
      references diagRecipe (DIREid);

table diagItem add constraint FK_DIAGITEM_RELATIONS_DRUG foreign key (dru_DRUGid)
      references drug (DRUGid);

table diagRecipe add constraint FK_DIAGRECI_RELATIONS_DIAGNOSE foreign key (DIAGid)
      references diagnose (DIAGid);

table diagRecipe add constraint FK_DIAGRECI_RELATIONS_FIXEDREC foreign key (FREPid)
      references fixedrecipe (FREPid);

table diagSymptom add constraint FK_DIAGSYMP_RELATIONS_DIAGNOSE foreign key (DIAGid)
      references diagnose (DIAGid);

table diagSymptom add constraint FK_DIAGSYMP_RELATIONS_SYMPTOM foreign key (SYPMid)
      references symptom (SYPMid);

table diagnose add constraint FK_DIAGNOSE_HAVE_DCASE foreign key (CASEid)
      references dCase (CASEid);

table dtmpExamination add constraint FK_DTMPEXAM_RELATIONS_DTEMPLAT foreign key (DTMPid)
      references dTemplate (DTMPid);

table dtmpExamination add constraint FK_DTMPEXAM_RELATIONS_EXAMINAT foreign key (EXAMid)
      references examination (EXAMid);

table dtmpSymptom add constraint FK_DTMPSYMP_RELATIONS_DTEMPLAT foreign key (DTMPid)
      references dTemplate (DTMPid);

table dtmpSymptom add constraint FK_DTMPSYMP_RELATIONS_SYMPTOM foreign key (SYPMid)
      references symptom (SYPMid);

table feature add constraint FK_FEATURE_RELATIONS_DATASET foreign key (DASEid)
      references dataSet (DASEid);

table fixedrecipeItem add constraint FK_FIXEDREC_RELATIONS_DRUG foreign key (DRUGid)
      references drug (DRUGid);

table fixedrecipeItem add constraint FK_FIXEDREC_RELATIONS_FIXEDREC foreign key (FREPid)
      references fixedrecipe (FREPid);

table genre add constraint FK_GENRE_RELATIONS_INHERITS foreign key (INSTid)
      references inheritStudy (INSTid);

table goodInstance add constraint FK_GOODINST_RELATIONS_READBOOK foreign key (REBOid)
      references readBook (REBOid);

table inherit add constraint FK_INHERIT_RELATIONS_INHERITS foreign key (INSTid)
      references inheritStudy (INSTid);

table inheritStudy add constraint FK_INHERITS_RELATIONS_SPECIALI foreign key (SPETid)
      references specialist (SPETid);

table integratedSym add constraint FK_INTEGRAT_RELATIONS_SYMPTOM foreign key (SYPMid)
      references symptom (SYPMid);

table learnMission add constraint FK_LEARNMIS_RELATIONS_DATASET foreign key (DASEid)
      references dataSet (DASEid);

table literature add constraint FK_LITERATU_RELATIONS_SCIENCE foreign key (SCIEid)
      references science (SCIEid);

table mainBook add constraint FK_MAINBOOK_RELATIONS_INHERITS foreign key (INSTid)
      references inheritStudy (INSTid);

table mediaInfo add constraint FK_mediaInfo_specialist foreign key (SpecialistId)
      references specialist (SPETid);

table modernBook add constraint FK_MODERNBO_RELATIONS_READBOOK foreign key (REBOid)
      references readBook (REBOid);

table modernSpecialist add constraint FK_MODERNSP_RELATIONS_READBOOK foreign key (REBOid)
      references readBook (REBOid);

table newDTechnology add constraint FK_newDTechnology_specialist foreign key (SpecialisId)
      references specialist (SPETid);

table operator add constraint FK_OPERATOR_ISA_USERROLE foreign key (ROLEid)
      references userrole (ROLEid);

table operatorfun add constraint FK_OPERATOR_OPERATORF_OPERATOR foreign key (OPTRid)
      references operator (OPTRid);

table operatorfun add constraint FK_OPERATOR_OPERATORF_SYSFUN foreign key (SFUNid)
      references sysfun (SFUNid);

table otherBook add constraint FK_OTHERBOO_RELATIONS_BACKGROU foreign key (BACKid)
      references background (BACKid);

table otherInformation add constraint FK_OTHERINF_RELATIONS_INHERITS foreign key (INSTid)
      references inheritStudy (INSTid);

table paperResult add constraint FK_paperResult_specialist foreign key (SpeicalistId)
      references specialist (SPETid);

table patentResult add constraint FK_patentResult_specialist foreign key (SpecialistId)
      references specialist (SPETid);

table pullulation add constraint FK_PULLULAT_RELATIONS_STUDYSTO foreign key (STSTid)
      references studyStory (STSTid);

table readBook add constraint FK_READBOOK_RELATIONS_STUDYSTO foreign key (STSTid)
      references studyStory (STSTid);

table rediagnose add constraint FK_REDIAGNO_RELATIONS_CASEANAL foreign key (CAANid)
      references caseAnalysis (CAANid);

table researchItem add constraint FK_researchItem_specialist foreign key (SpecialisId)
      references specialist (SPETid);

table resultReward add constraint FK_resultReward_specialist foreign key (SpecialistId)
      references specialist (SPETid);

table science add constraint FK_SCIENCE_RELATIONS_SPECIALI foreign key (SPETid)
      references specialist (SPETid);

table semiotic add constraint FK_SEMIOTIC_RELATIONS_CDISEASE foreign key (CDISid)
      references cDisease (CDISid);

table sourceTechnology add constraint FK_sourceTechnology_specialist foreign key (SpecialisId)
      references specialist (SPETid);

table student add constraint FK_STUDENT_RELATIONS_TEACHEXP foreign key (TEEXid)
      references teachExperience (TEEXid);

table studyRelation add constraint FK_STUDYREL_RELATIONS_PULLULAT foreign key (PULLid)
      references pullulation (PULLid);

table studyStory add constraint FK_STUDYSTO_RELATIONS_SPECIALI foreign key (SPETid)
      references specialist (SPETid);

table talentreward add constraint FK_talentreward_specialist foreign key (SpecialisId)
      references specialist (SPETid);

table teachExperience add constraint FK_TEACHEXP_RELATIONS_STUDYSTO foreign key (STSTid)
      references studyStory (STSTid);

table teaching add constraint FK_TEACHING_RELATIONS_PULLULAT foreign key (PULLid)
      references pullulation (PULLid);

table techCreative add constraint FK_techCreative_specialist foreign key (SpecialisId)
      references specialist (SPETid);

table technologyapplication add constraint FK_technologyapplication_specialist foreign key (SpecialisId)
      references specialist (SPETid);

table technologycase add constraint FK_technologycase_specialist foreign key (specialisId)
      references specialist (SPETid);

table userrolefun add constraint FK_USERROLE_USERROLEF_SYSFUN foreign key (SFUNid)
      references sysfun (SFUNid);

table userrolefun add constraint FK_USERROLE_USERROLEF_USERROLE foreign key (ROLEid)
      references userrole (ROLEid);

table wisdom add constraint FK_WISDOM_RELATIONS_READBOOK foreign key (REBOid)
      references readBook (REBOid);

