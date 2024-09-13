import argparse
import requests
import json
import base64
from PIL import Image
import io

def classify_image(image_path, model_name, confusion_matrix, accuracy_graph, save_json):
    url = 'https://obliging-oarfish-oddly.ngrok-free.app/predict_api'
    files = {'file': open(image_path, 'rb')}
    data = {'model': model_name}
    
    try:
        response = requests.post(url, files=files, data=data)
        response.raise_for_status()
        predictions = response.json()
        print("Predictions:")
        for label, score in predictions.items():
            print(f"{label}: {score:.2f}")

        if save_json:
            with open('predictions.json', 'w') as f:
                json.dump(predictions, f)
            print("Predictions saved to predictions.json")

        if accuracy_graph:
            graph_url = 'https://obliging-oarfish-oddly.ngrok-free.app/class_prediction_graph'
            graph_data = {'predictions': predictions}
            graph_response = requests.post(graph_url, json=graph_data)
            if graph_response.status_code == 200:
                graph = graph_response.json()
                img_data = base64.b64decode(graph.get('class_prediction_graph').split(',')[1])
                img = Image.open(io.BytesIO(img_data))
                img.show()
            else:
                print(f"Error: Failed to get class prediction graph (Status code: {graph_response.status_code})")

        if confusion_matrix:
            print("Confusion matrix is not available. Instead, a class prediction graph is provided.")

    except requests.RequestException as e:
        print(f"Request failed: {e}")

def main():
    parser = argparse.ArgumentParser(description="Classify an image using a trained model.")
    parser.add_argument('-i', '--image', required=True, help="Path to the image file")
    parser.add_argument('-M', '--model', required=True, help="Model name to use for classification")
    parser.add_argument('--c', action='store_true', help="Get confusion matrix (not available, replaced with class prediction graph)")
    parser.add_argument('--g', action='store_true', help="Get accuracy graph")
    parser.add_argument('--json', action='store_true', help="Save predictions to JSON")
    args = parser.parse_args()

    classify_image(args.image, args.model, args.c, args.g, args.json)

if __name__ == '__main__':
    main()