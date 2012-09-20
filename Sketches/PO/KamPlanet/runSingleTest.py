#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-*-*- encoding: utf-8 -*-*-
# 
# Copyright 2010 British Broadcasting Corporation and Kamaelia Contributors(1)
#
# (1) Kamaelia Contributors are listed in the AUTHORS file and at
#     http://www.kamaelia.org/AUTHORS - please extend this file,
#     not this notice.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -------------------------------------------------------------------------
# Licensed to the BBC under a Contributor Agreement: PO

import libraries, sys, os, unittest

if len(sys.argv) != 2:
        print >> sys.stderr, "python %s <testfile>" % sys.argv[0]
        sys.exit(1)

testfile = sys.argv[1]

if not testfile.endswith('.py'):
        print >> sys.stderr, "python %s <testfile>" % sys.argv[0]
        sys.exit(2)

module_name = testfile[:-3].replace(os.sep,'.')

print "Running... %s" % module_name
sys.argv = [sys.argv[0]]
module =  __import__(module_name, globals(), locals(), [module_name])
suite = module.suite
unittest.main(defaultTest = 'suite')
