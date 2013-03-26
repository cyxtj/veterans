
/****** Object:  Table [dbo].[genre]    Script Date: 03/24/2013 20:04:21 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[genre](
	[GENRid] [varchar](36) NOT NULL,
	[INSTid] [varchar](36) NULL,
	[main_specialist] [varchar](20) NOT NULL,
	[genre_name] [varchar](20) NOT NULL,
	[achievement] [varchar](100) NOT NULL,
 CONSTRAINT [PK_GENRE] PRIMARY KEY NONCLUSTERED 
(
	[GENRid] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
SET ANSI_PADDING OFF
GO
INSERT [dbo].[genre] ([GENRid], [INSTid], [main_specialist], [genre_name], [achievement]) VALUES (N'2f2e5cb8-eedd-4d2c-b7ad-d671de752e59', N'50bc9036-4277-48bf-b835-681f47ccb730', N'叶天士', N'', N'')
INSERT [dbo].[genre] ([GENRid], [INSTid], [main_specialist], [genre_name], [achievement]) VALUES (N'27ed5b68-ba98-4958-b557-fbbee556524d', N'50bc9036-4277-48bf-b835-681f47ccb730', N'刘河间', N'', N'')
INSERT [dbo].[genre] ([GENRid], [INSTid], [main_specialist], [genre_name], [achievement]) VALUES (N'b7f9e3eb-45db-47fd-9364-a9f5ff0aa6df', N'b0798623-ee9b-407b-a908-7fe375c8b2b3', N'张仲景', N'伤寒派', N'树立辨证论治的思想及系统中医内科学')
INSERT [dbo].[genre] ([GENRid], [INSTid], [main_specialist], [genre_name], [achievement]) VALUES (N'9e46529d-4650-4acc-9633-436f905893d3', N'b0798623-ee9b-407b-a908-7fe375c8b2b3', N'王清任', N'活血派', N'发扬了活血化瘀的理论和实践')
INSERT [dbo].[genre] ([GENRid], [INSTid], [main_specialist], [genre_name], [achievement]) VALUES (N'53a40d31-d0f0-46e6-85fa-9e86acd94b17', N'4fc85585-40fd-4373-85c9-a7d6c1f3a76d', N'张仲景', N'孟河派', N'擅长内科杂病')
INSERT [dbo].[genre] ([GENRid], [INSTid], [main_specialist], [genre_name], [achievement]) VALUES (N'8aa570ad-8943-4d6b-bbd2-b57fad066f4e', N'6a2b8135-b25e-4be1-bbef-7a506a9f8f3c', N'陈书森', N'孟河学派', N'')
