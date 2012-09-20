#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
#

# plays music at a whiteboard!

import Axon

from Axon.Component import component
from Axon.Ipc import WaitComplete, producerFinished, shutdownMicroprocess
from Kamaelia.Util.Console import ConsoleReader, ConsoleEchoer
from Kamaelia.Chassis.Graphline import Graphline
from Kamaelia.Chassis.Pipeline import Pipeline
from Kamaelia.Visualisation.PhysicsGraph.chunks_to_lines import chunks_to_lines
from Kamaelia.Visualisation.PhysicsGraph.lines_to_tokenlists import lines_to_tokenlists as text_to_tokenlists

#
# The following application specific components will probably be rolled
# back into the repository.
#

from Whiteboard.TagFiltering import TagAndFilterWrapper, FilterAndTagWrapper
from Whiteboard.Tokenisation import tokenlists_to_lines, lines_to_tokenlists

from Whiteboard.Canvas import Canvas
from Whiteboard.Painter import Painter
from Whiteboard.TwoWaySplitter import TwoWaySplitter
from Whiteboard.SingleShot import OneShot
from Whiteboard.CheckpointSequencer import CheckpointSequencer


# stuff for doing audio
import sys
sys.path.append("../pymedia/")
sys.path.append("../")
sys.path.append("../audio")
from Speex import SpeexEncode,SpeexDecode
from RawAudioMixer import RawAudioMixer as _RawAudioMixer

def RawAudioMixer():
    return _RawAudioMixer( sample_rate    = 8000,
                           readThreshold  = 0.5,
                           bufferingLimit = 2.0,
                           readInterval   = 0.1
                         ),

from Whiteboard.Entuple import Entuple
if __name__=="__main__":
    
    from Kamaelia.Internet.TCPClient import TCPClient
    from Kamaelia.File.Reading import RateControlledFileReader
    from Audio.Codec.PyMedia.Decoder import Decoder
    from Audio.PyMedia.Resample import Resample

    import sys
    try:
        if "--help" in sys.argv:
            sys.stderr.write("Usage:\n    ./MusicPlayer host port\n\n")
            sys.exit(0)
        rhost = sys.argv[1]
        rport = int(sys.argv[2])
    except:
        sys.stderr.write("Usage:\n    ./MusicPlayer host port\n\n")
        sys.exit(1)

#    rhost = "127.0.0.1"
#    rport=1500

    Pipeline(
        RateControlledFileReader("/home/matteh/music/Philip Glass/Solo Piano/01 - Metamorphosis One.mp3", readmode="bytes", rate=160*1024/8,chunksize=1024),
        Decoder("mp3"),
        Resample(sample_rate=44100, channels=2,
                 to_sample_rate=8000, to_channels=1),
        SpeexEncode(3),
        Entuple(prefix=["SOUND"],postfix=[]),
        tokenlists_to_lines(),
        TCPClient(host=rhost,port=rport),
    ).run()
    