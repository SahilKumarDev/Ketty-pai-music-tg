from KettyPai.core.bot import Gaana
from KettyPai.core.dir import dirr
from KettyPai.core.git import git
from KettyPai.core.userbot import Userbot
from KettyPai.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Gaana()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
