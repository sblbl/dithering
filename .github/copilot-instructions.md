# Copilot Instructions - Image Dithering Project

## Project Overview
Python-based image dithering implementation using PIL/Pillow. Converts images to grayscale and applies dithering algorithms for artistic/reduced-color effects.

## Architecture & Key Components

### Single-Module Design
- **[dither.py](../dither.py)**: Main entry point containing all image processing logic
- Processes images via command-line arguments
- Uses PIL/Pillow for image I/O and manipulation

### Core Workflow
1. Load image via `Image.open()`
2. Convert RGB pixels to grayscale using `pixel_rgb_to_grayscale()`
3. Store as flat matrix (1D list representing 2D pixel grid)
4. Apply dithering algorithm (currently stub)
5. Display/save result

## Development Workflow

### Running the Script
```bash
python3 dither.py ./image.jpeg
```
- Requires Python 3 with PIL/Pillow installed
- Expects image path as first command-line argument

### Dependencies
```bash
pip3 install Pillow
```

## Known Issues & Patterns

### Current Bugs to Fix
1. **Line 19**: String formatting syntax error - uses `%` operator incorrectly:
   ```python
   # Wrong:
   print('matrix size {}'.format % len(image_matrix))
   # Should be:
   print('matrix size {}'.format(len(image_matrix)))
   ```

2. **Line 22**: Type conversion error - `image_matrix` is a 1D list of floats, but `Image.fromarray()` expects numpy array or proper 2D shape:
   ```python
   # Current approach won't work - needs numpy array or reshape
   im = Image.fromarray(image_matrix)
   ```

3. **Global scope issues**: `IMAGE_WIDTH` and `IMAGE_HEIGHT` are assigned in function but declared global - need `global` keyword or refactor to return values

### Code Conventions
- **Grayscale conversion**: Simple averaging method `(r + g + b) / 3` (not perceptual weighting)
- **Threshold-based approach**: Uses `THRESHOLD = 128` constant for binary dithering
- **Flat matrix representation**: Pixels stored as 1D list, not 2D array

## Important Context for AI Agents

### Dithering Algorithm Implementation
The project is incomplete - `dither()` and `image_to_matrix()` are stubs. When implementing:
- Common algorithms: Floyd-Steinberg, Ordered (Bayer), Atkinson
- Error diffusion requires modifying neighboring pixels
- Need to convert grayscale values to binary (0 or 255) based on THRESHOLD
- Must preserve image dimensions during conversion

### PIL/Pillow Specifics
- `Image.getdata()` returns flattened pixel sequence
- To create image from matrix: use numpy array or reshape + specify mode ('L' for grayscale, '1' for binary)
- Display with `.show()` (opens system viewer), save with `.save(filename)`

### Expected Output Format
Based on setup, likely targeting:
- Binary (1-bit) output for classic dithered look
- Preserve original dimensions
- Save or display final image

## File References
- [dither.py](../dither.py) - All implementation code
- `image.jpeg` - Test image (not tracked, user-provided)
