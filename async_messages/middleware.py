from distutils.version import StrictVersion

from django.contrib import messages
from django.utils.version import get_version

from async_messages import get_messages


class AsyncMiddleware(object):
    # In Django>=1.10 User.is_authenticated is a property, not a method but a
    # strange one : CallbableBool. 
    #  - If default User is used you can use it as a boolean either a method. 
    #  - If this property is overrided you may have a bool instead and an
    #    exception.
    # Fix it by checking if the property is callable or not. 
    def is_authenticated(self, request):
        if hasattr(request, "session") and hasattr(request, "user"):
            auth = request.user.is_authenticated
            return auth() if callable(auth) else auth
        else:
            return False

    def process_response(self, request, response):
        """
        Check for messages for this user and, if it exists,
        call the messages API with it
        """
        if self.is_authenticated(request):
            msgs = get_messages(request.user)
            if msgs:
                for msg, level in msgs:
                    messages.add_message(request, level, msg)
        return response
