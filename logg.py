#-*- coding: utf-8 -*-
import xbmc,logging
import sys,os

import uuid
import urllib,urllib2
    
def logGA(user,channel): 
 
  url = 'http://www.google-analytics.com/collect'
  cid = str(uuid.uuid1())
  cid=cid[cid.rfind('-')+1:]   
  tid='UA-63363282-5'
  build=xbmc.getInfoLabel( "System.BuildVersion" )
  build='Kodi ' + build[:build.find(' ')]
  values = {'v' : '1',
          'tid' : tid,
          'cid' : cid,
          'uid' : user,
          'ds' : 'Kodi',
          't'   : 'pageview',
          'dl' : 'c=%s' % (channel),
          'ua' : build + '-' + 'Movix' }
  print 'Log','c=%s' % (channel)        
  data = urllib.urlencode(values)
  req = urllib2.Request(url, data)
  response = urllib2.urlopen(req)
  #logging.warning('logga'+"?????????"*40)
  return
