#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#

import wsgiref.handlers
from google.appengine.ext import webapp

class MainHandler(webapp.RequestHandler):

  def get(self):
    self.response.out.write("""
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta name="description" content="paul perry">
<meta name="keywords" content="paul perry">
<meta http-equiv="Content-Type" content="text/html; charset=US-ASCII">
<meta http-equiv="refresh" content="5;url=http://blog.paulperry.net">
<title>paul perry</title>

<style type="text/css">
.hidelink {text-decoration:none;}
.menu {text-decoration:none;font-family:arial;color:#798CB3;}
.menu:visited {text-decoration:none;font-family:arial;color:#798CB3;}
.menu:link {text-decoration:none;font-family:arial;color:#798CB3;}
.menu:hover {text-decoration:none;font-family:arial;color:red;}
BODY
{
    PADDING-RIGHT: 0px;
    PADDING-LEFT: 0px;
    PADDING-TOP: 0px;
    MARGIN: 0px;
}
</style>
</head>
<body bgcolor="#204080">
<center>
<table><tr><td>
<font face="arial" size="20"><a href="http://blog.paulperry.net" target="_top" class="menu">paul perry</a></font>
</td></tr>
<tr>
<td valign=bottom align=left><span style="color:#798CB3;font-size:11pt;font-weight:bold">
&nbsp&nbsp&nbsp&nbsp&nbsp<a href="http://blog.paulperry.net" class="menu">blog</a>
&nbsp | &nbsp <a href="/about/about.asp" class="menu">about</a>
&nbsp | &nbsp <a href="/notes/notes.asp" class="menu">notes</a>
</td></tr>
</table>
</center>
</body>
</html>
""")


def main():
  application = webapp.WSGIApplication([('/', MainHandler)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
