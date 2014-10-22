from api import TinderAPI
import models

class Session(object):
 def __init__(self, facebook_id, facebook_token):
  self._api=TinderAPI()
  # perform authentication
  self._api.auth(facebook_id, facebook_token)
  self.profile=models.Profile(self._api.profile(),self)
 def nearby_users(self):
  return map(lambda user: models.Hopeful(user, self), self._api.recs()['results'])
 def update_location(self,latitude,longitude):
  return self._api.ping(latitude,longitude)
 def matches(self):
  return map(lambda match: models.Match(match, self), self._api.matches())