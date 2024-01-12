---
title: Nginx安装部署
author: Muastu
tags: Nginx
categories: MiddleWare
abbrlink: 32308
date: 2024-01-11 14:55:36
---
* 安装nginx需要的依赖包

> yum install -y glib2-devel openssl-devel pcre-devel bzip2-devel perl-ExtUtils* zlib-devel gd-devel

* 下载nginx安装包

> wget http://nginx.org/download/nginx-1.14.2.tar.gz

* 解压安装包

> tar -xvf nginx-1.14.2.tar.gz

进入目录

cd nginx-1.14.2

* 检查nginx编译参数

> ./configure --prefix=/data/nginx --sbin-path=/data/nginx/sbin/nginx --conf-path=/data/nginx/conf/nginx.conf --error-log-path=/data/nginx/log/error.log --http-log-path=/data/nginx/log/access.log --pid-path=/data/nginx/log/pid/nginx.pid --lock-path=/data/nginx/log/lock/subsys/nginx --with-http_ssl_module --with-http_realip_module --with-http_addition_module --with-http_sub_module --with-http_dav_module --with-http_flv_module --with-http_gzip_static_module --with-http_stub_status_module --with-http_perl_module --with-ld-opt="-Wl,-E" --with-http_image_filter_module

* 编译并安装nginx

> make && make install

* 将nginx启动文件复制到/usr/bin下

> cp -p /data/nginx/sbin/nginx /usr/bin/

* 启动nginx

> nginx
