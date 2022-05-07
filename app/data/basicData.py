import os
import pickle

# runtime data
recv_posts = pickle.dumps([])
server_list = []

socket = None
address = None
connected = False
client_id = None

createPostPopup = None
settingsPopup = None

# predefined data
user_name = str(os.getlogin())
server_address = ('127.0.0.1', 8775)
USE_DEFAULT_IMAGE = False
BLUR_IMAGE = False
POST_TYPE_IMAGE = 'image'
POST_TYPE_TEXT = 'text'
POST_TYPE_VIDEO = 'video'
POST_TYPE_AUDIO = 'audio'
POST_TYPE_FILE = 'file'
POST_TYPE_LINK = 'link'
POST_TYPE_SPOILER_NSFW = 'spoiler_nsfw'

# Design data
sizer_color = (1, 0.8, 0.2, 0.7)
post_background_color = (0.2, 0.2, 0.2, 0.5)
