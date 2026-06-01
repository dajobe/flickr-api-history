# Flickr API Method History

This repository records the history of method names published by the Flickr
API.  It is a small data archive: the important file is `methods.lst`, and the
important view is the Git history of that file.

The list was captured by running the `list-methods` example program from
flickcurl.  That program calls Flickr's API reflection method:

```
flickr.reflection.getMethods
http://www.flickr.com/services/api/flickr.reflection.getMethods.html
```

Each time the published method list changed, `methods.lst` was updated and
committed.  As a result, the repository history shows roughly when Flickr added
new API methods.

The `archive/` directory stores occasional HTML captures of individual Flickr
API method documentation pages.  These are useful for method pages whose
arguments or prose change independently of the method name list.

## Reading The History

Use Git blame or annotate on `methods.lst` to see when each method first
appeared in this archive:

```
git blame --date=short methods.lst
```

For example, a line attributed to a 2010 commit means that the method was first
seen in one of my 2010 captures.  The date is approximate: it is the date of the
local capture and commit, not necessarily the exact date Flickr released or
documented the method.

To inspect the method-list changes over time:

```
git log --follow --stat -- methods.lst
git log --follow -p -- methods.lst
```

## File Format

`methods.lst` contains one Flickr API method name per line, sorted
alphabetically.  There is no extra metadata in the file itself; the metadata is
in Git:

- commit date: when the snapshot was recorded
- commit message: a short note about the newly observed methods
- blame output: the first recorded commit for each current line

Because deleted or renamed API methods would disappear from the current file,
use the full Git history rather than only the latest checkout when researching
older states of the API.

## Updating

Refresh the reflected method list with:

```
make update
```

This writes a temporary fresh method list, shows a unified diff against
`methods.lst`, and then replaces `methods.lst`.

Check an archived method documentation page for text changes with:

```
make check-method-doc METHOD_DOC=flickr.photos.search
```

This fetches the current method documentation page, extracts normalized text
from the archived and current HTML with a small Python helper, and shows a text
diff if the documentation changed.  The archived HTML is not replaced by this
check; if there is a change, the fetched HTML is left next to the archive with a
`.new` suffix for inspection.

For the archived `flickr.photos.search` page, the shorter alias is:

```
make check-photos-search-doc
```

## Development

Python helpers use the same `uv` workflow as my other small tools.  The minimum
Python version is 3.11, recorded in `.python-version` and `pyproject.toml`.

Set up the environment and run the checks with:

```
make dev-init
```

Or run individual checks:

```
make format
make typecheck
make test
```

## Provenance

This archive began as raw snapshot files, then moved through RCS and CVS before
being converted to Git.  Some conversion artifacts may remain, and the oldest
timestamps should be treated with care.  In particular, the original conversion
used UTC for some history.

Dave Beckett  
<http://www.dajobe.org/>  
2009-06-04
