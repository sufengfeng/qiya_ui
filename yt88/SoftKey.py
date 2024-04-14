# -- coding: utf-8 --
import platform
from datetime import datetime
import random
from ctypes import *

if 'Windows' in platform.system():
    if "32bit" in platform.architecture():
        Psyuunew=windll.LoadLibrary('Syunew3D.dll')
    else:
        Psyuunew=windll.LoadLibrary('Syunew3D_x64.dll')
else:
    if "32bit" in platform.architecture():
        Psyuunew=windll.LoadLibrary('libPsyunew3.so')
    else:
       Psyuunew=cdll.LoadLibrary('libPsyunew3_64.so')         

##获到锁的版本
NT_GetIDVersion=Psyuunew.NT_GetIDVersion
NT_GetIDVersion.argtypes=(c_void_p,c_char_p)
NT_GetIDVersion.restypes=(c_int)


##获取锁的扩展版本
NT_GetVersionEx=Psyuunew.NT_GetVersionEx
NT_GetVersionEx.argtypes=(c_void_p,c_char_p)
NT_GetVersionEx.restypes=(c_int)


##算法函数
sWrite_2Ex=Psyuunew.sWrite_2Ex  
sWrite_2Ex.argtypes=(c_ulong ,c_void_p,c_char_p)
sWrite_2Ex.restypes=(c_int)

sWriteEx=Psyuunew.sWriteEx  
sWriteEx.argtypes=(c_ulong ,c_void_p,c_char_p)
sWriteEx.restypes=(c_int)

sRead=Psyuunew.sRead  
sRead.argtypes=(c_void_p,c_char_p)
sRead.restypes=(c_int)

sWrite_2=Psyuunew.sWrite  
sWrite_2.argtypes=(c_ulong ,c_char_p)
sWrite_2.restypes=(c_int)

sWrite_2=Psyuunew.sWrite_2  
Psyuunew.argtypes=(c_ulong ,c_char_p)
sWrite_2.restypes=(c_int)
##算法函数

##写一个字节到加密锁中
YWrite=Psyuunew.YWrite
YWrite.argtypes=(c_byte ,c_short,c_char_p ,c_char_p,c_char_p )
YWrite.restypes=(c_int)

##从加密锁中读取一个字??
YRead=Psyuunew.YRead
YRead.argtypes=(c_void_p,c_short,c_char_p ,c_char_p,c_char_p )
YRead.restypes=(c_int)

##写一个字节到加密锁中
YWriteEx=Psyuunew.YWriteEx
YWriteEx.argtypes=(c_void_p,c_short,c_short,c_char_p,c_char_p,c_char_p )
YWriteEx.restypes=(c_int)

##从加密锁中读取一批字??
YReadEx=Psyuunew.YReadEx
YReadEx.argtypes=(c_void_p,c_short,c_short,c_char_p,c_char_p,c_char_p )
YReadEx.restypes=(c_int)

##查找指定的加密锁（使得普通算法一??
FindPort_2=Psyuunew.FindPort_2  
FindPort_2.argtypes=(c_int ,c_ulong ,c_ulong ,c_char_p)
FindPort_2.restypes=(c_int)

##查找加密??
FindPort=Psyuunew.FindPort  
FindPort.argtypes=(c_int ,c_char_p)
FindPort.restypes=(c_int)

##获取锁的ID
GetID=Psyuunew.GetID  
GetID.argtypes=(c_void_p,c_void_p,c_char_p)
GetID.restypes=(c_int)

##从加密锁中读字符??
YReadString=Psyuunew.YReadString 
YReadString.argtypes=(c_char_p ,c_short,c_int ,c_char_p ,c_char_p,c_char_p)
YReadString.restypes=(c_int)

##写字符串到加密锁??
YWriteString=Psyuunew.YWriteString
YWriteString.argtypes=(c_char_p,c_short,c_char_p ,c_char_p,c_char_p )
YWriteString.restypes=(c_int)

##设置写密??
SetWritePassword=Psyuunew.SetWritePassword
SetWritePassword.argtypes=(c_char_p ,c_char_p,c_char_p ,c_char_p,c_char_p)
SetWritePassword.restypes=(c_int)

##设置读密??
SetReadPassword=Psyuunew.SetReadPassword
SetReadPassword.argtypes=(c_char_p ,c_char_p,c_char_p ,c_char_p,c_char_p)
SetReadPassword.restypes=(c_int)

##设置增强算法密钥一
SetCal_2=Psyuunew.SetCal_2
SetCal_2.argtypes=(c_char_p,c_char_p)
SetCal_2.restypes=(c_int)

##使用增强算法一对字符串进行加密
EncString=Psyuunew.EncString  
EncString.argtypes=(c_char_p,c_char_p,c_char_p)
EncString.restypes=(c_int)

##使用增强算法一对二进制数据进行加密
Cal=Psyuunew.Cal  
Cal.argtypes=(c_void_p,c_void_p,c_char_p)
Cal.restypes=(c_int)

##设置增强算法密钥??
SetCal_New=Psyuunew.SetCal_New
SetCal_New.argtypes=(c_char_p,c_char_p)
SetCal_New.restypes=(c_int)

##使用增强算法二对字符串进行加??
Cal_New=Psyuunew.Cal_New  
Cal_New.argtypes=(c_void_p,c_void_p,c_char_p)
Cal_New.restypes=(c_int)

##使用增强算法二对字符串进行加??
EncString_New=Psyuunew.EncString_New  
EncString_New.argtypes=(c_char_p,c_char_p,c_char_p)
EncString_New.restypes=(c_int)

##返回锁的出厂编码
GetProduceDate=Psyuunew.GetProduceDate  
GetProduceDate.argtypes=(c_char_p,c_char_p)
GetProduceDate.restypes=(c_int)

##设置ID种子
SetID=Psyuunew.SetID
SetID.argtypes=(c_char_p ,c_char_p)
SetID.restypes=(c_int)

##设置普通算??
SetCal=Psyuunew.SetCal
SetCal.argtypes=(c_char_p ,c_char_p,c_char_p ,c_char_p,c_char_p)
SetCal.restypes=(c_int)

##生产日期转换函数
##SnToProduceDate=Psyuunew.SnToProduceDate
##SnToProduceDate.argtypes=(c_char_p ,c_char_p )
##SnToProduceDate.restypes=(c_void)

##使用增强算法对字符串进行解密使用软件
##StrDec=Psyuunew.StrDec
##StrDec.argtypes=(c_char_p,c_char_p,c_char_p)
##StrDec.restypes=(c_void )
##
##StrEnc=Psyuunew.StrEnc  
##StrEnc.argtypes=(c_char_p,c_char_p,c_char_p)
##StrEnc.restypes=(c_void)
##
##EnCode=Psyuunew.EnCode    
##EnCode.argtypes=(c_void_p ,c_void_p ,  c_char_p )
##EnCode.restypes=(c_void)
##
##DeCode=Psyuunew.DeCode   
##DeCode.argtypes=(c_void_p , c_void_p , c_char_p  )
##DeCode.restypes=(c_void)
##使用增强算法对字符串进行解密使用软件)


##使用增强算法对二进制数据进行加密使用软件)
##DecBySoft=Psyuunew.DecBySoft         
##DecBySoft.argtypes=(c_void_p, c_void_p )

##EncBySoft=Psyuunew.EncBySoft         
##EncBySoft.argtypes=(c_void_p   ,  c_void_p   )
##使用增强算法对二进制数据进行加密使用软件)

##字符串及二进制数据的转换
##HexStringToc_byteArray=Psyuunew.HexStringToc_byteArray
##HexStringToc_byteArray.argtypes=(c_char_p ,c_void_p)
##HexStringToc_byteArray.restypes=(c_void)
##
##ByteArrayToHexString=Psyuunew.ByteArrayToHexString
##ByteArrayToHexString.argtypes=(c_void_p,c_char_p ,c_int )
##ByteArrayToHexString.restypes=(c_void)
##字符串及二进制数据的转换

 ##初始化锁函数,注意，初始化锁后，所有的数据??，读写密码也??0000000-00000000，增强算法不会被初始??
ReSet=Psyuunew.ReSet
ReSet.argtypes=[c_char_p]
ReSet.restypes=(c_int)

##以下函数只限于带U盘的??
##设置是否显示U盘部分盘符，真为显示，否为不显示
SetHidOnly=Psyuunew.SetHidOnly 
SetHidOnly.argtypes=( c_bool,c_char_p)
SetHidOnly.restypes=(c_int)

##设置U盘部分为只读状态，
SetUReadOnly=Psyuunew.SetUReadOnly 
SetUReadOnly.argtypes=[c_char_p]
SetUReadOnly.restypes=(c_int)
##以上函数只限于带U盘的??

##以下函数只支持智能芯片的??
##生成SM2密钥??
YT_GenKeyPair=Psyuunew.YT_GenKeyPair
YT_GenKeyPair.argtypes=(c_char_p ,c_char_p,c_char_p,c_char_p)
YT_GenKeyPair.restypes=(c_int)

##设置Pin??
YtSetPin=Psyuunew.YtSetPin
YtSetPin.argtypes=(c_char_p,c_char_p,c_char_p )
YtSetPin.restypes=(c_int)

##设置SM2密钥对及身份
Set_SM2_KeyPair=Psyuunew.Set_SM2_KeyPair
Set_SM2_KeyPair.argtypes=(c_char_p,c_char_p,c_char_p,c_char_p,c_char_p )
Set_SM2_KeyPair.restypes=(c_int)

##返回加密锁的公钥
Get_SM2_PubKey=Psyuunew.Get_SM2_PubKey
Get_SM2_PubKey.argtypes=(c_char_p,c_char_p,c_char_p,c_char_p)
Get_SM2_PubKey.restypes=(c_int)

##对二进制数据进行SM2加密
SM2_EncBuf=Psyuunew.SM2_EncBuf
SM2_EncBuf.argtypes=(c_void_p,c_void_p,c_int ,c_char_p)
SM2_EncBuf.restypes=(c_int)

##对二进制数据进行SM2解密
SM2_DecBuf=Psyuunew.SM2_DecBuf
SM2_DecBuf.argtypes=(c_void_p,c_void_p,c_int ,c_char_p ,c_char_p)
SM2_DecBuf.restypes=(c_int)

##对字符串进行SM2加密
SM2_EncString=Psyuunew. SM2_EncString
SM2_EncString.argtypes=(c_char_p,c_char_p,c_char_p)
SM2_EncString.restypes=(c_int)

##对字符串进行SM2解密
SM2_DecString=Psyuunew.SM2_DecString
SM2_DecString.argtypes=(c_char_p,c_char_p,c_char_p ,c_char_p)
SM2_DecString.restypes=(c_int)

##对消息进行SM2签名
YtSign=Psyuunew.YtSign
YtSign.argtypes=(c_char_p , c_char_p  ,c_char_p ,c_char_p)
YtSign.restypes=(c_int)

##对SM2签名进行验签
YtVerfiy=Psyuunew.YtVerfiy
YtVerfiy.argtypes=(c_char_p,c_char_p,c_char_p,c_char_p,c_char_p,c_void_p,c_char_p)
YtVerfiy.restypes=(c_int)

##SM2算法初始化(使用软件)
IniSM2=Psyuunew.IniSM2
IniSM2.restypes=(c_int)

##对字符串进行SM2解密(使用软件)
SM2EncString=Psyuunew.SM2EncString
SM2EncString.argtypes=(c_char_p,c_char_p,c_char_p ,c_char_p)
SM2EncString.restypes=(c_int)


##对字符串进行SM2加密（使用软件）
SM2DecString=Psyuunew.SM2DecString
SM2DecString.argtypes=(c_char_p,c_char_p,c_char_p)
SM2DecString.restypes=(c_int)

##对消息进行SM2签名（使用软件）
SM2Sign=Psyuunew.SM2Sign
SM2Sign.argtypes=(c_char_p , c_char_p ,c_int ,c_char_p ,c_char_p)
SM2Sign.restypes=(c_int)

##对SM2签名进行验签（使用软件）
SM2Verfiy=Psyuunew.SM2Verfiy
SM2Verfiy.argtypes=(c_char_p,c_char_p,c_char_p,c_char_p,c_char_p)
SM2Verfiy.restypes=(c_int)

##释放SM2算法(使用软件)
ReleaseSM2=Psyuunew.ReleaseSM2

##返回锁的硬件芯片唯一ID
GetChipID=Psyuunew.GetChipID 
GetChipID.argtypes=(c_char_p,c_char_p)
GetChipID.restypes=(c_int)
##以上函数只支持智能芯片的锁

##以下函数只支持D8
CheckDate=Psyuunew.CheckDate
CheckDate.argtypes=(c_char_p,c_char_p)
CheckDate.restypes=(c_int)
##以上函数只支持D8


if 'Linux' in platform.system():
	CloseUsbHandle=Psyuunew.CloseUsbHandle
	CloseUsbHandle.argtype=c_char_p
	CloseUsbHandle.restypes=(c_void_p)

def CheckDateEx(Path):
    dt=datetime.now()
    nowDate=dt.strftime( '%Y/%m/%d/%H/%M/%S' )
    ret=CheckDate(nowDate.encode('utf-8'),Path)
    return ret

def HexStringToByteArrayEx(InString):
    
    mylen=len(InString)
    array_data={}
    in_data=c_byte
    temp=''
    for n in range(0,mylen,2):
        temp=InString[n:2+n]
        temp='0x'.encode()+temp
        in_data=int(temp,16)
        array_data[n/2]=(in_data)
    return array_data

def StringToByteArray(InString):
    
    mylen=len(InString)
    array_data={}
    in_data=c_int
    temp=''
    for n in range(0,mylen):
        temp=InString[n:1+n]
        in_data=ord(temp)
        array_data[n]=(in_data)
    array_data[n+1]=0
    return array_data

def ByteArrayToString(InBuf):
    arrBytes = bytearray()
    for n in range(0,len(InBuf)):
        arrBytes.append(InBuf[n])
    return arrBytes.decode()
    

def ByteArrayToHexString(in_data,inlen):
    OutString=''
    temp=''
    for n in range(0,inlen):
        temp='%02X' % in_data[n]
        OutString=OutString+temp
    return OutString

def EnCode(InData,Key,pos):
    KeyBuf=HexStringToByteArrayEx(Key)
    OutData=EncBySoft(InData,KeyBuf,pos)	
    return OutData

def DeCode(InData,Key,pos):
    KeyBuf=HexStringToByteArrayEx(Key)
    OutData=DecBySoft(InData,KeyBuf,pos)
    return OutData


def EncBySoft(inb, KeyBuf,pos):
    bufArray=c_uint32*16
    buf=bufArray

    temp_string=''
    cnDelta = 2654435769
    _sum = 0
    a = 0
    b = 0
    c = 0
    d = 0
 
    for n in range(0,4):
        a = (KeyBuf[n] << (n * 8)) | a
        b = (KeyBuf[n + 4] << (n * 8)) | b
        c = (KeyBuf[n + 4 + 4] << (n * 8)) | c
        d = (KeyBuf[n + 4 + 4 + 4] << (n * 8)) | d 
    y = 0
    z = 0

    for n in range(0,4):
        temp = (inb[pos +n])
        y = (temp << (n * 8)) | y
        temp = (inb[pos +n + 4])
        z = (temp << (n * 8)) | z

    n = 32
    while  n > 0:
        _sum = (cnDelta + _sum) & 0xffffffff
        temp=(z << 4) & 0xffffffff
        temp=(temp+a)& 0xffffffff
        temp_1= (z + _sum) & 0xffffffff
        temp_2=((z >> 5) + b)& 0xffffffff
        temp=temp ^ temp_1 ^ temp_2
        y = (y+ temp)& 0xffffffff
        temp=(y << 4)& 0xffffffff
        temp=(temp + c)& 0xffffffff
        temp_1=(y + _sum)& 0xffffffff
        temp_2=((y >> 5) + d)& 0xffffffff
        temp=temp ^ temp_1 ^ temp_2
        z=(z+temp)& 0xffffffff
        n = n - 1

    outb={}
    for n in range(0,4):
        outb [n]= (y >> (n) * 8) & 255
        outb[n + 4] = (z >> (n) * 8) & 255

    return outb

def DecBySoft(inb, KeyBuf,pos):
    bufArray=c_uint32*16
    buf=bufArray
    temp_string=''
    cnDelta = 2654435769
    _sum = 0xC6EF3720
    a = 0
    b = 0
    c = 0
    d = 0
    for n in range(0,4):
        a = (KeyBuf[n] << (n * 8)) | a
        b = (KeyBuf[n + 4] << (n * 8)) | b
        c = (KeyBuf[n + 4 + 4] << (n * 8)) | c
        d = (KeyBuf[n + 4 + 4 + 4] << (n * 8)) | d
    y = 0
    z = 0
    for n in range(0,4):
        temp = (inb[pos +n])
        y = (temp << (n * 8)) | y
        temp = inb[pos +n + 4]
        z = (temp << (n * 8)) | z

    n = 32
    while  n > 0:
        temp=(y << 4)
        temp= ( temp+ c) & 0xffffffff
        temp_1=(y + _sum)& 0xffffffff
        temp_2=((y >> 5) + d)& 0xffffffff
        temp= temp ^ temp_1 ^ temp_2
        z=(z-temp) & 0xffffffff
        #z -= ((y << 4) + c) ^ (y + _sum) ^ ((y >> 5) + d)
        temp=(z << 4)& 0xffffffff
        temp=(temp+a)& 0xffffffff
        temp_1=(z + _sum)& 0xffffffff
        temp_2=((z >> 5) + b)& 0xffffffff
        temp= temp ^ temp_1 ^ temp_2
        y = (y -temp)& 0xffffffff
        _sum = (_sum -cnDelta)& 0xffffffff
        n = n - 1
    
    outb={}
    for n in range(0,4):
        outb[n] = (y >> (n) * 8) & 255
        outb[n + 4] = (z >> (n) * 8) & 255

    return outb

def StrDec(InString,Key):
   OutBuf={}
   mylen=len(InString)/2
   KeyBuf=HexStringToByteArrayEx(Key)
   InBuf=HexStringToByteArrayEx(InString)
   for n in range(0,(mylen-8)+1,8):
        tempBuf=DecBySoft(InBuf,KeyBuf,n)
        for i in range(0,8):
             OutBuf[i+ n] = tempBuf[i]
   if mylen>8:
       n=len(OutBuf)-1
       for n in range(len(OutBuf),mylen):
            OutBuf[n]=(InBuf[n])
   return ByteArrayToString(OutBuf)


def StrEnc(InString,Key):
    OutBuf={}
    InBuf={}
    temp_Buf=InString.encode('utf-8')
    mylen=len(InString)+1
    for n in range(0,mylen-1):
        InBuf[n]=temp_Buf[n]
    InBuf[n+1]=(0)
    if mylen<8:
            for n in range(mylen,8):
                 InBuf[n]=(0)
            mylen=8
            
    KeyBuf=HexStringToByteArrayEx(Key)
    for n in range(0,(mylen-8)+1,8):
         tempBuf=EncBySoft(InBuf,KeyBuf,n)
 
         for i in range(0,8):
              OutBuf[i+ n] = tempBuf[i]
    if mylen>8:
       n=len(OutBuf)-1
       for n in range(len(OutBuf),mylen-1):
            OutBuf[n]=(InBuf[n])
       OutBuf[n+1]=0
    OutString=ByteArrayToHexString(OutBuf,mylen)
    return OutString

#使用增强算法二检查是否存在对应的加密锁
def CheckKeyByEncstring_New():
    DevicePath=create_string_buffer(260)
    EncInString=["16860","11918","26758","29299","1322","13197","3281","3004","18135","26092","12156","5730","28399","13708","2275","20821","2203","10480","3455","18218","15397","28474","14313","28689","26871","4652","29405","29661","24475","18470",  \
"9013","3072","15292","26157","20969","1419","24099","29153","30228","25392","1722","21381","24305","8003","3723","10234","15832","3508","16831","12995","20549","24085","22946","28674","10705","15770","5790","18040","7734","6419",  \
"31291","22920","19278","32498","8485","31539","17172","8523","15652","15901","21920","30669","12068","10118","31533","461","16686","337","24086","10299","108","19454","1237","16297","14120","20658","7169","10827","1740","21293",  \
"24663","6641","8675","25554","10416","29196","9749","20899","4103","18866","5678","15425","16244","3474","29718","17903","22578","16894","31449","25998","32156","25833","30880","22689","32554","28644","18613","13642","8825","31267",  \
"28034","7243","3392","31349","19090","2821","20314","10576","32397","19834","3266","706","23870","4174","18320","26750","2449","4800","18943","25559","12172","30900","12394","1984","24156","15533","4938","29384","587","16842",  \
"20792","28963","32448","1488","30960","16035","26697","29470","21324","26810","24205","21177","3396","20601","1624","24129","500","19603","9107","29177","9364","27481","21319","24258","2688","21694","26016","23583","5425","19540",  \
"22503","6707","15424","21324","28295","29628","30569","27257","28424","16417","18566","29772","31253","17760","25999","14041","1402","18973","672","32207","30237","18330","15345","23683","23051","15289","8158","4069","17005","6907",  \
"22751","136","15757","25218","30608","25756","28885","18962","23722","503","21199","5643","17159","4103","1319","2416","27041","14816","20131","30689","23955","16436","13615","30627","25621","15188","14294","13207","1156","32051",  \
"10433","23870","12886","4963","10043","16058","5928","26901","14764","27854","31923","2333","1951","6365","22225","32745","13246","743","28028","23952","21972","2958","9935","22464","5322","26132","28930","3022","24745","27228",  \
"19569","24746","19613","1769","30101","2279","2288","21210","12040","9398","32009","16372","11140","1002","375","27798","6115","2037","14815","5574","17695","9704","3854","10530","29266","2166","18668","30445","14007","20975",  \
"18565","1035","2983","32328","25090","31739","30363","25874","22189","17123","21296","23422","28400","10113","15645","30303","13398","13625","6717","27686","19335","9741","17546","5863","28238","29853","21534","5714","1431","3631",  \
"2357","4537","25448","9377","22053","6671","7406","8311","2411","11238","1139","13011","6048","20847","17246","1910","1406","25725","5181","5827","29150","28801","7352","6076","16317","13455","26520","4610","24626","17750",  \
"32456","4056","15481","20267","9556","28703","16363","30717","12643","22618","514","24929","1600","18091","4184","19079","11861","17363","22694","21058","5420","13621","13001","22788","24943","20178","2744","735","28393","9550",  \
"10894","22915","26755","24552","9350","3653","583","2693","23800","23572","21343","1958","13408","2437","20501","8811","20823","2761","25555","16536","2712","17328","11044","13455","28922","27054","19888","12114","31098","1494",  \
"30786","21122","18226","5848","30405","25185","5467","21254","28226","6099","16718","2643","14051","4696","29831","10321","22002","27154","28319","22064","6106","25029","28496","15558","18979","14545","16500","26241","5497","7481",  \
"24581","16757","30627","15774","18974","16724","23951","31554","25335","8560","23877","15369","237","18105","4080","23667","5750","16836","3032","16803","31790","28865","32359","2907","23249","16771","26154","26107","13622","4988",  \
"27848","31879","4697","14781","24845","2722","18258","7417","20706","3724","24924","32128","17233","6951","12242","21832","4740","18934","28204","23007"]
    EncOutString=["28723ED2D8C14C15","C4F33E69F5A4FC2E","908590089D998C9C","3DF6F14C39AF3A3B","08C6BD5B1F2E6CCF","47D6169A4C67359B","6F419DEDD0C3481A","9C844977FE2CFF41","8131E9EB346A20C9","DFB99D46F41420D7","6729BF323C1DDEDB","F47E6C69467256CF","18DB1FA96652EB31","D43B727FCC752C29","2D1449ED739DB312","8D05AE7187301B32","E44EF54A27CD11DB","E2C86D4E909A74CF","7D9FB152F0BF02FC","AC2096B2ACDD5DD6","980943344F492D6B","8B36030E5BE78EB4","7AD2BE470EE470CB","E4BDF843AB2F2E82","826A1EE4309E31D3","3BE5F412E6A83C07","85D26E455D986D8B","F93B52FFFC9D5168","76AB27C8C4DF81B2","64211364D7F40B94",  \
"E5CAE82DA6ED4E78","44DF811F44E1D980","B1461E7C1F0E2EFE","CE87D3F3F8CB790B","081770B6E23CEAA4","BC11D13B89D4E841","1E44D391534F5FFA","92AF40EC6FF50215","6E9F2DB1784487E6","EC0C024BE3CCD4E9","408EA003C52A4DAC","2495DAE9573B8DB3","23EC21263853BE89","34B30BD4C0119E29","30F947E07FE11407","C5F237BD1EAA9C71","5C9A9CE80FB31148","82808F7D59D55800","7BFB20E695F57AC3","09390965C88A02E9","8BB115721F3CF4B6","C29E95F937F2678F","9674F9164402D8FB","3E4CDD4906CE673E","3EE37A6045421F72","C15F3744717B7438","BB1847916AFBA004","A74CD5554E59A36E","8EFBEB262B3FB561","84809449A321E013",  \
"4994F601CC762EAD","1EA44FAA5F4E5C2A","7BB8767BD8CABDAB","7AECB47C12B856F6","284C85CDE310A45B","F6011262F7869E4D","ECE13982E8C7857A","26CC03B3E30CE97C","485DBF6A45B98C74","192B88DECB34B64C","8BA7772AF7C5B374","2D452396C31A6846","FE6FFF81212BF0FB","752F74C77D8F5EDB","4E3602173050497E","4DFC9AFDD238B1C7","B7C596348525164D","E45B8E6BFEE43019","A20FF127641960A0","5212EED9C93D8A63","F6EE75D67C28461F","CA391CE967B0F55A","1B729FA856681633","DA3614922BE636BE","44441EE574EC9104","8D5EF95CD55697A9","95CD3BFDEEC699B9","2D08D7EBEA800AF7","387609AF343B0375","4285B2075DA97553",  \
"658A35384CCFD23A","6028BCB5ABED417C","B81EC6EE83988A0C","7318F467815C7497","0734CB67562CFE31","BE2AEAD26A884206","F84BF3CB4BA7F973","F2834351FA3402CE","7E5A8F5C2BE88D36","54A072CE3E9296E0","E85DCCCE44B57ACD","05D78E17F3C9D0E7","B7389ECB1F2C68A6","DF17141C92CD965B","1223BB261D3DF672","D8461BB0B3D69C18","5AC5DE496A589041","FE3627267FF7A4B9","EE7CEE79003403D4","870FEA77797896AF","3D9C824617E030C6","71B92A32C263B3B8","0410CB90E3304A81","3F34A6EA2218A7AA","9FBD98CB862897EE","4CE511B7B03F8FA3","91935CCB21B4EFA5","7905D86C52990163","1D729797F4D7A4E7","ED54B35C92508ABD",  \
"BA83C0028DFDF190","F96C7F56D6ADFB2F","6AD8A8298F81B2C8","795D7F391EC93CE7","98D3740920DC5F9D","C1C2626DC0B32FC3","CC3CF55F2E673D5E","690793070264328E","FA09CF3AEA930168","BC659B60DCECCE62","348005850373663C","32684081EE32675E","A0A2EF488A29D8D6","EA42C0477988ED9E","8BF8FE7DEA331CFF","6A86181D86EF390F","E0618CF35241F336","0BF797C105F4CEAA","1E390F7D581B6AD8","7D1DA9ED993733D7","0FFC2F2F24E5C8B6","0CBABC5CDB8B11C3","F7F33ECF9C04C8CD","F76F970FE87503B2","299CA2AC813F3C43","DABF293060810A2B","EB2AD49830490147","7809D3D8864CCF76","CFD594133B150AB2","906F4C1E2A6D6BC4",  \
"F565954E61049484","4BDD5C7405A3962D","2EA09567B594517C","7FF0060695B305F0","CD87B00C04B92AA8","F711E962CC6CA9E8","7EC64AEDC6C20885","AAC2CFFBF47969BF","92857C1AD18F8893","EF5246398CB66CE9","8B6CD380F4175552","7E760C4BA34C90F0","455433801B479DE8","020C435641C1A26F","2E26E69BB64E96CC","53845160C1C9CF3F","7642CF01C8B546DA","692ECC03D42F1CF4","6DBFE97511CD1C0A","8D8C8897CDD8D8B6","19C90A3CB3F0ED91","102760813754EDEF","E3D547095C4C4415","83FF508D02EFAEFF","0FAFDEE9186510C8","3E5E9C8292E52FD9","57F710EAA9830885","42364E3F0C940318","2A6F0F3084A33416","C85B693199343B5E",  \
"858D07826F919AEC","392B5F9E556C2F70","4D3F4E32BB274EC4","92857C1AD18F8893","716E0AD15099E5B3","6219F3E26C41658C","4465F747CF7B4233","63F457C10F479E68","FFCA072110B79B5A","4E5BC55A9D18F7E3","1B5120DF4FFE95A3","87BEFBD6ECD9C1E7","C0F59871239360A4","93CBA34AC8435633","4E5B03C5C245FB3F","F63770166424F68A","88ABED9E5B73F5EE","A264855501D8DFB7","7E0CE0F50DEE5965","B8B4B065611B91DB","F5D4CBD3AC9DC2BB","30062E957B7F47B6","E48DED8F747EF235","3D61790D43551911","B120A6D7837B5BCD","585364E1E8102E85","D0D9EE58A6EDE8B5","717D6C8540B19BB4","1CBE155F76DF7D46","8FFB9BB1174424F6",  \
"266173E645C78346","8ED6F46077B5972B","2B6BB7CF184E6B44","09345865DF91E287","96975821F2CB0841","C26C6ABE40575740","32B9FE1755315485","8004C57ABA3B3336","B077041BC02E5950","0B39EEBEB2FF9343","9385026D82CC48C4","E3E24A4C8FAE4A57","F2ACA15E3F58D242","7E5A8F5C2BE88D36","5241A39AB0E17848","F2E263AE4D030117","52080F39759E60AB","C5E4490B1BBB11DE","DFD092EB1011A3FD","A0EE4B472E7E575A","DB7A0656077CFB5A","850701EC27E4DB69","BA412DF7A11FF71F","D46C930D5503AD7A","C7B68192B96D86DE","50791EA0111A8AE4","CFCB96D1F3572017","60DE83C2EECBF280","CE31340C5890EDBB","D4E828B6EF9058E8",  \
"00021B9BD05188E7","A0A2EF488A29D8D6","006B5F330C4E3B95","F877E267859BAB3C","C57CC8C5852D0CCF","665651C16B1413D3","D1AD0A3609762BEE","09A5F3A34166CCD1","53E3D92C14B74A75","43EFB2275FEA3856","726A437AA1B9E109","43BC6AF8749CD9F8","26E0E78DAD93ECFD","8CF8C4EE110D7399","85A1DB25D19837E2","5B5A4C32385C6C5A","91659A029BA41D6A","6B4978DD37B4EB27","E6176C2FF999861C","BB1328FEC83A2DE2","79B48D1C6F27EB81","533CD714158BD535","9C16637B01AAAAE3","7E6CA7BDC15126EF","2DBEB0C188901E13","B42F88A7C0F4616F","5C0FEF4FC9D8EAAA","490BCAD36BE924A3","3B05969771E66749","31F96FEA8F1AA32D",  \
"C0C38EF2DD62A2A3","02A8CE527B731101","F1FC1C88C61A84EC","49E8C5622B846B30","5ABCBD4248452E4C","E4C7DBFA5744F41A","F2F4935B66398CD2","CBBE2785787EC0A3","B41AA4641128FAF3","9EAFA36089C26958","667A3F8C93B6632B","CEF18FD6F088063D","23DF71B52A658A58","AB1FDA5CFDABDF61","21EB22E81D28B203","89C5BCF80A2CED75","2F7148620374A488","CEDDD81CB976223A","D5700B60362306E2","870128C6083521BD","606710E97D8DA117","CB18C2116CA915FD","825D048526B0EDC4","FEAEF29A28DF6A73","A25F6522B586688B","8C416BC9BA814E3A","187CBF7F262AEDAA","4229E51B7BAFBCE7","2C3B7B527D1FD88F","2458082048800863",  \
"2C6A990C25C6F102","CF2EC5C4185AD820","AED6AA5426E8010F","37A49197613FC93E","7C1E14DF74070A79","38A649A6A79614A9","CD018089499079C1","E4EDB64CA2CF187E","C89723C8EFDB017E","D0F5D10B3A2AF4FD","462D4E165D4497CE","E0580768CC50F25F","DC9AF0BB1DB44428","5F7B5B3BAC47227E","9AC0E4D45243BE19","4768DE9F11011BFD","F7F1AE38335E5746","3F10DA603CF6EF9F","EF32D8F851C590B8","9448198FE6D27C8F","59454D7D552C6D04","1FBB03D9313231F3","6C7D590DAA1F6DDC","10459E8C60C42B7E","3CEDAB9A5A89BD80","F6C1D20D2ED123CF","EBF28F86ABD494B5","87849AE033F7A18B","C2CAA32DE82C97DA","B0914C2E8FCD666B",  \
"08C9E77326ADE648","8D2FDB46FF0EC977","882BB6A9E1D206CF","D40927C41BF4B237","EF36D1581CA7E455","D74E5221ADCCE6AC","4C9DDE8E0BBD47C0","5ABE62BAAAA793DF","D82B19AFCA969A90","F0D18C7F1AEA732F","E713CC8134E46B75","366ADF59A76BAA87","EB374E67A93807E2","ED89D73E280496AB","27454B58C93AE6C3","C87C55806C953B43","462A52D0C6E2C321","416A894147741A41","11FA66A783EBA2DE","6CCD68D2F1A7DC1D","FCF3B635EE0E7589","98C1FFF80748FAC7","82B0AE77EE41091E","6A3ED2C40139116E","FE65C5AE60D02017","89220AA2C106884E","728ECE766B75926B","0E0CF32FE4304511","19DC13259F843483","B3FE37DD8DD5F148",  \
"E546F839D9C2CF52","A7AEC3D5EA7C64BB","DE84FF71386CB4BD","59130B68E5F1AC6D","499C2D5A22AE8A3A","AAE457A21F1B3EBB","ED99980A1C796B66","20792C7A0C2057E4","381F8EEF114B659C","AA9206EE9716FFBA","124DF543C6804224","77AD88DDD6DE9C4F","A8CE91681C38E0E3","A13FCB15F9A2D43C","A94B656410D17B01","DCB0BDF8EBBC0927","C86DF9EC633C31D1","ED5DB99BB462D9A4","A936DD606AE60DC0","63765470105C9EEC","E5AA245FF9E62BA7","2E0BA3F6AD680E0B","7200432B8B10EF41","B3D1D251E7BF1506","FF47F6B96BE03B0B","41873F469E714B01","F5AE80596DD1EE1B","2ABEDD0B65378973","DA2C51F706B11CC6","BC77FE556ABDACFF",  \
"6FE92A53B674BE95","FBC63B2172117ABD","4C84F8612BD6472A","CAA30DD11790C81F","9F41C09CDDAB441A","F37DE50CBC6221AD","F9E81503373E8CB5","DFC1B209076B7F5F","507B899E393CFD89","E9DFD6B79127436F","AB6FEACB77B67FB1","934C1894409BF738","FE6A75E2236677A8","CFA9D1AC1FADD4E5","71C4099622D2D39E","7929AFC1191D2B3D","7D230DA8638CD013","52215D28812F5DD9","CDDE2E74D0375754","620D071AA02DEBAB","F22DC1DD5EA1B382","AF09E471EFC9B775","5A56C3A05E171EAB","89220AA2C106884E","FBAC8FD6F9067A72","C67CE3D594B4A45C","EF28C3D3A184007F","6C893DC33A89D3F7","1211826FBB427D63","743964CD3F07EEBD",  \
"940C95AB3097C1D9","8CD518EC0D736DBD","39A96FD4F34DEF21","410D1478DCC705B2","B46F99C7CBCDF21C","576BE8482B82BCA9","BBC22903FDF621A5","9A29ECDBC351C91A","7FC2D31879FD2960","E11C64AC9A59B53B","E3198738001DA2B1","5BD63D8145EEE60E","D320596CF9C8FC6E","43E8EC16FDECA74D","6B9A4B594C061742","4E363345D14D830F","CCF7F845B51A85CB","7E920B94DBB88F95","486471E766F2F67C","5F1AA8E30273AD70","7326FA10973FC7F9","080156B8631714FF","3E1D955D98E3B9B0","B2C00554FEBAE9EA","B600D01A841DC012","83763022F986E03E","A7B4399CEDA5A43B","3DBC2282C912DA06","CE1C0C7947A1D945","DC5550AC89BC171B",  \
"FF193C8455242477","0644CC3390BBFCC7","D46C930D5503AD7A","52615BE63853EFE0","9B9EEA5739AEEC56","25BFE7159BF3D229","A63B86BA96081507","F302BFA9147A0254","7CBB72477F07AEC4","218C51A516D847AC","C9834D17E3E319C8","E019A8606BEF8B51","1496859C6FBAC1ED","4446424B7815CD64","F8D4B1F210F1F125","64C2D0F213BEB7D8","C52D54AD81271869","7A95BFD618F5E597","08C694D7E0A10204","C1D8B03A5B3EEC24","9FDB2D5297FE5970","0316F50C22550D6B","2D36134C41D94548","9D3D2201E86C8708","39D9219F29FE10D1","95978AE3EABB04D2","8A9ADCCE385BC6C4","E149EAA1DD1E3DD4","E18411D012A348A8","A107BED7263578E9",  \
"13E9EF13B52DF1EE","7981FFC7230DCEFA","3706605C679FDDE6","5E94A055FF29F2F3","066CD0FF8146A606","F9C60EF452344080","787794810FD198A4","2CD5EFEA8B4FC56F","6E6E6A367A12CB7A","527B4B9619B151D9","53FFA3D96DCC801D","4679DA30F2B6DA98","9B27B654AA15F0A3","AB0696C75C950E6D","145C75B30C73494A","17AF21937D33265D","D8FD979F6AB98028","626793C8F65E8075","5BBC2E0F20CF8D19","B526ACC28B13353A"]
#@NoUseNewKeyEx return 1 #如果没有使用这个功能，直接返回1
#@NoSupNewKeyEx return 2 #果该锁不支持这个功能，直接返回2
    myrnd=random.randint(1, (500 -1 ))
    mylen = len(EncInString[myrnd])+1
    if  mylen < 8 :
        mylen = 8 
    outstring = create_string_buffer((mylen* 2+1))#//注意，这里要??一个长度，用于储存结束学符串
    for n in range(0,255):
         ret=FindPort(n,DevicePath)
         if ret!=0:
             CloseDongle(DevicePath)
             return ret
         ret=EncString_New(EncInString[myrnd].encode('utf-8'), outstring,DevicePath)
         if outstring.value.decode('utf-8').lower()==EncOutString[myrnd].lower():
             CloseDongle(DevicePath)
             return 0
    CloseDongle(DevicePath)
    return -92


#使用增强算法一检查加密锁，这个方法可以有效地防止仿真
def CheckKeyByEncstring():
#推荐加密方案：生成随机数，让锁做加密运算，同时在程序中端使用代码做同样的加密运算，然后进行比较判断。
    DevicePath=create_string_buffer(260)
#@NoUseKeyEx return 1 #如果没有使用这个功能，直接返回1
    InString=('%X%X' % ((int)(random.uniform(0, 24174836)),(int)(random.uniform(0, 24174836))))
    for n in range(0,255):
         ret=FindPort(n,DevicePath)
         if ret!=0 :
            CloseDongle(DevicePath)
            return ret
         if Sub_CheckKeyByEncstring(InString,DevicePath)==0:
            CloseDongle(DevicePath)
            return 0
    return -92

def Sub_CheckKeyByEncstring(InString,DevicePath):
#//'使用增强算法对字符串进行加密
    nlen = len(InString) + 1
    if nlen < 8 :
          nlen = 8
    outstring = create_string_buffer((nlen * 2+1))#//注意，这里要加1一个长度，用于储存结束学符??
    outstring = StrEnc(InString, ''.encode('utf-8'))
    outstring_2 = create_string_buffer((nlen * 2+1))#//注意，这里要加1一个长度，用于储存结束学符??
    EncString(InString.encode('utf-8'),outstring_2,DevicePath)
    if outstring.lower()==outstring_2.value.decode('utf-8').lower():#//比较结果是否相符
         ret=0
    else:
         ret=-92
    return ret

#//使用带长度的方法从指定的地址读取字符串
def ReadStringEx(addr,DevicePath):
    InArray=c_ubyte*1
    blen = InArray(0)
#//先从地址0读到以前写入的字符串的长??
    ret = YReadEx(blen, addr, 1, 'D0C9E8D4'.encode('utf-8'), 'F133D9A2'.encode('utf-8'), DevicePath)
    if ret != 0 :
        return ''
    outstring=create_string_buffer(blen[0])		
#再从地址1读取指定长度的字符串
    ret = YReadString(outstring, addr+1, blen[0], 'D0C9E8D4'.encode('utf-8'), 'F133D9A2'.encode('utf-8'), DevicePath)
    if ret!=0:
        return ''
    return outstring.value


#//使用从储存器读取相应数据的方式检查是否存在指定的加密锁
def CheckKeyByReadEprom():
    DevicePath=create_string_buffer(260)
#@NoUseCode_data return 1 #如果没有使用这个功能，直接返回1
    for n in range(0,255):
        ret=FindPort(n,DevicePath)
        if ret!=0 :
            CloseDongle(DevicePath)
            return ret
        outstring=ReadStringEx(0,DevicePath)
        if(outstring==''.encode('utf-8')):
            CloseDongle(DevicePath)
            return 0
    CloseDongle(DevicePath)
    return -92

#使用普通算法一查找指定的加密锁
def CheckKeyByFindort_2():
    DevicePath=create_string_buffer(260)
    ret=FindPort_2(0, 1, 1680413494, DevicePath)
    CloseDongle(DevicePath)
    return ret

def CloseDongle(DevicePath):
    if 'Linux' in platform.system():
        CloseUsbHandle(DevicePath)#关闭USB设备

