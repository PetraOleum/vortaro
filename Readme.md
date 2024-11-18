# Roboto por esperanta vortaro

("_Robot for an Esperanto dictionary_")

This is a Mastodon bot that posts entries from a [English-Esparanto dictionary](http://www.gutenberg.org/ebooks/16967). It is hosted [@vortaro@botsin.space](https://botsin.space/@vortaro), and uses the [Mastodon.py](https://github.com/halcy/Mastodon.py) Python wrapper.

This is my first bot for either Twitter or Mastodon, and my first python program in a long time. It's not perfect, but it works.

## Source

The bot takes its wordlist from the utf-8 version of the above-linked dictionary, editing out the section headings and other elements that do not fit the pattern "(English) = (Esperanto).", e.g:

> Bed (river) = kuŝujo.

A handful of words I'd rather not have appear are removed, along with the first entry which for posterity reads:

> A = indefinite article, not used in Esperanto.

This is a very important feature of the language! It just doesn't fit the formulae I use.

## Usage

Obviously you're more likely to use this to make your own bot, but supposing you were going to deploy an exact copy this is what you would do:

1. Make an account on a Mastodon instance or another server with a Mastodon-compatible. Mark it as a bot and do all the other profile things.
2. Under Settings->Development create a new application, give it a name etc, leave the permissions as they are, and submit.
    * If you're not using Mastodon specifically you'll need to use whatever system works on your software, e.g. [these instructions](https://docs.gotosocial.org/en/latest/api/authentication/) for GoToSocial
3. Clone this repository onto whatever computer you want to run the app.
4. Using pip, download the Mastodon.py API interface. For example, `pip3 install --user Mastodon.py`.
5. Back on the website, find the application you created under Settings->Development->Your Applications, and copy its access token into a file named `vortaro.secret` in the same directory as `bot.py` _etc_.
    * Again, this depends on server software and UI
6. Run your app with `python3 bot.py`, or equivalent. If all is successful it will print to `stdout` as well as tooting.
    * Run with `--help` to see options; run with `--debug` to not post to the server.

