#! /usr/bin/python3
import random
from mastodon import Mastodon
import argparse

def parseArgs():
    argparser = argparse.ArgumentParser(
        description="Esperanto Vortaro mastodon bot")
    argparser.add_argument("--debug", help="Debug (don't post to mastodon)",
                           dest="debug", action="store_true")
    argparser.add_argument("--wordlist",
                           help=("Wordlist filepath. "
                                 "Default: wl.txt"),
                           dest="wordlist_path", default="wl.txt")
    argparser.add_argument("--usercred",
                           help=("Usercred filepath. "
                                 "Default: usercred.secret"),
                           dest="usercred_path", default="usercred.secret")
    argparser.add_argument("--server",
                           help=("Mastodon server. "
                                 "Default: https://mastodon.social"),
                           dest="server", default="https://mastodon.social")
    argparser.add_argument("--no-check-api-version",
                           help=("Don't check API version. "
                                 "Useful for other servers like GtS"),
                           dest="no_check_api", action="store_true")
    argparser.add_argument("--visibility",
                           help="Post visibility. Default: public",
                           dest="post_visibility", default="public")
    args = argparser.parse_args()
    return args


def getFormat():
    dformats = [
            "English: \'{}.\'\nEsperanto: \'{}\'",
            "English: \'{}.\'\nEsperanto: \'{}\'",
            "English: \'{}.\'\nEsperanto: \'{}\'",
            "English: \'{}.\'\nEsperanto: \'{}\'",
            "English: \'{}.\'\nEsperanto: \'{}\'",
            "Instead of \'{}\', try saying \'{}\'",
            "The Esperanto for \'{}\' is \'{}\'",
            "The Esperanto for \'{}\' is \'{}\'",
            "The Esperanto for \'{}\' is \'{}\'",
            "{} = {}",
            "{} = {}",
            "Esperanto: \'{1}\'\nEnglish: \'{0}.\'"
        ]
    dl = len(dformats)
    dr = random.randint(0, dl - 1)
    return dformats[dr]

def getWordPair(fpath):
    with open(fpath, encoding="utf-8-sig") as f:
        content = f.readlines()
    wl = [x.strip() for x in content]
    l = len(wl)
    r = random.randint(0, l - 1)
    wpair = wl[r].split(" = ")
    return {
        "eng": wpair[0],
        "esp": wpair[1].capitalize()
    }

if __name__ == "__main__":
    args = parseArgs()
    word = getWordPair(args.wordlist_path)
    fstr = getFormat()
    tstr = fstr.format(word["eng"], word["esp"])
    print(tstr)

    if not args.debug:
        ver_checkmode = "none" if args.no_check_api else "created"
        mastodon = Mastodon(
            access_token = args.usercred_path,
            api_base_url = args.server,
            ratelimit_method='wait',
            version_check_mode=ver_checkmode
        )

        mastodon.status_post(tstr, visibility=args.post_visibility)
