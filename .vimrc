" enables markdown syntax for blog posts
call vam#ActivateAddons(["markdown@tpope"])

"macros for tag substituting markdown --> yaml [blog]
let @a='/[[!tag^M:s/\[\[!tag/-/^M:s/\]\]//g^M:s/^/    /g^MVd:4^Mp^M'
let @b=':goto 12^Mi"^[A"^['