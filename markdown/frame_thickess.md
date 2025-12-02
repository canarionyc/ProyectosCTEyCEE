A window has a frame percentage equal to f. What are the dimensions of the glass? 

If a window has **overall dimensions** (W \times H) (width by height) and a **frame percentage** (f) (the fraction of the window area taken up by the frame), then the **glass area** is:

[
A_{\text{glass}} = (1 - f), W H.
]

But if you want the **actual glass *dimensions*** (glass width and glass height), you need to know **how the frame is distributed** around the edges.

---

## **If the frame is uniform (same thickness on all sides)**

Let the frame thickness be (t).
Then:

[
\text{Glass width} = W - 2t
]
[
\text{Glass height} = H - 2t
]

The glass area is:

[
(W - 2t)(H - 2t) = (1 - f)WH.
]

You can solve for (t):

[
(W - 2t)(H - 2t) = (1 - f)WH.
]

Expanding:

[
WH - 2t(W + H) + 4t^2 = (1 - f)WH,
]

[
-2t(W + H) + 4t^2 = -fWH,
]

[
4t^2 - 2(W+H)t + fWH = 0.
]

This is a quadratic in (t):

[
t = \frac{(W+H) \pm \sqrt{(W+H)^2 - 4 \cdot 4 \cdot fWH}}{8}.
]

Only the **smaller** root is physically meaningful.

---

## If you want, tell me:

* the window width (W),
* height (H),
* frame fraction (f),

and I'll compute the exact glass width and height for you.
