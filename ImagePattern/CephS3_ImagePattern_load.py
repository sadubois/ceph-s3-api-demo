#!/usr/bin/python
# =====================================================================
#        File:  CephS3_ImagePattern_load.py
#    Location:  https://github.com/sadubois/ceph-s3-api.git
#   Launguage:  Python
#    Category:  s3-api-demo
#     Purpose:  Demonstrates Red Hat Ceph Storage RadowsGw/S3 Interface
#      Author:  Sacha Dubois, Red Hat
#
# Copyright (c) 2010 - 2012 Red Hat, Inc.
# This software is licensed to you under the GNU General Public License,
# version 2 (GPLv2). There is NO WARRANTY for this software, express or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
# along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
#
# Red Hat trademarks are not licensed under GPLv2. No permission is
# granted to use or replicate Red Hat trademarks that are incorporated
# in this software or its documentation.
# =====================================================================
# 18.04.2015  Sacha Dubois  new
# =====================================================================

import boto
import boto.s3.connection
import sys
import os

# --- CHECK S3 ACCESS_KEY ---
if os.environ.has_key("ACCESS_KEY"):
        access_key = os.environ['ACCESS_KEY']
else:
        print "ERROR: environment variable ACCESS_KEY is not set"
        print "  ie. export ACCESS_KEY=\"F8T4P40OCX8KD96SVDX0\""
        sys.exit(0)

# --- CHECK S3 SECRET_KEY ---
if os.environ.has_key("SECRET_KEY"):
        secret_key = os.environ['SECRET_KEY']
else:
        print "ERROR: environment variable SECRET_KEY is not set"
        print "  ie. export SECRET_KEY=\"mSTz7NNOpsn27cc03Rfez+FpHdV2lHn4BinLGG3N\""
        sys.exit(0)

print "# CEPH RADOSGW S3 CONNECTION DETAILLS"
print "SECRET_KEY='"+secret_key+"'"
print "ACCESS_KEY='"+access_key+"'"
print ""

conn = boto.connect_s3(
	aws_access_key_id = access_key,
	aws_secret_access_key = secret_key,
	host = '192.168.15.200',
	port = 80,
	is_secure=False,
	calling_format = boto.s3.connection.OrdinaryCallingFormat(),
	)

list = ['beige.jpg', 'blue.jpg', 'green.jpg', 'pink.jpg', 'white.jpg'];

bucket = conn.create_bucket('image-pattern')

bucket = conn.get_bucket("image-pattern")

print "=> Adding Pattern to Bucket: image-pattern"
for pattern in list:
  file = "images/"+pattern
  key = bucket.new_key(pattern)
  key.set_contents_from_filename(file)
  print "Adding Pattern: ", file

print "\n=> Show objects in Bucket: image-pattern"
for key in bucket.list():
        print "{name}\t{size}\t{modified}".format(
                name = key.name,
                size = key.size,
                modified = key.last_modified,
                )


#key = bucket.new_key('/etc/hosts')
#key.set_contents_from_filename('/etc/hosts')
#
#for key in bucket.list():
#        print "{name}\t{size}\t{modified}".format(
#                name = key.name,
#                size = key.size,
#                modified = key.last_modified,
#                )
