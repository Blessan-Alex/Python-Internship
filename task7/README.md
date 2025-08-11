## Task 7: Image Resizer Tool

A Python script that resizes and converts images in batch using Pillow (PIL).

### Features
- Batch resize all images in a folder
- Convert between image formats (JPG, PNG, etc.)
- Maintains aspect ratio during resizing
- Error handling for corrupted images
- Creates sample images for testing

### Setup (Windows PowerShell)
```powershell
cd task7
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Usage

#### Basic usage
```powershell
python image_resizer.py
```
This will:
1. Create sample images if none exist
2. Resize all images in `sample_images/` to 800x600
3. Save results in `resized_images/`

#### Custom usage
```python
from image_resizer import batch_resize_images

# Resize all images in a folder
batch_resize_images(
    input_folder="my_images",
    output_folder="resized",
    size=(1024, 768),
    format="JPEG"  # Optional: convert to JPEG
)
```

### Functions

#### `resize_image(input_path, output_path, size, format=None)`
Resize a single image.

#### `batch_resize_images(input_folder, output_folder, size, format=None, extensions=(...))`
Process all images in a folder.

#### `create_sample_images()`
Create test images for demonstration.

### Supported Formats
- Input: JPG, JPEG, PNG, BMP, TIFF
- Output: Any format supported by Pillow

### Notes
- Uses LANCZOS resampling for high quality
- Preserves original format unless specified
- Creates output directories automatically
- Handles errors gracefully (continues processing other images)
