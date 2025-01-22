import warnings
from transformers import AutoProcessor, AutoModelForVisualQuestionAnswering
from PIL import Image

def main():
    # Suppress specific warnings
    warnings.filterwarnings("ignore", message="Using the model-agnostic default `max_length`")
    
    # Load the model and processor
    processor = AutoProcessor.from_pretrained("Salesforce/blip-vqa-base")
    model = AutoModelForVisualQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base")

    # Load the image
    image_path = "image.jpg"  # Change this to your local image path
    image = Image.open(image_path)

    # Define the question
    question = "Describe the photo for me?"

    # Process the input
    inputs = processor(image, question, return_tensors="pt")
    
    # Generate the answer
    out = model.generate(**inputs)
    
    # Print the result
    print(processor.decode(out[0], skip_special_tokens=True))

if __name__ == "__main__":
    main()
