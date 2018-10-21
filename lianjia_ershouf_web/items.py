# -*- coding: utf-8 -*-
import scrapy


class LianjiaErshoufWebItem(scrapy.Item):
    MONGO_TABLE = 'ershouf'
    title = scrapy.Field() # 标题
    follow = scrapy.Field() # 关注人数
    view = scrapy.Field() # 带看人数

    link_id = scrapy.Field() # 链家编号
    community = scrapy.Field() # 小区
    address = scrapy.Field() # 所在区域
    age = scrapy.Field() # 建成年
    totalPrice = scrapy.Field() # 总价格
    unitPrice = scrapy.Field() # 每平方米价格

    houseType = scrapy.Field() # 房屋户型
    floor = scrapy.Field() # 所在楼层
    all_area = scrapy.Field() # 建筑面积
    structure = scrapy.Field() # 户型结构
    inner_area = scrapy.Field() # 套内面积
    architecturalType = scrapy.Field() # 建筑类型
    orientation = scrapy.Field() # 房屋朝向
    buildingStructure = scrapy.Field() # 建筑结构
    decorationSituation = scrapy.Field() # 装修情况
    ladder = scrapy.Field() # 梯户比例
    heatingMode = scrapy.Field() # 供暖方式
    elevators = scrapy.Field() # 配备电梯
    propertyAge = scrapy.Field() # 产权年限

    listingTime = scrapy.Field() # 挂牌时间
    tradingRights = scrapy.Field() # 交易权属
    lastTransaction = scrapy.Field() # 上次交易
    houseUsage = scrapy.Field() # 房屋用途
    ageLimit = scrapy.Field() # 房屋年限
    propertyBelong = scrapy.Field() # 产权所属
    mortgageInfo = scrapy.Field() # 抵押信息
    paper = scrapy.Field() # 房本备件


