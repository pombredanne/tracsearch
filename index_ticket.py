#!/usr/bin/env python

import datetime
from trac import Trac
from search import Search


trac = Trac()
search = Search()
search.recreate()

week = datetime.timedelta(15)
for ticket, comments in trac.ticket(week):
    print ticket['summary']
    search.index(ticket, 'trac', 'ticket', id=ticket['id'], bulk=True)
    for comment in comments:
        search.index(comment, 'trac', 'comment', parent=ticket['id'], bulk=True)
search.flush()