# admitsanalysis
Tools for fetching and analyzing data from the Yale Admitted Students website.

The Admits website has lots of fun data on new admitted Yale students, however it's a little inconvenient to use (you must click through a paginated list of students and click on each to view information, and searching is unintuitive). `admits.py` will simulate a login (using the environment variables `$YALE_PORTAL_EMAIL` and `$YALE_PORTAL_PASSWORD`) to the website and scrape all the data in order to create a nice CSV which you can then process as you wish.

It will also output all admit profile photos into `photos/`.

## Authorship
Developed and maintained by [Erik Boesen](https://erikboesen.com).
## Licensing
[GPL](LICENSE)
