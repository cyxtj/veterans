#关于init__
class a:
    写出def __init__(self):
            abc = db.column(asdfa)

class b: 
    把上面的abc = db.column()拷到temp里加工成一行再放到
        def __init__(self, abc):

class c:
    把def __init__(self, abc):
            abc = db.column(asdfa)
    变成
    def __init__(self, abc):
            self.abc = abc
#关于建class
class d:
    加primary_key

class e: 
    加foreign_key

#关于将sqlserver产生的脚本.sql变成python脚本
class f:
    INSERT [dbo][ddd]([GENRid], [INSTid], [main_specialist], [genre_name], [achievement]) VALUES (N'2f2e5cb8-eedd-4d2c-b7ad-d671de752e59', N'50bc9036-4277-48bf-b835-681f47ccb730', N'叶天士', N'', N'')
    变成
    INSERT ([GENRid], [INSTid], [main_specialist], [genre_name], [achievement]) VALUES (N'2f2e5cb8-eedd-4d2c-b7ad-d671de752e59', N'50bc9036-4277-48bf-b835-681f47ccb730', N'叶天士', N'', N'')

class i:
    f 之后到下一行

之后自己手工去掉N''
    :%s/N'/'/g
    INSERT ([GENRid], [INSTid], [main_specialist], [genre_name], [achievement]) VALUES ('2f2e5cb8-eedd-4d2c-b7ad-d671de752e59', '50bc9036-4277-48bf-b835-681f47ccb730', '叶天士', '', '')

class g不需要(是中间步骤）: 
    INSERT ([GENRid], [INSTid], [main_specialist], [genre_name], [achievement]) VALUES ('2f2e5cb8-eedd-4d2c-b7ad-d671de752e59', '50bc9036-4277-48bf-b835-681f47ccb730', '叶天士', '', '')
    变成
    INSERT (GENRid='2f2e5cb8-eedd-4d2c-b7ad-d671de752e59', , [INSTid], [main_specialist], [genre_name], [achievement]) VALUES ('50bc9036-4277-48bf-b835-681f47ccb730', '叶天士', '', '')

class h:
    def 注意要在最后的）前加个，变成，）
    重复x遍g把
    INSERT ([GENRid], [INSTid], [main_specialist], [genre_name], [achievement]) VALUES ('2f2e5cb8-eedd-4d2c-b7ad-d671de752e59', '50bc9036-4277-48bf-b835-681f47ccb730', '叶天士', '', '')
    变成
    INSERT (GENRid:'2f2e5cb8-eedd-4d2c-b7ad-d671de752e59', INSTid:'50bc9036-4277-48bf-b835-681f47ccb730', main_specialist:'叶天士', genre_name:'', achievement:'') VALUES (, , , , )
    光标移到下一行
    n@h

#关于把sqlserver查询到的数据.csv变成.py
class j
    手工：
        先在每行前加‘#’
        去掉第一行的#
    q：
        把第一行复制到第一个没有#的行的上一行
        去掉该行的#标记
        光标回到gg
    n@j

    手工：
        去掉第一行多余的行
        在属性和数据上加''
        行末加，
        光标在第一行
        
class k
    q：
        把一个数据从第二行插入到第一行适当位置


class l
    q:
        光标移到行首
        n次
            @k
        做好一行
        光标移到下一行
class m
    把data_drug.csv变成.py
    开两个窗口
        在属性和数据上加''
        行末加，
        光标在第一行

class n
    在temp窗口返回原窗口，剪切一个数据后粘贴到现在光标之后

class o
    n@n --> o
    n@o
    把data_fixedrecipe.csv 变成.py


class p
    n@n --> p
    n@p
    把data_fixedrecipeItem.csv 变成.py

