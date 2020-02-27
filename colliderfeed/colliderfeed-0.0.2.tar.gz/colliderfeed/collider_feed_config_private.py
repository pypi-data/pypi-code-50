

_SYMBOLS          = sorted(["SQ", "DVN", "FCX", "COP", "PE"])
_VENDOR_KEY       = "GLKJSAF987SA98DF98A7SDF"
_WRITE_KEY        = "collider-write-key-2asdfaf2a0-asdfab-4asdf8-a485-1basdfdef047"
COLLIDER_FEED_CONFIG = {"template_url":"https://www.bigdata.co/query?function=SHOW_ME_THE_MONEY&symbol=SYMBOL&apikey=" + _VENDOR_KEY,
                       "symbols":list(map(lambda s:s.lower(), sorted(_SYMBOLS))),
                       "write_key":_WRITE_KEY,
                       "write_keys":[_WRITE_KEY for s in _SYMBOLS],
                       "budgets":[200 for s in _SYMBOLS],
                       "names":[s +'.json' for s in _SYMBOLS],
                       "delays":[70]}

