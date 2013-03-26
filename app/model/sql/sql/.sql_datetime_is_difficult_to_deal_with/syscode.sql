
/****** Object:  Table [dbo].[syscode]    Script Date: 03/24/2013 20:04:21 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[syscode](
	[CODEid] [varchar](36) NOT NULL,
	[no] [int] NOT NULL,
	[code] [varchar](20) NOT NULL,
	[name] [varchar](50) NOT NULL,
	[illustration] [text] NOT NULL,
 CONSTRAINT [PK_SYSCODE] PRIMARY KEY NONCLUSTERED 
(
	[CODEid] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY],
 CONSTRAINT [AK_SYSCODE_PK_CODE_SYSCODE] UNIQUE NONCLUSTERED 
(
	[code] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY],
 CONSTRAINT [AK_SYSCODE_PK_NO_SYSCODE] UNIQUE NONCLUSTERED 
(
	[no] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
SET ANSI_PADDING OFF
GO
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'a13b1c0a-8539-47a9-b93b-34f8a854158f', 1, N'00001', N'性别', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'd0bec375-20c1-44d5-afc1-eb223dd616c6', 2, N'00002', N'民族', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'49757835-5bad-47ea-ada8-684cd715da2f', 3, N'00003', N'婚姻状况', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'266a1993-4dbc-4d99-8fa9-96ea877b9edc', 4, N'00004', N'文化程度', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'51866b47-3255-47ad-ac5d-c933e5c21331', 5, N'00005', N'医案性质', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'71193868-5fb4-4f30-8ba0-84ec6b2018b3', 6, N'00006', N'节气', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'19dd1cd0-78a1-44b3-959a-6c7eb57c770d', 7, N'00007', N'给药途径', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'46f0ce34-bf95-495f-9376-2dfd4fb8c9ba', 8, N'00008', N'剂型 ', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'46f0ce34-bf95-4s5f-9376-2dad4fb8c9ba', 9, N'00009', N'是否', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'26f0ae34-ba95-4s5f-9376-2dad4fb8c9ba', 10, N'00010', N'审核状态', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'26f0ae34-0095-4s5f-9376-2dad4fb8c9ba', 11, N'00011', N'症状种类', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'51866b47-3255-47ad-ac5d-c933e5c21333', 12, N'00012', N'取值类型', N'′ó1?aê?￡?2??ü???ˉ?￡')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'dd280210-c930-4777-9394-659d9ba55059', 13, N'00013', N'检查种类', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'fe1162a1-d9ae-4395-b224-3de37783768b', 14, N'00014', N'应诊方式', N'ó|??·?ê?°üà¨￡o?????￠ 2é·??￠?á???￠ ?????￠ ó????￠ ????')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'7113a2d9-1333-4fb1-8e05-e042d799de96', 15, N'00015', N'人员类别', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'2f91b952-d5e6-4cc6-9b9d-0cbea352aaa0', 16, N'00016', N'就诊序列', N'3???￡??′??￡?èy??...')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'64757fef-981d-4ca6-840a-bc249cfa505b', 17, N'00017', N'治疗结果', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'ea4fae73-65a8-47a6-b2ca-196fc7fca991', 18, N'00018', N'应诊方法', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'a8ae1e16-69f1-4002-a9d0-bf75cf1a5a97', 19, N'00019', N'辨证方法', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'5bd60939-0f1b-4b48-ac75-966c5e69a9cd', 20, N'00020', N'学医动机', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'8917c348-f244-4afe-bd15-50fcf66a5179', 21, N'00021', N'学医形式', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'71bb69ab-e7d3-4522-8ed5-dcce589ba696', 22, N'00022', N'学习资料类型', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'3f2208ce-38b4-4048-b3e1-da60254eb391', 29, N'00029', N'中医书籍', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'8a2d0595-f492-4a5c-aab2-8b9dbddad14f', 30, N'00030', N'学习中医书籍的关键', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'a7ec7943-2af7-4279-9b78-e9f7d3bd296d', 31, N'00031', N'精度与泛读处理', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'e2300a86-270f-474f-b95b-5b9ff45fe8b5', 32, N'00032', N'中医知识与学习西医知识的关系', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'960283f8-dce6-4e20-8c75-4d24ee2c7ed6', 33, N'00033', N'学习任务类型', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'36eecede-75ea-4a96-bfa8-432a4a1e8a22', 34, N'00034', N'字段类型', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'0d0c5ea9-da2e-4860-9dde-05f8215c84a5', 35, N'00035', N'数据集状态', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'6c421db6-a349-4b20-a34e-911d1eb91fd2', 36, N'00036', N'算法类别', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'4b91b17d-fec8-41f0-8448-4c7cff026e41', 37, N'00037', N'测试类型', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'fbd5f630-5308-4c00-9a75-be15269ccc6c', 38, N'00038', N'学习任务状态', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'8b6bc2ed-0209-4a7a-8725-b567f02767cf', 39, N'00039', N'统计类型', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'80e5858c-09e0-478f-9dc6-084f3aba45db', 23, N'00023', N'开悟事件类型', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'3addf0a5-fbb2-45a9-8b02-7e702691a652', 25, N'00025', N'成名领域', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'0603a2da-f024-46d6-90fc-381754d3f27a', 28, N'00028', N'成名启示', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'87597f21-be29-4758-ad34-980c7bc23d1e', 24, N'00024', N'学医关键', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'1499d654-7040-4f26-bd86-21fc2505dc19', 26, N'00026', N'成名原因', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'd5df8511-42cb-477d-88f2-c5a044fa0e07', 27, N'00027', N'成名业绩', N' ')
INSERT [dbo].[syscode] ([CODEid], [no], [code], [name], [illustration]) VALUES (N'80e0ef29-079e-4e67-9cf5-ed288886be68', 40, N'00040', N'文档类型', N'')
