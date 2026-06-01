# Flickr API Changes

This document summarizes the human-facing API changes captured by this
repository.  It is manually maintained from `methods.lst` history and archived
method documentation diffs; it is not generated automatically.

Dates use ISO format (`YYYY-MM-DD`) and are the capture or commit dates in this
archive.  They are approximate observation dates, not necessarily Flickr's exact
release dates.

## 2026-05-31

### Method list refresh

Refreshed `methods.lst` from `flickr.reflection.getMethods`.  The reflected API
list increased from 206 to 224 methods.

Added:

- `flickr.galleries.removePhoto`
- `flickr.photos.getPopular`
- `flickr.photos.licenses.getAvailable`
- `flickr.photos.licenses.getLicenseHistory`
- `flickr.profile.getProfile`
- `flickr.stats.getMostPopularPhotoDateRange`
- `flickr.testimonials.addTestimonial`
- `flickr.testimonials.approveTestimonial`
- `flickr.testimonials.deleteTestimonial`
- `flickr.testimonials.editTestimonial`
- `flickr.testimonials.getAllTestimonialsAbout`
- `flickr.testimonials.getAllTestimonialsAboutBy`
- `flickr.testimonials.getAllTestimonialsBy`
- `flickr.testimonials.getPendingTestimonialsAbout`
- `flickr.testimonials.getPendingTestimonialsAboutBy`
- `flickr.testimonials.getPendingTestimonialsBy`
- `flickr.testimonials.getTestimonialsAbout`
- `flickr.testimonials.getTestimonialsAboutBy`
- `flickr.testimonials.getTestimonialsBy`

Removed:

- `flickr.groups.browse`

### `flickr.photos.search` documentation refresh

Refreshed the archived `flickr.photos.search` documentation page from the live
Flickr API documentation, comparing it with the 2014-11-10 archive baseline.
Most of the raw HTML diff is page chrome, but the method documentation changed
in these API-facing ways:

- Fixed the `sort` argument typo from "Deafults" to "Defaults".
- Added `content_types` for photo content filtering, including virtual photos.
- Added `video_content_types` for video, screencast, animation, and machinima
  filtering.
- Marked the legacy `content_type` argument as deprecated in favor of
  `content_types`.
- Removed the "Experimental" label from the `contacts` argument.
- Added error `5: User deleted` for a user id that does not match a Flickr
  user.

## 2014-11-10

### `flickr.photos.search` documentation baseline

Archived an HTML capture of the `flickr.photos.search` method documentation.
This baseline makes later argument and error-code changes visible in Git.

## 2013-05-27

### Cameras API

Added:

- `flickr.cameras.getBrandModels`
- `flickr.cameras.getBrands`

## 2012-08-23

### Group join requests

Added:

- `flickr.groups.joinRequest`

## 2012-05-28

### Group discussion info methods

Added:

- `flickr.groups.discuss.replies.getInfo`
- `flickr.groups.discuss.topics.getInfo`

## 2012-05-24

### Groups, discussions, contacts, people, suggestions, and tags

Added:

- `flickr.contacts.getTaggingSuggestions`
- `flickr.groups.discuss.replies.add`
- `flickr.groups.discuss.replies.delete`
- `flickr.groups.discuss.replies.edit`
- `flickr.groups.discuss.replies.getList`
- `flickr.groups.discuss.topics.add`
- `flickr.groups.discuss.topics.getList`
- `flickr.groups.join`
- `flickr.groups.leave`
- `flickr.people.getGroups`
- `flickr.people.getLimits`
- `flickr.photos.suggestions.approveSuggestion`
- `flickr.photos.suggestions.getList`
- `flickr.photos.suggestions.rejectSuggestion`
- `flickr.photos.suggestions.removeSuggestion`
- `flickr.photos.suggestions.suggestLocation`
- `flickr.tags.getMostFrequentlyUsed`

## 2012-01-15

### OAuth token check

Added:

- `flickr.auth.oauth.checkToken`

## 2011-10-15

### Push APIs and favorite context

Added:

- `flickr.favorites.getContext`
- `flickr.push.getSubscriptions`
- `flickr.push.getTopics`
- `flickr.push.subscribe`
- `flickr.push.unsubscribe`

## 2011-06-23

### OAuth access token

Added:

- `flickr.auth.oauth.getAccessToken`

## 2010-07-02

### Photoset bulk and ordering methods

Added:

- `flickr.photosets.removePhotos`
- `flickr.photosets.reorderPhotos`
- `flickr.photosets.setPrimaryPhoto`

## 2010-05-13

### Stats CSV export

Added:

- `flickr.stats.getCSVFiles`

## 2010-04-09

### Galleries API expansion

Added:

- `flickr.galleries.create`
- `flickr.galleries.editMeta`
- `flickr.galleries.editPhoto`
- `flickr.galleries.editPhotos`
- `flickr.galleries.getInfo`
- `flickr.galleries.getPhotos`
- `flickr.urls.lookupGallery`

## 2010-03-18

### People photos and restored test method

Added:

- `flickr.people.getPhotos`
- `flickr.test.echo`

## 2010-03-03

### Stats API

Added:

- `flickr.stats.getCollectionDomains`
- `flickr.stats.getCollectionReferrers`
- `flickr.stats.getCollectionStats`
- `flickr.stats.getPhotoDomains`
- `flickr.stats.getPhotoReferrers`
- `flickr.stats.getPhotoStats`
- `flickr.stats.getPhotosetDomains`
- `flickr.stats.getPhotosetReferrers`
- `flickr.stats.getPhotosetStats`
- `flickr.stats.getPhotostreamDomains`
- `flickr.stats.getPhotostreamReferrers`
- `flickr.stats.getPhotostreamStats`
- `flickr.stats.getPopularPhotos`
- `flickr.stats.getTotalViews`

Removed:

- `flickr.test.echo`

## 2010-01-21

### Galleries and people-in-photos methods

Added:

- `flickr.galleries.addPhoto`
- `flickr.galleries.getList`
- `flickr.galleries.getListForPhoto`
- `flickr.people.getPhotosOf`
- `flickr.photos.people.add`
- `flickr.photos.people.delete`
- `flickr.photos.people.deleteCoords`
- `flickr.photos.people.editCoords`
- `flickr.photos.people.getList`

## 2009-07-02

### Top places

Added:

- `flickr.places.getTopPlacesList`

## 2009-06-30

### Blog services

Added:

- `flickr.blogs.getServices`

## 2009-06-23

### Recent comments from contacts

Added:

- `flickr.photos.comments.getRecentForContacts`

## 2009-06-05

### Recent machine tag values

Added:

- `flickr.machinetags.getRecentValues`

## 2009-06-03

### Collections

Added:

- `flickr.collections.getInfo`
- `flickr.collections.getTree`

## 2009-03-03

### Panda methods

Added:

- `flickr.panda.getList`
- `flickr.panda.getPhotos`

### Group members

Added:

- `flickr.groups.members.getList`

## 2009-02-06

### Commons institutions

Added:

- `flickr.commons.getInstitutions`

## 2009-01-29

### Contacts and places

Added:

- `flickr.contacts.getListRecentlyUploaded`
- `flickr.places.getShapeHistory`
- `flickr.places.tagsForPlace`

## 2008-12-18

### Place types and place searches

Added:

- `flickr.places.getPlaceTypes`
- `flickr.places.placesForContacts`
- `flickr.places.placesForTags`

## 2008-12-05

### Geo correction and bounding-box places

Added:

- `flickr.photos.geo.batchCorrectLocation`
- `flickr.photos.geo.correctLocation`
- `flickr.photos.geo.photosForLocation`
- `flickr.photos.geo.setContext`
- `flickr.places.placesForBoundingBox`

## 2008-11-19

### Machine tags

Added:

- `flickr.machinetags.getNamespaces`
- `flickr.machinetags.getPairs`
- `flickr.machinetags.getPredicates`
- `flickr.machinetags.getValues`

## 2008-11-10

### Place hierarchy and URL lookup

Added:

- `flickr.places.getChildrenWithPhotosPublic`
- `flickr.places.getInfoByUrl`

## 2008-11-03

### Place info

Added:

- `flickr.places.getInfo`

## 2008-09-20

### Tag clusters

Added:

- `flickr.tags.getClusterPhotos`

## 2008-09-04

### User places

Added:

- `flickr.places.placesForUser`

## 2008-08-17

### Tag cluster list

Added:

- `flickr.tags.getClusters`

## 2008-03-24

### Geo preferences

Added:

- `flickr.prefs.getGeoPerms`

## 2008-03-06

### Initial captured baseline

Recorded the first non-empty captured method list in this Git history: 110
methods across these namespaces:

- `activity`: 2 methods
- `auth`: 4 methods
- `blogs`: 2 methods
- `contacts`: 2 methods
- `favorites`: 4 methods
- `groups`: 8 methods
- `interestingness`: 1 method
- `people`: 6 methods
- `photos`: 42 methods
- `photosets`: 15 methods
- `places`: 4 methods
- `prefs`: 4 methods
- `reflection`: 2 methods
- `tags`: 6 methods
- `test`: 3 methods
- `urls`: 5 methods
