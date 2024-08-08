from vlc import EventType, Media, MediaPlayer, MediaParseFlag, Meta

def _media_cb(event, *unused):
    # XXX callback ... never called
    print(event)
# http://112.121.151.133:8147/live
# https://node-35.zeno.fm/15wnypt6by8uv?rj-ttl=5&rj-tok=AAABfDKF7kcA-7G6h4qIRegXKA
# https://radioindia.net/radio/mirchi98/icecast.audio
# http://d2q8p4pe5spbak.cloudfront.net/bpk-tv/9XJalwa/9XJalwa.isml/9XJalwa-audio_208482_und=208000-video=877600.m3u8
p = MediaPlayer()
# cmd1 = "sout=file/ts:%s" % outfile
media = Media("http://d2q8p4pe5spbak.cloudfront.net/bpk-tv/9XJalwa/9XJalwa.isml/9XJalwa-audio_208482_und=208000-video=877600.m3u8")  # , cmd1)
# media.get_mrl()
p.set_media(media)
p.play()

e = p.event_manager()
e.event_attach(EventType.MediaMetaChanged, _media_cb, media)
e.event_attach(EventType.MediaParsedChanged, _media_cb, media)


meta = {Meta.Album: None,
        Meta.Genre: None,
        Meta.NowPlaying: None,
        Meta.Title: None,
        Meta.ShowName: None,}


print(media.get_meta(Meta.Album),media.get_meta(Meta.Genre),media.get_meta(Meta.NowPlaying))

while True:  # loop forever
    # XXX using MediaParseFlag.local is not any different
    media.parse_with_options(MediaParseFlag.network, 2)  # 2 sec timeout