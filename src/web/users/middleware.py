from django import shortcuts, http


class UserProfileMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        request.user_profile = None
        if request.user.is_authenticated:
            if not hasattr(request.user, 'user_profile'):
                # It's here to avoid infinity redirects. Only school's views
                # are redirecting to user's profile.
                if hasattr(request, 'school'):
                    redirect_url = shortcuts.resolve_url('user:profile')
                    return http.HttpResponseRedirect(redirect_url)
        return None
