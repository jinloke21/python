
from optparse import OptionParser
import optparse
usage="python %prog -H <target host> -p/-P <target ports>"  #用于显示帮助信息
optParser=optparse.OptionParser(usage=usage)  #创建对象实例
optParser.add_option('-H',dest='Host',type='string',help='target host')   ##需要的命令行参数
optParser.add_option('-P','-p',dest='Ports',type='string',help='target ports', default="20,21")  ## -p/-P 都可以
(options,args)=parser.parse_args()
print(options.Host)
print(options.Ports)

