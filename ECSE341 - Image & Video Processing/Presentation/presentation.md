# Histogram Processing 
#### BY
### Saksham Puri
#### E18CSE158

![](background2.jpg)

---

# What are histograms?

#### Histograms help us visualise the distribution of the pixels among various intensity levels
#### In a nutshell, they are plots of the number of pixels corresponding to certain intensity level.


![inline](histogram_example.png)

---

# Cumulative Frequency

![inline](cumulative_freq_example.png)

- Cumulative frequency histogram tells us that number of pixels **_less than or equal to_** the corresponding intensity value as opposed to the exact number of pixels at that point.

---

# Lets take an example

![inline](example_image.png)

The image above has dimensions 5184x3456 or about **18 million** pixels

---

The image is greyscale and each pixel has a range of 0-255

![](example_image.png)

---

We obtain the following histogram of this image

![inline](histogram_example.png)

---

This can be further normalised by dividing by the total number of pixels

![inline](histogram_norm_example.png)

---

Now we can build a mental model for the cumulative frequency histogram which contains values <= the specific intensity value

![inline](cumulative_freq_example.png)

---

We can observe the changes in the corresponding plots when we consider different spread of intensity values

![inline](hist_dark.png)

---

Here is an example with bright image

![inline](hist_light.png)

---
Low Contrast Example

![inline](hist_lc.png)

---

High Contrast Example

![inline](hist_hc.png)

---

# histogram equalisation

---

Normal Equalised

![inline, left](example_image.png)![inline, right](eq/normal.png)

---

Dark Equalised

![inline, left](hist_dark.png)![inline, right](eq/dark.png)

---

Light Equalised

![inline, left](hist_light.png)![inline, right](eq/light.png)

---

Low Contrast Equalised

![inline](hist_lc.png) ![inline, right](eq/lc.png)

---

Low Contrast Equalised

![inline](hist_hc.png) ![inline, right](eq/hc.png)

---

# Thank you