from rest_framework.throttling import SimpleRateThrottle


class RequestRateLimiter(SimpleRateThrottle):
    """Limiter to restrict each user to n requests per time frame."""

    # rate = '10/min'
    scope = 'users'

    def get_cache_key(self, request, view):
        return self.cache_format % {
            'scope': self.scope,
            'ident': self.get_ident(request=request)
        }
