#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/7/6
# @Author   : tangle
# @File     : bsgl_js_data.py

class JsJcfs_jcfs(object):
    """金数准备金缴存配置-缴存方式"""
    JCFS_BJC = "不缴存"
    JCFS_QEJC = "全额缴存"
    JCFS_BLJC = "比例缴存"
    JCFS_JEJC = "净额缴存"

class JsBscs_pjhl(object):
    """金数报送参数-启用平均汇率"""
    YES = "是"
    NO = "否"
