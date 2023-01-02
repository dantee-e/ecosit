import socket
if socket.gethostname()=="pop-os":
    from siteR.local_settings import *

else:
    from siteR.production_settings import *