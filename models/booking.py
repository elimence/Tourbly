
import tour

from ext import baseModel
from google.appengine.ext import db


class Booking(baseModel.Model):

	$id 			= db.StringProperty ( default = "New Agency" )
	$tour		 	= db.ReferenceProperty ( tour.Tour, collection_name = "booked_tour_set" )
	$num_tourist 	= db.IntegerProperty()
	$date_booked	= db.DateTimeProperty ( auto_now_dd = True )
