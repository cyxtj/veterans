/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2013-3-22 22:33:52                           */
/*==============================================================*/


drop table if exists MissionAlgor;

drop table if exists MissionPar;

drop table if exists accessory;

drop table if exists algorithm;

drop table if exists algorithmPar;

drop table if exists ancientBook;

drop table if exists ancientSpecialist;

drop table if exists background;

drop table if exists badInstance;

drop table if exists basicinformation;

drop table if exists bookResult;

drop table if exists cDisease;

drop table if exists caseAnalysis;

drop table if exists classicCase;

drop table if exists classicCaseDiagnosis;

drop table if exists continuingeducation;

drop table if exists dCase;

drop table if exists dMethod;

drop table if exists dTemplate;

drop table if exists dataSet;

drop table if exists diagExam;

drop table if exists diagItem;

drop table if exists diagRecipe;

drop table if exists diagSymptom;

drop table if exists diagnose;

drop table if exists district;

drop table if exists drug;

drop table if exists dtmpExamination;

drop table if exists dtmpSymptom;

drop table if exists examination;

drop table if exists feature;

drop table if exists fileinfo;

drop table if exists fixedrecipe;

drop table if exists fixedrecipeItem;

drop table if exists genre;

drop table if exists goodInstance;

drop table if exists inherit;

drop table if exists inheritStudy;

drop table if exists integratedSym;

drop table if exists learnMission;

drop table if exists literature;

drop table if exists mainBook;

drop table if exists mediaInfo;

drop table if exists message;

drop table if exists modernBook;

drop table if exists modernSpecialist;

drop table if exists newDTechnology;

drop table if exists operator;

drop table if exists operatorfun;

drop table if exists otherBook;

drop table if exists otherInformation;

drop table if exists paperResult;

drop table if exists patentResult;

drop table if exists pullulation;

drop table if exists readBook;

drop table if exists rediagnose;

drop table if exists researchItem;

drop table if exists resultReward;

drop table if exists science;

drop table if exists semiotic;

drop table if exists sourceTechnology;

drop table if exists specialist;

drop table if exists student;

drop table if exists studyRelation;

drop table if exists studyStory;

drop table if exists symptom;

drop table if exists syscode;

drop table if exists syscodeValue;

drop table if exists sysfun;

drop table if exists table1;

drop table if exists talentreward;

drop table if exists teachExperience;

drop table if exists teaching;

drop table if exists techCreative;

drop table if exists technologyapplication;

drop table if exists technologycase;

drop table if exists userrole;

drop table if exists userrolefun;

drop table if exists wDisease;

drop table if exists wisdom;

/*==============================================================*/
/* User: dbo                                                    */
/*==============================================================*/
create user dbo;

/*==============================================================*/
/* Table: MissionAlgor                                          */
/*==============================================================*/
create table MissionAlgor
(
   MIALid               varchar(36) not null,
   LEMIid               varchar(36),
   ALGOid               varchar(36),
   code                 varchar(30) not null,
   name                 varchar(50) not null,
   type                 tinyint not null,
   sequence             int not null,
   primary key (MIALid)
);

/*==============================================================*/
/* Table: MissionPar                                            */
/*==============================================================*/
create table MissionPar
(
   MIPAid               varchar(36) not null,
   MIALid               varchar(36),
   code                 varchar(50) not null,
   name                 varchar(50) not null,
   value                varchar(100) not null,
   illustration         varchar(200) not null default ' ',
   primary key (MIPAid)
);

/*==============================================================*/
/* Table: accessory                                             */
/*==============================================================*/
create table accessory
(
   ACCEid               varchar(36) not null,
   ownerid              varchar(36) not null,
   realFilename         varchar(100) not null default ' ',
   filename             varchar(100) not null default ' ',
   filetype             varchar(50) not null default ' ',
   path                 varchar(200) not null default ' ',
   illustration         text not null default ' ',
   createDay            datetime not null default '1900-1-1',
   optrid               varchar(36) not null default ' ',
   primary key (ACCEid)
);

/*==============================================================*/
/* Table: algorithm                                             */
/*==============================================================*/
create table algorithm
(
   ALGOid               varchar(36) not null,
   code                 varchar(30) not null,
   name                 varchar(50) not null,
   type                 tinyint not null,
   illustration         varchar(300) not null default ' ',
   primary key (ALGOid)
);

/*==============================================================*/
/* Table: algorithmPar                                          */
/*==============================================================*/
create table algorithmPar
(
   ALPAid               varchar(36) not null,
   ALGOid               varchar(36),
   code                 varchar(50) not null,
   name                 varchar(50) not null,
   value                varchar(100) not null,
   illustration         varchar(200) not null default ' ',
   primary key (ALPAid)
);

/*==============================================================*/
/* Table: ancientBook                                           */
/*==============================================================*/
create table ancientBook
(
   ANBOid               varchar(36) not null,
   REBOid               varchar(36),
   literature_name      varchar(20) not null default ' ',
   pubType              varchar(10) not null default ' ',
   benefit              varchar(100) not null default ' ',
   primary key (ANBOid)
);

/*==============================================================*/
/* Table: ancientSpecialist                                     */
/*==============================================================*/
create table ancientSpecialist
(
   ANSPid               varchar(36) not null,
   REBOid               varchar(36),
   name                 varchar(20) not null,
   major                varchar(100) not null,
   primary key (ANSPid)
);

/*==============================================================*/
/* Table: background                                            */
/*==============================================================*/
create table background
(
   BACKid               varchar(36) not null,
   STSTid               varchar(36),
   sport                varchar(300) not null,
   literature           varchar(300) not null,
   health               varchar(300) not null,
   tour                 varchar(300) not null,
   other_hobby          varchar(300) not null,
   smoke                varchar(300) not null,
   coffee               varchar(300) not null,
   alcohol              varchar(300) not null,
   tea                  varchar(300) not null,
   movie                varchar(300) not null,
   other_habit          varchar(300) not null,
   chinese              varchar(300) not null,
   philosophy           varchar(300) not null,
   art                  varchar(300) not null,
   custom               varchar(300) not null,
   belief               varchar(300) not null,
   other_culture        varchar(300) not null,
   other_experience     text not null default ' ',
   tiptop_duty          varchar(300) not null,
   years                varchar(10) not null,
   organization         varchar(300) not null,
   parttime_duty        varchar(300) not null,
   glory                varchar(300) not null,
   acquire_time         varchar(10) not null,
   primary key (BACKid)
);

/*==============================================================*/
/* Table: badInstance                                           */
/*==============================================================*/
create table badInstance
(
   BAINid               varchar(36) not null,
   REBOid               varchar(36),
   content              text not null default ' ',
   primary key (BAINid)
);

/*==============================================================*/
/* Table: basicinformation                                      */
/*==============================================================*/
create table basicinformation
(
   Num                  varchar(50) not null,
   Name                 varchar(50) not null,
   Gender               varchar(50) not null,
   Age                  varchar(50) not null,
   Diploma              varchar(50) not null,
   Dgree                varchar(50) not null,
   Rank                 varchar(50),
   PromotionTime        varchar(50),
   Duty                 text,
   HashId               varchar(36) not null,
   State                tinyint,
   SpecialisId          varchar(36),
   OperatorId           varchar(36),
   CreateDate           datetime,
   primary key (HashId)
);

/*==============================================================*/
/* Table: bookResult                                            */
/*==============================================================*/
create table bookResult
(
   Num                  varchar(50),
   Title                varchar(50),
   Author               varchar(50),
   AuthorAffiliation    varchar(50),
   Abstract             text,
   Source               varchar(50),
   Files                varchar(50),
   SpecialistId         varchar(36),
   OperatorId           varchar(36),
   HashId               varchar(36) not null,
   State                tinyint,
   primary key (HashId)
);

/*==============================================================*/
/* Table: cDisease                                              */
/*==============================================================*/
create table cDisease
(
   CDISid               varchar(36) not null,
   code                 varchar(20) not null,
   name                 varchar(100) not null,
   parentcode           varchar(20) not null,
   level                tinyint not null,
   isClassical          bool not null default 1,
   SPETid               varchar(36) not null default ' ',
   illustration         text not null default ' ',
   createDay            datetime not null default '1900-1-1',
   optrid               varchar(36) not null default ' ',
   state                tinyint not null default 0,
   primary key (CDISid),
   key AK_CDISEASE_PK_CODE_CDISEASE (code)
);

/*==============================================================*/
/* Table: caseAnalysis                                          */
/*==============================================================*/
create table caseAnalysis
(
   CAANid               varchar(36) not null,
   SPETid               varchar(36),
   CASEid               varchar(36) not null,
   diagnose_mode        tinyint not null default 0,
   diagnose_method      tinyint not null default 0,
   look_body            varchar(50) not null,
   illustration         text not null,
   tongue               tinyint not null default 0,
   tongue1              varchar(50) not null,
   look_place           varchar(50) not null,
   sound                varchar(50) not null,
   taste                varchar(50) not null,
   question_answer      varchar(200) not null,
   question_content     text not null,
   special_question     varchar(200) not null,
   feel_diagnose        varchar(200) not null,
   habit_dmethod        varchar(200) not null,
   important_question   varchar(500) not null,
   information_select   varchar(200) not null,
   analysis_way         varchar(500) not null,
   analysis_method      tinyint not null default 0,
   other_method         varchar(200) not null,
   analysis_evidence    varchar(200) not null,
   reason_evidence      varchar(200) not null,
   character_evidence   varchar(200) not null,
   place_evidence       varchar(200) not null,
   situation_evidence   varchar(200) not null,
   semiotics            varchar(50) not null,
   recipe_name          varchar(50) not null,
   produce_method       varchar(200) not null,
   takedrug_way         varchar(200) not null,
   doctor_advice        text not null,
   experience           varchar(500) not null,
   createDay            datetime not null default '1900-1-1',
   optrid               varchar(36) not null default ' ',
   state                tinyint not null default 0,
   primary key (CAANid)
);

/*==============================================================*/
/* Table: classicCase                                           */
/*==============================================================*/
create table classicCase
(
   clcaid               varchar(36) not null,
   operatorId           varchar(36),
   SPETid               varchar(36),
   state                tinyint,
   diagnosisNo          varchar(50),
   creatDate            datetime,
   num                  varchar(36) not null,
   title                varchar(50),
   source               tinyint,
   caseNum              varchar(50),
   name                 varchar(50),
   gender               varchar(50),
   birthday             varchar(50),
   people               varchar(50),
   job                  varchar(50),
   hometown             varchar(50),
   married              varchar(50),
   address              varchar(50),
   postcode             varchar(50),
   phone                varchar(50),
   presentIll           text,
   pastIll              text,
   familyIll            text,
   personalIll          text,
   visit                text,
   note                 text,
   remark               text,
   collectPerson        varchar(50),
   collectTime          varchar(50),
   verifyOpinion        text,
   verifyName           varchar(50),
   verifyTime           varchar(50),
   diagTime1            varchar(50),
   mainDisease1         text,
   caseAbstract1        text,
   zhengKeys1           text,
   westdisease1         varchar(50),
   tcmdisease1          varchar(50),
   tcmsyndrome1         varchar(50),
   therapy1             text,
   fangYao1             text,
   otherCure1           text,
   doctorAdvice1        text,
   efficacy1            varchar(50),
   diagTime2            varchar(50),
   mainDisease2         text,
   caseAbstract2        text,
   zhengKeys2           text,
   westdisease2         varchar(50),
   tcmdisease2          varchar(50),
   tcmsyndrome2         varchar(50),
   therapy2             text,
   fangYao2             text,
   otherCure2           text,
   doctorAdvice2        text,
   efficacy2            varchar(50),
   diagTime3            varchar(50),
   mainDisease3         text,
   caseAbstract3        text,
   zhengKeys3           text,
   westdisease3         varchar(50),
   tcmdisease3          varchar(50),
   tcmsyndrome3         varchar(50),
   therapy3             text,
   fangYao3             text,
   otherCure3           text,
   doctorAdvice3        text,
   efficacy3            varchar(50),
   diagTime4            varchar(50),
   mainDisease4         text,
   caseAbstract4        text,
   zhengKeys4           text,
   westdisease4         varchar(50),
   tcmdisease4          varchar(50),
   tcmsyndrome4         varchar(50),
   therapy4             text,
   fangYao4             text,
   otherCure4           text,
   doctorAdvice4        text,
   efficacy4            varchar(50),
   diagTime5            varchar(50),
   mainDisease5         text,
   caseAbstract5        text,
   zhengKeys5           text,
   westdisease5         varchar(50),
   tcmdisease5          varchar(50),
   tcmsyndrome5         varchar(50),
   therapy5             text,
   fangYao5             text,
   otherCure5           text,
   doctorAdvice5        text,
   efficacy5            varchar(50),
   diagTime6            varchar(50),
   mainDisease6         text,
   caseAbstract6        text,
   zhengKeys6           text,
   westdisease6         varchar(50),
   tcmdisease6          varchar(50),
   tcmsyndrome6         varchar(50),
   therapy6             text,
   fangYao6             text,
   otherCure6           text,
   doctorAdvice6        text,
   efficacy6            varchar(50),
   diagTime7            varchar(50),
   mainDisease7         text,
   caseAbstract7        text,
   zhengKeys7           text,
   westdisease7         varchar(50),
   tcmdisease7          varchar(50),
   tcmsyndrome7         varchar(50),
   therapy7             text,
   fangYao7             text,
   otherCure7           text,
   doctorAdvice7        text,
   efficacy7            varchar(50),
   diagTime8            varchar(50),
   mainDisease8         text,
   caseAbstract8        text,
   zhengKeys8           text,
   westdisease8         varchar(50),
   tcmdisease8          varchar(50),
   tcmsyndrome8         varchar(50),
   therapy8             text,
   fangYao8             text,
   otherCure8           text,
   doctorAdvice8        text,
   efficacy8            varchar(50),
   diagTime9            varchar(50),
   mainDisease9         text,
   caseAbstract9        text,
   zhengKeys9           text,
   westdisease9         varchar(50),
   tcmdisease9          varchar(50),
   tcmsyndrome9         varchar(50),
   therapy9             text,
   fangYao9             text,
   otherCure9           text,
   doctorAdvice9        text,
   efficacy9            varchar(50),
   diagTime10           varchar(50),
   mainDisease10        text,
   caseAbstract10       text,
   zhengKeys10          text,
   westdisease10        varchar(50),
   tcmdisease10         varchar(50),
   tcmsyndrome10        varchar(50),
   therapy10            text,
   fangYao10            text,
   otherCure10          text,
   doctorAdvice10       text,
   efficacy10           varchar(50),
   diagTime11           varchar(50),
   mainDisease11        text,
   caseAbstract11       text,
   zhengKeys11          text,
   westdisease11        varchar(50),
   tcmdisease11         varchar(50),
   tcmsyndrome11        varchar(50),
   therapy11            text,
   fangYao11            text,
   otherCure11          text,
   doctorAdvice11       text,
   efficacy11           varchar(50),
   diagTime12           varchar(50),
   mainDisease12        text,
   caseAbstract12       text,
   zhengKeys12          text,
   westdisease12        varchar(50),
   tcmdisease12         varchar(50),
   tcmsyndrome12        varchar(50),
   therapy12            text,
   fangYao12            text,
   otherCure12          text,
   doctorAdvice12       text,
   efficacy12           varchar(50),
   diagTime13           varchar(50),
   mainDisease13        text,
   caseAbstract13       text,
   zhengKeys13          text,
   westdisease13        varchar(50),
   tcmdisease13         varchar(50),
   tcmsyndrome13        varchar(50),
   therapy13            text,
   fangYao13            text,
   otherCure13          text,
   doctorAdvice13       text,
   efficacy13           varchar(50),
   diagTime14           varchar(50),
   mainDisease14        text,
   caseAbstract14       text,
   zhengKeys14          text,
   westdisease14        varchar(50),
   tcmdisease14         varchar(50),
   tcmsyndrome14        varchar(50),
   therapy14            text,
   fangYao14            text,
   otherCure14          text,
   doctorAdvice14       text,
   efficacy14           varchar(50),
   diagTime15           varchar(50),
   mainDisease15        text,
   caseAbstract15       text,
   zhengKeys15          text,
   westdisease15        varchar(50),
   tcmdisease15         varchar(50),
   tcmsyndrome15        varchar(50),
   therapy15            text,
   fangYao15            text,
   otherCure15          text,
   doctorAdvice15       text,
   efficacy15           varchar(50),
   diagTime16           varchar(50),
   mainDisease16        text,
   caseAbstract16       text,
   zhengKeys16          text,
   westdisease16        varchar(50),
   tcmdisease16         varchar(50),
   tcmsyndrome16        varchar(50),
   therapy16            text,
   fangYao16            text,
   otherCure16          text,
   doctorAdvice16       text,
   efficacy16           varchar(50),
   diagTime17           varchar(50),
   mainDisease17        text,
   caseAbstract17       text,
   zhengKeys17          text,
   westdisease17        varchar(50),
   tcmdisease17         varchar(50),
   tcmsyndrome17        varchar(50),
   therapy17            text,
   fangYao17            text,
   otherCure17          text,
   doctorAdvice17       text,
   efficacy17           varchar(50),
   diagTime18           varchar(50),
   mainDisease18        text,
   caseAbstract18       text,
   zhengKeys18          text,
   westdisease18        varchar(50),
   tcmdisease18         varchar(50),
   tcmsyndrome18        varchar(50),
   therapy18            text,
   fangYao18            text,
   otherCure18          text,
   doctorAdvice18       text,
   efficacy18           varchar(50),
   primary key (clcaid)
);

/*==============================================================*/
/* Table: classicCaseDiagnosis                                  */
/*==============================================================*/
create table classicCaseDiagnosis
(
   clcaid               varchar(36) not null,
   caseNum              varchar(50),
   diagnosisNum         varchar(50),
   diagTime             varchar(50),
   mainDisease          text,
   caseAbstract         text,
   zhengKeys            text,
   westdisease          varchar(50),
   tcmdisease           varchar(50),
   tcmsyndrome          varchar(50),
   therapy              text,
   fangYao              text,
   otherCure            text,
   doctorAdvice         text,
   efficacy             varchar(50),
   primary key (clcaid)
);

/*==============================================================*/
/* Table: continuingeducation                                   */
/*==============================================================*/
create table continuingeducation
(
   Participent          varchar(50),
   TrainingName         varchar(50),
   Category             varchar(50),
   TrainingDate         varchar(50),
   Hours                varchar(50),
   CreditHour           varchar(50),
   HashId               varchar(36) not null,
   SpecialisId          varchar(36),
   State                tinyint,
   OperatorId           varchar(36),
   CreateDate           datetime,
   primary key (HashId)
);

/*==============================================================*/
/* Table: dCase                                                 */
/*==============================================================*/
create table dCase
(
   CASEid               varchar(36) not null,
   SPETid               varchar(36) not null default ' ',
   DTMPid               varchar(36) not null default ' ',
   code                 varchar(20) not null,
   outpatientCode       varchar(20) not null,
   caseKind             smallint not null,
   name                 varchar(20) not null,
   age                  smallint not null,
   month                smallint not null default 0,
   gender               tinyint not null,
   nationality          tinyint not null,
   personSort           tinyint not null,
   afflication          varchar(200) not null default ' ',
   job                  varchar(20) not null default ' ',
   tel                  varchar(20) not null default ' ',
   address              varchar(200) not null default ' ',
   birthplace           varchar(6) not null,
   liveplace            varchar(6) not null,
   education            tinyint not null,
   marriage             tinyint not null,
   ohistory             text not null default ' ',
   phistory             text not null default ' ',
   fhistory             text not null default ' ',
   allergy              text not null default ' ',
   extraMed             varchar(500) not null default ' ',
   nhistory             text not null default ' ',
   mresult              tinyint not null,
   vresult              varchar(500) not null,
   illustration         text not null default ' ',
   state                tinyint not null default 0,
   createDay            datetime not null default '1900-1-1',
   optrid               varchar(36) not null default ' ',
   hasFile              bool not null default 0,
   preState             tinyint not null default 0,
   primary key (CASEid),
   check ([age] >= 0 and [age] <= 999)
);

/*==============================================================*/
/* Table: dMethod                                               */
/*==============================================================*/
create table dMethod
(
   DMETid               varchar(36) not null,
   code                 varchar(20) not null,
   name                 varchar(100) not null,
   parentcode           varchar(20) not null,
   level                tinyint not null,
   isClassical          bool not null default 1,
   SPETid               varchar(36) not null default ' ',
   illustration         text not null default ' ',
   createDay            datetime not null default '1900-1-1',
   optrid               varchar(36) not null default ' ',
   state                tinyint not null default 0,
   primary key (DMETid),
   key AK_DMETHOD_PK_CODE_DMETHOD (code)
);

/*==============================================================*/
/* Table: dTemplate                                             */
/*==============================================================*/
create table dTemplate
(
   DTMPid               varchar(36) not null,
   code                 varchar(20) not null,
   name                 varchar(200) not null,
   useClassCdis         bool not null default 0,
   useClassDmet         bool not null default 0,
   CDISid               varchar(36) not null default ' ',
   WDISid               varchar(36) not null default ' ',
   SEMCid               varchar(36) not null,
   DMETid               varchar(36) not null,
   takeWay              tinyint not null,
   drugForm             tinyint not null,
   SPETid               varchar(36) not null default ' ',
   illustration         text not null default ' ',
   createDay            datetime not null default '1900-1-1',
   optrid               varchar(36) not null default ' ',
   useClassWdis         bool not null default 0,
   state                tinyint not null default 0,
   primary key (DTMPid),
   key AK_DTEMPLATE_PK_CODE_DTEMPLAT (code)
);

/*==============================================================*/
/* Table: dataSet                                               */
/*==============================================================*/
create table dataSet
(
   DASEid               varchar(36) not null,
   DTMPid               varchar(36) not null,
   code                 varchar(20) not null,
   name                 varchar(50) not null,
   missionType          tinyint not null,
   sampleNum            int not null default 0,
   attributeNum         int not null default 0,
   state                tinyint not null default 0,
   createDay            datetime not null default '1900-1-1',
   optrid               varchar(36) not null default ' ',
   primary key (DASEid)
);

/*==============================================================*/
/* Table: diagExam                                              */
/*==============================================================*/
create table diagExam
(
   DIEXid               varchar(36) not null,
   DIAGid               varchar(36),
   EXAMid               varchar(36),
   value                varchar(200) not null default ' ',
   illustration         text not null default ' ',
   date                 datetime,
   sequence             int default 0,
   address              varchar(100),
   primary key (DIEXid)
);

/*==============================================================*/
/* Table: diagItem                                              */
/*==============================================================*/
create table diagItem
(
   DIITid               varchar(36) not null,
   DIREid               varchar(36),
   dru_DRUGid           varchar(36),
   DRUGid               varchar(36),
   quality              decimal(18,4) not null default 0,
   sequence             int not null default 0,
   illustration         text not null default ' ',
   primary key (DIITid)
);

/*==============================================================*/
/* Table: diagRecipe                                            */
/*==============================================================*/
create table diagRecipe
(
   DIREid               varchar(36) not null,
   DIAGid               varchar(36),
   FREPid               varchar(36),
   isCustomed           bool not null default 0,
   name                 varchar(36) not null default ' ',
   doctorAdvice         text not null default ' ',
   drugForm             tinyint not null,
   takeWay              tinyint not null,
   quality              smallint not null,
   produceMethod        varchar(100) not null,
   "usage"              varchar(100) not null,
   primary key (DIREid)
);

/*==============================================================*/
/* Table: diagSymptom                                           */
/*==============================================================*/
create table diagSymptom
(
   DISYid               varchar(36) not null,
   SYPMid               varchar(36),
   DIAGid               varchar(36),
   value                varchar(200) not null default ' ',
   illustration         text not null default ' ',
   sequence             int default 0,
   primary key (DISYid)
);

/*==============================================================*/
/* Table: diagnose                                              */
/*==============================================================*/
create table diagnose
(
   DIAGid               varchar(36) not null,
   CASEid               varchar(36),
   CDISid               varchar(36) not null default ' ',
   CDISid2              varchar(36) not null default ' ',
   WDISid               varchar(36) not null default ' ',
   WDISid2              varchar(36) not null default ' ',
   SEMCid               varchar(36) not null,
   SEMCid2              varchar(36) not null,
   SEMCid3              varchar(36) not null,
   DMETid               varchar(36) not null,
   DMETid2              varchar(36) not null,
   DMETid3              varchar(36) not null,
   DIAGno               tinyint not null default 1,
   DIAGnum              tinyint not null,
   DIAGday              datetime not null,
   lunarDay             varchar(50) not null default ' ',
   solarTerm            tinyint not null default 0,
   DIAway               tinyint not null default 0,
   majorSue             text not null,
   illustration         text not null default ' ',
   optrid               varchar(36) not null default ' ',
   createDay            datetime not null default '1900-1-1',
   westernMed           text not null default ' ',
   other                text not null default ' ',
   preSEMCid            varchar(36),
   primary key (DIAGid)
);

/*==============================================================*/
/* Table: district                                              */
/*==============================================================*/
create table district
(
   DISTid               varchar(36) not null,
   code                 varchar(20) not null,
   parentcode           varchar(20) not null,
   name                 varchar(50) not null,
   level                tinyint not null,
   py                   varchar(20) not null default ' ',
   wb                   varchar(20) not null default ' ',
   illustration         text not null default ' ',
   primary key (DISTid),
   key AK_DISTRICT_PK_CODE_DISTRICT (code)
);

/*==============================================================*/
/* Table: drug                                                  */
/*==============================================================*/
create table drug
(
   DRUGid               varchar(36) not null,
   code                 varchar(20) not null,
   name                 varchar(50) not null,
   unit                 varchar(10) not null,
   alias                varchar(100) not null default ' ',
   py                   varchar(20) not null default ' ',
   wb                   varchar(20) not null default ' ',
   isClassical          bool not null default 1,
   SPETid               varchar(36) not null default ' ',
   illustration         text not null default ' ',
   createDay            datetime not null default '1900-1-1',
   optrid               varchar(36) not null default ' ',
   state                tinyint not null default 0,
   primary key (DRUGid),
   key AK_DRUG_PK_CODE_DRUG (code)
);

/*==============================================================*/
/* Table: dtmpExamination                                       */
/*==============================================================*/
create table dtmpExamination
(
   DTEXid               varchar(36) not null,
   DTMPid               varchar(36),
   EXAMid               varchar(36),
   sequence             int not null,
   illustration         text not null,
   primary key (DTEXid)
);

/*==============================================================*/
/* Table: dtmpSymptom                                           */
/*==============================================================*/
create table dtmpSymptom
(
   DTSYid               varchar(36) not null,
   DTMPid               varchar(36),
   SYPMid               varchar(36),
   isFirst              bool not null default 1,
   sequence             int not null default 0,
   illustration         text not null default ' ',
   primary key (DTSYid)
);

/*==============================================================*/
/* Table: examination                                           */
/*==============================================================*/
create table examination
(
   EXAMid               varchar(36) not null,
   code                 varchar(20) not null,
   name                 varchar(100) not null,
   abbreviation         varchar(50) not null default ' ',
   kind                 tinyint not null default 0,
   normalValue          varchar(200) not null default ' ',
   hasFile              bool not null default 0,
   isClassical          bool not null default 1,
   SPETid               varchar(36) not null default ' ',
   illustration         text not null default ' ',
   createDay            datetime not null default '1900-1-1',
   optrid               varchar(36) not null default ' ',
   state                tinyint not null default 0,
   primary key (EXAMid),
   key AK_EXAMINATION_PK_COD_EXAMINAT (code)
);

/*==============================================================*/
/* Table: feature                                               */
/*==============================================================*/
create table feature
(
   FEATid               varchar(36) not null,
   DASEid               varchar(36),
   code                 varchar(20) not null,
   name                 varchar(50) not null,
   featType             tinyint not null,
   valSort              tinyint not null default 0,
   sequence             int not null,
   primary key (FEATid)
);

/*==============================================================*/
/* Table: fileinfo                                              */
/*==============================================================*/
create table fileinfo
(
   FIlEINFOid           varchar(36) not null,
   code                 varchar(20) not null,
   name                 varchar(50) not null,
   SPETid               varchar(36) not null,
   illustration         text not null default ' ',
   createDay            datetime not null,
   optrid               varchar(36) not null,
   state                tinyint not null,
   fileinfoType         tinyint not null,
   primary key (FIlEINFOid)
);

/*==============================================================*/
/* Table: fixedrecipe                                           */
/*==============================================================*/
create table fixedrecipe
(
   FREPid               varchar(36) not null,
   code                 varchar(20) not null,
   name                 varchar(50) not null,
   effect               varchar(200) not null default ' ',
   py                   varchar(20) not null default ' ',
   wb                   varchar(20) not null default ' ',
   isClassical          bool not null default 1,
   SPETid               varchar(36) not null default ' ',
   illustration         text not null default ' ',
   createDay            datetime not null default '1900-1-1',
   optrid               varchar(36) not null default ' ',
   state                tinyint not null default 0,
   primary key (FREPid),
   key AK_FIXEDRECIPE_PK_COD_FIXEDREC (code)
);

/*==============================================================*/
/* Table: fixedrecipeItem                                       */
/*==============================================================*/
create table fixedrecipeItem
(
   FRITid               varchar(36) not null,
   DRUGid               varchar(36),
   FREPid               varchar(36),
   quality              decimal(18,4) not null default 0,
   sequence             int not null default 0,
   illustration         text not null default ' ',
   primary key (FRITid)
);

/*==============================================================*/
/* Table: genre                                                 */
/*==============================================================*/
create table genre
(
   GENRid               varchar(36) not null,
   INSTid               varchar(36),
   main_specialist      varchar(20) not null default ' ',
   genre_name           varchar(20) not null default ' ',
   achievement          varchar(100) not null default ' ',
   primary key (GENRid)
);

/*==============================================================*/
/* Table: goodInstance                                          */
/*==============================================================*/
create table goodInstance
(
   GOINid               varchar(36) not null,
   REBOid               varchar(36),
   content              text not null default ' ',
   primary key (GOINid)
);

/*==============================================================*/
/* Table: inherit                                               */
/*==============================================================*/
create table inherit
(
   INHEid               varchar(36) not null,
   INSTid               varchar(36),
   name                 varchar(20) not null,
   start_date           varchar(16) not null default '1900-1-1',
   end_date             varchar(16) not null default '1900-1-1',
   theoretics           varchar(100) not null default ' ',
   introduction         text not null default ' ',
   key_factor           varchar(100) not null default ' ',
   primary key (INHEid)
);

/*==============================================================*/
/* Table: inheritStudy                                          */
/*==============================================================*/
create table inheritStudy
(
   INSTid               varchar(36) not null,
   SPETid               varchar(36),
   enlighten_teacher    varchar(20) not null,
   work_place           varchar(50) not null,
   major                varchar(50) not null,
   early_degree         text not null default ' ',
   textbook_type        tinyint not null,
   textbook             text not null default ' ',
   other_book           text not null default ' ',
   study_time           text not null default ' ',
   wisdom               text not null default ' ',
   aphorism             text not null default ' ',
   ideal                text not null default ' ',
   point                text not null default ' ',
   createDay            datetime not null default '1900-1-1',
   optrid               varchar(36) not null default ' ',
   state                tinyint not null default 0,
   primary key (INSTid)
);

/*==============================================================*/
/* Table: integratedSym                                         */
/*==============================================================*/
create table integratedSym
(
   INSYid               varchar(36) not null,
   SYPMid               varchar(36),
   name                 varchar(50) not null,
   valSort              int not null,
   sequence             int not null,
   primary key (INSYid)
);

/*==============================================================*/
/* Table: learnMission                                          */
/*==============================================================*/
create table learnMission
(
   LEMIid               varchar(36) not null,
   DASEid               varchar(36),
   DTMPid               varchar(36) not null,
   code                 varchar(20) not null,
   name                 varchar(50) not null,
   missionType          tinyint not null,
   testType             tinyint not null,
   testPar              decimal(4,1) not null,
   illustration         text not null default ' ',
   state                tinyint not null default 0,
   createDay            datetime not null default '1900-1-1',
   optrid               varchar(36) not null default ' ',
   primary key (LEMIid)
);

/*==============================================================*/
/* Table: literature                                            */
/*==============================================================*/
create table literature
(
   LITEid               varchar(36) not null,
   SCIEid               varchar(36),
   literature_name      varchar(20) not null default ' ',
   pubType              varchar(10) not null default ' ',
   publishing_date      varchar(16) not null default '1900-1-1',
   publishing_company   varchar(30) not null default ' ',
   paper                varchar(30) not null default ' ',
   magazine             varchar(30) not null default ' ',
   primary key (LITEid)
);

/*==============================================================*/
/* Table: mainBook                                              */
/*==============================================================*/
create table mainBook
(
   MABOid               varchar(36) not null,
   INSTid               varchar(36),
   literature_name      varchar(20) not null default ' ',
   pubType              varchar(10) not null default ' ',
   publishing_date      varchar(16) not null default '1900-1-1',
   edition              varchar(30) not null default ' ',
   publishing_company   varchar(30) not null default ' ',
   primary key (MABOid)
);

/*==============================================================*/
/* Table: mediaInfo                                             */
/*==============================================================*/
create table mediaInfo
(
   Num                  varchar(50),
   Name                 varchar(50),
   Category             varchar(50),
   Abs                  text,
   ProducedTime         varchar(50),
   Maker                varchar(50),
   FileName             varchar(50),
   Longth               varchar(50),
   DataFormat           varchar(50),
   SpecialistId         varchar(36),
   OperatorId           varchar(36),
   HashId               varchar(36) not null,
   State                tinyint,
   CreateDate           datetime,
   primary key (HashId)
);

/*==============================================================*/
/* Table: message                                               */
/*==============================================================*/
create table message
(
   MESGid               varchar(36) not null,
   title                varchar(100) not null,
   content              varchar(256) not null,
   sender               varchar(36) not null,
   receivor             varchar(36) not null,
   readed               bool not null,
   msgDate              datetime not null,
   sysMsg               bool not null,
   primary key (MESGid)
);

/*==============================================================*/
/* Table: modernBook                                            */
/*==============================================================*/
create table modernBook
(
   MOBOid               varchar(36) not null,
   REBOid               varchar(36),
   literature_name      varchar(20) not null default ' ',
   pubType              varchar(10) not null default ' ',
   benefit              varchar(100) not null default ' ',
   primary key (MOBOid)
);

/*==============================================================*/
/* Table: modernSpecialist                                      */
/*==============================================================*/
create table modernSpecialist
(
   MOSPid               varchar(36) not null,
   REBOid               varchar(36),
   name                 varchar(20) not null,
   isprofession         bool not null default 0,
   afflication          varchar(100) not null,
   major                varchar(100) not null,
   primary key (MOSPid)
);

/*==============================================================*/
/* Table: newDTechnology                                        */
/*==============================================================*/
create table newDTechnology
(
   OperatorId           varchar(36),
   Num                  varchar(50),
   Name                 varchar(50),
   Content              text,
   FormationTime        varchar(50),
   DevelopingPeople     varchar(50),
   Possessor            varchar(50),
   Bearer               varchar(50),
   DevelopmentAffiliation text,
   PossesionAffiliation text,
   ApplicationAffiliation text,
   ApplicationStartingTime varchar(50),
   Files                varchar(50),
   SpecialisId          varchar(36),
   HashId               varchar(36) not null,
   State                tinyint,
   CreateDate           datetime,
   primary key (HashId)
);

/*==============================================================*/
/* Table: operator                                              */
/*==============================================================*/
create table operator
(
   OPTRid               varchar(36) not null,
   ROLEid               varchar(36) not null,
   username             varchar(20) not null,
   password             varchar(100) not null,
   realname             varchar(20) not null,
   gender               tinyint not null default 0,
   part                 varchar(100) not null default ' ',
   SPETid               char(36) not null default ' ',
   illustration         text not null default ' ',
   insertLock           bool not null default 0,
   editLock             bool not null default 0,
   deleteLock           bool not null default 0,
   state                tinyint not null default 0,
   primary key (OPTRid),
   key AK_OPERATOR_PK_USERNA_OPERATOR (username)
);

/*==============================================================*/
/* Table: operatorfun                                           */
/*==============================================================*/
create table operatorfun
(
   OPTRid               varchar(36) not null,
   SFUNid               varchar(36) not null,
   primary key (OPTRid, SFUNid)
);

/*==============================================================*/
/* Table: otherBook                                             */
/*==============================================================*/
create table otherBook
(
   OTBOid               varchar(36) not null,
   BACKid               varchar(36),
   literature_name      varchar(20) not null default ' ',
   pubType              varchar(10) not null default ' ',
   benefit              varchar(100) not null default ' ',
   primary key (OTBOid)
);

/*==============================================================*/
/* Table: otherInformation                                      */
/*==============================================================*/
create table otherInformation
(
   OTINid               varchar(36) not null,
   INSTid               varchar(36),
   literature_name      varchar(20) not null default ' ',
   publishing_date      varchar(16) not null default '1900-1-1',
   edition              varchar(30) not null default ' ',
   publishing_company   varchar(30) not null default ' ',
   magazine             varchar(30) not null default ' ',
   entrepreneur         varchar(30) not null default ' ',
   primary key (OTINid)
);

/*==============================================================*/
/* Table: paperResult                                           */
/*==============================================================*/
create table paperResult
(
   num                  varchar(50),
   Title                varchar(150),
   Author               varchar(50),
   AuthorAffiliation    varchar(50),
   Abstract             text,
   Source               varchar(50),
   Files                varchar(50),
   SpeicalistId         varchar(36),
   OperatorId           varchar(36),
   HashId               varchar(36) not null,
   State                tinyint,
   CreateDate           datetime,
   primary key (HashId)
);

/*==============================================================*/
/* Table: patentResult                                          */
/*==============================================================*/
create table patentResult
(
   Num                  varchar(50),
   Name                 varchar(50),
   ApplicationNum       varchar(50),
   PatentNum            varchar(50),
   PatentMandate        varchar(50),
   Inventor             varchar(50),
   Patentee             varchar(50),
   Files                varchar(50),
   SpecialistId         varchar(36),
   OperatorId           varchar(36),
   HashId               varchar(36) not null,
   State                tinyint,
   createDate           datetime,
   primary key (HashId)
);

/*==============================================================*/
/* Table: pullulation                                           */
/*==============================================================*/
create table pullulation
(
   PULLid               varchar(36) not null,
   STSTid               varchar(36),
   famous_domain        varchar(100) not null default ' ',
   famous_date          datetime not null default '1900-1-1',
   famous_age           smallint not null,
   famous_reason        varchar(50) not null default ' ',
   famous_achievement   varchar(50) not null default ' ',
   revelation           varchar(50) not null default ' ',
   experience           text not null,
   aphorism             varchar(100) not null default ' ',
   advice               varchar(100) not null,
   credendum            varchar(100) not null,
   hope                 varchar(100) not null,
   other_advice         varchar(100) not null,
   all_clinic_time      smallint not null,
   old_clinic_time      smallint not null,
   last_clinic_time     smallint not null,
   clinic_regard        text not null default ' ',
   diagnose_custom      text not null default ' ',
   primary key (PULLid)
);

/*==============================================================*/
/* Table: readBook                                              */
/*==============================================================*/
create table readBook
(
   REBOid               varchar(36) not null,
   STSTid               varchar(36),
   sequence             varchar(300) not null,
   study_emphases       tinyint not null,
   emphases_reason      text not null,
   study_advice         tinyint not null,
   advice_reason        text not null,
   con_book             text not null,
   extensive_book       text not null,
   bad_book             text not null,
   classic_opinion      text not null,
   genre_attitude       text not null,
   relation_opinion     tinyint not null,
   opinion_reason       text not null,
   special_book         varchar(500) not null,
   ratio                varchar(100) not null,
   primary key (REBOid)
);

/*==============================================================*/
/* Table: rediagnose                                            */
/*==============================================================*/
create table rediagnose
(
   RDIAid               varchar(36) not null,
   CAANid               varchar(36),
   RDIAno               tinyint not null,
   disease_state        varchar(200) not null,
   tongue               tinyint not null default 0,
   tongue1              varchar(50) not null,
   artery               varchar(50) not null,
   other_artery         varchar(200) not null,
   rediagnose_analysis  text not null,
   primary key (RDIAid)
);

/*==============================================================*/
/* Table: researchItem                                          */
/*==============================================================*/
create table researchItem
(
   Name                 varchar(50),
   Leval                varchar(50),
   Princial             varchar(50),
   Participent          varchar(50),
   Affiliation          text,
   Duration             varchar(50),
   Source               text,
   Abstruct             varchar(50),
   HashId               varchar(36) not null,
   SpecialisId          varchar(36),
   State                tinyint,
   OperationId          varchar(36),
   Category             varchar(50),
   CreateDate           datetime,
   primary key (HashId)
);

/*==============================================================*/
/* Table: resultReward                                          */
/*==============================================================*/
create table resultReward
(
   Num                  varchar(50),
   ResultName           varchar(50),
   Author               varchar(50),
   AuthorAffiliation    varchar(50),
   RewardName           varchar(50),
   Leval                varchar(50),
   RewardDate           varchar(50),
   LicensingGroup       varchar(50),
   Files                varchar(50),
   SpecialistId         varchar(36),
   OperatorId           varchar(36),
   State                tinyint,
   HashId               varchar(36) not null,
   CreateDate           datetime,
   primary key (HashId)
);

/*==============================================================*/
/* Table: science                                               */
/*==============================================================*/
create table science
(
   SCIEid               varchar(36) not null,
   SPETid               varchar(36),
   recipe_description   text not null default ' ',
   drugs                text not null,
   technique            text not null default ' ',
   recipes              text not null default ' ',
   study_opinion        text not null default ' ',
   study_advice         text not null default ' ',
   reports              text not null default ' ',
   contents             text not null default ' ',
   reference            text not null default ' ',
   createDay            datetime not null default '1900-1-1',
   optrid               varchar(36) not null default ' ',
   state                tinyint not null default 0,
   primary key (SCIEid)
);

/*==============================================================*/
/* Table: semiotic                                              */
/*==============================================================*/
create table semiotic
(
   SEMCid               varchar(36) not null,
   CDISid               varchar(36),
   code                 varchar(20) not null,
   groupCode            varchar(20) not null default ' ',
   name                 varchar(100) not null,
   isClassical          bool not null default 1,
   SPETid               varchar(36) not null default ' ',
   illustration         text not null default ' ',
   createDay            datetime not null default '1900-1-1',
   optrid               varchar(36) not null default ' ',
   state                tinyint not null default 0,
   primary key (SEMCid),
   key AK_SEMIOTIC_PK_CODE_SEMIOTIC (code)
);

/*==============================================================*/
/* Table: sourceTechnology                                      */
/*==============================================================*/
create table sourceTechnology
(
   OperatorId           varchar(36),
   Num                  varchar(50),
   Name                 varchar(50),
   Content              text,
   FormationTime        varchar(50),
   Possessor            varchar(50),
   Bearer               varchar(50),
   PossetionAffiliation text,
   ApplicaionAffiliation text,
   Duration             varchar(50),
   Files                varchar(50),
   SpecialisId          varchar(36),
   HashId               varchar(36) not null,
   State                tinyint,
   CreateDate           datetime,
   primary key (HashId)
);

/*==============================================================*/
/* Table: specialist                                            */
/*==============================================================*/
create table specialist
(
   SPETid               varchar(36) not null,
   name                 varchar(20) not null,
   code                 varchar(20),
   birthday             datetime not null,
   nationality          tinyint not null,
   native_place         varchar(6) not null,
   gender               tinyint not null,
   afflication          varchar(100) not null,
   telephone            varchar(100) not null,
   address              varchar(100) not null,
   postalcode           varchar(20) not null,
   status               varchar(100) not null,
   principalship        varchar(100) not null,
   major                varchar(100) not null,
   social_status        text not null,
   school_degree        varchar(100) not null,
   school               varchar(100) not null,
   graduation_date      datetime not null,
   other_degree         varchar(100) not null,
   learning_date        datetime not null,
   work_date            datetime not null,
   motivation           varchar(100) not null,
   mode                 varchar(100) not null,
   resume               text not null,
   contribution         text not null,
   health_info          varchar(50) not null,
   clinic_info          varchar(50) not null,
   reseach_disease      text not null,
   recips               text not null,
   drugs                text not null,
   optrid               varchar(36) not null default ' ',
   state                tinyint not null default 0,
   createDay            datetime not null default '1900-1-1',
   primary key (SPETid)
);

/*==============================================================*/
/* Table: student                                               */
/*==============================================================*/
create table student
(
   STUDid               varchar(36) not null,
   TEEXid               varchar(36),
   name                 varchar(20) not null,
   years                varchar(20) not null default ' ',
   major                varchar(100) not null,
   domain               varchar(30) not null default ' ',
   achievement          varchar(100) not null default ' ',
   primary key (STUDid)
);

/*==============================================================*/
/* Table: studyRelation                                         */
/*==============================================================*/
create table studyRelation
(
   STRLid               varchar(36) not null,
   PULLid               varchar(36),
   name                 varchar(20) not null,
   afflication          varchar(100) not null,
   reason               varchar(100) not null default ' ',
   primary key (STRLid)
);

/*==============================================================*/
/* Table: studyStory                                            */
/*==============================================================*/
create table studyStory
(
   STSTid               varchar(36) not null,
   SPETid               varchar(36),
   study_start_date     datetime not null,
   start_age            smallint not null default 0,
   read_day             smallint not null default 0,
   read_week            smallint not null default 0,
   practice_day         smallint not null default 0,
   practice_week        smallint not null default 0,
   study_end_date       datetime not null,
   end_age              smallint not null default 0,
   matter_type          tinyint not null,
   matter               text not null default ' ',
   work_start_date      datetime not null,
   work_age             smallint not null default 0,
   clinic_day           smallint not null default 0,
   clinic_week          smallint not null default 0,
   study_day            smallint not null default 0,
   study_week           smallint not null default 0,
   clinic_years         smallint not null default 0,
   root_years           smallint not null default 0,
   root_place           varchar(50) not null,
   work_start           varchar(20) not null,
   work_middle          varchar(20) not null,
   work_end             varchar(20) not null,
   work_mode            varchar(50) not null,
   study_key            varchar(50) not null default ' ',
   other_situation      text not null default ' ',
   createDay            datetime not null default '1900-1-1',
   optrid               varchar(36) not null default ' ',
   state                tinyint not null default 0,
   primary key (STSTid)
);

/*==============================================================*/
/* Table: symptom                                               */
/*==============================================================*/
create table symptom
(
   SYPMid               varchar(36) not null,
   code                 varchar(20) not null,
   name                 varchar(50) not null,
   parentcode           varchar(20) not null,
   level                tinyint not null,
   kind                 tinyint not null default 0,
   sort                 tinyint not null default 1,
   valSort              int not null default 0,
   hasFile              bool not null default 0,
   isClassical          bool not null default 1,
   SPETid               varchar(36) not null default ' ',
   illustration         text not null default ' ',
   createDay            datetime not null default '1900-1-1',
   optrid               varchar(36) not null default ' ',
   state                tinyint not null default 0,
   primary key (SYPMid),
   key AK_SYMPTOM_PK_CODE_SYMPTOM (code)
);

/*==============================================================*/
/* Table: syscode                                               */
/*==============================================================*/
create table syscode
(
   CODEid               varchar(36) not null,
   no                   int not null,
   code                 varchar(20) not null,
   name                 varchar(50) not null default ' ',
   illustration         text not null default ' ',
   primary key (CODEid),
   key AK_SYSCODE_PK_CODE_SYSCODE (code),
   key AK_SYSCODE_PK_NO_SYSCODE (no)
);

/*==============================================================*/
/* Table: syscodeValue                                          */
/*==============================================================*/
create table syscodeValue
(
   SVALid               varchar(36) not null,
   CODEid               varchar(36) not null default ' ',
   subno                int not null,
   subcode              varchar(20) not null,
   truevalue            varchar(100),
   py                   varchar(20) default ' ',
   wb                   varchar(20) default ' ',
   illustration         text default ' ',
   primary key (SVALid)
);

/*==============================================================*/
/* Table: sysfun                                                */
/*==============================================================*/
create table sysfun
(
   SFUNid               varchar(36) not null,
   code                 varchar(20) not null,
   parentcode           varchar(20) not null default '-1',
   level                tinyint not null,
   name                 varchar(100) not null,
   href                 varchar(200) not null default ' ',
   targetFrame          varchar(100) not null default ' ',
   illustration         text not null default ' ',
   state                tinyint not null default 0,
   primary key (SFUNid),
   key AK_SYSFUN_PK_CODE_SYSFUN (code)
);

/*==============================================================*/
/* Table: table1                                                */
/*==============================================================*/
create table table1
(
   id                   char(10) not null,
   name                 char(10),
   primary key (id)
);

/*==============================================================*/
/* Table: talentreward                                          */
/*==============================================================*/
create table talentreward
(
   OperatorId           varchar(36),
   Name                 varchar(50),
   Category             varchar(50),
   Leval                varchar(50),
   Principal            varchar(50),
   Participent          varchar(50),
   Affiliation          text,
   StaringTime          varchar(50),
   Source               text,
   Absturct             text,
   SpecialisId          varchar(36),
   HashId               varchar(36) not null,
   State                tinyint,
   CreateDate           datetime,
   primary key (HashId)
);

/*==============================================================*/
/* Table: teachExperience                                       */
/*==============================================================*/
create table teachExperience
(
   TEEXid               varchar(36) not null,
   STSTid               varchar(36),
   study_gist           varchar(300) not null,
   clinic_gist          varchar(300) not null,
   interaction_gist     varchar(300) not null,
   other_gist           varchar(300) not null,
   schoolage_request    varchar(300) not null,
   knowledge_request    varchar(300) not null,
   moral_request        varchar(300) not null,
   other_request        varchar(300) not null,
   school_opinion       text not null,
   course_ratio         varchar(300) not null,
   "period _ratio"      varchar(300) not null,
   textbook             text not null,
   inherit_mode         text not null,
   teach_opinion        text not null,
   combine_opinion      text not null,
   system_opinion       text not null,
   department_opinion   text not null,
   research_opinion     text not null,
   support_opinion      text not null,
   primary key (TEEXid)
);

/*==============================================================*/
/* Table: teaching                                              */
/*==============================================================*/
create table teaching
(
   TEACid               varchar(36) not null,
   PULLid               varchar(36),
   start_date           varchar(16) not null default '1900-1-1',
   end_date             varchar(16) not null default '1900-1-1',
   teach_place          varchar(100) not null default ' ',
   major                varchar(100) not null,
   primary key (TEACid)
);

/*==============================================================*/
/* Table: techCreative                                          */
/*==============================================================*/
create table techCreative
(
   Num                  varchar(50),
   Name                 text,
   Conent               text,
   FormationTime        varchar(50),
   Author               varchar(50),
   Files                varchar(50),
   HashId               varchar(36) not null,
   State                tinyint,
   SpecialisId          varchar(36),
   CreateDate           datetime,
   OperatorId           varchar(36),
   primary key (HashId)
);

/*==============================================================*/
/* Table: technologyapplication                                 */
/*==============================================================*/
create table technologyapplication
(
   OperatorId           varchar(36),
   Num                  varchar(50),
   Name                 varchar(50),
   Disease              varchar(50),
   Department           varchar(50),
   Author               varchar(50),
   Affiliation          text,
   Percentage           varchar(50),
   Beneficiary          text,
   EfficacyAssement     text,
   HealthEconomics      text,
   SpecialisId          varchar(36),
   HashId               varchar(36) not null,
   State                tinyint,
   CreateDate           datetime,
   primary key (HashId)
);

/*==============================================================*/
/* Table: technologycase                                        */
/*==============================================================*/
create table technologycase
(
   OperatorId           varchar(36),
   Num                  varchar(50),
   Name                 varchar(50),
   Possessor            varchar(50),
   PossesstionAffilation varchar(50),
   specialisId          varchar(36),
   HashId               varchar(36) not null,
   State                tinyint,
   CreateDate           datetime,
   primary key (HashId)
);

/*==============================================================*/
/* Table: userrole                                              */
/*==============================================================*/
create table userrole
(
   ROLEid               varchar(36) not null,
   code                 varchar(20) not null,
   name                 varchar(100) not null,
   illustration         text not null default ' ',
   state                tinyint not null default 0,
   primary key (ROLEid),
   key AK_USERROLE_PK_CODE_USERROLE (code)
);

/*==============================================================*/
/* Table: userrolefun                                           */
/*==============================================================*/
create table userrolefun
(
   ROLEid               varchar(36) not null,
   SFUNid               varchar(36) not null,
   primary key (ROLEid, SFUNid)
);

/*==============================================================*/
/* Table: wDisease                                              */
/*==============================================================*/
create table wDisease
(
   WDISid               varchar(36) not null,
   code                 varchar(20) not null,
   name                 varchar(100) not null,
   parentcode           varchar(20) not null,
   level                tinyint not null,
   isClassical          bool not null default 1,
   SPETid               varchar(36) not null default ' ',
   illustration         text not null default ' ',
   createDay            datetime not null default '1900-1-1',
   optrid               varchar(36) not null default ' ',
   state                tinyint not null default 0,
   primary key (WDISid),
   key AK_WDISEASE_PK_CODE_WDISEASE (code)
);

/*==============================================================*/
/* Table: wisdom                                                */
/*==============================================================*/
create table wisdom
(
   WISDid               varchar(36) not null,
   REBOid               varchar(36),
   content              text not null default ' ',
   primary key (WISDid)
);

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

