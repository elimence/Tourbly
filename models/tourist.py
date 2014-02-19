
from ext import baseModel
from google.appengine.ext import db

class Tourist(baseModel.Model):

	$name 			= db.StringProperty ( default = "" )
	$email		 	= db.StringProperty ( default = "" )
	$gender 		= db.StringProperty ( default = "" )
	$country		= db.StringProperty ( default = "" )
	$city			= db.StringProperty ( default = "" )
	$phone			= db.StringProperty ( default = "" )
