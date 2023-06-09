# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/11/30 14:50
 Tool   : PyCharm
 Content: 模拟百度搜索
"""
import urllib, urllib2, cookielib


# urllib2 支持 http,https
def loginWeb(site, user, pwd):
    '''
    模拟网页登陆，登陆网址，用户名，密码不能为空
    登录post form 表单逻辑需要对应登录网站,可以使用火狐浏览器firebug插件查看登陆请求的网址和参数
    '''
    formValue = {'account': user,
                 'password': pwd,
                 # 这里可以根据网站添加相应的form表单
                 }

    # 启用cookie自动管理
    cj = cookielib.CookieJar()
    opender = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    # 伪装浏览器访问
    opender.addheaders = [('User-Agent',
                           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36')]
    # 绑定结果
    re = opender.open(site, urllib.urlencode(formValue))
    print
    re.getcode()
    print
    re.read()

    # 这里可以把抓取的网页内容，做 解析，判断是否登陆成功的逻辑

    # 登陆成功之后的带着cookie的页面访问
    pc = 'https://console.oray.com'  # 比如个人中心页面
    pcre = opender.open(pc)
    print
    pcre.getcode()
    print
    pcre.read()


if __name__ == '__main__':
    site = 'https://console.oray.com/passport/login'
    user = 'uname'
    password = 'upwd'
    loginWeb(site, user, password)