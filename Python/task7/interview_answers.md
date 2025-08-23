## Interview Questions: Answers (Image Processing)

1. **What is PIL/Pillow?**
   - PIL (Python Imaging Library) is a library for opening, manipulating, and saving image files. Pillow is the modern fork of PIL that's actively maintained and compatible with Python 3.

2. **How do you open and save images?**
   - Open: `Image.open('path/to/image.jpg')` or `with Image.open('path') as img:`
   - Save: `img.save('output.jpg', 'JPEG')` or `img.save('output.png', 'PNG')`

3. **What is the resize() method?**
   - `img.resize((width, height), resampling_method)` changes image dimensions. Common resampling methods include `Image.Resampling.LANCZOS` (high quality) and `Image.Resampling.NEAREST` (fast).

4. **How do you read all files in a directory?**
   - Use `os.listdir()`, `pathlib.Path.glob()`, or `pathlib.Path.iterdir()` to get file listings, then filter by extension.

5. **What is the os module?**
   - Python's built-in module for operating system interfaces. Provides functions for file/directory operations, path manipulation, and system calls.

6. **How do you change file formats (e.g., JPG to PNG)?**
   - Open the image and save with a different format: `img.save('output.png', 'PNG')`. The format parameter determines the output type.

7. **What is a pixel?**
   - The smallest unit of a digital image. Each pixel has color information (RGB values) and together they form the complete image.

8. **What's the use of try-except here?**
   - Error handling for corrupted images, unsupported formats, or file permission issues. Prevents the entire batch from failing if one image has problems.

9. **How can you make the app dynamic?**
   - Add command-line arguments (argparse), GUI (tkinter), web interface (Flask), or configuration files to make size, format, and folder paths configurable.

10. **Can this be extended to GUI?**
    - Yes, using tkinter, PyQt, or web frameworks. Add file pickers, size input fields, format selection, and progress bars for a user-friendly interface.
