django 布局模板
简介
平时使用django时，所有配置都在settings.py中，开发环境和生产环境的 差异，布部署时要修改

根据各个环境把配置文件拆分为
setting
    conf
           base.py
           dev.py
           prod.py
           test.py

使用
    1、根据模板创建工程
    django-admin startproject --template=
    2、经常使用的变量放base.py 和 common/context_processors中，如STATIC_URL，在模板中就可以使用STATIC_URL变量
    <script  src="{{STATIC_URL}}js/jquery-2.2.3.min.js"></script>
    3、打印日志调试
    from common.log import logger
    logger.info('打印日志{0}'.format(需要打印的变量)
    日志存储在log中的root.log

