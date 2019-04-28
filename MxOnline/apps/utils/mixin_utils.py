# _*_ coding: utf-8 _*_
__author__ = 'wangtt'
__date__ = '2018/6/17 11:07'



from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class LogRequiredMixin(object):
    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LogRequiredMixin, self).dispatch(request, *args, **kwargs)



