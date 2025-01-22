# BLIP Visual Question Answering

This project uses the BLIP model to perform visual question answering on images.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/jimmy7707/blip-vqa.git
   cd blip-vqa
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place your image in the same directory as `app.py` and rename it to `image.jpg` (or update the path in the script).
2. Run the script:

   ```bash
   python app.py
   ```

## Dependencies

- `transformers` (for loading the BLIP model)
- `Pillow` (for handling images)
- `torch` (for running the model)

## License

This project is licensed under the MIT License.
