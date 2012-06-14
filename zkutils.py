#!/usr/bin/python

import os,sys
import zookeeper
import time
from optparse import OptionParser

connected = False
zh = None

def check_connected(p1,p2,state,p4):
	global connected
	if state == zookeeper.CONNECTED_STATE:
		connected = True


def initialize(zkservers):
	global connected
	global zh
	zh = zookeeper.init(zkservers,check_connected)
	while True:
		if connected:
			break
		time.sleep(0.5)

def find(node_name):
	global zh
	yield node_name
	children = zookeeper.get_children(zh,node_name)
	for c in children:
		for f in find(os.path.join(node_name,c)):
			yield f

def find_leaves_first(node_name):
	global zh
	children = zookeeper.get_children(zh,node_name)
	for c in children:
		for n in find_leaves_first(os.path.join(node_name,c)):
			yield n
	yield node_name
	
def get_node(node_name):
	global zh
	return zookeeper.get(zh,node_name)

def delete_node(node_name):
	global zh
	return zookeeper.delete(zh,node_name)
