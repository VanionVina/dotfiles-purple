config.load_autoconfig(False)

c.auto_save.session = True

c.content.cookies.accept = 'never'
c.content.cookies.store = False

config.set('content.cookies.accept', 'all', 'https://social.076.moe/*')
config.set('content.cookies.accept', 'all', 'http://127.0.0.1:7657/*')

c.content.blocking.enabled = True
c.content.blocking.hosts.block_subdomains = True
c.content.blocking.method = "both"
c.content.notifications.enabled = False

c.tabs.show = "multiple"
c.tabs.position = "left"
c.tabs.width = 200

c.zoom.default = "110%"

c.fonts.default_size = "11pt"

c.content.blocking.adblock.lists = ['https://easylist.to/easylist/easylist.txt', 'https://easylist.to/easylist/easyprivacy.txt', 'https://secure.fanboy.co.nz/fanboy-annoyance.txt', 'https://raw.githubusercontent.com/bogachenko/fuckfuckadblock/master/fuckfuckadblock.txt', 'https://www.i-dont-care-about-cookies.eu/abp/', 'https://abp.oisd.nl/']

c.content.blocking.hosts.lists = ["https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts",]

c.content.headers.user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"
#c.content.headers.accept_language = "en_US,en;q=0.5"
#c.content.headers.accept_language = "ja-JP,ja;q=0.9"
c.content.headers.do_not_track = True
c.content.webgl = False
c.content.canvas_reading = False

c.content.javascript.enabled = False
c.content.images = True

#c.url.searchengines = {"DEFAULT": "https://duckduckgo.com/?q={}"}
c.url.searchengines = {"DEFAULT": "https://paulgo.io/search?q={}"}
c.url.start_pages = "file:///home/sunny/Documents/1Other/NewPage/som.html"
c.url.default_page = "file:///home/sunny/Documents/1Other/NewPage/som.html"

config.bind('h', 'tab-prev')
config.bind('l', 'tab-next')
config.bind('j', 'scroll-px 0 100')
config.bind('k', 'scroll-px 0 -100')

c.colors.webpage.darkmode.enabled =  True
c.colors.webpage.bg = "#151025"

config.source('themes/onedark.py')
