#!/usr/bin/env python
# encoding: utf-8
"""
fnordmetric.py

Copyright 2012 Stephen Holiday

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os
import hashlib
import redis
import json
import base64

class Fnordmetric:
    """
        A class to interact with the fnordmetric api
    """
    def __init__(self, host="localhost", port=6379, db=0):
        self.redis = redis.StrictRedis(host = host,
                                       port = port,
                                       db = db)

    def queue_event(self, event):
        """
            Function to send a new event to redis
        """
        event_id = base64.urlsafe_b64encode(os.urandom(33))
        
        self.redis.set("fnordmetric-event-%s"%event_id, json.dumps(event))
        self.redis.expire("fnordmetric-event-%s"%event_id, 60)
        self.redis.lpush("fnordmetric-queue", event_id)
            
    def event(self, eventtype, session=None):
        """
            Send an event to redis
        """
        if session:
            event = { "_type":eventtype, "_session":session}
        else:
            event = { "_type":eventtype }
        self.queue_event(event)
        
    def pageview(self, url, session=None):
        """
            Register a pageview with optional session key.
        """
        event = { "_type": "_pageview", "url": url}
        
        if session is not None:
            event["_session"] = session
        self.queue_event(event)
    
    def set_name(self, name, session):
        """
            Set the name for the given session.
        """
        event = { "_type": "_set_name", "name": name, "_session": session }
        self.queue_event(event)

    def set_picture(self, image_url, session):
        """
            Set the picture for the given session
        """
        event = { "_type": "_set_picture", "url": image_url, "_session": session }
        self.queue_event(event)

    def set_gravatar(self, email, session, default="identicon"):
        """
            Use a gravatar as image for the current session
        """
        if default not in ["mm", "identicon", "monsterid", "wavatar", "retro"]:
            raise ValueError('default must be one of "mm", "identicon", "monsterid", "wavatar", "retro"')
            
        key = hashlib.md5(email.strip().lower()).hexdigest()
        self.set_picture("http://www.gravatar.com/avatar/%s?s=40&d=%s"%(key, deafult), session)

"""
class FnordmetricTests(unittest.TestCase):
    def setUp(self):
        pass


if __name__ == "__main__":
    unittest.main()"""