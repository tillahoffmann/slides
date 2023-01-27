---
css: static/css/harvard.css
---

# 📽️ slides

Create stunning presentations using [markdown](https://www.markdownguide.org) powered by [reveal.js](https://revealjs.com).

---

This README is a slide deck. Run `python -m slides` from the command line to launch a presentation server and view the deck.

---

Here is a simple figure.

![](figure.png)

Note:

Speaker notes start with `Note:` on each slide and can be accessed by hitting the `S` code.

---

You can also [include equations](https://revealjs.com/math/#markdown) wrapped in backticks.

`\[\begin{aligned}
F(x)&=\int dx\, \cos(x)\\
&=\sin(x) + C.
\end{aligned}\]`

---

Reveal.js supports special syntax to set arbitrary HTML attributes on [slides](https://revealjs.com/markdown/#slide-attributes), such as this background gradient.

<!-- .slide: data-background-gradient="radial-gradient(white, #E5CAC9)" -->

```html
<!-- .slide: data-background-gradient="radial-gradient(#E5CAC9, #B55A5A)" -->
```

This also works for [elements](https://revealjs.com/markdown/#element-attributes):
- green bullet point <!-- .element: style="color: #4db848" -->

```markdown
- green bullet point <!-- .element: style="color: #4db848" -->
```

---

Code can be included with [code fences](https://www.markdownguide.org/extended-syntax/#fenced-code-blocks).

```python
def add(a: int, b: int) -> int:
    """
    Add two integers.
    """
    return a + b
```

---

For labeled slides, we can link back to them. E.g., the [next one](#next-slide).

---

<!-- .slide: id="next-slide" -->

This is a slide labeled with the id `next-slide`.

```markdown
<!-- .slide: id="next-slide" -->
```

^^^

[Vertical slides](https://revealjs.com/vertical-slides/) can be used to logically group content. They are created using the `^^^` separator between slides.

---

[Jekyll-style frontmatter](https://jekyllrb.com/docs/front-matter/) can be used to configure the presentation. See [`slides/frontmatter.schema.yaml`](slides/frontmatter.schema.yaml) for details.

---

Visit the [reveal.js website](https://revealjs.com/markdown/) for further information.
