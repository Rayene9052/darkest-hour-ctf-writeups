# Pixels&Samples

## Challenge Description
I was so impressed by SSTV transmission that I decided to create a simple image-to-audio conversion method, which I used to hide a secret image. Can you retrieve it?

**File:** `music.wav`  
**Flag format:** `Securinets{flag_here}`  
**Author:** PetriQore

---

## Solution

### Step 1. Inspect WAV File Properties
**Command line:** `soxi music.wav`  
**Requirements:** SoX must be installed (`sudo apt install sox`).

![Screenshot 1](Screenshots/p1.png)

#### Understanding the Relationship Between Samples and Image Dimensions
The WAV file contains 2959725 samples (from `soxi music.wav`). Since the audio was converted to raw 16-bit grayscale, each sample corresponds to a single pixel in an image.

To reconstruct the image, we need to find valid dimensions (W × H) that multiply to 2959725.

#### Finding Possible Dimensions
Since 2,959,725 = 3 × 5² × 19 × 31 × 67, some possible factor pairs are:

- `775 × 3,819`
- `1,005 × 2,945`
- `1,273 × 2,325`
- `1,425 × 2,077`
- `1,767 × 1,675`

### Step 2. Extract Raw PCM Data from WAV File
A WAV file has a 44-byte header. Skip that header to get just the sample data.  
**Command line:** `dd if=music.wav of=rawdata.bin bs=64K skip=44 iflag=skip_bytes`

![Screenshot 2](Screenshots/p2.png)

This produces **rawdata.bin** containing the 16-bit PCM samples.

**Explanation:**
- `bs=64K`: The block size is set to 64KB, which helps speed up the process.
- `skip=44`: Skips the first 44 bytes (the header).
- `iflag=skip_bytes`: This flag ensures the skip of 44 bytes is handled correctly without losing any data.

### Step 3. Convert Raw Data to an Image
**Command line:** `convert -depth 16 -size 775x3819 gray:rawdata.bin output.png`  
**Requirements:** ImageMagick must be installed (`sudo apt install imagemagick`).

![Screenshot 3](Screenshots/p3.png)

What it does:
- Converts raw binary image data (`rawdata.bin`) into a viewable image (`output.png`).
- `-depth 16`: Specifies 16-bit grayscale pixels.
- `-size 775x3819`: Defines image width × height (must match total samples).
- `gray:rawdata.bin`: Treats raw data as grayscale pixel values.

### Step 4. Adjust Dimensions If Needed
Check the `output.png` file.  
If the image appears stretched or distorted, try different factor pairs until it looks correct. In this case, `775 × 3819` works. If it didn’t, we would test other pairs.

### Step 5: Retrieving the Flag
We get a black-and-white image flipped and mirrored.

![Screenshot 4](Screenshots/p4.png)

We flip and mirror and get to see the flag.

![Screenshot 5](Screenshots/p5.png)

---

## Flag

```
Securinets{d1d_y0u_3nj0y_th3_mus1c????}
```

---
