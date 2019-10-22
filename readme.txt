照着django的pdf所做的项目练习

工具：
数据库：sqlite
前端：bootstrap（jquery.js,popper.js--下拉组件） markdown

项目名称：论坛系统
	板块：boards（只有管理员可以创建）
	主题：topics
	回帖：post

	boards:
		name//名字
		description//描述

	topcis:
		subject//主题内容
		board//属于哪个板块
		starter//发起人
		last_update//更新日期

	post:
		message//回复内容
		topic//输入哪个主题
		create_by//回复人
		create_at//创建时间
		update_at//更新时间