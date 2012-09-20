# -*- coding: utf-8 -*-
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
"""\
This is a deprecation stub, due for later removal.
"""

import Kamaelia.Support.Deprecate as Deprecate
from Kamaelia.File.UnixProcess import UnixProcess as __UnixProcess

Deprecate.deprecationWarning("Use Kamaelia.File.UnixProcess instead of Kamaelia.File.UnixPipe")

Pipethrough = Deprecate.makeClassStub(
    __UnixProcess,
    "Use Kamaelia.File.UnixProcess:UnixProcess instead of Kamaelia.File.UnixPipe:Pipethrough",
    "WARN"
    )

# def __foo(*larg, **darg):
#     return __Pipeline(*larg,**darg)
#
# foo = Deprecate.makeFuncStub(__foo, message="blob")
