
import tour
import agency

from ext import baseModel
from google.appengine.ext import db

class TourImages(baseModel.Model):

	$name 			= db.StringProperty ( default = "Name of place" )
	$description 	= db.StringProperty ( default = "A short description of the image" )
	$caption		= db.StringProperty ( default = "Caption to display on the image" )
	$date_taken		= db.StringProperty ( default = "Year picture was taken" )
	$src			= db.StringProperty ( default = "image url" )
	$tour 			= db.ReferenceProperty ( tour.Tour, collection_name = "??" )
	$agency			= db.ReferenceProperty agency.Agency, collection_name = "??" )
