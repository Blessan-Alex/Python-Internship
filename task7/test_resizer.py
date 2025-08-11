import unittest
import os
import tempfile
from pathlib import Path
from PIL import Image

from image_resizer import resize_image, batch_resize_images, create_sample_images


class ImageResizerTestCase(unittest.TestCase):
    def setUp(self):
        # Create temporary directories for testing
        self.test_dir = tempfile.mkdtemp()
        self.input_dir = os.path.join(self.test_dir, "input")
        self.output_dir = os.path.join(self.test_dir, "output")
        os.makedirs(self.input_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Create a test image
        self.test_image_path = os.path.join(self.input_dir, "test.jpg")
        test_img = Image.new('RGB', (100, 100), color='red')
        test_img.save(self.test_image_path, "JPEG")

    def tearDown(self):
        # Clean up temporary files
        import shutil
        shutil.rmtree(self.test_dir)

    def test_resize_single_image(self):
        """Test resizing a single image."""
        output_path = os.path.join(self.output_dir, "resized.jpg")
        resize_image(self.test_image_path, output_path, (50, 50))
        
        # Check that output file exists and has correct size
        self.assertTrue(os.path.exists(output_path))
        with Image.open(output_path) as img:
            self.assertEqual(img.size, (50, 50))

    def test_batch_resize_images(self):
        """Test batch resizing multiple images."""
        # Create another test image
        test_img2 = Image.new('RGB', (200, 150), color='blue')
        test_img2.save(os.path.join(self.input_dir, "test2.png"), "PNG")
        
        batch_resize_images(self.input_dir, self.output_dir, (75, 75))
        
        # Check that both images were processed
        expected_files = ["test.jpg", "test2.png"]
        for filename in expected_files:
            output_path = os.path.join(self.output_dir, filename)
            self.assertTrue(os.path.exists(output_path))
            
            with Image.open(output_path) as img:
                self.assertEqual(img.size, (75, 75))

    def test_format_conversion(self):
        """Test converting image format."""
        output_path = os.path.join(self.output_dir, "test.png")
        resize_image(self.test_image_path, output_path, (50, 50), format="PNG")
        
        self.assertTrue(os.path.exists(output_path))
        # Check that it's actually a PNG
        with Image.open(output_path) as img:
            self.assertEqual(img.format, "PNG")

    def test_create_sample_images(self):
        """Test creating sample images."""
        sample_dir = os.path.join(self.test_dir, "samples")
        os.makedirs(sample_dir, exist_ok=True)
        
        # Temporarily change to sample directory
        original_cwd = os.getcwd()
        os.chdir(sample_dir)
        
        try:
            create_sample_images()
            
            # Check that sample images were created
            self.assertTrue(os.path.exists("sample_images/test1.jpg"))
            self.assertTrue(os.path.exists("sample_images/test2.png"))
            
            # Check image sizes
            with Image.open("sample_images/test1.jpg") as img:
                self.assertEqual(img.size, (1200, 800))
            with Image.open("sample_images/test2.png") as img:
                self.assertEqual(img.size, (800, 1200))
        finally:
            os.chdir(original_cwd)


if __name__ == '__main__':
    unittest.main(verbosity=2)
