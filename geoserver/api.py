from tastypie.resources import ModelResource
from .models import PollData


class PollDataResource(ModelResource):

    class Meta:
        queryset = PollData.objects.using('geoserver').all()
        resource_name = 'polldata'
        allowed_methods = ['get']
        filtering = {'poll_id': ('exact',)}
        # include all of the districts
        limit = 180

    def dehydrate(self, bundle):
        # Include the poll name
        # FIXME include the real poll name!
        bundle.data['poll_name'] = 'fgm'
        return bundle
