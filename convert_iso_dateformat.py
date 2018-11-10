import datetime

date_format_twitter="%a %b %d %X %z %Y"
#datetime.datetime.strptime(date_string, format1).strftime(format2)
date_string="Sun Aug 05 18:03:45 +0000 2018"

datetime.datetime.strptime(date_string, date_format_twitter).isoformat()