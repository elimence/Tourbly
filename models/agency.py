
from ext import baseModel
from google.appengine.ext import db

class Agency(baseModel.Model):

	$name 			= db.StringProperty ( default = "New Agency" )
	$city			= db.StringProperty ( default = "" )
	$phone			= db.StringProperty ( default = "" )
	$country		= db.StringProperty ( default = "" )
	$address		= db.StringProperty ( default = "" )
	$website		= db.StringProperty ( default = "" )	# URLProperty ?
	$location 		= db.
	$description 	= db.StringProperty ( default = "A short description about the Agency" )
