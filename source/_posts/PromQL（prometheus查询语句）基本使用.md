title: PromQL（prometheus查询语句）基本使用
author: Muastu
date: 2024-01-11 14:59:19
tags: 
  - PromQL
  - Prometheus
categories: MiddleWare
---
**[官方参考文档](https://songjiayang.gitbooks.io/prometheus/content/promql/summary.html)**
  
PromQL(prometheus Query Language)是Prometheus自己开发的数据查询DSL语言。语言表现力非常丰富，内置含税很多，在日常数据可视化一级rule告警都会使用到。

## 查询结果类型
> PromQL查询结果主要有三种类型：
>* 瞬时数据(Instant vector)：包含一组时序，每个时序只有一个点，例如：http_requests_total
>* 区间数据(Range vector): 包含一组时序，每个时序有多个点，例如：http_requests_total[5m]
>* 纯量数据(Scalar): 纯量只是一个数字，没有时序，例如：count(http_requests_total)

## 查询条件
> Prometheus 存储的是时序数据，而它的时序是由名字和一组标签构成的，其实名字也可以写出标签的形式，例如 http_requests_total 等价于 {name="http_requests_total"}。
>* http_requests_total{code!="200"}  // 表示查询 code 不为 "200" 的数据
>* http_requests_total{code=～"2.."} // 表示查询 code 为 "2xx" 的数据
>* http_requests_total{code!～"2.."} // 表示查询 code 不为 "2xx" 的数据

## 操作符
Prometheus 查询语句中，支持常见的各种表达式操作符，例如：
#### 算术运算符
> 支持的算术运算符有 +，-，*，/，%，^  
> `%` 代表取余;`^`代表乘幂
>* http_requests_total * 2 表示将 http_requests_total 所有数据 double 一倍。  

#### 比较运算符
> 支持的比较运算符有 ==, !=, >, >=, <=,
>* http_requests_total > 100 表示 http_requests_total 结果中大于 100 的数据。

#### 逻辑运算符
> 支持的逻辑运算符有 and, or, unless,
>* http_requests_total == 5 or http_requests_total == 2 表示 http_requests_total 结果中等于 5 或者 2 的数据。

#### 聚合运算符
> 支持的聚合运算符有 
>* sum(求和),   
>* min(最小值),  
>* max(最大值), 
>* avg(平均值), 
>* stddev(标准差), 
>* stdvar(方差), 
>* count（计数）, 
>* coubt_values(某个valuse元素个数),  
>* bottomk(最小的k个元素),  
>* topk(最大的k个元素),   
>* quantile(分位数),  

> 聚合操作语法如下：
>* <aggr-op>([parameter,] <vector expression>) [without|by (<label list>)]  

> 其中`without`用来指定不需要保留的标签，`by`用来指定需要保留的标签。  
和四则运算一样，Prometheus的运算符也有优先级，它们遵从(^)>(*, /, %)>(+, -)>(==, !=, <=, <, >=, >)>(and, unless)>(or)的原则。

#### 内置函数

> Prometheus内置了许多函数，方便数据查询及格式化，例如将结果由浮点数转为整数的floor和ceil。更多函数详情请参考[官方文档](https://prometheus.io/docs/prometheus/latest/querying/functions/)。
