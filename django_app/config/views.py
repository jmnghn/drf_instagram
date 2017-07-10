from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


def index(request):
    return redirect('post:post_list')


class Index(APIView):
    def get(self, request):
        return Response({
            'post': reverse('post-list', request=request),
        })
