# -*- coding: utf-8 -*-

from openerp import models, fields, api

class needs(models.Model):
    _name = 'ccb_firewall.needs'

    name = fields.Char(string="需求名称")
    source_areas = fields.Char(string="源区域")
    dst_areas = fields.Char(string="目的区域")
    source_ip = fields.Text(string="源IP")
    dst_ip = fields.Text(string="目的IP")
    control_points1 = fields.Text(string="访问控制点1")
    control_points2 = fields.Text(string="访问控制点2")
    control_points3 = fields.Text(string="访问控制点3")
    active = fields.Boolean(string="有效",default=True)




