
alter table MissionAlgor add constraint FK_MISSIONA_RELATIONS_ALGORITH foreign key (ALGOid)
      references algorithm (ALGOid);

alter table MissionAlgor add constraint FK_MISSIONA_RELATIONS_LEARNMIS foreign key (LEMIid)
      references learnMission (LEMIid);

alter table MissionPar add constraint FK_MISSIONP_RELATIONS_MISSIONA foreign key (MIALid)
      references MissionAlgor (MIALid);

alter table algorithmPar add constraint FK_ALGORITH_RELATIONS_ALGORITH foreign key (ALGOid)
      references algorithm (ALGOid);

alter table ancientBook add constraint FK_ANCIENTB_RELATIONS_READBOOK foreign key (REBOid)
      references readBook (REBOid);

alter table ancientSpecialist add constraint FK_ANCIENTS_RELATIONS_READBOOK foreign key (REBOid)
      references readBook (REBOid);

alter table background add constraint FK_BACKGROU_RELATIONS_STUDYSTO foreign key (STSTid)
      references studyStory (STSTid);

alter table badInstance add constraint FK_BADINSTA_RELATIONS_READBOOK foreign key (REBOid)
      references readBook (REBOid);

alter table basicinformation add constraint FK_basicinformation_specialist foreign key (SpecialisId)
      references specialist (SPETid);

alter table bookResult add constraint FK_bookResult_specialist foreign key (SpecialistId)
      references specialist (SPETid);

alter table caseAnalysis add constraint FK_CASEANAL_RELATIONS_SPECIALI foreign key (SPETid)
      references specialist (SPETid);

alter table classicCase add constraint FK_classicCase_specialist foreign key (SPETid)
      references specialist (SPETid);

alter table continuingeducation add constraint FK_continuingeducation_specialist foreign key (SpecialisId)
      references specialist (SPETid);

alter table diagExam add constraint FK_DIAGEXAM_RELATIONS_DIAGNOSE foreign key (DIAGid)
      references diagnose (DIAGid);

alter table diagExam add constraint FK_DIAGEXAM_RELATIONS_EXAMINAT foreign key (EXAMid)
      references examination (EXAMid);

alter table diagItem add constraint FK_DIAGITEM_RELATIONS_DIAGRECI foreign key (DIREid)
      references diagRecipe (DIREid);

alter table diagItem add constraint FK_DIAGITEM_RELATIONS_DRUG foreign key (dru_DRUGid)
      references drug (DRUGid);

alter table diagRecipe add constraint FK_DIAGRECI_RELATIONS_DIAGNOSE foreign key (DIAGid)
      references diagnose (DIAGid);

alter table diagRecipe add constraint FK_DIAGRECI_RELATIONS_FIXEDREC foreign key (FREPid)
      references fixedrecipe (FREPid);

alter table diagSymptom add constraint FK_DIAGSYMP_RELATIONS_DIAGNOSE foreign key (DIAGid)
      references diagnose (DIAGid);

alter table diagSymptom add constraint FK_DIAGSYMP_RELATIONS_SYMPTOM foreign key (SYPMid)
      references symptom (SYPMid);

alter table diagnose add constraint FK_DIAGNOSE_HAVE_DCASE foreign key (CASEid)
      references dCase (CASEid);

alter table dtmpExamination add constraint FK_DTMPEXAM_RELATIONS_DTEMPLAT foreign key (DTMPid)
      references dTemplate (DTMPid);

alter table dtmpExamination add constraint FK_DTMPEXAM_RELATIONS_EXAMINAT foreign key (EXAMid)
      references examination (EXAMid);

alter table dtmpSymptom add constraint FK_DTMPSYMP_RELATIONS_DTEMPLAT foreign key (DTMPid)
      references dTemplate (DTMPid);

alter table dtmpSymptom add constraint FK_DTMPSYMP_RELATIONS_SYMPTOM foreign key (SYPMid)
      references symptom (SYPMid);

alter table feature add constraint FK_FEATURE_RELATIONS_DATASET foreign key (DASEid)
      references dataSet (DASEid);

alter table fixedrecipeItem add constraint FK_FIXEDREC_RELATIONS_DRUG foreign key (DRUGid)
      references drug (DRUGid);

alter table fixedrecipeItem add constraint FK_FIXEDREC_RELATIONS_FIXEDREC foreign key (FREPid)
      references fixedrecipe (FREPid);

alter table genre add constraint FK_GENRE_RELATIONS_INHERITS foreign key (INSTid)
      references inheritStudy (INSTid);

alter table goodInstance add constraint FK_GOODINST_RELATIONS_READBOOK foreign key (REBOid)
      references readBook (REBOid);

alter table inherit add constraint FK_INHERIT_RELATIONS_INHERITS foreign key (INSTid)
      references inheritStudy (INSTid);

alter table inheritStudy add constraint FK_INHERITS_RELATIONS_SPECIALI foreign key (SPETid)
      references specialist (SPETid);

alter table integratedSym add constraint FK_INTEGRAT_RELATIONS_SYMPTOM foreign key (SYPMid)
      references symptom (SYPMid);

alter table learnMission add constraint FK_LEARNMIS_RELATIONS_DATASET foreign key (DASEid)
      references dataSet (DASEid);

alter table literature add constraint FK_LITERATU_RELATIONS_SCIENCE foreign key (SCIEid)
      references science (SCIEid);

alter table mainBook add constraint FK_MAINBOOK_RELATIONS_INHERITS foreign key (INSTid)
      references inheritStudy (INSTid);

alter table mediaInfo add constraint FK_mediaInfo_specialist foreign key (SpecialistId)
      references specialist (SPETid);

alter table modernBook add constraint FK_MODERNBO_RELATIONS_READBOOK foreign key (REBOid)
      references readBook (REBOid);

alter table modernSpecialist add constraint FK_MODERNSP_RELATIONS_READBOOK foreign key (REBOid)
      references readBook (REBOid);

alter table newDTechnology add constraint FK_newDTechnology_specialist foreign key (SpecialisId)
      references specialist (SPETid);

alter table operator add constraint FK_OPERATOR_ISA_USERROLE foreign key (ROLEid)
      references userrole (ROLEid);

alter table operatorfun add constraint FK_OPERATOR_OPERATORF_OPERATOR foreign key (OPTRid)
      references operator (OPTRid);

alter table operatorfun add constraint FK_OPERATOR_OPERATORF_SYSFUN foreign key (SFUNid)
      references sysfun (SFUNid);

alter table otherBook add constraint FK_OTHERBOO_RELATIONS_BACKGROU foreign key (BACKid)
      references background (BACKid);

alter table otherInformation add constraint FK_OTHERINF_RELATIONS_INHERITS foreign key (INSTid)
      references inheritStudy (INSTid);

alter table paperResult add constraint FK_paperResult_specialist foreign key (SpeicalistId)
      references specialist (SPETid);

alter table patentResult add constraint FK_patentResult_specialist foreign key (SpecialistId)
      references specialist (SPETid);

alter table pullulation add constraint FK_PULLULAT_RELATIONS_STUDYSTO foreign key (STSTid)
      references studyStory (STSTid);

alter table readBook add constraint FK_READBOOK_RELATIONS_STUDYSTO foreign key (STSTid)
      references studyStory (STSTid);

alter table rediagnose add constraint FK_REDIAGNO_RELATIONS_CASEANAL foreign key (CAANid)
      references caseAnalysis (CAANid);

alter table researchItem add constraint FK_researchItem_specialist foreign key (SpecialisId)
      references specialist (SPETid);

alter table resultReward add constraint FK_resultReward_specialist foreign key (SpecialistId)
      references specialist (SPETid);

alter table science add constraint FK_SCIENCE_RELATIONS_SPECIALI foreign key (SPETid)
      references specialist (SPETid);

alter table semiotic add constraint FK_SEMIOTIC_RELATIONS_CDISEASE foreign key (CDISid)
      references cDisease (CDISid);

alter table sourceTechnology add constraint FK_sourceTechnology_specialist foreign key (SpecialisId)
      references specialist (SPETid);

alter table student add constraint FK_STUDENT_RELATIONS_TEACHEXP foreign key (TEEXid)
      references teachExperience (TEEXid);

alter table studyRelation add constraint FK_STUDYREL_RELATIONS_PULLULAT foreign key (PULLid)
      references pullulation (PULLid);

alter table studyStory add constraint FK_STUDYSTO_RELATIONS_SPECIALI foreign key (SPETid)
      references specialist (SPETid);

alter table talentreward add constraint FK_talentreward_specialist foreign key (SpecialisId)
      references specialist (SPETid);

alter table teachExperience add constraint FK_TEACHEXP_RELATIONS_STUDYSTO foreign key (STSTid)
      references studyStory (STSTid);

alter table teaching add constraint FK_TEACHING_RELATIONS_PULLULAT foreign key (PULLid)
      references pullulation (PULLid);

alter table techCreative add constraint FK_techCreative_specialist foreign key (SpecialisId)
      references specialist (SPETid);

alter table technologyapplication add constraint FK_technologyapplication_specialist foreign key (SpecialisId)
      references specialist (SPETid);

alter table technologycase add constraint FK_technologycase_specialist foreign key (specialisId)
      references specialist (SPETid);

alter table userrolefun add constraint FK_USERROLE_USERROLEF_SYSFUN foreign key (SFUNid)
      references sysfun (SFUNid);

alter table userrolefun add constraint FK_USERROLE_USERROLEF_USERROLE foreign key (ROLEid)
      references userrole (ROLEid);

alter table wisdom add constraint FK_WISDOM_RELATIONS_READBOOK foreign key (REBOid)
      references readBook (REBOid);

