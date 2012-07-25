" enables markdown syntax for blog posts
call vam#ActivateAddons(["vim-markdown"], {"force_loading_plugins_now": 1})

"macros for tag substituting markdown --> yaml [blog]
let @a='/[[!tag^M:s/\[\[!tag/-/^M:s/\]\]//g^M:s/^/    /g^MVd:4^Mp^M'
let @b=':goto 12^Mi"^[A"^['
