
import webapp2
import logging

# BASE HANDLER
from ext.BaseHandler import Handler



# APPLICATION ENTRY

class RenderPartial(Handler):
    def get(self):
        self.render("index.html",{"title": "My Angular App"})


# URI ROUTING

app = webapp2.WSGIApplication([

    # CLIENT SIDE PAGES (LET ANGULAR HANDLE ROUTING)
    ('/', RenderPartial),
    ('/view2', RenderPartial),
    ('/view3', RenderPartial)

], debug=True)          # CHANGE TO False BEFORE FINAL DEPLOYMENT
