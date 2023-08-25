## My solutions to be-refactoring-test

1. Nested Data API Implementation

    - To resolve this question, I use [Nested Serializer](https://www.django-rest-framework.org/api-guide/serializers/#writable-nested-representations)

    - In addition, I'd like to `prefetch_related` to avoid N+1 problem and optimize database queries and manage related objects' retrieval in a more efficient manner. 

2. Prevent spamming API (Rate limit)

    - I overrode `rest_framework.throttles.BaseThrottle` to limit each IP to a maximum of 10 requests per minute to the endpoints.
    - Pros:
        - quite easy to implement: we generate unique cache key for each IP address then implement Sliding Window algorithm to identify if a certain request exceeds the request number limit within a time frame.
        - Request Rate Limiter is the most common kind of rate limiter in practice. We should start with it and may introduce other type of rate limiter as we scale (Concurrent requests limiter, Fleet usage load shedder)
    - Cons:
        - DRF's built-in throttle implementations are subject to race condition, so under high concurrency they may allow a few extra requests through. We may need implement your own throttle class to ensure our rate limiting requirements during concurrent requests. See more: https://github.com/encode/django-rest-framework/issues/5181

3. (Optional) Base Authentication Change
    There're at least two approach to this question.
    The first one is that we write our own custom authentication backend, similar to this article: https://reintech.io/blog/writing-custom-authentication-backend-django

    However, I notice we did install `dj_rest_auth` so I think I should get the idea from `dj_rest_auth.serializers.LoginSerializer`.

    For details, I have `user_id` and `password` as serializer fields. When a request comes in, we retrieve User instance with given request data then get value of `USERNAME_FIELD`. After that, `authenticate()` loop over list of `settings.AUTHENTICATION_BACKENDS` where we use default, built-in `django.contrib.auth.backends.ModelBackend`

 