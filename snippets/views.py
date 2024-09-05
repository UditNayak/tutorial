from rest_framework import mixins
from rest_framework import generics
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

class SnippetList(mixins.ListModelMixin,  # Provides the list method to handle GET requests and list all objects.
                  mixins.CreateModelMixin, # Provides the create method to handle POST requests and create a new object.
                  generics.GenericAPIView): # A base class that provides the core functionality needed for handling typical view operations.
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs): # Using *args and **kwargs allows you to override methods without needing to worry about the specific arguments that might be passed in or their order.
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):  # Here generics.GenericAPIView do not provide any implementations of the methods, and it provides the core functionality, by mixing in the mixins.RetrieveModelMixin, mixins.UpdateModelMixin, and mixins.DestroyModelMixin classes.
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)