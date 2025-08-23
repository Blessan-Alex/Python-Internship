from __future__ import annotations

import os
from pathlib import Path
from typing import Optional, Tuple

from PIL import Image


def resize_image(
    input_path: str,
    output_path: str,
    size: Tuple[int, int],
    format: Optional[str] = None,
) -> None:
    """Resize an image and save it to the output path.

    Args:
        input_path: Path to the input image
        output_path: Path to save the resized image
        size: Target size as (width, height)
        format: Output format (e.g., 'JPEG', 'PNG'). If None, uses input format.
    """
    try:
        with Image.open(input_path) as img:
            # Resize the image, maintaining aspect ratio
            resized_img = img.resize(size, Image.Resampling.LANCZOS)
            
            # Determine output format
            if format is None:
                format = img.format or 'JPEG'
            
            # Save the resized image
            resized_img.save(output_path, format=format, optimize=True)
            print(f"✓ Resized {input_path} -> {output_path}")
            
    except Exception as e:
        print(f"✗ Error processing {input_path}: {e}")


def batch_resize_images(
    input_folder: str,
    output_folder: str,
    size: Tuple[int, int],
    format: Optional[str] = None,
    extensions: Tuple[str, ...] = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff'),
) -> None:
    """Resize all images in a folder.

    Args:
        input_folder: Folder containing images to resize
        output_folder: Folder to save resized images
        size: Target size as (width, height)
        format: Output format. If None, preserves original format
        extensions: File extensions to process
    """
    input_path = Path(input_folder)
    output_path = Path(output_folder)
    
    # Create output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Find all image files
    image_files = []
    for ext in extensions:
        image_files.extend(input_path.glob(f"*{ext}"))
        image_files.extend(input_path.glob(f"*{ext.upper()}"))
    
    if not image_files:
        print(f"No image files found in {input_folder}")
        return
    
    print(f"Found {len(image_files)} images to process...")
    
    # Process each image
    for img_file in image_files:
        # Determine output filename
        if format:
            output_file = output_path / f"{img_file.stem}.{format.lower()}"
        else:
            output_file = output_path / img_file.name
        
        resize_image(str(img_file), str(output_file), size, format)


def main() -> None:
    """Example usage of the image resizer."""
    # Example: resize all images in 'sample_images' to 800x600
    input_dir = "sample_images"
    output_dir = "resized_images"
    target_size = (800, 600)
    
    if not os.path.exists(input_dir):
        print(f"Input directory '{input_dir}' not found. Creating sample images...")
        create_sample_images()
    
    print(f"Resizing images to {target_size[0]}x{target_size[1]}...")
    batch_resize_images(input_dir, output_dir, target_size)
    print("Done!")


def create_sample_images() -> None:
    """Create sample images for testing."""
    os.makedirs("sample_images", exist_ok=True)
    
    # Create a simple test image
    test_img = Image.new('RGB', (1200, 800), color='red')
    test_img.save("sample_images/test1.jpg", "JPEG")
    
    # Create another test image
    test_img2 = Image.new('RGB', (800, 1200), color='blue')
    test_img2.save("sample_images/test2.png", "PNG")
    
    print("Created sample images in 'sample_images/' directory")


if __name__ == "__main__":
    main()
