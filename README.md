# ComfyUI Unload Model Memory Management

This repository provides developers with a way to better manage their ComfyUI model memory. It includes nodes that allow developers to either unload all models or unload one model at a time. These nodes are designed as pass-through nodes, so they can be used anywhere in the flow. The nodes can be found in the "Unload Model" section.

These are massive hammers, and it could be possible to break things, please don't use them if you need finesse.

## Features

- **Unload One Model**: Unload a specific model from memory.
- **Unload All Models**: Unload all models from memory.
- **Delete Any Object**: Delete any object from memory and clear the cache.

## Nodes

### Unload One Model

**File**: `unload_one_model.py`

This node allows you to unload a specific model from memory.

### Unload All Models

**File**: `unload_all_models.py`

This node allows you to unload all models from memory.

### Delete Any Object

**File**: `delete_any_object.py`

This node allows you to delete any object from memory and clear the cache.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/willblaschko/ComfyUI---Unload-Models
    ```
2. Navigate to the repository directory:
    ```sh
    cd comfyui-model-memory-management
    ```
3. Follow the instructions to integrate the nodes into your ComfyUI environment.

## Usage

1. Import the necessary files into your ComfyUI project.
2. Use the nodes `UnloadOneModel`, `UnloadAllModels`, and `DeleteAnyObject` as needed to manage your model memory effectively.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or enhancements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
