import functools
import xmlrpc.client

HOST = "localhost"
PORT = 8069
DB = "testdb1"
USER = "admin"
PASS = "admin"
ROOT = "http://%s:%d/xmlrpc/" % (HOST, PORT)

# 1. Login
uid = xmlrpc.client.ServerProxy(ROOT + "common").login(DB, USER, PASS)
print("Logged in as %s (uid:%d)" % (USER, uid))

call = functools.partial(
    xmlrpc.client.ServerProxy(ROOT + "object").execute, DB, uid, PASS
)

# 2. Read the session
sessions = call("academy.session", "search_read", [], ["name", "seats"])
for session in sessions:
    print("Session %s (%s seats)" % (session["name"], session["seats"]))
# 3.create a new course

course = call(
    "academy.course",
    "create",
    {
        "name": "cs303RPC",
        "description": "record inserted from XML-RPC",
        "responsible_id": "2",
    },
)
