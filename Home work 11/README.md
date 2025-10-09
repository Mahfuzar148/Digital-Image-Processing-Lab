

---

## 📘 THEORY: Grid-wise Image Processing and Histogram Equalization Methods

### 1. Concept of Grid-wise Image Processing

An image of size (N \times M) can be divided into (s \times s) **grids or tiles**—each tile being a small sub-image.
By processing each grid independently, we can apply **different operations** (like linear or non-linear filters) to different image regions depending on their texture, brightness, or noise.

This technique allows **localized enhancement**—for example:

* Apply contrast stretching to darker regions,
* Apply smoothing or sharpening to textured regions,
* Perform adaptive histogram equalization locally.

After processing, all grids are recombined to form the final image.

---

### 2. Linear vs Non-linear Image Operations

| Type                      | Description                                             | Examples                                     | Nature                                                  |
| ------------------------- | ------------------------------------------------------- | -------------------------------------------- | ------------------------------------------------------- |
| **Linear operations**     | Output pixel is a *linear combination* of input pixels. | Mean filter, Gaussian blur, sharpening       | Simple and fast; affects all intensities proportionally |
| **Non-linear operations** | Output depends *non-linearly* on input values.          | Median filter, histogram equalization, CLAHE | More adaptive; preserves edges, enhances contrast       |

**Linear operations** use convolution; they preserve the linearity of the image signal.
**Non-linear operations** modify intensity relationships, giving better control over contrast or noise.

---

### 3. Histogram Equalization (HE)

#### Principle:

Histogram Equalization enhances contrast by redistributing pixel intensities so that they cover the entire available range (0–255).
It relies on the **Cumulative Distribution Function (CDF)** of the image histogram.

#### Steps:

1. Compute the histogram (h(k)) of gray levels.
2. Compute the cumulative distribution function (H(k)).
3. Map each input intensity (k) to a new intensity:
   [
   s = (L-1) \times \frac{H(k)}{H_{max}}
   ]
   where (L) = total gray levels (256).

#### Effects:

* Improves overall (global) contrast.
* Works well for images with low dynamic range.
* May **over-enhance noise** and **saturate bright/dark regions**, as the same mapping is applied globally.

---

### 4. Adaptive Histogram Equalization (AHE)

#### Principle:

AHE divides the image into small tiles and applies histogram equalization **independently** on each tile.

#### Purpose:

To enhance **local contrast** and reveal details in each region, especially when illumination varies across the image.

#### Process:

1. Split image into non-overlapping tiles (e.g., 8×8).
2. Perform HE on each tile separately.
3. Combine tiles using **bilinear interpolation** between adjacent tiles to smooth transitions.

#### Effects:

* Enhances local features and textures.
* Useful in non-uniform lighting.
* However, it **amplifies noise** in smooth regions because small tiles can make minor fluctuations look significant.

---

### 5. Contrast-Limited Adaptive Histogram Equalization (CLAHE)

#### Principle:

CLAHE is an improved version of AHE that limits how much contrast is increased in each tile.

#### Process:

1. Divide the image into tiles.
2. For each tile, compute the histogram.
3. Clip histogram bins that exceed a threshold (the **clip limit**) to reduce over-enhancement.
4. Redistribute the clipped pixels uniformly to other bins.
5. Apply local equalization using the modified histogram.
6. Use bilinear interpolation between neighboring tiles to remove visible boundaries.

#### Parameter Effects:

* **Clip Limit**: Controls contrast amplification.

  * Low value → smoother image (less contrast, less noise).
  * High value → stronger contrast (closer to AHE behavior).
* **Tile Size**: Determines localness.

  * Small tiles → more local contrast, but risk of noise.
  * Large tiles → smoother global appearance.

#### Effects:

* Produces balanced contrast enhancement.
* Reduces noise amplification compared to AHE.
* Removes tile artifacts using interpolation.

---

### 6. Bilinear Interpolation in AHE/CLAHE

#### Why needed:

If each tile’s histogram is equalized independently, the image will show **block boundaries** because of abrupt changes between tiles.

#### Role:

Bilinear interpolation **smoothly blends** the mappings from adjacent tiles so transitions are gradual.

#### How it works:

For any pixel between four neighboring tiles, the output intensity is calculated by weighting each tile’s mapping based on the pixel’s relative position:
[
I'(x,y) = \sum_{i,j} w_{ij} \times f_{ij}(I(x,y))
]
where:

* (f_{ij}) = mapping function of the (i,j) tile
* (w_{ij}) = bilinear interpolation weights (sum = 1)

#### Effect:

* Eliminates sharp boundaries between tiles.
* Produces a **smooth and natural appearance**.
* Slightly softens local contrast, which is usually beneficial.

---

### 7. Comparative Summary

| Method                     | Domain               | Main Feature               | Pros                             | Cons                                       |
| -------------------------- | -------------------- | -------------------------- | -------------------------------- | ------------------------------------------ |
| **HE**                     | Global               | Equalizes entire image     | Simple, fast                     | May over-enhance noise, global effect only |
| **AHE**                    | Local                | Tile-based equalization    | Enhances local contrast          | Amplifies noise, block artifacts           |
| **CLAHE**                  | Local + controlled   | Tile-based with clip limit | Balanced enhancement, less noise | More parameters to tune                    |
| **Bilinear Interpolation** | Transition smoothing | Blends adjacent tiles      | Removes seams                    | Slight loss of sharpness near borders      |

---

### 8. Overall Theoretical Insight

* HE enhances overall visibility but ignores local variations.
* AHE corrects for spatially varying illumination by enhancing each tile independently.
* CLAHE introduces a **clipping mechanism** that prevents over-saturation and controls noise.
* Bilinear interpolation ensures the **continuity** of brightness and contrast across tiles, making AHE/CLAHE visually smooth and artifact-free.

---

### 9. Applications

* Medical imaging (X-rays, MRI, CT scans)
* Satellite and aerial images
* Low-light or non-uniformly illuminated photos
* Microscopic and industrial image enhancement

---


