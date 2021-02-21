"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""


import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
application = get_wsgi_application()

# ML registry
import inspect
from apps.ml.registry import MLRegistry
from apps.ml.nails_segmentation.nails_seg import NailsSegmenter

try:
    registry = MLRegistry() # create ML registry
    # Nails Segmentation model
    ns = NailsSegmenter()
    # add to ML registry
    registry.add_algorithm(endpoint_name="nails_segmenter",
                            algorithm_object=ns,
                            algorithm_name="segmentation",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="xyz",
                            algorithm_description="--",
                            algorithm_code=inspect.getsource(NailsSegmenter))

except Exception as e:
    print("Exception while loading the algorithms to the registry, oui", str(e))