
from ext import baseModel
from google.appengine.ext import db

class Tour(baseModel.Model):

	$id 			= db.StringProperty ( default = "" )
	$name 			= db.StringProperty ( default = "" )
	$description 	= db.StringProperty ( default = "A short description about the tour" )
	$type	 		= db.StringProperty ( default = "" )
	$country		= db.StringProperty ( default = "" )
	$city			= db.StringProperty ( default = "" )
	$date_start		= db.DateTimeProperty ( )
	$date_end		= db.DateTimeProperty ( )	# URLProperty ?
	$price			= db.StringProperty ( default = "" )
	$images			= db.ListProperty ( db.Key )
