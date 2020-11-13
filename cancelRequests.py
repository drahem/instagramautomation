from instagram_private_api import Client, ClientCompatPatch
import loginInfo

api = Client(loginInfo.username, loginInfo.password)
r = open("follow_req.txt", "r").read().split("\n")

for i in r:
  if bool(i):
    user_info = api.username_info(i)
    uid = user_info['user']['pk']
    api.friendships_destroy(uid)
    print ("Follow request cancelled for: "+i)

