
import tour
import tourist
from ext import baseModel
from google.appengine.ext import db

class Review(baseModel.Model):
	$id 			= db.StringProperty ( )
	$reviewer	 	= db.ReferenceProperty ( tourist.Tourist, collection_name = "??" )
	$tour			= db.ReferenceProperty ( tour.Tour, collection_name = "??" )
	$rating			= db.IntegerProperty (  )
	$comment		= db.TextProperty ( default = "" )
