# 项目描述
api 接口自动化项目

#环境准备
- python 3.6
- pytest 5.4.3

-其他依赖包
>pip install pytest-html==2.1.1 下载报告模板
> 
>pip install PyMySQL==0.9.3 下数据库版本包

> pip install pytest-base-url  匹配测试环境包
> 
> pip install allure-pytest==2.8.6  allrue报告插件下载 


.allure版本下载：https://github.com/allure-framework/allure2/releases（下载2.13.10有问题版本，2.13.10以下比较稳定）
下载包之后解压版本文件，将版本的bin目录下得路径添加到本地系统路径中,文件不要放在项目工程中，会报错虚拟内存不足的问题。



#执行用例
cmd 先cd到项目跟目录，执行命令
>pytest


- 生成测试报告，report文件下
> pytest --html=./report/test_report.html --self-contained-html


. 执行等级级别用例的命令
> pytest --alluredir ./report/report_allure --allure-severities=(级别参数例如:blocker)

. 生成allure测试报告命令,命令行运行
> pytest--alluredir ./report/report_alluredir(只是生成文件数据)

. 执行前清空之前的已下载的报告数据的执行命令(如果之前有遗留数据最好使用这个命令执行，可能回有部分修改用例无法覆盖掉
)
>pytest --alluredir ./report/report_allure --clean-alluredir

. 启动allure服务器，生成测试报告
> allure serve E:./report/report_allure(当前目录找到文件地址生成报告)


# 本地环境迁移
进入当前目录cmd入口输入命令
> pip freeze >requirements.txt 下载到本地所有配置

> pip install -r D:\api_project\requirements.txt
> 
> 这样就可以下载到本地所有的测试环境配置依赖包


# 注意事项
- 1: 配置文件logfixture，记得一定要配置在运行脚本文件夹下面，不然cmd文件运行会保存，但是在编辑器下面不会报错
- 2: base_url为可配置环境项，在但接口流程测试中需要自己代码中定义， 在fixture和测试代码中可以直接调用pytestini中的配置再不用定义。
- 3: pytestini中配置python_files= xxxx_test.py,意思就是执行为xxx前缀的庸碌  
- 4：pytestini中配置python_class=Demo*,执行文件中Demo开口的类工程
- 5：pytestini中配置python_functions=Demo*,匹配方法或者函数执行
- 5：soap接口协议和webseveics接口类型的传输数据是按照xml格式传输，自动化如果涉及到该
    类型接口，先下载库 
  >pip install suds-jurko
  
  (详情使用方法见地址：https://cloud.tencent.com/developer/article/1796727)
    
  
