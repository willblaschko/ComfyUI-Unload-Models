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

class UnloadAllModelsNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {"value": (any, )},
        }

    @classmethod
    def VALIDATE_INPUTS(s, **kwargs):
        return True

    RETURN_TYPES = (any,)
    FUNCTION = "route"
    CATEGORY = "Unload Modules"

    def route(self, value):
        # Unload all models
        print("Unload Model:")
        print(" - Unloading all models...")
        model_management.unload_all_models()
        model_management.soft_empty_cache(True)
        try:
            print(" - Clearing Cache...")
            gc.collect()
            torch.cuda.empty_cache()
            torch.cuda.ipc_collect()
        except:
            print("      - Unable to clear cache")
        time.sleep(2)

        return (value,)
   

NODE_CLASS_MAPPINGS = {
    "UnloadAllModels": UnloadAllModelsNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "UnloadAllModels": "Unload ALL Models",
}
