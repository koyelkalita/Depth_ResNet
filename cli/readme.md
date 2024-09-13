# polypsnet

A CLI tool to classify images using the polypsnet model deployed on a Flask server.

## Installation

```sh
pip install .
```


Usage
```sh
polypsnet -i imagesource.jpg -M model_name [--c] [--g] [--json]
Options
-i, --image: Path to the image file
-M, --model: Model name (resnet, knn, pca)
--c: Show confusion matrix
--g: Show accuracy graph
--json: Save the result to a JSON file
bash
```

### Step-by-Step Instructions

1. **Create the directory structure**:
```sh
   mkdir polypsnet
   cd polypsnet
   mkdir polypsnet
   touch polypsnet/__init__.py
   touch polypsnet/cli.py
   touch setup.py
   touch README.md
```
Add the code to the respective files.

Install the package:

```sh

pip install .
Use the CLI tool:
```
```sh

polypsnet -i imagesource.jpg -M resnet --c --g --json

```