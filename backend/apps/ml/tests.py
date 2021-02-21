import inspect
from apps.ml.registry import MLRegistry
from django.test import TestCase
from apps.ml.nails_segmentation.nails_seg import NailsSegmenter

# ...
# the rest of the code
# ...

    # add below method to MLTests class:
def test_registry(self):
    registry = MLRegistry()
    self.assertEqual(len(registry.endpoints), 0)
    endpoint_name = "nails_segmenter"
    algorithm_object = NailsSegmenter()
    algorithm_name = "segmentation"
    algorithm_status = "production"
    algorithm_version = "0.0.1"
    algorithm_owner = "xyz"
    algorithm_description = "-"
    algorithm_code = inspect.getsource(NailsSegmenter)
    # add to registry
    registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
                algorithm_status, algorithm_version, algorithm_owner,
                    algorithm_description, algorithm_code)
        # there should be one endpoint available
    self.assertEqual(len(registry.endpoints), 1)

