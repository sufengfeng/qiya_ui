# -- coding: utf-8 --
import platform
from datetime import datetime
import random
from ctypes import *

if 'Windows' in platform.system():
    if "32bit" in platform.architecture():
        Psyuunew=windll.LoadLibrary('yt88/Syunew3D.dll')
    else:
        Psyuunew=windll.LoadLibrary('yt88/Syunew3D_x64.dll')
else:
    if "32bit" in platform.architecture():
        Psyuunew=windll.LoadLibrary('yt88/libPsyunew3.so')
    else:
       Psyuunew=cdll.LoadLibrary('yt88/libPsyunew3_64.so')

##�����İ汾
NT_GetIDVersion=Psyuunew.NT_GetIDVersion
NT_GetIDVersion.argtypes=(c_void_p,c_char_p)
NT_GetIDVersion.restypes=(c_int)


##��ȡ������չ�汾
NT_GetVersionEx=Psyuunew.NT_GetVersionEx
NT_GetVersionEx.argtypes=(c_void_p,c_char_p)
NT_GetVersionEx.restypes=(c_int)


##�㷨����
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
##�㷨����

##дһ���ֽڵ���������
YWrite=Psyuunew.YWrite
YWrite.argtypes=(c_byte ,c_short,c_char_p ,c_char_p,c_char_p )
YWrite.restypes=(c_int)

##�Ӽ������ж�ȡһ����??
YRead=Psyuunew.YRead
YRead.argtypes=(c_void_p,c_short,c_char_p ,c_char_p,c_char_p )
YRead.restypes=(c_int)

##дһ���ֽڵ���������
YWriteEx=Psyuunew.YWriteEx
YWriteEx.argtypes=(c_void_p,c_short,c_short,c_char_p,c_char_p,c_char_p )
YWriteEx.restypes=(c_int)

##�Ӽ������ж�ȡһ����??
YReadEx=Psyuunew.YReadEx
YReadEx.argtypes=(c_void_p,c_short,c_short,c_char_p,c_char_p,c_char_p )
YReadEx.restypes=(c_int)

##����ָ���ļ�������ʹ����ͨ�㷨һ??
FindPort_2=Psyuunew.FindPort_2  
FindPort_2.argtypes=(c_int ,c_ulong ,c_ulong ,c_char_p)
FindPort_2.restypes=(c_int)

##���Ҽ���??
FindPort=Psyuunew.FindPort  
FindPort.argtypes=(c_int ,c_char_p)
FindPort.restypes=(c_int)

##��ȡ����ID
GetID=Psyuunew.GetID  
GetID.argtypes=(c_void_p,c_void_p,c_char_p)
GetID.restypes=(c_int)

##�Ӽ������ж��ַ�??
YReadString=Psyuunew.YReadString 
YReadString.argtypes=(c_char_p ,c_short,c_int ,c_char_p ,c_char_p,c_char_p)
YReadString.restypes=(c_int)

##д�ַ�����������??
YWriteString=Psyuunew.YWriteString
YWriteString.argtypes=(c_char_p,c_short,c_char_p ,c_char_p,c_char_p )
YWriteString.restypes=(c_int)

##����д��??
SetWritePassword=Psyuunew.SetWritePassword
SetWritePassword.argtypes=(c_char_p ,c_char_p,c_char_p ,c_char_p,c_char_p)
SetWritePassword.restypes=(c_int)

##���ö���??
SetReadPassword=Psyuunew.SetReadPassword
SetReadPassword.argtypes=(c_char_p ,c_char_p,c_char_p ,c_char_p,c_char_p)
SetReadPassword.restypes=(c_int)

##������ǿ�㷨��Կһ
SetCal_2=Psyuunew.SetCal_2
SetCal_2.argtypes=(c_char_p,c_char_p)
SetCal_2.restypes=(c_int)

##ʹ����ǿ�㷨һ���ַ������м���
EncString=Psyuunew.EncString  
EncString.argtypes=(c_char_p,c_char_p,c_char_p)
EncString.restypes=(c_int)

##ʹ����ǿ�㷨һ�Զ��������ݽ��м���
Cal=Psyuunew.Cal  
Cal.argtypes=(c_void_p,c_void_p,c_char_p)
Cal.restypes=(c_int)

##������ǿ�㷨��Կ??
SetCal_New=Psyuunew.SetCal_New
SetCal_New.argtypes=(c_char_p,c_char_p)
SetCal_New.restypes=(c_int)

##ʹ����ǿ�㷨�����ַ������м�??
Cal_New=Psyuunew.Cal_New  
Cal_New.argtypes=(c_void_p,c_void_p,c_char_p)
Cal_New.restypes=(c_int)

##ʹ����ǿ�㷨�����ַ������м�??
EncString_New=Psyuunew.EncString_New  
EncString_New.argtypes=(c_char_p,c_char_p,c_char_p)
EncString_New.restypes=(c_int)

##�������ĳ�������
GetProduceDate=Psyuunew.GetProduceDate  
GetProduceDate.argtypes=(c_char_p,c_char_p)
GetProduceDate.restypes=(c_int)

##����ID����
SetID=Psyuunew.SetID
SetID.argtypes=(c_char_p ,c_char_p)
SetID.restypes=(c_int)

##������ͨ��??
SetCal=Psyuunew.SetCal
SetCal.argtypes=(c_char_p ,c_char_p,c_char_p ,c_char_p,c_char_p)
SetCal.restypes=(c_int)

##��������ת������
##SnToProduceDate=Psyuunew.SnToProduceDate
##SnToProduceDate.argtypes=(c_char_p ,c_char_p )
##SnToProduceDate.restypes=(c_void)

##ʹ����ǿ�㷨���ַ������н���ʹ�����
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
##ʹ����ǿ�㷨���ַ������н���ʹ�����)


##ʹ����ǿ�㷨�Զ��������ݽ��м���ʹ�����)
##DecBySoft=Psyuunew.DecBySoft         
##DecBySoft.argtypes=(c_void_p, c_void_p )

##EncBySoft=Psyuunew.EncBySoft         
##EncBySoft.argtypes=(c_void_p   ,  c_void_p   )
##ʹ����ǿ�㷨�Զ��������ݽ��м���ʹ�����)

##�ַ��������������ݵ�ת��
##HexStringToc_byteArray=Psyuunew.HexStringToc_byteArray
##HexStringToc_byteArray.argtypes=(c_char_p ,c_void_p)
##HexStringToc_byteArray.restypes=(c_void)
##
##ByteArrayToHexString=Psyuunew.ByteArrayToHexString
##ByteArrayToHexString.argtypes=(c_void_p,c_char_p ,c_int )
##ByteArrayToHexString.restypes=(c_void)
##�ַ��������������ݵ�ת��

 ##��ʼ��������,ע�⣬��ʼ���������е�����??����д����Ҳ??0000000-00000000����ǿ�㷨���ᱻ��ʼ??
ReSet=Psyuunew.ReSet
ReSet.argtypes=[c_char_p]
ReSet.restypes=(c_int)

##���º���ֻ���ڴ�U�̵�??
##�����Ƿ���ʾU�̲����̷�����Ϊ��ʾ����Ϊ����ʾ
SetHidOnly=Psyuunew.SetHidOnly 
SetHidOnly.argtypes=( c_bool,c_char_p)
SetHidOnly.restypes=(c_int)

##����U�̲���Ϊֻ��״̬��
SetUReadOnly=Psyuunew.SetUReadOnly 
SetUReadOnly.argtypes=[c_char_p]
SetUReadOnly.restypes=(c_int)
##���Ϻ���ֻ���ڴ�U�̵�??

##���º���ֻ֧������оƬ��??
##����SM2��Կ??
YT_GenKeyPair=Psyuunew.YT_GenKeyPair
YT_GenKeyPair.argtypes=(c_char_p ,c_char_p,c_char_p,c_char_p)
YT_GenKeyPair.restypes=(c_int)

##����Pin??
YtSetPin=Psyuunew.YtSetPin
YtSetPin.argtypes=(c_char_p,c_char_p,c_char_p )
YtSetPin.restypes=(c_int)

##����SM2��Կ�Լ����
Set_SM2_KeyPair=Psyuunew.Set_SM2_KeyPair
Set_SM2_KeyPair.argtypes=(c_char_p,c_char_p,c_char_p,c_char_p,c_char_p )
Set_SM2_KeyPair.restypes=(c_int)

##���ؼ������Ĺ�Կ
Get_SM2_PubKey=Psyuunew.Get_SM2_PubKey
Get_SM2_PubKey.argtypes=(c_char_p,c_char_p,c_char_p,c_char_p)
Get_SM2_PubKey.restypes=(c_int)

##�Զ��������ݽ���SM2����
SM2_EncBuf=Psyuunew.SM2_EncBuf
SM2_EncBuf.argtypes=(c_void_p,c_void_p,c_int ,c_char_p)
SM2_EncBuf.restypes=(c_int)

##�Զ��������ݽ���SM2����
SM2_DecBuf=Psyuunew.SM2_DecBuf
SM2_DecBuf.argtypes=(c_void_p,c_void_p,c_int ,c_char_p ,c_char_p)
SM2_DecBuf.restypes=(c_int)

##���ַ�������SM2����
SM2_EncString=Psyuunew. SM2_EncString
SM2_EncString.argtypes=(c_char_p,c_char_p,c_char_p)
SM2_EncString.restypes=(c_int)

##���ַ�������SM2����
SM2_DecString=Psyuunew.SM2_DecString
SM2_DecString.argtypes=(c_char_p,c_char_p,c_char_p ,c_char_p)
SM2_DecString.restypes=(c_int)

##����Ϣ����SM2ǩ��
YtSign=Psyuunew.YtSign
YtSign.argtypes=(c_char_p , c_char_p  ,c_char_p ,c_char_p)
YtSign.restypes=(c_int)

##��SM2ǩ��������ǩ
YtVerfiy=Psyuunew.YtVerfiy
YtVerfiy.argtypes=(c_char_p,c_char_p,c_char_p,c_char_p,c_char_p,c_void_p,c_char_p)
YtVerfiy.restypes=(c_int)

##SM2�㷨��ʼ��(ʹ�����)
IniSM2=Psyuunew.IniSM2
IniSM2.restypes=(c_int)

##���ַ�������SM2����(ʹ�����)
SM2EncString=Psyuunew.SM2EncString
SM2EncString.argtypes=(c_char_p,c_char_p,c_char_p ,c_char_p)
SM2EncString.restypes=(c_int)


##���ַ�������SM2���ܣ�ʹ�������
SM2DecString=Psyuunew.SM2DecString
SM2DecString.argtypes=(c_char_p,c_char_p,c_char_p)
SM2DecString.restypes=(c_int)

##����Ϣ����SM2ǩ����ʹ�������
SM2Sign=Psyuunew.SM2Sign
SM2Sign.argtypes=(c_char_p , c_char_p ,c_int ,c_char_p ,c_char_p)
SM2Sign.restypes=(c_int)

##��SM2ǩ��������ǩ��ʹ�������
SM2Verfiy=Psyuunew.SM2Verfiy
SM2Verfiy.argtypes=(c_char_p,c_char_p,c_char_p,c_char_p,c_char_p)
SM2Verfiy.restypes=(c_int)

##�ͷ�SM2�㷨(ʹ�����)
ReleaseSM2=Psyuunew.ReleaseSM2

##��������Ӳ��оƬΨһID
GetChipID=Psyuunew.GetChipID 
GetChipID.argtypes=(c_char_p,c_char_p)
GetChipID.restypes=(c_int)
##���Ϻ���ֻ֧������оƬ����

##���º���ֻ֧��D8
CheckDate=Psyuunew.CheckDate
CheckDate.argtypes=(c_char_p,c_char_p)
CheckDate.restypes=(c_int)
##���Ϻ���ֻ֧��D8


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

#ʹ����ǿ�㷨������Ƿ���ڶ�Ӧ�ļ�����
def CheckKeyByEncstring_New():
    DevicePath=create_string_buffer(260)
    EncInString=["20858","31211","30661","20652","9878","31487","4946","16817","10384","5625","32684","25800","9939","1179","6033","4549","25062","11589","12248","12823","25975","5372","16764","17106","590","29024","13207","30375","26708","23220",  \
"17764","30698","24725","7642","6204","19083","10043","11859","22936","19997","25997","14401","3349","24529","19449","21095","30313","7290","19462","20519","9074","17033","29279","13187","5671","13330","24783","16156","3747","6340",  \
"26687","10293","29984","8180","17081","26799","25593","25233","28006","12558","20903","25904","8851","31345","23236","14850","29607","14493","11274","17111","814","11250","3156","4900","24272","21362","1690","29177","31064","32448",  \
"13303","31752","17585","30","9638","26021","27620","32365","28415","23744","11547","26416","20350","2796","21408","138","31931","14170","20957","6970","3187","2269","31580","25763","32380","26598","24264","22729","26324","137",  \
"16362","21580","14227","25717","12716","18031","10994","19711","20503","788","19789","32022","6744","13500","10013","17231","27829","28297","1788","7131","6812","24126","27555","29322","10388","7742","3567","1233","9801","10120",  \
"2776","25536","10371","25536","11639","5642","25389","24360","22791","23040","25426","6818","4835","1942","26907","32174","11396","4699","25042","26737","3460","11139","482","26027","7581","993","32467","31935","20136","11748",  \
"26960","9135","18082","8096","10021","20764","10658","21702","3384","11849","996","4266","6550","26903","21440","16444","19816","9738","13234","31758","9976","4674","9299","10836","15280","5505","30301","16606","29210","9258",  \
"21674","10014","23521","12606","28212","14375","12238","16480","16406","25771","25546","6099","32648","29947","26337","4726","9191","27402","31548","4557","4265","1130","12325","4090","24427","23628","31750","20926","18918","11651",  \
"30313","14460","13300","13441","12793","13365","21903","12631","13951","21900","1234","2488","6885","32707","8182","2805","16181","15036","5972","19457","9881","9464","5992","12142","29018","1434","21195","1389","30436","32354",  \
"27703","19921","32705","23990","135","6668","8090","4245","20658","3887","12088","13473","3030","2029","26247","18972","14634","22166","5776","1514","16906","10016","893","17291","7151","282","24216","5922","4723","27061",  \
"24651","32623","12624","9670","545","14296","20064","7102","22722","10844","13213","21934","3578","413","26913","9033","31409","23261","7975","23520","24819","6144","14344","16486","17897","20870","29245","32108","27613","26769",  \
"12899","19750","27705","14565","27952","14692","29063","27362","12674","32152","4467","25994","21072","2262","18115","24704","12469","8142","2916","5639","9708","7890","4703","5374","3406","23508","8670","13033","28244","10344",  \
"3371","7658","18074","29630","20144","3778","29657","3242","16887","6868","15852","923","32170","9762","203","11429","19860","30028","30353","16762","19614","24471","8569","9067","7890","8420","21979","15723","19290","19380",  \
"25651","1548","13952","23338","25370","8575","15278","25863","6474","9111","26478","27566","1950","29125","20843","20512","4878","17693","5742","25601","20149","19534","29280","7057","26061","28076","31309","24498","9649","10538",  \
"30302","32743","10202","6744","23517","17490","7138","6760","26420","8116","12675","557","21998","369","8855","3096","16563","18312","23832","22076","5455","20637","19745","1099","12459","11762","18154","407","6353","30056",  \
"4303","25360","22250","13186","3401","26955","28994","32097","1266","8824","1347","8905","4228","11370","374","27","8921","5779","32643","28758","13035","25603","15928","24353","1493","11632","15229","31418","6351","25384",  \
"28251","1543","11061","12063","8447","19077","26751","30438","27311","10842","12874","32176","18905","21062","2637","9808","24068","2989","7267","21813"]
    EncOutString=["4E2422EB824DA07A","D725F95C72E0534C","A3E8C064553BB4E6","3AB41972E280424A","9FB4C3235B78A5D3","8F8E7842E1820E46","22451864ABC3960F","FE6662846AC2551F","F767864976852EDB","CA1185736604AA2C","AC678FABAEFB4D73","EE700AD0A353F48D","8BDF6B5E371EE50F","5720CB0BD1E8E882","F781F92DDC6F3ECE","B699E2AC3BF2D9D7","695A4D21FA838458","12B5B27ABFB33960","78CEBA63D11880BE","EBF4DEE12BFBE9FC","D87FF189B6B10279","A964F0088C5E9FCA","439741D3FF5CFBE6","275B5D2F700A653B","9F205DEC5A410A4A","711A9B98297AB10C","60DE83C2EECBF280","81BFC788B4C0653B","46FAC42B74D9E07D","396665C48B44CFF0",  \
"307BEA552A4B3072","DB1DE2D0AA22305D","91CF320437A31F03","C8631DFE15D38B5C","CF90371FD4C2A5F8","454246039786B2CF","C57CC8C5852D0CCF","86E218CCB79CE6B7","55735649F22DB204","417E448A9D7BE12A","BD9DA5B2F49A4746","A3C835B4440B95A4","2608744BDA1097EE","B9321CB93A2FB1DE","E4A51D238981C580","BEB2629CE4AB5E58","8AEECADE866490AB","12E8CD3EEA155868","7416BC77B36E45C8","5C370EAA07AEEB82","479F6C320A0A5CF7","A765E5B3DAFAA6A3","50C1DB709CE1C5D2","789CCA58221774FB","E1E2F03642F3EF25","F579224C7C0F2EA8","E39DB9AC8A8FCB5F","EBC7251AF649F803","468DBE6CC7879176","7D260A78CDC2C76F",  \
"3549EA348AB2B63D","91D92BD12B28AEFD","F154BFE53093FFB9","96C5511CA380E02D","50A55F8B920441DC","BD9C409C064A6F8A","44690110BCE0F50F","8860EF52E65AD648","26C8A7F938F812EB","5AD4A386DAB62CC4","3D35BE4A5D9CBB9B","E34F1F04E3344964","5EAFE1051AE4433E","26DB98381EB4B108","06F15ED78766189B","245B145201FD4A66","B18B8B6A90E63636","EC00D00153DAE11A","7D6A7A06C22B2AF9","B5D3F4AA8A1BEA25","5947C6384369CACE","E38785006D279BF9","26AD64A3FFF880A5","6F9089607C22CA2A","462D9B8C89F83A70","94A57A1A9FA769F8","E01D45D1EC92255A","8D8C8897CDD8D8B6","6515CA8AC03CF7A1","2EA09567B594517C",  \
"46720372BE2FA257","90279E2C9D381A66","FB59388374BA80FF","451D8B9D6089E0FF","B181E01185379D47","E80A16117750FA4A","99F093E2691708E7","049A1C6AD90461D3","E031E10280DE9E11","14062D65878EACAB","B2402BAC4F67FBF0","B821FAF11222E006","EE58A1C360794529","EDC4EA46254E9851","EE2E260975C33984","992DEF868B52E97D","FBB4B4955A6D2A8E","624528C2EE7366AE","85EB9169FDCD6632","E83EFFE7E43777C8","5F2B7E955565FB58","F91AA4444212C7E3","9441DC5414220FD8","D75E2E41EF5EF948","46F1324626C56BFF","9D39B3D95AFD2D50","01A0560D271D2A4D","D09E183E44DB6DB3","D735C48C884531F3","2258CC9F937F072D",  \
"3841AC923FD96D70","57F57F8EFBFC58DE","CCDA3DA872581354","46F5385D6EDD0FA3","FBDF819640E0E62E","73D9EEBE5D992F35","6EAD5B67B204DDEF","6CE17FCA3E2E8EDB","88109679784D5496","B2012D351D47B98A","2FC739546B4ABCA5","49459522BBD42595","062F62C8973CD460","51538A068A27F4EC","4A3F8C65834D5A03","658BF583F33B942D","8010C5525B2191B6","DF4741BF52F39DE8","7CB9F6A54383E71C","7BE51B023BBA0EA4","37D839B061FDA958","8D305F7980A39F19","F276024A02CABA3C","8F687C3519763B6E","A812CADCE08746A3","20E37BD79EE89DE5","63D8E3A0848E3BD7","6B72268FE098616C","B8FFF57F741267C0","1F7FCBED90022F86",  \
"5EC906E1144D75B1","678A6EA8858EB8B1","6EB69419EB3F2EFC","678A6EA8858EB8B1","67E61912202431FE","FD451ACDB476AFC9","6A24039E175CC959","0B3F22852E433BC6","4C0C9892F66DA959","77255713204153CD","92E32988D384A7BA","2BF1219ABEC2B393","AE61D540A75C9110","4B904C796584D5DA","22D24D70B64D14A4","B5194640087FA608","478CF3B194C0C219","A9360B19E6838FAD","0ACA3756520DB3D9","BA5BED21B51A5346","9BCD29598F46A546","E5E2F66335BD8565","C8FBB6BF64D8ACF5","09213872369375BC","DFE1514A027356F1","E56DCCB8BCE4B1AD","9E723F83007DD0AB","682CAC74A000ED10","DD39748EA9609693","4D52237E8BCD9207",  \
"EF05CA9BC96C05AE","1D773211817C71FF","C1FAD2E650E7694F","5BE7BFA7A1BCB9C8","EBDF6572C6BA13FB","98560C0B17AC14E2","3D8CD735FFE3F686","5510C5C2B6DBE328","804207E17A30583A","4BD0F11BC5B18BF1","1C38D1E2ACB37043","D7CD3F596D4EBC38","764714538F397343","A5B5BFB88EC60A60","EF6C88482D9B96C0","B846F3131BFC86C1","C08EF237EA5F4025","DFF7C8A9A06B94D5","700F7B70AEEE62D8","139D5909B9BF0538","200AF3F9846496FB","E36B96A2B66F3F23","2760DA4BD213FAE7","E8B785B4E62429AA","53065BB3DF024B4B","870C3AF2BB5CAB70","61BEFD212E0BA792","D81018EA0C7191F3","9FBEEE3AE0DCD6C3","A2DD86000F70FC63",  \
"628113D48E1B85CB","45A75B2EC766ABCC","C3E7333D720E9A26","E20751D6041DE2C4","5A80EAAF20123CF3","36105D6E95E3D841","40FF8748CB42DC6C","AD06F7A5C0063540","E033ED4E151E7EA1","800224CBDAFC6F39","FF14A0E3699DD469","E11C64AC9A59B53B","0FF42F18875873F0","1AF057FDDA2E472D","F540BA3646AA990E","5866D553B515C62B","98F42C60B5A9D8E3","62521EA4DAAEDADE","05EE27384ADB2346","177219BDB21920AA","71465F30E748515F","C7EE752CFE81B216","DE0E1F5A53576D9A","200F5E93BBDA5C84","037FC0BEAA9E8A8E","0E8486A760CC8EE5","AE471625BA531615","7A51CD6D9B95B053","9414ACB56F18658D","C757BAD43CF801FF",  \
"8AEECADE866490AB","CB44BA7671D3DC71","4BD2147435451D0C","22F228292C777D07","D0386C02D256749C","6CE8FA118DDB51BB","720C7EB6A933521B","B4D363D904485948","BA2419ABDAE95927","96A3F2BBC37A41EE","CCDB74C9D6EEEF38","74ACC8A079510710","3AD1C232797106ED","789FEE4871AE682C","857C95162A05541D","BE912CB37BA5F30D","5FEFC21647BADB3A","3819CD091E3E36FB","E6C853A8BE29ECD0","AA60EF77FAC26D77","EF82FF96B6CA4719","B06C58BCDF753138","3091DD9EEFC2D7C9","EA2353497384648E","4B1835B1DB0AD678","A95ACE655054E120","2A80195E9E811C38","739957E1C40C5301","DC77F5224ECB264F","DDB6225DEDCA4B7A",  \
"805DE7A215CD08D8","830E4C6F87CC80D8","F760359C3E1876B8","5C0E6B1DBAAF849F","3520549BFEA6580C","9E9E77FB0E281858","FFC13A8A35D4F975","53F59A5F08C16DF7","8D5EF95CD55697A9","2DB2B92E7D605C9D","801E0F933F922B33","D9DD8284286E9C38","B63404F6B264D654","A4C0439758040492","CFF0657D7C11427F","2A42603B3AE0D84C","613F78AB14C8B223","563BE61CDCDA5762","F87E0DABB028705A","F1904DE64DCBD959","254B853CA1A49ECA","881DA205FD3AB639","6BA4C86F8F626235","ED91227239FE9285","9695F4CB6566B7A8","D930C66F17F543B7","E04C09A19E511C78","F876BEDB6F31587F","3BBAAF85741E5F47","E3AD8B595EAEA460",  \
"07D279B94706942A","33C862BB896C00CB","144DE833672E47B7","170EEB0D75E121DD","ADD283D57DC497F9","31699595F765252A","7E5D70C58BF02474","AAA61786615528A8","E6DE58F10194C6DC","EE0383BA8A1D64C0","F095E49A36CB5EF5","744C7C3D58C6EF70","8058C3BACF72F6F2","3F90D11B32A03D14","631C616F99B984E6","C5CAF1B7ACD3C2C2","B56D089EDA18832A","291D4E84DF125498","8F69675DB87F52DD","963C88EFC4AF3605","1BC7B6D36C11ED4C","7F5334A404E276AF","E21D46814BF9D613","4EAFF8FA7955C117","D707177CC28933C6","3FD0D076768CFAAD","BE8E367C6DF0D94D","78FFC22C73CEE50D","0883E5B3DD1C6012","91E0846EF6ED832A",  \
"67512F5928F88785","CD1CDDC0289A1B52","98954017D5113371","E3CD1A2C81C30EC1","CCEF3474B87E34D0","2A9BED8269AFB44B","CE4E070EB8BA6A72","E73C29742251225F","7B1C1818338B9EEB","EF4D2CA08EFBFDB4","B9957189F52B60C0","8FB164C4D11AC219","EC7EE06E3C174CFC","5283B6552169D66D","63EEA58DCFB1E306","D42AD7CCCA800FEA","1CF830760DDB4516","CFF5BF43EC4EADD7","E4E3B4E7D6AAF0A4","B6A391984248310E","4041B60F7EB40C54","3D5887AA7D571725","8EB8CDEE698B9E17","6D119F4338447581","E2219638C9C3C5CC","923D7C6594F7A8A5","984D3CD0047842B7","5483A617DE582A27","3CAF3409D439636D","A2192072661B75E5",  \
"B4F66E615FDA1DEC","C8F44EC43F1D52D8","4087CD2CA787256A","BB1D1476D0D62B0F","8B3B2DBE23A34197","9C644A302C224124","A2B02EE19351FA76","07862BD79466140B","BDE63657F3AFB2C4","965B8ED0E9EC4F0D","E7E1E4E1A6DDC178","4BFDF4A534A7E1A0","E79B4AC7ABDC7AD5","D992EC774432ECA2","1851059AD159DB7B","97CFDEF7998C634C","4FFBCD0650377108","1C7E6F89DE9D2DAF","EAE53323660D4D8A","BD1EE749F426C81E","6DC4ADE3A58CCDB6","7FC5CCACA16946F2","44D7D8B2F77D9E25","00BBBE9DE704024E","3D5887AA7D571725","ADCD96ECCE65DDEF","CF55BD4CC5B5DDA9","17FC78D663C5E93E","366B058784BC3724","76C9CF575F25935A",  \
"3CF20FE5FD755688","ED9EEDD3732829D4","6DD16F87BF8DE6D0","F601AC1BC8B28031","5BC9728EFD0869EC","0AE4907D5927D052","E1E614D0601D976F","7C73B38EE97EDCB7","F8C6591A79AC3618","C248476E8277CF69","D9B5854AD9643363","2E0E6250F997D3F5","A19E84E2015F8BF4","1375A23D7001E231","1F70D3EA0869AF61","D171D49221CE9821","99EC88780CBA6425","32226A1AB1624BAE","DFF6639692443172","99E104DA2DE8300C","9867E8BCF7F5DAC7","0C33E1027F260817","8D8E2C8E8EDF1E5F","306D5E2BCE424701","1DF227DBBB3B51B6","FD3454D7934881A4","43144CFB13713681","55770398D929F16F","AA890D5D1FBA0635","C3A37A09811AA915",  \
"376DE1AC162B89D6","731A9221C6B27C6F","C344A525D35E02CB","062F62C8973CD460","4ED566FAA06D549C","87BAF24ADC28B999","FF18BF43288C2DE5","67EF66FB927E71A5","D52B053D5FC5557B","6BBCB55D2E902827","2AB2BD761EC42368","0D5830442A92FF8C","A72E8E085EE6DF73","79D9D333EEBF5C79","52B0CEBE6A50483A","1AFB11C94985A26F","597ED7199493CA9C","CB44CCB96662531E","86C29633184AE6E3","9E64015F1C50F3C8","DA10895976DFAD07","8875FF46F8AF3735","4D0715C5C3DEB366","F365372F30F46A58","D300C69575BFCC8C","F03091ACF403296C","B8413B2CACA44CEB","AC0017DB351822A0","FF6EE690BF8822FB","112CF99B6FBC61D2",  \
"41D083DD916E9D5C","5FDBA76D204E19CB","FE20353461260138","FEAEBD835ED72ACA","D8D3FC250FB9F4F0","E5D40A4A2EDE99F8","57C38122133B82CE","FB5A810D1866ED0B","02BCE3822C1A1966","37E413E091F7CA2F","FCECA04CC1B15DD8","3F26BC1D15E80ABE","C3740CA68E3AD8DA","101F5C24543001A4","FB02B0195B433903","F22BEAC6FC6A25C2","9E747A20BC1E31E1","614C0079AB69F1F9","A06AC9208E9676B2","4D4365A21B921E12","81437D64D8E0273A","1EF81B64C6208ABD","01B6BF7B2C2A859B","F35155D72555E254","825FC8CD7C5125CC","A712355875E8C58B","5E42B7DDC90C0BA8","75A870D9265AC914","9131727ACB303EF3","A81A0AE9EFA835D7",  \
"5F370395575F780C","359DE52C6C9807E8","F122496E1EF21B7B","038FDD4BFB966D98","092229C8A262D89B","1B367182AE63971A","8599BE5C87AC7195","8447F82E72D20861","477A786A886221A0","77F557D05F478809","587383A3FC165DB7","985001294C3EEB7A","A1F23FF6B6517D6B","5843722F517573F5","9EEA8E2FDDC42EDD","1C1827D5279EF53F","4A0D0904F86C71D6","8D54C0D3A0552085","6D8EC7A20181CB9D","630796EF3AF2BF99"]
#@NoUseNewKeyEx return 1 #���û��ʹ��������ܣ�ֱ�ӷ���1
#@NoSupNewKeyEx return 2 #��������֧��������ܣ�ֱ�ӷ���2
    myrnd=random.randint(1, (500 -1 ))
    mylen = len(EncInString[myrnd])+1
    if  mylen < 8 :
        mylen = 8 
    outstring = create_string_buffer((mylen* 2+1))#//ע�⣬����Ҫ??һ�����ȣ����ڴ������ѧ����
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


#ʹ����ǿ�㷨һ�����������������������Ч�ط�ֹ����
def CheckKeyByEncstring():
#�Ƽ����ܷ�����������������������������㣬ͬʱ�ڳ����ж�ʹ�ô�����ͬ���ļ������㣬Ȼ����бȽ��жϡ�
    DevicePath=create_string_buffer(260)
#@NoUseKeyEx return 1 #���û��ʹ��������ܣ�ֱ�ӷ���1
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
#//'ʹ����ǿ�㷨���ַ������м���
    nlen = len(InString) + 1
    if nlen < 8 :
          nlen = 8
    outstring = create_string_buffer((nlen * 2+1))#//ע�⣬����Ҫ��1һ�����ȣ����ڴ������ѧ��??
    outstring = StrEnc(InString, ''.encode('utf-8'))
    outstring_2 = create_string_buffer((nlen * 2+1))#//ע�⣬����Ҫ��1һ�����ȣ����ڴ������ѧ��??
    EncString(InString.encode('utf-8'),outstring_2,DevicePath)
    if outstring.lower()==outstring_2.value.decode('utf-8').lower():#//�ȽϽ���Ƿ����
         ret=0
    else:
         ret=-92
    return ret

#//ʹ�ô����ȵķ�����ָ���ĵ�ַ��ȡ�ַ���
def ReadStringEx(addr,DevicePath):
    InArray=c_ubyte*1
    blen = InArray(0)
#//�ȴӵ�ַ0������ǰд����ַ����ĳ�??
    ret = YReadEx(blen, addr, 1, 'D0C9E8D4'.encode('utf-8'), 'F133D9A2'.encode('utf-8'), DevicePath)
    if ret != 0 :
        return ''
    outstring=create_string_buffer(blen[0])		
#�ٴӵ�ַ1��ȡָ�����ȵ��ַ���
    ret = YReadString(outstring, addr+1, blen[0], 'D0C9E8D4'.encode('utf-8'), 'F133D9A2'.encode('utf-8'), DevicePath)
    if ret!=0:
        return ''
    return outstring.value


#//ʹ�ôӴ�������ȡ��Ӧ���ݵķ�ʽ����Ƿ����ָ���ļ�����
def CheckKeyByReadEprom():
    DevicePath=create_string_buffer(260)
#@NoUseCode_data return 1 #���û��ʹ��������ܣ�ֱ�ӷ���1
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

#ʹ����ͨ�㷨һ����ָ���ļ�����
def CheckKeyByFindort_2():
    DevicePath=create_string_buffer(260)
    ret=FindPort_2(0, 1, 1680413494, DevicePath)
    CloseDongle(DevicePath)
    return ret

def CloseDongle(DevicePath):
    if 'Linux' in platform.system():
        CloseUsbHandle(DevicePath)#�ر�USB�豸

