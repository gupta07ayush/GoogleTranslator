# GoogleTranslator
Google translator using python


googletrans 3.0.0
pip install googletrans

Free Google Translate API for Python. Translates totally free of charge.

Googletrans is a free and unlimited python library that implemented Google Translate API. This uses the Google Translate Ajax API to make calls to such methods as detect and translate.

Compatible with Python 3.6+..

# Features
Fast and reliable - it uses the same servers that translate.google.com uses
Auto language detection
Bulk translations
Customizable service URL
HTTP/2 support

# How does this library work
You may wonder why this library works properly, whereas other approaches such like goslate won’t work since Google has updated its translation service recently with a ticket mechanism to prevent a lot of crawler programs.

I eventually figure out a way to generate a ticket by reverse engineering on the obfuscated and minified code used by Google to generate such token, and implemented on the top of Python. However, this could be blocked at any time.

# Note on library usage
DISCLAIMER: this is an unofficial library using the web API of translate.google.com and also is not associated with Google.

The maximum character limit on a single text is 15k.

Due to limitations of the web version of google translate, this API does not guarantee that the library would work properly at all times (so please use this library if you don’t care about stability).

Important: If you want to use a stable API, I highly recommend you to use Google’s official translate API.

If you get HTTP 5xx error or errors like #6, it’s probably because Google has banned your client IP address.