import comfy.model_management as model_management
import gc
import torch
import time

# Hack: string type that is always equal in not equal comparisons
class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False

# Our any instance wants to be a wildcard string
any = AnyType("*")

class DeleteAnyObject:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {"value": (any, )},
            "optional": {"object": (any, )},
        }

    @classmethod
    def VALIDATE_INPUTS(s, **kwargs):
        return True

    RETURN_TYPES = (any, )
    FUNCTION = "route"
    CATEGORY = "Unload Modules"

    def route(self, **kwargs):
        
        # Remove object if we can
        print("Delete Object:")
        
        try:
            print(" - Deleting Object...")
            obj = kwargs.get("object")
            delete_recursively(obj)
        except:
            print("      - Unable to delete object cache")

        try:
            print(" - Clearing Cache...")
            gc.collect()
            torch.cuda.empty_cache()
            torch.cuda.ipc_collect()
        except:
            print("      - Unable to clear cache")
        time.sleep(2)

        return (list(kwargs.values()))
   

def delete_recursively(obj):
    # Handle dictionaries
    if isinstance(obj, dict):
        for key in list(obj.keys()):
            delete_recursively(obj[key])
            del obj[key]
    # Handle lists
    elif isinstance(obj, list):
        for item in obj:
            delete_recursively(item)
        obj.clear()
    # Handle sets
    elif isinstance(obj, set):
        for item in obj:
            delete_recursively(item)
        obj.clear()
    # Handle tuples (tuples are immutable, so we just delete the references)
    elif isinstance(obj, tuple):
        for item in obj:
            delete_recursively(item)
    # Handle custom objects
    elif hasattr(obj, "__dict__"):
        for attr in list(obj.__dict__.keys()):
            delete_recursively(getattr(obj, attr))
            delattr(obj, attr)
    # Handle objects with slots
    elif hasattr(obj, "__slots__"):
        for slot in obj.__slots__:
            delete_recursively(getattr(obj, slot))
            delattr(obj, slot)

    # Delete the object itself if it's not a basic type
    del obj

NODE_CLASS_MAPPINGS = {
    "DeleteAnyObject": DeleteAnyObject,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DeleteAnyObject": "Delete Any Object",
}
