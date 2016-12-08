# -*- coding: utf-8 -*-
from openerp import http
from IPy import IP
import os,re
import json
class CcbFirewall(http.Controller):
    @http.route('/ccb_firewall/needs/', auth='public')
    def index(self, **kw):
        print http.request.httprequest.remote_addr
        return http.request.httprequest.remote_addr
        #return http.request.render('ccb_firewall.search')

    @http.route('/ccb_firewall/needs/objects/', type='http', auth="public", methods=['POST'])
    def list(self, **post):
        src_ip=post['source_ip'].strip()
        dst_ip=post['dst_ip'].strip()
        objects = []
        objs = http.request.env['ccb_firewall.needs'].search([])
        if src_ip.lower() == "any":
            if dst_ip.lower() == "any":
                #return http.request.render('ccb_firewall.listing', {
                    #'root': '/ccb_firewall/needs',
                    #'objects': http.request.env['ccb_firewall.needs'].search([]).ids,
                #})
                return repr(http.request.env['ccb_firewall.needs'].search([]).ids)
            else:
                for obj in objs:
                    if obj.dst_ip.strip().find('.') < 0:
                        continue
                    if obj.dst_ip.strip().find('\r\n') >= 0:
                        dsts = obj.dst_ip.strip().split('\r\n')
                    elif obj.dst_ip.strip().find('\n') >= 0 :
                        dsts = obj.dst_ip.strip().split('\n')
                    elif obj.dst_ip.strip().find('\r') >= 0 :
                        dsts = obj.dst_ip.strip().split('\r')
                    else:
                        dsts = obj.dst_ip.strip().split(' ')
                    if obj.dst_ip.strip() == "any":
                        objects.append(obj.id)
                    else:
                        for dst in dsts:
                            dst = dst.strip()
                            if IP(dst_ip) in IP(dst):
                                objects.append(obj.id)
                                break
                #return http.request.render('ccb_firewall.listing', {
                    #'root': '/ccb_firewall/needs',
                    #'objects': objects,
                #})
                return repr(objects)
        else:
            if dst_ip.lower() == "any":
                for obj in objs:
                    if obj.source_ip.strip().find('.') < 0:
                        continue
                    if obj.source_ip.strip().find('\r\n') >= 0:
                        srcs = obj.source_ip.strip().split('\r\n')
                    elif obj.source_ip.strip().find('\n') >= 0:
                        srcs = obj.source_ip.strip().split('\n')
                    elif obj.source_ip.strip().find('\r') >= 0:
                        srcs = obj.source_ip.strip().split('\r')
                    else:
                        srcs = obj.source_ip.strip().split(' ')
                    if obj.source_ip.strip() == "any":
                        objects.append(obj.id)
                    else:

                        for src in srcs:
                            src = src.strip()
                            if IP(src_ip) in IP(src):
                                objects.append(obj.id)
                                break
                #return http.request.render('ccb_firewall.listing', {
                    #'root': '/ccb_firewall/needs',
                    #'objects': objects,
                #})
                return repr(objects)
            else:
                for obj in objs:
                    if obj.source_ip.strip().find('.') < 0 or obj.dst_ip.strip().find('.') < 0:
                        continue
                    if obj.source_ip.strip().find('\r\n') >= 0:
                        srcs = obj.source_ip.strip().split('\r\n')
                    elif obj.source_ip.strip().find('\n') >= 0:
                        srcs = obj.source_ip.strip().split('\n')
                    elif obj.source_ip.strip().find('\r') >= 0:
                        srcs = obj.source_ip.strip().split('\r')
                    else:
                        srcs = obj.source_ip.strip().split(' ')

                    if obj.dst_ip.strip().find('\r\n') >= 0:
                        dsts = obj.dst_ip.strip().split('\r\n')
                    elif obj.dst_ip.strip().find('\n') >= 0:
                        dsts = obj.dst_ip.strip().split('\n')
                    elif obj.dst_ip.strip().find('\r') >=0:
                        dsts = obj.dst_ip.strip().split('\r')
                    else:
                        dsts = obj.dst_ip.strip().split(' ')
                    if obj.dst_ip.strip() == "any" and obj.source_ip.strip() == "any":
                        objects.append(obj.id)
                    else:
                        for src in srcs:
                            src = src.strip()
                            if obj.dst_ip.strip() == "any":

                                if IP(src_ip) in IP(src):
                                    objects.append(obj.id)
                                    break
                            elif src == "any":
                                for dst in dsts:
                                    dst = dst.strip()
                                    if IP(dst_ip) in IP(dst):
                                        objects.append(obj.id)
                                        break
                                else:
                                    continue
                                break
                            else:
                                for dst in dsts:
                                    dst = dst.strip()
                                    if IP(src_ip) in IP(src) and IP(dst_ip) in IP(dst):
                                        objects.append(obj.id)
                                        break
                                else:
                                    continue
                                break
                #return http.request.render('ccb_firewall.listing', {
                        #'root': '/ccb_firewall/needs',
                        #'objects': objects,
                #})
                return repr(objects)


    # @http.route('/ccb_firewall/needs/objects/<model("ccb_firewall.needs"):obj>/', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('ccb_firewall.object', {
    #         'object': obj
    #     })