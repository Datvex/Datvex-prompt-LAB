# Product & E-commerce

Find prompts based on your specific task.

## 1-Object Print Ad Generation Framework

A conceptual framework prompt for generating a premium editorial print advertisement centered around a single product, requiring brand-matched lighting, a surreal twist, and a three-word slogan.

```text
1-Object Print Ad
Drop ONE product ({argument name="product example 1" default="iPhone"}, {argument name="product example 2" default="Nike"}), get:
1. premium editorial print ad
2. product as the hero
3. brand-matched lighting
4. 1 surreal twist tied to the product
5. 3-word slogan
```

---

## 1/7 Scale Collectible Figure Product Shot

Creates a high-resolution commercial product photograph of a detailed 1/7 scale collectible figure.

```text
A high-resolution commercial product photograph of an incredibly detailed 1/7 scale collectible figure. The figure features intricate clothing textures and realistic skin, standing on a pristine transparent circular acrylic base on a modern artist's desk surface. Eye-level close-up. In the soft-focus background, a computer monitor displays the complex 3D wireframe mesh of the same figure, next to a premium matte collector's box with vibrant 2D character art. Lighting is a mix of professional soft studio light and the subtle blue glow from the monitor screen creating rim lighting.
```

---

## 1Wrd Ad Generator

A meta-prompt describing a template designed to generate a complete brand identity package from a single word/brand name, including a surreal minimalist photoreal print ad, automatic palette/type pair

```text
Drop ONE brand/product name, get:
1. surreal + minimalist photoreal print ad
2. instant brand identity + vibe
3. auto palette + type pair
4. clean wordmark logo direction
5. a punchy 2-word slogan
```

---

## 2x2 Grid Car Development Phases

A concise Nano Banana Pro prompt requesting a 2x2 grid illustrating the four distinct development phases of a car: initial sketch, clay model, early prototype, and the final production release.

```text
"a 2x2 grid showing the development phases of this car: sketch, clay model, early prototype, 1st final production released car."
```

---

## 2x2 Grid Identity Lock Photo Collage Prompt

A highly structured JSON-based prompt for Nano Banana Pro to generate a 2x2 grid photo collage. It strictly locks the identity of the subject from an uploaded image while varying the setting, action,

```text
{
  "image_layout": "2x2 grid collage featuring four distinct photographs of the same female subject.",

  "identity_lock": {
    "reference": "uploaded image",
    "rules": [
      "Preserve the exact same face, facial structure, body shape, skin tone, and overall identity as the uploaded reference image",
      "Do NOT change the person’s appearance, age, ethnicity, or attractiveness",
      "The subject must clearly be the same individual in all four panels"
    ]
  },

  "clothing_rules": {
    "base_rule": "Clothing may either match the uploaded image exactly OR be naturally inferred outfits that the same person would realistically wear",
    "constraints": [
      "No drastic style change",
      "No costume-like outfits",
      "Outfits must feel coherent with the subject’s real-life fashion sense"
    ]
  },

  "panels": [
    {
      "position": "top_left",
      "setting": "Outdoors at night, dark background with softly illuminated green foliage",
      "action": "She holds a cake in one hand and licks frosting from the index finger of the other hand",
      "outfit": {
        "description": "A sleek, night-out look that fits the subject’s real style (can match the uploaded outfit or a realistic alternative)",
        "jewelry": "Gold-toned accessories such as a wristwatch, bracelet, rings, and small hoop earrings"
      },
      "props": {
        "item": "Round white frosted cake",
        "details": [
          "Red cherries on top",
          "Clean white piping along the edges",
          "Black icing text on the cake"
        ]
      },
      "mood": "Playful, confident, slightly cheeky"
    },

    {
      "position": "top_right",
      "setting": "Daytime upscale city street with storefronts and trees",
      "action": "She leans casually out of the open door of a black luxury car, looking directly at the camera",
      "outfit": {
        "description": "Casual-chic daytime outfit consistent with her identity (may reuse the uploaded outfit or a plausible streetwear variation)",
        "accessories": "Minimal jewelry, small shoulder bag"
      },
      "lighting": "Bright natural daylight with realistic shadows",
      "mood": "Confident, aspirational, influencer-like"
    },

    {
      "position": "bottom_left",
      "setting": "Indoor hallway with beige walls and wooden flooring",
      "action": "Full-body mirror selfie",
      "outfit": {
        "description": "A coordinated outfit suitable for an indoor mirror selfie, consistent with her fashion sense",
        "accessories": "Designer-style handbag, stacked bracelets"
      },
      "background_details": [
        "Large gold-framed mirror leaning against the wall",
        "Minimal interior decor such as dried plants",
        "Doorway visible in the reflection"
      ],
      "mood": "Stylish, composed, fashion-focused"
    },

    {
      "position": "bottom_right",
      "setting": "Inside a vehicle or near a window during gold"
```

---

## 3x3 Grid Commercial Marketing Campaign Prompt

A prompt for generating a 3x3 grid layout (3:4 aspect ratio) for a high-end commercial marketing campaign, requiring the use of an uploaded product as the central subject. The actual prompt text is in

```text
Create a 3×3 grid in 3:4 aspect ratio for a high-end commercial marketing campaign using the uploaded product as the central subject.
```

---

## 3x3 Grid Luxury Beauty Collage Prompt

A detailed JSON prompt for creating a 3x3 grid collage focused on luxury beauty and fashion, featuring a woman with vibrant red hair in a maroon satin dress, emphasizing jewelry (gold sunburst earring

```text
{
  "image_composition": {
    "type": "Collage",
    "layout": "3x3 Grid",
    "total_panels": 9
  },
  "subject_details": {
    "appearance": "Young woman with fair skin",
    "hair": {
      "color": "Vibrant red",
      "style": "Loose waves, shoulder-length, side-parted",
      "texture": "Silky and voluminous"
    },
    "eyes": "Blue/Green",
    "expression": "Varied (serious, smiling, laughing, focused)"
  },
  "fashion_and_style": {
    "outfit": {
      "garment": "Strapless corset-style dress or top",
      "color": "Deep maroon / Berry",
      "fabric": "Satin or Silk",
      "details": "Ruched bodice, structural boning visible"
    },
    "makeup": {
      "style": "Natural glam",
      "features": "Glowing skin, soft blush, defined lashes, nude/pink glossy lips"
    }
  },
  "jewelry_focus": {
    "item_type": "Dangle Earrings",
    "metal": "Gold",
    "design_elements": [
      "Huggie hoop base",
      "Large sunburst/starburst main charm",
      "Pave set crystals",
      "Delicate hanging chains",
      "Small star charms at ends of chains"
    ]
  },
  "setting_and_environment": {
    "location": "Luxury interior (likely a hotel suite or upscale bathroom)",
    "key_features": [
      "Large rectangular mirror with integrated LED lighting border",
      "White marble countertops",
      "Wood paneling on walls",
      "Large floor-to-ceiling windows",
      "Beige curtains"
    ],
    "lighting": "Mix of natural daylight and warm artificial vanity lighting"
  },
  "props_and_objects": {
    "cosmetics": [
      "Lip gloss tube",
      "Mascara/Eyeliner tube",
      "Glass perfume bottle with gold cap",
      "Round compact powder"
    ],
    "tech": "Black smartphone",
    "background_props": "Beige silk/satin fabric cloth (in flat lay)"
  },
  "panel_breakdown": {
    "top_row": [
      "Reflection in lit mirror applying makeup",
      "Flat lay of jewelry and cosmetics on marble",
      "Close-up putting on earring near window"
    ],
    "middle_row": [
      "Extreme close-up of earring on ear",
      "Side profile focusing on hair texture and shoulder",
      "Waist-up portrait facing forward near window"
    ],
    "bottom_row": [
      "Portrait touching hair looking away",
      "Reflection in mirror laughing/smiling",
      "Flat lay of earrings on folded beige silk cloth"
    ]
  }
}
```

---

## 8K Product Photography with Conceptual Cutaway

Creates an 8K studio product photograph of a Borjomi flavored water can with conceptual cutaway.

```text
8K studio product photography with conceptual cutaway, portrait orientation. Metallic beverage can labeled 'Borjomi Flavored Water', brushed aluminum. Horizontal torn-paper cutaway revealing densely packed red pomegranate seeds inside. White rough fibrous torn-paper texture at outer edges. Interior filled with deep red to ruby red pomegranate seeds, slightly translucent with glossy highlights. Soft studio lighting, frontal with slight top illumination. Light gray background with subtle cloudy texture.
```

---

## 9-Panel Christmas Photobooth Sticker Generator

A detailed prompt for generating a 9-panel grid collage in a photobooth style, featuring a specific character in 9 different Christmas-themed poses. The critical instruction is maintaining exact facia

```text
(9-panel grid collage, photobooth style, studio lighting). A fun and vibrant 3x3 grid featuring the specific character in 9 different poses. [CRITICAL: Maintain exact facial features, preserve original face structure across all panels].

Styling: She is wearing a soft white mohair sweater. Accessories change slightly in panels: a reindeer antler headband, a thick red knitted scarf, and holding a giant Christmas lollipop. Poses: 1. Winking with a V-sign. 2. Pouting while holding a miniature Christmas tree. 3. Surprised face with snowflake stickers on cheeks. 4. Laughing with eyes closed. 5. Blowing a kiss. 6. Holding a wrapped gift box on head. 7. Making a heart shape with hands. 8. Pretending to eat a gingerbread man. 9. Saluting with a serious cute face. Background: Uniform pastel blue studio backdrop for all panels. Lighting: Bright, shadowless beauty lighting, high-key, commercial pop style.
```

---

## 9-Panel Collage of Fashion and Cosmetics

A highly structured prompt designed to generate a 3x3 photo collage focusing on a young woman, her fashion (maroon corset dress), and specific gold dangle earrings, with panels dedicated to close-ups,

```text
{
  "image_composition": {
    "type": "Collage",
    "layout": "3x3 Grid",
    "total_panels": 9
  },
  "subject_details": {
    "appearance": "Young woman with fair skin",
    "hair": {
      "color": "natural",
      "style": "Loose waves, shoulder-length, side-parted",
      "texture": "Silky and voluminous"
    },
    "eyes": "Blue/Green",
    "expression": "Varied (serious, smiling, laughing, focused)"
  },
  "fashion_and_style": {
    "outfit": {
      "garment": "Strapless corset-style dress or top",
      "color": "Deep maroon / Berry",
      "fabric": "Satin or Silk",
      "details": "Ruched bodice, structural boning visible"
    },
    "makeup": {
      "style": "Natural glam",
      "features": "Glowing skin, soft blush, defined lashes, nude/pink glossy lips"
    }
  },
  "jewelry_focus": {
    "item_type": "Dangle Earrings",
    "metal": "Gold",
    "design_elements": [
      "Huggie hoop base",
      "Large sunburst/starburst main charm",
      "Pave set crystals",
      "Delicate hanging chains",
      "Small star charms at ends of chains"
    ]
  },
  "setting_and_environment": {
    "location": "Luxury interior (likely a hotel suite or upscale bathroom)",
    "key_features": [
      "Large rectangular mirror with integrated LED lighting border",
      "White marble countertops",
      "Wood paneling on walls",
      "Large floor-to-ceiling windows",
      "Beige curtains"
    ],
    "lighting": "Mix of natural daylight and warm artificial vanity lighting"
  },
  "props_and_objects": {
    "cosmetics": [
      "Lip gloss tube",
      "Mascara/Eyeliner tube",
      "Glass perfume bottle with gold cap",
      "Round compact powder"
    ],
    "tech": "Black smartphone",
    "background_props": "Beige silk/satin fabric cloth (in flat lay)"
  },
  "panel_breakdown": {
    "top_row": [
      "Reflection in lit mirror applying makeup",
      "Flat lay of jewelry and cosmetics on marble",
      "Close-up putting on earring near window"
    ],
    "middle_row": [
      "Extreme close-up of earring on ear",
      "Side profile focusing on hair texture and shoulder",
      "Waist-up portrait facing forward near window"
    ],
    "bottom_row": [
      "Portrait touching hair looking away",
      "Reflection in mirror laughing/smiling",
      "Flat lay of earrings on folded beige silk cloth"
    ]
  }
}
```

---

## 9-Panel Collage of Woman with Gold Jewelry

A highly detailed, structured prompt for generating a 3x3 image collage focused on a young woman, her maroon satin dress, and specific gold dangle earrings. The prompt breaks down the content of each

```text
{
  "image_composition": {
    "type": "Collage",
    "layout": "3x3 Grid",
    "total_panels": 9
  },
  "subject_details": {
    "appearance": "Young woman with fair skin",
    "hair": {
      "color": "{argument name="hair color" default="Vibrant red"}",
      "style": "Loose waves, shoulder-length, side-parted",
      "texture": "Silky and voluminous"
    },
    "eyes": "Blue/Green",
    "expression": "Varied (serious, smiling, laughing, focused)"
  },
  "fashion_and_style": {
    "outfit": {
      "garment": "Strapless corset-style dress or top",
      "color": "{argument name="outfit color" default="Deep maroon / Berry"}",
      "fabric": "Satin or Silk",
      "details": "Ruched bodice, structural boning visible"
    },
    "makeup": {
      "style": "Natural glam",
      "features": "Glowing skin, soft blush, defined lashes, nude/pink glossy lips"
    }
  },
  "jewelry_focus": {
    "item_type": "Dangle Earrings",
    "metal": "Gold",
    "design_elements": [
      "Huggie hoop base",
      "Large sunburst/starburst main charm",
      "Pave set crystals",
      "Delicate hanging chains",
      "Small star charms at ends of chains"
    ]
  },
  "setting_and_environment": {
    "location": "Luxury interior (likely a hotel suite or upscale bathroom)",
    "key_features": [
      "Large rectangular mirror with integrated LED lighting border",
      "White marble countertops",
      "Wood paneling on walls",
      "Large floor-to-ceiling windows",
      "Beige curtains"
    ],
    "lighting": "Mix of natural daylight and warm artificial vanity lighting"
  },
  "props_and_objects": {
    "cosmetics": [
      "Lip gloss tube",
      "Mascara/Eyeliner tube",
      "Glass perfume bottle with gold cap",
      "Round compact powder"
    ],
    "tech": "Black smartphone",
    "background_props": "Beige silk/satin fabric cloth (in flat lay)"
  },
  "panel_breakdown": {
    "top_row": [
      "Reflection in lit mirror applying makeup",
      "Flat lay of jewelry and cosmetics on marble",
      "Close-up putting on earring near window"
    ],
    "middle_row": [
      "Extreme close-up of earring on ear",
      "Side profile focusing on hair texture and shoulder",
      "Waist-up portrait facing forward near window"
    ],
    "bottom_row": [
      "Portrait touching hair looking away",
      "Reflection in mirror laughing/smiling",
      "Flat lay of earrings on folded beige silk cloth"
    ]
  }
}
```

---

## Act as an Etsy Niche Product Researcher

Optimizes product and e-commerce strategies for act as an etsy niche product researcher.

```text
Act as an Etsy Niche Product Researcher. You are an expert in identifying niche markets and trending products on Etsy. Your task is to help users find profitable niche products for their Etsy store.

You will:
- Analyze current market trends on Etsy
- Identify gaps and opportunities in various product categories
- Suggest unique product ideas that align with the user's interests

Rules:
- Focus on originality and uniqueness
- Consider competition and demand
- Provide actionable insights and data-backed recommendations
```

---

## AI Face Swapping for E-commerce Personalization

Optimizes product and e-commerce strategies for ai face swapping for e-commerce personalization.

```text
Act as a state-of-the-art AI system specialized in face-swapping technology for e-commerce applications. Your task is to enable users to visualize e-commerce products using AI face swapping, enhancing personalization by integrating their facial features with product images.

Responsibilities:
- Swap the user's facial features onto various product models.
- Maintain high realism and detail in face integration.
- Ensure compatibility with diverse product categories (e.g., apparel, accessories).

Rules:
- Preserve user privacy by not storing facial data.
- Ensure seamless blending and natural appearance.

Variables:
- ${productCategory} - the category of product for visualization.
- ${userImage} - the uploaded image of the user.

Examples:
- Input: User uploads a photo and selects a t-shirt.
- Output: Image of the user’s face swapped onto a model wearing the t-shirt.
```

---

## Alexandra Daddario Full-Body Panel Portrait

Creates a full-body portrait of Alexandra Daddario in a bikini, presented as three vertically stacked panels.

```text
{
  "subject": {
    "name": "{argument name="celebrity name" default="Alexandra Daddario"}",
    "profession": "actress",
    "pose": "full-body portrait in three vertically stacked panels, outdoors",
    "expression": "serene, looking off-camera",
    "hair": {
      "color": "dark",
      "texture": "wavy",
      "appearance": "damp"
    },
    "eyes": {
      "color": "light blue",
      "focus": "prominent"
    }
  },
  "attire": {
    "type": "bikini",
    "top": {
      "color_pattern": "teal and white, stylized feather/organic shapes",
      "style": "twist-front with thin spaghetti straps"
    },
    "bottom": {
      "color_pattern": "matches top",
      "style": "high-cut leg"
    }
  },
  "composition": {
    "panels": [
      {
        "name": "top",
        "focus": "face and upper torso",
        "details": "arm raised near head"
      },
      {
        "name": "middle",
        "focus": "midsection and swimwear",
        "details": "bikini top twist-front, patterned fabric"
      },
      {
        "name": "bottom",
        "focus": "lower torso and hips",
        "details": "bikini bottom high-cut, hand resting naturally at side"
      }
    ],
    "background": {
      "type": "outdoors",
      "appearance": "vibrant green, soft-focus, lush natural environment near water"
    },
    "lighting": {
      "type": "bright natural",
      "highlights": "fair complexion, textures of damp hair and fabric"
    },
    "style": "lifestyle/fashion, summer/outdoor aesthetic"
  }
}
```

---

## Ana de Armas Fashion Editorial in Rome

A detailed prompt for generating a high-fashion editorial image of Ana de Armas on a stone balcony overlooking Rome, focusing on golden hour lighting, a structured dark red corset top, and a high-wais

```text
{
  "image_description": {
    "scene": {
      "location": {
        "city": "{argument name="city" default="Rome"}",
        "setting": "Stone balcony overlooking historic Roman architecture",
        "details": "The scene is set on a classic stone balcony, featuring an expansive view of Rome's ancient buildings, monuments, and the city skyline. The warm golden light of natural daylight casts soft shadows on the stone, highlighting intricate architectural elements of the city."
      },
      "environment": {
        "elements": [
          "Stone balcony with ornate railings",
          "Ancient Roman buildings in the background",
          "Clear sky with gentle light reflecting off glass windows",
          "Warm, soft glow from the golden hour sunlight"
        ],
        "atmosphere": "Serene, sophisticated, with a sense of timeless luxury and romance, evoking the beauty of luxury travel and refined femininity."
      },
      "lighting": {
        "type": "Natural daylight",
        "effect": "The lighting is soft and crisp, highlighting architectural textures and the subject with a gentle glow. Shadows are softened, creating an inviting and elevated atmosphere."
      }
    },
    "subject": {
      "identity": "{argument name="celebrity name" default="Ana de Armas"}",
      "pose": {
        "description": "The subject stands confidently near the stone railing, gazing outward towards the Roman skyline. She maintains a poised and elegant posture, embodying grace and sophistication, with a slight smile suggesting confidence and thoughtfulness."
      },
      "outfit": {
        "top": {
          "type": "Structured corset-style top",
          "color": "Dark red",
          "style": "Fashion editorial, modern yet classic, designed to accentuate the figure. The corset features sharp, defined lines and a clean, structured fit that contrasts beautifully with the natural environment."
        },
        "bottom": {
          "type": "High-waisted skirt",
          "details": "The skirt is high-waisted, with a dramatic thigh-high slit on both sides, giving it an edgy yet refined feel. The fabric flows gracefully, emphasizing the subject's femininity and modern elegance."
        }
      },
      "hair_and_makeup": {
        "hair": {
          "style": "Soft waves",
          "details": "Her hair is styled in natural, soft waves that cascade effortlessly, adding a sense of movement and vitality to the look. The waves are glossy, offering a polished yet relaxed style."
        },
        "makeup": {
          "style": "Refined and natural",
          "details": "The makeup enhances her natural beauty with subtle contouring and a soft highlight. Her eyes are defined with light eyeliner, and her lips sport a neutral shade, contributing to a sophisticated and timeless look."
        }
      }
    },
    "composition": {
      "aspect_ratio": "3:4",
      "orientation": "Vertical",
      "focus": {
        "subject": "The subject is the"
```

---

## Ana de Armas Fashion Editorial in Rome (Duplicate)

A detailed prompt for generating a high-fashion editorial image of Ana de Armas on a stone balcony overlooking Rome, focusing on golden hour lighting, a structured dark red corset top, and a high-wais

```text
{
  "image_description": {
    "scene": {
      "location": {
        "city": "{argument name="city" default="Rome"}",
        "setting": "Stone balcony overlooking historic Roman architecture",
        "details": "The scene is set on a classic stone balcony, featuring an expansive view of Rome's ancient buildings, monuments, and the city skyline. The warm golden light of natural daylight casts soft shadows on the stone, highlighting intricate architectural elements of the city."
      },
      "environment": {
        "elements": [
          "Stone balcony with ornate railings",
          "Ancient Roman buildings in the background",
          "Clear sky with gentle light reflecting off glass windows",
          "Warm, soft glow from the golden hour sunlight"
        ],
        "atmosphere": "Serene, sophisticated, with a sense of timeless luxury and romance, evoking the beauty of luxury travel and refined femininity."
      },
      "lighting": {
        "type": "Natural daylight",
        "effect": "The lighting is soft and crisp, highlighting architectural textures and the subject with a gentle glow. Shadows are softened, creating an inviting and elevated atmosphere."
      }
    },
    "subject": {
      "identity": "{argument name="celebrity name" default="Ana de Armas"}",
      "pose": {
        "description": "The subject stands confidently near the stone railing, gazing outward towards the Roman skyline. She maintains a poised and elegant posture, embodying grace and sophistication, with a slight smile suggesting confidence and thoughtfulness."
      },
      "outfit": {
        "top": {
          "type": "Structured corset-style top",
          "color": "Dark red",
          "style": "Fashion editorial, modern yet classic, designed to accentuate the figure. The corset features sharp, defined lines and a clean, structured fit that contrasts beautifully with the natural environment."
        },
        "bottom": {
          "type": "High-waisted skirt",
          "details": "The skirt is high-waisted, with a dramatic thigh-high slit on both sides, giving it an edgy yet refined feel. The fabric flows gracefully, emphasizing the subject's femininity and modern elegance."
        }
      },
      "hair_and_makeup": {
        "hair": {
          "style": "Soft waves",
          "details": "Her hair is styled in natural, soft waves that cascade effortlessly, adding a sense of movement and vitality to the look. The waves are glossy, offering a polished yet relaxed style."
        },
        "makeup": {
          "style": "Refined and natural",
          "details": "The makeup enhances her natural beauty with subtle contouring and a soft highlight. Her eyes are defined with light eyeliner, and her lips sport a neutral shade, contributing to a sophisticated and timeless look."
        }
      }
    },
    "composition": {
      "aspect_ratio": "3:4",
      "orientation": "Vertical",
      "focus": {
        "subject": "The subject is the"
```

---

## Ana de Armas High Fashion Editorial in Paris

A prompt designed to generate a photorealistic, high-fashion editorial image of a young woman resembling Ana de Armas. The scene is a luxury rooftop balcony in Paris with the Eiffel Tower visible, fea

```text
Use the same face from the reference image without changing facial features

stunning young woman with long platinum blonde hair, heavy glamorous makeup, blue eyes, full lips with dark lipstick, seductive expression tongue slightly out, holding black eyeglasses in front of mouth, deep plunging navy pinstripe blazer dress with choker, very short skirt, thigh-high view, posing on luxury rooftop balcony, Eiffel Tower in background, dramatic cloudy Paris sky, high fashion editorial style, cinematic lighting, ultra detailed, photorealistic
```

---

## Ana de Armas Lifestyle Editorial Portrait Prompt

A simple, high-level prompt for generating a lifestyle editorial portrait of Ana de Armas using Gemini Nano Banana Pro.

```text
Gemini Nano Banana Pro
{argument name="celebrity name" default="Ana de Armas"}
{argument name="style" default="Lifestyle Editorial Portrait"}
```

---

## Ana de Armas on a Roman Balcony in Golden Hour

A detailed JSON prompt for generating a sophisticated, photorealistic image of Ana de Armas standing on a stone balcony overlooking historic Roman architecture during the golden hour. The prompt speci

```text
{
  "image_description": {
    "scene": {
      "location": {
        "city": "Rome",
        "setting": "Stone balcony overlooking historic Roman architecture",
        "details": "The scene is set on a classic stone balcony, featuring an expansive view of Rome's ancient buildings, monuments, and the city skyline. The warm golden light of natural daylight casts soft shadows on the stone, highlighting intricate architectural elements of the city."
      },
      "environment": {
        "elements": [
          "Stone balcony with ornate railings",
          "Ancient Roman buildings in the background",
          "Clear sky with gentle light reflecting off glass windows",
          "Warm, soft glow from the golden hour sunlight"
        ],
        "atmosphere": "Serene, sophisticated, with a sense of timeless luxury and romance, evoking the beauty of luxury travel and refined femininity."
      },
      "lighting": {
        "type": "Natural daylight",
        "effect": "The lighting is soft and crisp, highlighting architectural textures and the subject with a gentle glow. Shadows are softened, creating an inviting and elevated atmosphere."
      }
    },
    "subject": {
      "identity": "Ana de Armas",
      "pose": {
        "description": "The subject stands confidently near the stone railing, gazing outward towards the Roman skyline. She maintains a poised and elegant posture, embodying grace and sophistication, with a slight smile suggesting confidence and thoughtfulness."
      },
      "outfit": {
        "top": {
          "type": "Structured corset-style top",
          "color": "Dark red",
          "style": "Fashion editorial, modern yet classic, designed to accentuate the figure. The corset features sharp, defined lines and a clean, structured fit that contrasts beautifully with the natural environment."
        },
        "bottom": {
          "type": "High-waisted skirt",
          "details": "The skirt is high-waisted, with a dramatic thigh-high slit on both sides, giving it an edgy yet refined feel. The fabric flows gracefully, emphasizing the subject's femininity and modern elegance."
        }
      },
      "hair_and_makeup": {
        "hair": {
          "style": "Soft waves",
          "details": "Her hair is styled in natural, soft waves that cascade effortlessly, adding a sense of movement and vitality to the look. The waves are glossy, offering a polished yet relaxed style."
        },
        "makeup": {
          "style": "Refined and natural",
          "details": "The makeup enhances her natural beauty with subtle contouring and a soft highlight. Her eyes are defined with light eyeliner, and her lips sport a neutral shade, contributing to a sophisticated and timeless look."
        }
      }
    },
    "composition": {
      "aspect_ratio": "3:4",
      "orientation": "Vertical",
      "focus": {
        "subject": "The subject is the
```

---

## Ana de Armas on a Roman Balcony in High-Fashion Outfit

A detailed, structured prompt for generating a sophisticated, high-fashion image of Ana de Armas standing on a stone balcony overlooking the historic Roman skyline during golden hour. The prompt speci

```text
{
  "image_description": {
    "scene": {
      "location": {
        "city": "Rome",
        "setting": "Stone balcony overlooking historic Roman architecture",
        "details": "The scene is set on a classic stone balcony, featuring an expansive view of Rome's ancient buildings, monuments, and the city skyline. The warm golden light of natural daylight casts soft shadows on the stone, highlighting intricate architectural elements of the city."
      },
      "environment": {
        "elements": [
          "Stone balcony with ornate railings",
          "Ancient Roman buildings in the background",
          "Clear sky with gentle light reflecting off glass windows",
          "Warm, soft glow from the golden hour sunlight"
        ],
        "atmosphere": "Serene, sophisticated, with a sense of timeless luxury and romance, evoking the beauty of luxury travel and refined femininity."
      },
      "lighting": {
        "type": "Natural daylight",
        "effect": "The lighting is soft and crisp, highlighting architectural textures and the subject with a gentle glow. Shadows are softened, creating an inviting and elevated atmosphere."
      }
    },
    "subject": {
      "identity": "Ana de Armas",
      "pose": {
        "description": "The subject stands confidently near the stone railing, gazing outward towards the Roman skyline. She maintains a poised and elegant posture, embodying grace and sophistication, with a slight smile suggesting confidence and thoughtfulness."
      },
      "outfit": {
        "top": {
          "type": "Structured corset-style top",
          "color": "Dark red",
          "style": "Fashion editorial, modern yet classic, designed to accentuate the figure. The corset features sharp, defined lines and a clean, structured fit that contrasts beautifully with the natural environment."
        },
        "bottom": {
          "type": "High-waisted skirt",
          "details": "The skirt is high-waisted, with a dramatic thigh-high slit on both sides, giving it an edgy yet refined feel. The fabric flows gracefully, emphasizing the subject's femininity and modern elegance."
        }
      },
      "hair_and_makeup": {
        "hair": {
          "style": "Soft waves",
          "details": "Her hair is styled in natural, soft waves that cascade effortlessly, adding a sense of movement and vitality to the look. The waves are glossy, offering a polished yet relaxed style."
        },
        "makeup": {
          "style": "Refined and natural",
          "details": "The makeup enhances her natural beauty with subtle contouring and a soft highlight. Her eyes are defined with light eyeliner, and her lips sport a neutral shade, contributing to a sophisticated and timeless look."
        }
      }
    },
    "composition": {
      "aspect_ratio": "3:4",
      "orientation": "Vertical",
      "focus": {
        "subject":
```

---

## Ana de Armas Roman Balcony Editorial Prompt (Version 1)

A detailed prompt for generating a vertical fashion editorial image of Ana de Armas on a stone balcony overlooking the historic Roman skyline during golden hour. The prompt specifies her outfit (struc

```text
{
  "image_description": {
    "scene": {
      "location": {
        "city": "Rome",
        "setting": "Stone balcony overlooking historic Roman architecture",
        "details": "The scene is set on a classic stone balcony, featuring an expansive view of Rome's ancient buildings, monuments, and the city skyline. The warm golden light of natural daylight casts soft shadows on the stone, highlighting intricate architectural elements of the city."
      },
      "environment": {
        "elements": [
          "Stone balcony with ornate railings",
          "Ancient Roman buildings in the background",
          "Clear sky with gentle light reflecting off glass windows",
          "Warm, soft glow from the golden hour sunlight"
        ],
        "atmosphere": "Serene, sophisticated, with a sense of timeless luxury and romance, evoking the beauty of luxury travel and refined femininity."
      },
      "lighting": {
        "type": "Natural daylight",
        "effect": "The lighting is soft and crisp, highlighting architectural textures and the subject with a gentle glow. Shadows are softened, creating an inviting and elevated atmosphere."
      }
    },
    "subject": {
      "identity": "Ana de Armas",
      "pose": {
        "description": "The subject stands confidently near the stone railing, gazing outward towards the Roman skyline. She maintains a poised and elegant posture, embodying grace and sophistication, with a slight smile suggesting confidence and thoughtfulness."
      },
      "outfit": {
        "top": {
          "type": "Structured corset-style top",
          "color": "Dark red",
          "style": "Fashion editorial, modern yet classic, designed to accentuate the figure. The corset features sharp, defined lines and a clean, structured fit that contrasts beautifully with the natural environment."
        },
        "bottom": {
          "type": "High-waisted skirt",
          "details": "The skirt is high-waisted, with a dramatic thigh-high slit on both sides, giving it an edgy yet refined feel. The fabric flows gracefully, emphasizing the subject's femininity and modern elegance."
        }
      },
      "hair_and_makeup": {
        "hair": {
          "style": "Soft waves",
          "details": "Her hair is styled in natural, soft waves that cascade effortlessly, adding a sense of movement and vitality to the look. The waves are glossy, offering a polished yet relaxed style."
        },
        "makeup": {
          "style": "Refined and natural",
          "details": "The makeup enhances her natural beauty with subtle contouring and a soft highlight. Her eyes are defined with light eyeliner, and her lips sport a neutral shade, contributing to a sophisticated and timeless look."
        }
      }
    },
    "composition": {
      "aspect_ratio": "3:4",
      "orientation": "Vertical",
      "focus": {
        "subject": "The subject is the
```

---

## Ana de Armas Roman Balcony Editorial Prompt (Version 2)

A detailed prompt for generating a vertical fashion editorial image of Ana de Armas on a stone balcony overlooking the historic Roman skyline during golden hour. The prompt specifies her outfit (struc

```text
{
  "image_description": {
    "scene": {
      "location": {
        "city": "Rome",
        "setting": "Stone balcony overlooking historic Roman architecture",
        "details": "The scene is set on a classic stone balcony, featuring an expansive view of Rome's ancient buildings, monuments, and the city skyline. The warm golden light of natural daylight casts soft shadows on the stone, highlighting intricate architectural elements of the city."
      },
      "environment": {
        "elements": [
          "Stone balcony with ornate railings",
          "Ancient Roman buildings in the background",
          "Clear sky with gentle light reflecting off glass windows",
          "Warm, soft glow from the golden hour sunlight"
        ],
        "atmosphere": "Serene, sophisticated, with a sense of timeless luxury and romance, evoking the beauty of luxury travel and refined femininity."
      },
      "lighting": {
        "type": "Natural daylight",
        "effect": "The lighting is soft and crisp, highlighting architectural textures and the subject with a gentle glow. Shadows are softened, creating an inviting and elevated atmosphere."
      }
    },
    "subject": {
      "identity": "Ana de Armas",
      "pose": {
        "description": "The subject stands confidently near the stone railing, gazing outward towards the Roman skyline. She maintains a poised and elegant posture, embodying grace and sophistication, with a slight smile suggesting confidence and thoughtfulness."
      },
      "outfit": {
        "top": {
          "type": "Structured corset-style top",
          "color": "Dark red",
          "style": "Fashion editorial, modern yet classic, designed to accentuate the figure. The corset features sharp, defined lines and a clean, structured fit that contrasts beautifully with the natural environment."
        },
        "bottom": {
          "type": "High-waisted skirt",
          "details": "The skirt is high-waisted, with a dramatic thigh-high slit on both sides, giving it an edgy yet refined feel. The fabric flows gracefully, emphasizing the subject's femininity and modern elegance."
        }
      },
      "hair_and_makeup": {
        "hair": {
          "style": "Soft waves",
          "details": "Her hair is styled in natural, soft waves that cascade effortlessly, adding a sense of movement and vitality to the look. The waves are glossy, offering a polished yet relaxed style."
        },
        "makeup": {
          "style": "Refined and natural",
          "details": "The makeup enhances her natural beauty with subtle contouring and a soft highlight. Her eyes are defined with light eyeliner, and her lips sport a neutral shade, contributing to a sophisticated and timeless look."
        }
      }
    },
    "composition": {
      "aspect_ratio": "3:4",
      "orientation": "Vertical",
      "focus": {
        "subject": "The subject is the
```

---

## Ana de Armas Roman Balcony Editorial Prompt (Version 3)

A detailed prompt for generating a vertical fashion editorial image of Ana de Armas on a stone balcony overlooking the historic Roman skyline during golden hour. The prompt specifies her outfit (struc

```text
{
  "image_description": {
    "scene": {
      "location": {
        "city": "Rome",
        "setting": "Stone balcony overlooking historic Roman architecture",
        "details": "The scene is set on a classic stone balcony, featuring an expansive view of Rome's ancient buildings, monuments, and the city skyline. The warm golden light of natural daylight casts soft shadows on the stone, highlighting intricate architectural elements of the city."
      },
      "environment": {
        "elements": [
          "Stone balcony with ornate railings",
          "Ancient Roman buildings in the background",
          "Clear sky with gentle light reflecting off glass windows",
          "Warm, soft glow from the golden hour sunlight"
        ],
        "atmosphere": "Serene, sophisticated, with a sense of timeless luxury and romance, evoking the beauty of luxury travel and refined femininity."
      },
      "lighting": {
        "type": "Natural daylight",
        "effect": "The lighting is soft and crisp, highlighting architectural textures and the subject with a gentle glow. Shadows are softened, creating an inviting and elevated atmosphere."
      }
    },
    "subject": {
      "identity": "Ana de Armas",
      "pose": {
        "description": "The subject stands confidently near the stone railing, gazing outward towards the Roman skyline. She maintains a poised and elegant posture, embodying grace and sophistication, with a slight smile suggesting confidence and thoughtfulness."
      },
      "outfit": {
        "top": {
          "type": "Structured corset-style top",
          "color": "Dark red",
          "style": "Fashion editorial, modern yet classic, designed to accentuate the figure. The corset features sharp, defined lines and a clean, structured fit that contrasts beautifully with the natural environment."
        },
        "bottom": {
          "type": "High-waisted skirt",
          "details": "The skirt is high-waisted, with a dramatic thigh-high slit on both sides, giving it an edgy yet refined feel. The fabric flows gracefully, emphasizing the subject's femininity and modern elegance."
        }
      },
      "hair_and_makeup": {
        "hair": {
          "style": "Soft waves",
          "details": "Her hair is styled in natural, soft waves that cascade effortlessly, adding a sense of movement and vitality to the look. The waves are glossy, offering a polished yet relaxed style."
        },
        "makeup": {
          "style": "Refined and natural",
          "details": "The makeup enhances her natural beauty with subtle contouring and a soft highlight. Her eyes are defined with light eyeliner, and her lips sport a neutral shade, contributing to a sophisticated and timeless look."
        }
      }
    },
    "composition": {
      "aspect_ratio": "3:4",
      "orientation": "Vertical",
      "focus": {
        "subject": "The subject is the
```

---

## Ana de Armas Rome balcony fashion editorial prompt

A detailed JSON prompt for generating a sophisticated fashion editorial image of Ana de Armas on a stone balcony overlooking historic Rome. It specifies her outfit (dark red structured corset top, hig

```text
{
  "image_description": {
    "scene": {
      "location": {
        "city": "Rome",
        "setting": "Stone balcony overlooking historic Roman architecture",
        "details": "The scene is set on a classic stone balcony, featuring an expansive view of Rome's ancient buildings, monuments, and the city skyline. The warm golden light of natural daylight casts soft shadows on the stone, highlighting intricate architectural elements of the city."
      },
      "environment": {
        "elements": [
          "Stone balcony with ornate railings",
          "Ancient Roman buildings in the background",
          "Clear sky with gentle light reflecting off glass windows",
          "Warm, soft glow from the golden hour sunlight"
        ],
        "atmosphere": "Serene, sophisticated, with a sense of timeless luxury and romance, evoking the beauty of luxury travel and refined femininity."
      },
      "lighting": {
        "type": "Natural daylight",
        "effect": "The lighting is soft and crisp, highlighting architectural textures and the subject with a gentle glow. Shadows are softened, creating an inviting and elevated atmosphere."
      }
    },
    "subject": {
      "identity": "Ana de Armas",
      "pose": {
        "description": "The subject stands confidently near the stone railing, gazing outward towards the Roman skyline. She maintains a poised and elegant posture, embodying grace and sophistication, with a slight smile suggesting confidence and thoughtfulness."
      },
      "outfit": {
        "top": {
          "type": "Structured corset-style top",
          "color": "Dark red",
          "style": "Fashion editorial, modern yet classic, designed to accentuate the figure. The corset features sharp, defined lines and a clean, structured fit that contrasts beautifully with the natural environment."
        },
        "bottom": {
          "type": "High-waisted skirt",
          "details": "The skirt is high-waisted, with a dramatic thigh-high slit on both sides, giving it an edgy yet refined feel. The fabric flows gracefully, emphasizing the subject's femininity and modern elegance."
        }
      },
      "hair_and_makeup": {
        "hair": {
          "style": "Soft waves",
          "details": "Her hair is styled in natural, soft waves that cascade effortlessly, adding a sense of movement and vitality to the look. The waves are glossy, offering a polished yet relaxed style."
        },
        "makeup": {
          "style": "Refined and natural",
          "details": "The makeup enhances her natural beauty with subtle contouring and a soft highlight. Her eyes are defined with light eyeliner, and her lips sport a neutral shade, contributing to a sophisticated and timeless look."
        }
      }
    },
    "composition": {
      "aspect_ratio": "3:4",
      "orientation": "Vertical",
      "focus": {
        "subject": "
```

---

## Ana de Armas Rustic Elegance Poolside Editorial

A detailed JSON prompt, written partially in Hindi/Urdu (Romanized), for generating a high-end lifestyle editorial featuring Ana de Armas by a pool. It focuses on a rustic elegance aesthetic, Mediterr

```text
{
  "project_metadata": {
    "celebrity_name": "{argument name="celebrity name" default="Ana de Armas"}",
    "shoot_category": "High-end Lifestyle / Fashion Editorial",
    "visual_aesthetic": "Rustic Elegance & Mediterranean Minimalist",
    "shooting_date": "January 26, 2026 (Ref: File Metadata)"
  },
  "detailed_environment_analysis": {
    "architectural_style": "Ibiza-inspired / Cycladic minimalist (safaid plaster ki deewarain, curved niches)",
    "pool_characteristics": {
      "type": "Infinity style or sunken pool",
      "water_color": "Turquoise / Crystal Clear Blue",
      "decking": "Light beige natural stone tiles"
    },
    "furniture_elements": {
      "lounge_chairs": "Lakri ka frame aur woven (buni hui) rassi ki seating",
      "sun_shade": "Traditional raffia/straw umbrella (chattri) jo bohot hi organic look de rahi hai",
      "planters": "Terracotta mitti ke bade gamlay jo rustic touch de rahe hain"
    }
  },
  "wardrobe_breakdown": {
    "set_combination": {
      "shirt": "Deep {argument name="shirt color" default="chocolate brown"}, lightweight linen ya silk blend, relaxed fit with button-down front",
      "skirt": "Matching earth-toned high-waisted midi skirt, breathable fabric, clean silhouette",
      "inner_wear": "Hand-knit beige crochet bralette, textured pattern, triangle shape"
    },
    "styling_philosophy": "Quiet Luxury (Bina kisi bade logo ke mehenga aur mayari dikhne wala style)"
  },
  "beauty_and_grooming": {
    "hair_style": "Loose beachy waves, side-parted, chestnut brown highlights ke sath",
    "makeup_look": "Dewy 'no-makeup' makeup look, soft pink lips, neutral eyeshadow, aur natural glowing skin"
  },
  "individual_frame_deep_dive": {
    "frame_01_analysis": {
      "filename": "20260126_150448.jpg",
      "composition": "Rule of thirds ka istemal, model left-center mein hai",
      "narrative": "Ek thoughtful ya dreamy lamha, jahan model door kahin dekh rahi hai"
    },
    "frame_02_analysis": {
      "filename": "20260126_150443.jpg",
      "composition": "Close-up portrait with bokeh background (dhundla pichla hissa)",
      "narrative": "Direct eye contact ke sath ek garmiyon ki pur-sukoon muskurahat"
    },
    "frame_03_analysis": {
      "filename": "20260126_150436.jpg",
      "composition": "Dynamic pose, vertical alignment",
      "narrative": "Shooting ke darmiyan ek confident aur playful pose"
    }
  },
  "color_palette_hex_codes": {
    "earth_brown": "#4B3621",
    "sand_beige": "#D2B48C",
    "sky_white": "#F5F5F5",
    "pool_blue": "#00CED1"
  }
}
```

---

## Ana de Armas Y2K Surreal Glamour Portrait

A highly specific JSON prompt for generating a high-fashion editorial portrait of Ana de Armas, capturing a decadent, post-party fatigue mood in a luxury bathroom, utilizing Y2K flash photography styl

```text
{
  "version": "1.0",
  "aspect_ratio": "3:4",
  "subject": {
    "identity": "{argument name="celebrity name" default="Ana de Armas"}",
    "fidelity": "Exact facial preservation, high-detail skin texture",
    "expression": {
      "eyes": "Heavy-lidded, tired but piercing",
      "mouth": "Slightly parted lips, subtly smudged red lipstick",
      "gaze": "Lazy, confident, post-party fatigue",
      "mood": "Decadent, surreal glamour, beautiful discomfort"
    },
    "pose": {
      "position": "Half-seated on white marble bathroom vanity",
      "body_language": "Elegantly arched back, chest pushed forward, one arm bracing behind with flat palm on marble",
      "legs": "One leg raised with knee bent and foot on vanity edge; one leg hanging with toes grazing the floor",
      "hands": "Free hand resting loosely on the raised knee"
    }
  },
  "wardrobe_accessories": {
    "clothing": "Form-fitting golden metallic mini-dress, iridescent purple accents, sweetheart neckline, reflective sequin texture, hem ridden up to reveal upper thigh",
    "jewelry": [
      "Long dangling gold earrings",
      "Stacked beaded bracelets",
      "Elegant luxury wristwatch"
    ],
    "footwear": "Barefoot"
  },
  "environment": {
    "setting": "Luxury bathroom at 3:00 AM",
    "materials": "White marble countertops, gold-finished fixtures",
    "key_elements": "Large floor-to-ceiling mirror behind subject, multiplying reflections of back and profile",
    "props": "Scattered champagne glass, decadent party debris"
  },
  "lighting_style": {
    "aesthetic": "Guy Bourdin surrealism mixed with Y2K millennium flash",
    "key_light": "Direct on-camera flash (high-intensity, Y2K style)",
    "accent_lights": {
      "camera_left": "Hot pink and magenta wash",
      "camera_right": "Electric cyan and blue rim lighting"
    },
    "effects": "High saturation light play on marble, mirror reflections creating voyeuristic tension, subtle halation on sequin highlights"
  },
  "technical_specs": {
    "camera": "35mm film aesthetic",
    "lens": "35mm wide-angle at f/2.8",
    "angle": "Slightly low angle to emphasize height and dominance",
    "focus": "Sharp focus on eyes and dress texture",
    "film_stock_simulation": {
      "contrast": "High",
      "grain": "Fine film grain",
      "color_grading": "Punchy, saturated, high-fashion editorial"
    }
  }
}
```

---

## Asian Beauty Gravure Keywords Prompt

A prompt consisting entirely of a long list of keywords and hashtags in Chinese, Japanese, and English, typically used for generating gravure, lingerie, or suggestive images of Asian models, focusing

```text
#擦边 #福利 #纯欲 #反差 #黑丝 #白丝 #美腿 #足控 #私房 #女大 #纯欲天花板 #グラビア #セクシー #えっち #自撮り女子 #自撮り界隈 #雰囲気 #裏垢女子 #美脚 #雰囲気嫌いじゃないよって人いいね #らぶりつください #NSFW #Tease #Lingerie #Boudior #Gravure #Egirl #Model #Cosplay #AsianBeauty #Legs #feetworshi̇p
```

---

## Asian Woman in White Bikini in Luxury Villa

Creates a medium shot of an Asian woman with a fit physique, wearing a white crinkled bikini set, seated in a luxurious villa interior.

```text
{
  "subject": {
    "description": "Young woman of Asian descent with a tanned, glowing complexion. She has long, dark, wavy hair parted in the middle, cascading over her shoulders. Her physique is fit and toned with visible abdominal definition."
  },
  "attire": {
    "garment_type": "Two-piece bikini set",
    "color": "White",
    "material": "Textured, crinkled fabric",
    "top_details": "Bandeau-style top with a central knot tie, featuring detached off-the-shoulder ruffled flutter sleeves. The top supports a large, full bust with significant volume and forward projection.",
    "bottom_details": "Matching white bikini bottoms with side ties, sitting low on the hips.",
    "accessories": "Gold hoop earrings, a delicate gold chain necklace with a small pendant, a thin gold bangle bracelet on the left wrist, and a ring on the left hand. Manicure is painted white."
  },
  "anatomical_features": {
    "bust_volume": "Visually heavy and full, matching reference exactly, with natural gravity and projection clearly exceeding ribcage depth.",
    "skin_texture": "Realistic skin texture with natural pores and slight shine from lighting, no plastic smoothing.",
    "body_type": "Slim but curvaceous, with a narrow waist and toned abs contrasting with a full bust."
  },
  "pose": {
    "body_orientation": "Seated on a sofa, torso angled slightly to the viewer's left, head turned to face the camera directly.",
    "limbs": {
      "left_arm": "Extended back, hand resting on the sofa cushion for support.",
      "right_arm": "Relaxed, with the hand resting on the upper right thigh.",
      "left_leg": "Bent at the knee, leg resting on the sofa surface.",
      "right_leg": "Extended forward along the sofa, cropped at the thigh."
    },
    "posture": "Upright but relaxed spine, shoulders down, engaging the core.",
    "head_tilt": "Neutral, facing forward."
  },
  "environment": {
    "setting": "Luxury villa or resort interior, bright and airy.",
    "architecture": "White walls, high ceilings with exposed white wooden beams. Large glass sliding doors or windows in the background.",
    "decor": "White sofa with plush, slightly rumpled cream-colored cushions. A hanging black lantern fixture is visible in the background room.",
    "background_view": "Through the glass, a sunny outdoor scene is visible featuring lush green trees, a distant building, and blue sky."
  },
  "camera": {
    "shot_type": "Medium shot (thighs up).",
    "perspective": "Eye-level.",
    "focal_length": "50mm to 85mm portrait lens.",
    "depth_of_field": "Subject in sharp focus, background slightly softened but distinct.",
    "framing": "Centered subject, capturing the upper body and thighs, with space above the head showing the ceiling beams."
  },
  "lighting": {
    "source": "Natural daylight entering from the right and front.",
    "quality": "Bright, high-key lighting with soft, diffused shadows.",
    "shadows": "Subtle shadows on the left side of the torso and face (rembrandt-style lighting on face), defining muscle tone and depth.",
    "tone": "Warm and sunny."
  }
}
```

---

## Asymmetrical Dark Luxury Beauty Editorial Spread

A highly structured prompt for generating an asymmetrical editorial spread (1 large hero image, 2 stacked supporting images) for a beauty product (lipstick). The aesthetic is 'Dark luxury hybrid' with

```text
Asymmetrical editorial spread, 4:5 ratio.

LAYOUT: Irregular grid (1+2) - large hero (60%) left, two supporting images (20% each) stacked right
DIRECTION: None (editorial arrangement)
BACKGROUND: Deep burgundy velvet, single spotlight, Rembrandt lighting
PRODUCT: Hero - A glamorous Eurasian woman with wet, glossy dark red lips and dewy skin poses seductively in a burgundy velvet dress, dramatic rim lighting; Supporting 1 - Close up of blood-red glossy lipstick being applied with a brush; Supporting 2 - Lipstick tube lying on a dark velvet surface with scattered crimson glitter.
DYNAMIC: Subtle glitter particles floating around the lipstick and model - subtle intensity.
TONE: Brand monochrome - deep burgundy, wine red, crimson
STYLE: Dark luxury hybrid, opulent glamour
HERO CELL (left 60%): Seductive woman, hourglass figure, wet lips, intense sultry gaze
SUPPORTING CELL 1 (top right, 20%): Macro shot, extreme close-up, product texture
SUPPORTING CELL 2 (bottom right, 20%): Product flat lay, moody dark velvet surface
TYPOGRAPHY: Elegant serif, high contrast, gold foil effect on headlines
CAMERA: Hasselblad H6D, 85mm f/1.2, shallow depth of field, Rembrandt lighting
Style keywords: Opulent beauty, velvet, glossy lips, high fashion, dramatic lighting. A stylish handwritten signature {argument name="signature name" default="Willy"} is elegantly and small letters placed at the Bottom Right corner
```

---

## Bento Grid Product Infographic

Creates a bento grid infographic for product marketing with customizable modules.

```text
Create an infographic with bento grid 8 module layout, user can specify any product name in Food, Medicine, tech etc category, choose language, Background style, Hero grid style.
```

---

## Blonde Woman at Luxury Pool

Creates a photorealistic vertical portrait of a blonde woman in a black and cream one-piece swimsuit at a luxury outdoor pool.

```text
{
  "subject": {
    "identity": "a beautiful blonde woman",
    "gender": "female",
    "age": "early 20s",
    "body_type": "fit, feminine, toned legs, slim waist",
    "skin_tone": "light sun-kissed skin",
    "expression": "neutral, calm, confident",
    "gaze_direction": "looking slightly downward",
    "facial_features": "strong resemblance to beautiful woman, recognizable facial structure, eyes, lips, and nose"
  },
  "hair": {
    "color": "light blonde",
    "style": "messy high bun",
    "details": "loose strands falling naturally around face",
    "texture": "natural, soft"
  },
  "face_and_accessories": {
    "sunglasses": {
      "type": "small rectangular sunglasses",
      "color": "dark lenses, thin frame",
      "position": "worn properly on face"
    },
    "makeup": "natural summer makeup, minimal, glowing skin"
  },
  "clothing": {
    "swimsuit": {
      "type": "one-piece swimsuit",
      "color": "black body with cream/ivory bust detail",
      "cut": "high-cut legs, deep neckline, structured bust",
      "fabric": "smooth, matte swim fabric"
    },
    "outerwear": {
      "type": "oversized white shirt",
      "material": "light cotton",
      "position": "worn open, slipping off shoulders, sleeves loose"
    }
  },
  "pose": {
    "body_position": "standing upright near pool edge",
    "hip_position": "slightly shifted to one side",
    "arms": {
      "left_arm": "relaxed downward holding shirt edge",
      "right_arm": "slightly bent holding pool ladder"
    },
    "legs": {
      "stance": "one leg slightly forward",
      "feet": "barefoot on stone poolside"
    }
  },
  "environment": {
    "location": "luxury outdoor pool area",
    "pool": "clear turquoise water",
    "background_elements": [
      "sun loungers",
      "white umbrellas",
      "stone tiles",
      "large green pine trees",
      "terrace railing"
    ],
    "setting_vibe": "Mediterranean luxury resort"
  },
  "lighting": {
    "type": "natural daylight",
    "time_of_day": "midday",
    "sun_position": "high sun",
    "shadows": "soft natural shadows",
    "overall_mood": "bright, warm, summer atmosphere"
  },
  "camera": {
    "angle": "slightly low angle, eye-level torso focus",
    "distance": "medium-full body shot",
    "lens": "35mm",
    "depth_of_field": "sharp subject, slightly soft background"
  },
  "composition": {
    "framing": "vertical portrait",
    "subject_centering": "subject centered",
    "crop": "head to upper thighs visible"
  },
  "style_and_quality": {
    "style": "photorealistic",
    "resolution": "high resolution, ultra-detailed",
    "color_grading": "natural, warm tones",
    "skin_detail": "realistic skin texture, no over-smoothing"
  },
  "negative_prompt": [
    "cartoon",
    "anime",
    "illustration",
    "overexposed",
    "blurry",
    "extra limbs",
    "distorted body",
    "bad anatomy",
    "low quality"
  ]
}
```

---

## Book-Themed Diorama Grid Prompt

A complex prompt for Nano Banana Pro requesting a 2x2 grid of flawless, extreme close-up diorama miniatures built into prestigious museum pedestals, each panel representing a classic book ('The Hobbit

```text
2x2 grid format, prestigious museum pedestal, quartz and copper elements, flawless extreme close-up realism. Panel A: “The Hobbit” as a dragon hoard diorama excavated from adventure book pages: golden treasures piled, smaug coiled protectively with jeweled eyes. Panel B: “Inception” as a dream-layer folding mechanical sculpture inside dream journal: cityscapes bending via articulated hinges, totem spinning eternally. Panel C: “Breaking Bad” as a desert RV lab miniature set carved into chemistry text: crystal production setup, tiny hazmat figures at work. Panel D: “The Godfather” as a wedding garden combo automaton over family saga volume: dancing couples with implied tension, orange peel details, subtle turning mechanisms.
```

---

## Bossy Gangster with Cheetah Portrait Prompt

A prompt for generating a powerful, stylish image of a man radiating 'bossy gangster vibes' seated on a velvet sofa. The key element is a cheetah draped across his lap, adorned with heavy gold chains,

```text
GENERATE A POWERFUL AND STYLISH IMAGE OF THE UPLOADED MAN, 100 PERCENT FACE RESERVED, RADIATING BOSSY GANGSTER VIBES. HE IS SEATED CONFIDENTLY ON A LUXURIOUS VELVET SOFA, LEANING BACK IN A RELAXED YET COMMANDING POSE. A CHEETAH, ADORNED WITH HEAVY GOLD CHAINS, SITS ACROSS HIS LAP, ITS SLEEK BODY DRAPED NATURALLY OVER HIM.

THE MAN'S HEAD IS TURNED SLIGHTLY DOWNWARD, GAZING AT THE CHEETAH WITH A COOL, COMPOSED EXPRESSION, SUNGLASSES ENHANCING HIS AURA OF DOMINANCE AND STYLE. ONE HAND RESTS CASUALLY ON THE CHEETAH'S BACK WHILE THE OTHER RESTS ALONG THE ARM OF THE SOFA, SHOWING BOTH CONTROL AND EASE.

HE IS DRESSED IN HIGH-FASHION DARK ATTIRE - EITHER A PINSTRIPE SUIT OR AN OPEN-COLLARED SILK SHIRT LAYERED WITH BOLD GOLD JEWELRY. THE CHEETAH HAS A FIERCE, OPEN-MOUTH EXPRESSION, MIRRORING THE MAN'S AURA OF RAW POWER.
```

---

## Botanical Luxury Product Design Prompt

A simple, high-level prompt used with Nano Banana Pro to generate images focused on botanical luxury product design, likely requiring further detail or a specific style to be effective.

```text
Botanical Luxury Product Design
```

---

## Brand x Sneakers Product Matchmaker Prompt

A conceptual prompt title suggesting the generation of imagery that matches a brand aesthetic with sneakers. The full prompt text is linked externally and not provided in the tweet content.

```text
Brand x Sneakers prod. matchmaker
```

---

## Brand-to-Duffle Design Conversion

A simple prompt instructing the Nano Banana model to transform any specified brand into a duffle bag design, likely used for creative product visualization or mockups.

```text
Turning any {argument name="brand" default="brand"} into a duffle design
```

---

## Branded Crumpled Stickers (Placeholder)

This tweet mentions a prompt for 'Branded crumpled stickers' but the prompt text is missing, indicated by the trailing ellipsis and lack of content.

```text
Branded crumpled stickers
```

---

## Branded Fast Food Leather Bag

A simple prompt requesting the generation of a branded fast food leather bag.

```text
Branded fast food leather bag
```

---

## Brands in 19th Century Prompt

A simple text prompt intended to generate images of modern brands reimagined in a 19th-century aesthetic, likely for visual humor or historical mashups.

```text
Brands in 19th century
```

---

## Brutalist Poster Generation Prompt

A general prompt for transforming any brand concept into a Brutalist style poster, suggesting a visual aesthetic characterized by raw, uncompromising design.

```text
Any brand to Brutalist Poster
```

---

## Building an Inventory Management System

Optimizes product and e-commerce strategies for building an inventory management system.

```text
Act as a Software Architect. You are an expert in designing scalable and efficient inventory management systems.

Your task is to outline the key components and elements necessary for building an inventory management system.

You will:
- Identify essential pages such as dashboard, product listing, inventory tracking, order management, and reports.
- Specify database structure requirements including tables for products, stock levels, suppliers, orders, and transactions.
- Recommend technologies and frameworks suitable for the system.
- Provide guidelines for integrating with existing systems or APIs.

Rules:
- Focus on scalability and efficiency.
- Ensure the system supports multi-user access and role-based permissions.
```

---

## Campy High-Fashion Editorial at a Gas Station

A detailed prompt for generating a high-fashion, glamorous, and campy editorial image. It features a woman in a voluminous feather gown refueling a luxury SUV at a gas station at night, juxtaposing hi

```text
{
  "prompt_description": {
    "subject_details": {
      "gender": "Female",
        "color": "Platinum blonde",
        "style": "Messy high ponytail or updo",
      "expression": "Model-like pout, looking directly at the camera",
     "skin_features": "light skin tone with freckles",
      "pose": "Standing profile-forward, leaning slightly towards the vehicle, holding a gas nozzle"
    },
    "outfit": {
      "dress": "Strapless, voluminous baby {argument name="dress color" default="pink"} gown entirely covered in feathers (ostrich style), high-low hemline (mini in front, floor-length train in back)",
      "legwear": "White, sheer floral lace patterned tights/stockings",
      "footwear": "Metallic silver pointed-toe stiletto heels",
      "accessories": "Large diamond drop earrings, delicate bracelets on both wrists"
    },
    "action": {
      "primary_activity": "Refueling a vehicle",
      "interaction": "Hand gripping the black handle of a gas pump nozzle inserted into the fuel tank"
    },
    "setting": {
      "location": "Gas station under a canopy",
      "time_of_day": "Night",
      "vehicle": "Black luxury SUV (resembling a Mercedes-Benz G-Wagon), glossy paint, chrome running boards/exhaust tips",
      "equipment": "Gas pump with blue and white branding (Chevron logo visible), digital price displays, green and black nozzle handles",
      "background": "Convenience store with illuminated interior visible through glass windows in the distance, dark night sky"
    },
    "aesthetic": {
      "style": "High-fashion editorial, glamorous, campy",
      "lighting": "Bright, cool-toned overhead artificial lights from the gas station canopy, creating highlights on the car and subject",
      "atmosphere": "Juxtaposition of high-end luxury fashion with a mundane everyday activity"
    }
  }
}
```

---

## Candid Outdoor Bikini Portrait with Tropical Background

Creates a photorealistic, candid outdoor portrait of a young woman in a colorful floral bikini with a fit, curvy physique.

```text
{
  "subject": {
    "description": "A young woman with long blonde hair tied in a high, messy ponytail. She has a tanned complexion and a fit, curvy physique. She is wearing a colorful floral bikini consisting of a strapless bandeau top and high-cut thong bottoms. The bikini features a bright pattern with hues of yellow, orange, pink, green, and blue. She is wearing gold jewelry, including small hoop earrings, a ring on her left hand, and a gold bangle bracelet on her left wrist. Her skin shows natural texture, including moles and sun-kissed tone."
  },
  "anatomical_details": {
    "body_type": "Fit and curvy with prominent gluteal muscle definition.",
    "proportions": "Athletic build with a slim waist and wider hips relative to the waist. The buttocks are full and round, visually emphasized by the pose.",
    "hair": "Blonde, highlighted, straight texture, pulled back into a high ponytail with loose strands framing the face.",
    "face": "Oval face shape, bright white smile with visible teeth, joyful expression, looking directly at the viewer over her left shoulder."
  },
  "pose": {
    "orientation": "Standing rear view, twisting torso to the left.",
    "head_position": "Turned over the left shoulder to face the camera.",
    "limbs": {
      "left_arm": "Raised, elbow bent, hand touching the top of the head/base of the ponytail.",
      "right_arm": "Extended downwards, hand resting on the upper left thigh/glute area.",
      "legs": "Standing straight with weight slightly shifted, emphasizing the curve of the hips."
    },
    "spine_curvature": "Natural lumbar curve accentuated by the twist and rear angle."
  },
  "environment": {
    "setting": "Outdoor tropical park or garden walkway.",
    "background_elements": [
      "Lush green tropical foliage",
      "Palm tree trunks",
      "Dense bushes"
    ],
    "midground": "A low, light gray concrete retaining wall running horizontally behind the subject.",
    "foreground": "Light gray paved walkway with dappled shadows from the trees."
  },
  "camera": {
    "shot_type": "Medium shot (thighs up).",
    "angle": "Eye-level or slightly low angle relative to the subject's hips.",
    "focus": "Sharp focus on the subject, slight depth of field blurring the background foliage.",
    "perspective": "Rear perspective capturing the back and side profile."
  },
  "lighting": {
    "type": "Natural bright daylight.",
    "direction": "Overhead and slightly from the right, creating distinct shadows.",
    "quality": "High contrast, hard sunlight creating dappled leaf shadows on the ground and bright highlights on the skin and hair.",
    "shadows": "Natural cast shadows on the ground and self-shadowing on the back and legs."
  },
  "mood_and_expression": {
    "emotion": "Happy, confident, playful, radiant.",
    "facial_expression": "Wide, genuine smile."
  },
  "style_and_realism": {
    "style": "Candid outdoor photography, lifestyle portrait.",
    "render_quality": "Photorealistic, high fidelity, raw photo quality.",
    "texture": "Realistic skin texture, fabric weave of the bikini, concrete texture of the wall."
  }
}
```

---

## Car Selfie with Cheese Cracker Prompt

A structured JSON prompt for generating an image of a young woman winking and smiling in the driver's seat of a car, specifically holding a cheese cracker in her mouth, detailing her features, attire,

```text
{
  "subject": {
    "type": "person",
    "gender": "female",
    "age_group": "young adult",
    "hair_color": "blonde",
    "eye_color": "blue",
    "features": "freckles",
    "expression": "winking, smiling",
    "action": "holding a cheese cracker in mouth"
  },
  "attire": {
    "clothing": "black long-sleeved scoop-neck top"
  },
  "setting": {
    "location": "inside a car",
    "position": "driver's seat",
    "interior": "black and white leather seats",
    "background": "trees, daylight, car window"
  },
  "object": {
    "type": "food",
    "description": "orange square cheese cracker"
  }
}
```

---

## Carbon Pattern Printed Ehomaki Sushi Roll

Generates an Ehomaki sushi roll with carbon fiber pattern printed on nori.

```text
I saw an Ehomaki with a checkered pattern printed on the nori, so I wondered what it would look like with a carbon fiber pattern?
```

---

## Casual Lifestyle Portrait in Cafe

A detailed JSON prompt for generating a casual lifestyle portrait of a young woman in a cafe, focusing on specific pose details, athleisure outfit (unitard/jumpsuit), and high-end accessories like a L

```text
{
  "scene": "Casual lifestyle portrait in an indoor cafe setting",
  "subject": {
    "character": "Young female with a friendly, relaxed demeanor",
    "face": {
      "structure": "Oval shape with prominent cheekbones and visible dimples",
      "skin": "Tan, smooth, glowing complexion",
      "eyes": {
        "shape": "Almond",
        "color": "Dark brown",
        "expression": "Direct eye contact, engaging"
      },
      "mouth": {
        "lips": "Natural pink, smiling gently"
      },
      "makeup": "Natural 'no-makeup' look, light blush, groomed brows"
    },
    "hair": {
      "color": "Dark brown to black",
      "length": "Shoulder-length (lob)",
      "texture": "Straight with slight volume",
      "style": "Loose with wispy bangs framing the forehead",
      "shine": "Healthy, slight sheen"
    },
    "accessories": {
      "necklace": "Thin gold chain with a heart pendant",
      "earrings": "Small silver or gold hoops",
      "bracelets": "Thin metallic bracelets on both wrists",
      "rings": "Simple bands on fingers"
    }
  },
  "pose": {
    "overall": "Casual seated pose, leaning back slightly against the chair",
    "position": {
      "base": "Sitting on a wooden chair",
      "orientation": "Facing forward towards the camera"
    },
    "torso": {
      "direction": "Frontal",
      "posture": "Relaxed but upright"
    },
    "arms": {
      "position": "Right arm holding a straw/drink, left arm resting near the table",
      "other": "Holding an iced drink near chest level"
    },
    "legs": {
      "position": "Asymmetrical; right leg bent with knee drawn up, left leg extended downwards",
      "visible": "Legs fully visible in tight fitting clothing"
    },
    "head": {
      "turn": "Facing straight forward",
      "expression": "Soft, confident smile"
    }
  },
  "outfit": {
    "activewear": {
      "type": "Sleeveless unitard / jumpsuit",
      "color": "Beige / Nude",
      "style": "Athleisure",
      "details": {
        "top": "V-neckline, sleeveless",
        "fit": "Form-fitting, skin-tight",
        "material": "Ribbed or smooth stretch fabric"
      }
    },
    "footwear": {
      "type": "Sneakers",
      "style": "Grey athletic running shoes (New Balance style)",
      "socks": "White ribbed crew socks"
    }
  },
  "body": {
    "type": "Fit, slender",
    "skin": "Tan"
  },
  "environment": {
    "location": "Coffee shop interior",
    "furniture": {
      "table": "Round wooden table with slatted base",
      "chair": "Wooden chairs with simple backrests"
    },
    "objects": {
      "drink": "Glass of iced {argument name="drink type" default="green matcha latte"} with a glass straw",
      "bag": "Louis Vuitton Monogram Speedy handbag on the table",
      "sunglasses": "Black frame sunglasses on the table",
      "coaster": "Small wooden plate/coaster"
    },
    "background": {
      "people": "Blurred figures sitting at other tables",
      "floor": "Concrete or stone tile"
    }
  }
}
```

---

## Casual Main Character Selfie with Pink BMW i8 Prompt

A highly detailed Chinese prompt for generating a hyper-realistic image of a young woman taking a selfie next to a chrome pink BMW i8. The prompt specifies a 'casual main character energy', detailed c

```text
{
  "subject": {
    "description": "Young woman taking selfie next to chrome pink BMW i8, casual main character energy",
    "setting_rules": "street scene, luxury car, urban modern backdrop",
    "age": "early 20s",

    "expression": {
      "eyes": "focused on phone screen, taking selfie, casual confidence",
      "mouth": "relaxed, soft, natural",
      "brows": "relaxed, effortless",
      "overall": "unbothered, 'just casually next to a pink supercar' energy"
    },

    "hair": {
      "color": "platinum blonde",
      "style": "loose, flowing from under cap",
      "details": "messy-pretty, some pieces falling forward, effortless waves",
      "length": "medium-long, past shoulders"
    },

    "body": {
      "frame": "petite, slim, toned",
      "waist": "tiny, fully exposed midriff",
      "legs": "toned, athletic, fully visible",
      "stance": "casual lean against car, weight shifted"
    },

    "pose": {
      "position": "standing next to driver door of car, leaning slightly against it",
      "upper_body": {
        "action": "one arm UP holding phone for selfie",
        "phone_angle": "high, classic selfie position",
        "other_arm": "relaxed at side"
      },
      "lower_body": {
        "stance": "one leg straight, one slightly crossed or bent",
        "weight": "casual lean, hip near car",
        "energy": "relaxed but aware of angles"
      },
      "overall": "the 'caught me with this random supercar' pose that's definitely not random"
    },

    "clothing": {
      "top": {
        "type": "ultra cropped baby tee",
        "color": "bright YELLOW, sunshine yellow",
        "graphic": "small star or cute graphic on chest (or {argument name="标志" default="BANANA logo"})",
        "fit": {
          "length": "EXTREME crop - ends just below chest, full stomach exposed",
          "tightness": "fitted, hugging curves",
          "sleeves": "short sleeves, casual"
        },
        "effect": "entire midriff visible from just under chest to shorts"
      },
      "bottom": {
        "type": "ultra mini athletic shorts",
        "color": "WHITE, clean bright white",
        "fit": {
          "style": "tight fitted athletic shorts",
          "length": "very short, upper thigh",
          "waist": "high-waisted, sits at natural waist",
          "effect": "shows full leg length, hugs curves"
        },
        "material": "stretchy athletic fabric, smooth"
      },
      "shoes": {
        "type": "white sneakers",
        "style": "clean, casual, athletic vibe",
        "effect": "completes sporty-cute look"
      }
    },

    "face": {
      "features": "pretty, big eyes, small nose, soft lips",
      "makeup": "natural, minimal, fresh-faced",
      "expression": "focused on selfie, casual pretty"
    }
  },

  "accessories": {
    "headwear": {
      "type": "baseball cap",
      "color": "BLACK",
      "style": "worn forward, classic",
      "logo": "small patch or logo visible",
      }
```

---

## Celebrity Image Database Prompt Structure

A structured JSON prompt that functions as a database or instruction set for generating images of specific celebrities (Sydney Sweeney and Ana de Armas) in various predefined scenes, outfits, and mood

```text
{
  "celebrity_image_database": {
    "subject_1": {
      "name": "{argument name="subject 1 name" default="Sydney Sweeney"}",
      "visual_data": [
        {
          "scene_type": "Summer Boat Trip",
          "setting": "Speedboat on a sunny lake, forest background",
          "outfit": "Black and white athletic zip-up wetsuit",
          "features": "Blonde beach waves, chunky black sunglasses",
          "mood": "Playful and laughing"
        },
        {
          "scene_type": "Cinematic Indoor",
          "setting": "Dimly lit indoor staircase",
          "outfit": "Hot pink cut-out swimsuit",
          "props": "Holding a glass bottle with blue liquid",
          "hair_style": "Blonde hair with thin face-framing braids"
        }
      ]
    },
    "subject_2": {
      "name": "{argument name="subject 2 name" default="Ana de Armas"}",
      "visual_data": [
        {
          "scene_type": "High-Fashion Editorial",
          "setting": "Luxury lounge, black leather sofa, neon blue and pink background",
          "outfit": "Red sequined blazer and matching skirt, black silk inner",
          "jewelry": "Layered gold necklaces, multiple gold bangles",
          "pose": "Sitting elegantly leaning on a round black table"
        },
        {
          "scene_type": "Outdoor Garden",
          "setting": "Lush tropical greenery, wicker sofa with white cushions",
          "outfit": "Yellow and blue patterned strapless dress, magenta heels",
          "props": "Lime green champagne bucket with bottles"
        },
        {
          "scene_type": "Candid/Fan Interaction",
          "setting": "Rainy street, under a black umbrella",
          "outfit": "White button-up blouse with decorative buttons",
          "hair_style": "Dark hair in a messy elegant updo"
        },
        {
          "scene_type": "Beach Lifestyle",
          "setting": "Ocean waves in the background",
          "outfit": "White high-waisted bikini with pineapple print top",
          "accessories": "Round sunglasses, blue beaded bracelet"
        },
        {
          "scene_type": "Casual Outdoor",
          "setting": "Sitting on green grass, white wall background",
          "outfit": "Mustard yellow off-the-shoulder top, floral embroidered shorts",
          "hair_style": "Sleek high ponytail"
        }
      ]
    },
    "technical_meta": {
      "image_quality": "High-definition, realistic",
      "platform_focus": "Social media content creation (Twitter/Instagram)",
      "target_year": "2026"
    }
  }
}
```

---

## Change clothing to match reference outfit

A fashion-edit prompt that swaps the user’s clothes to match those shown in a reference image while keeping everything else intact.

```text
Take the clothing from the reference and change mine to match it
```

---

## Chocolate Cinematic Ad Prompt

A short, high-level prompt for generating a cinematic advertisement image of chocolate, focusing on luxury, molten texture, and a floating presentation style.

```text
Floating fondant, molten core, luxury ad vibes.
```

---

## Christmas Tree Branding Template Prompt

A simple template prompt for Nano Banana Pro designed to generate images of a Christmas tree styled according to a specified brand's theme, set against a contrasting studio background.

```text
A Christmas tree designed in the theme of {argument name="brand name" default="[BRAND NAME]"} brand, contrasting studio background in bold color.
```

---

## Chrome Ripple Flow Product Photography

Creates a floating product with matte black and metallic silver finishes on a ribbed surface.

```text
{
  "image_generation_request": {
    "subject": "{argument name="product name" default="PRODUCT"}",
    "product_finish": {
      "primary": "matte black with subtle light absorption",
      "secondary": "polished metallic silver with mirror-like reflections",
      "treatment": "duotone — matte black body with metallic silver accents, trim, edges, or panel insets"
    },
    "composition": {
      "placement": "dead center, full view, floating suspended within the folded surface environment",
      "scale": "product occupies roughly 30-40% of the frame",
      "constraints": [
        "product must be entirely visible with no cropping",
        "no pedestals, stands, platforms, or ground planes"
      ]
    },
    "background_environment": {
      "description": "A single continuous undulating surface that fills the entire frame, folding over and around itself in large voluminous waves",
      "surface_texture": {
        "type": "fine parallel ribs embossed into the surface — like the grooves on a vinyl record or finely pleated accordion fabric"
      }
    }
  }
}
```

---

## Cinematic Concept Art of Sadie Sink as Jean Grey

Creates a cinematic 3D render or concept art of Sadie Sink portraying Jean Grey with three distinct costume variants.

```text
{
  "subject": {
    "actor_likeness": "Sadie Sink",
    "character": "Jean Grey (Marvel Comics)",
    "physical_features": {
      "hair": "Long, voluminous, wavy ginger-red hair, natural texture",
      "eyes": "Pale blue/grey",
      "expression": "Stoic, determined, heroic neutral",
      "build": "Athletic, slender"
    }
  },
  "costume_variants": {
    "variant_1_phoenix": {
      "base_color": "Metallic emerald green",
      "accents": "Gold chrome gloves, boots, and waist sash",
      "insignia": "Large white Phoenix force emblem on chest",
      "style": "Sleek spandex-metallic hybrid"
    },
    "variant_2_classic_xmen": {
      "base_color": "Dark forest green leather",
      "accents": "Yellow 'X' symbols on belt and boot straps",
      "armor": "Metallic green sculpted breastplate and abdominal plating",
      "headwear": "V-shaped green metallic tiara/circlet"
    },
    "variant_3_tactical_armor": {
      "base_color": "Deep crimson/burgundy textured fabric",
      "armor_plating": "Iridescent cobalt blue metallic plating on chest, shoulders, forearms, and shins",
      "insignia": "Red and black 'X' logo on belt",
      "headwear": "Integrated blue metallic combat headset/tiara"
    }
  },
  "artistic_style": {
    "type": "Cinematic 3D render / Concept art",
    "lighting": "Studio rim lighting, volumetric glow, subtle golden aura or smoke",
    "background": "Solid studio backdrop (Slate blue or Charcoal) with atmospheric haze",
    "framing": "Full-body shot, centered composition, eye-level camera angle",
    "texture_quality": "High-fidelity fabric weave, metallic reflections, realistic skin pores"
  },
  "technical_parameters": {
    "aspect_ratio": "2:3",
    "resolution": "4K",
    "rendering_engine": "Unreal Engine 5 / Octane Render style"
  }
}
```

---

## Cinematic Fashion Editorial of Sydney Sweeney on a Roman Balcony

An image generation prompt structured in JSON format to create a high-fashion, cinematic portrait of Sydney Sweeney on a stone balcony overlooking historic Roman architecture during the golden hour. T

```text
{
  "image_description": {
    "scene": {
      "location": {
        "city": "{argument name="city" default="Rome"}",
        "setting": "Stone balcony overlooking historic Roman architecture",
        "details": "The scene is set on a classic stone balcony, featuring an expansive view of Rome's ancient buildings, monuments, and the city skyline. The warm golden light of natural daylight casts soft shadows on the stone, highlighting intricate architectural elements of the city."
      },
      "environment": {
        "elements": [
          "Stone balcony with ornate railings",
          "Ancient Roman buildings in the background",
          "Clear sky with gentle light reflecting off glass windows",
          "Warm, soft glow from the golden hour sunlight"
        ],
        "atmosphere": "Serene, sophisticated, with a sense of timeless luxury and romance, evoking the beauty of luxury travel and refined femininity."
      },
      "lighting": {
        "type": "Natural daylight",
        "effect": "The lighting is soft and crisp, highlighting architectural textures and the subject with a gentle glow. Shadows are softened, creating an inviting and elevated atmosphere."
      }
    },
    "subject": {
      "identity": "{argument name="subject identity" default="Sydney Sweeney"}",
      "pose": {
        "description": "The subject stands confidently near the stone railing, gazing outward towards the Roman skyline. She maintains a poised and elegant posture, embodying grace and sophistication, with a slight smile suggesting confidence and thoughtfulness."
      },
      "outfit": {
        "top": {
          "type": "Structured corset-style top",
          "color": "Dark red",
          "style": "Fashion editorial, modern yet classic, designed to accentuate the figure. The corset features sharp, defined lines and a clean, structured fit that contrasts beautifully with the natural environment."
        },
        "bottom": {
          "type": "High-waisted skirt",
          "details": "The skirt is high-waisted, with a dramatic thigh-high slit on both sides, giving it an edgy yet refined feel. The fabric flows gracefully, emphasizing the subject's femininity and modern elegance."
        }
      },
      "hair_and_makeup": {
        "hair": {
          "style": "Soft waves",
          "details": "Her hair is styled in natural, soft waves that cascade effortlessly, adding a sense of movement and vitality to the look. The waves are glossy, offering a polished yet relaxed style."
        },
        "makeup": {
          "style": "Refined and natural",
          "details": "The makeup enhances her natural beauty with subtle contouring and a soft highlight. Her eyes are defined with light eyeliner, and her lips sport a neutral shade, contributing to a sophisticated and timeless look."
        }
      }
    },
    "composition": {
      "aspect_ratio": "3:4",
      "orientation": "Vertical",
      "focus": {
        "subject": "The subject is the main focal point, "
      }
    }
  }
}
```

---

## Cinematic Fashion Portrait of Sadie Sink in Red Dress

Creates a high-resolution professional portrait of Sadie Sink in a glamorous red halter-neck mini dress in a luxurious penthouse lounge.

```text
A high-resolution, professional portrait of a beautiful woman with voluminous, wavy blonde hair and striking blue eyes. She is wearing a sleek, vibrant red halter-neck mini dress with a stylish V-shaped neckline. Her makeup is glamorous, featuring bold red lipstick and defined eye makeup. She is posed elegantly inside a modern, luxurious penthouse lounge with soft, ambient lighting. In the background, there is a warm, circular chandelier and wooden slatted room dividers, creating a cozy yet sophisticated atmosphere. The style is that of a cinematic fashion magazine photoshoot, capturing refined elegance and confidence.
```

---

## Cinematic Grunge Collage Portrait

Creates an ultra-photorealistic editorial fashion portrait with dark grunge aesthetic.

```text
Ultra photorealistic, 8K, 2:3 aspect ratio, 50mm prime lens f/1.8. Cinematic grunge collage portrait. Adult female early 20s, slim natural proportions. Confident fashion pose, right hand gently touching near face, left hand inside pants pocket. Calm self-assured expression. Voluminous curly shoulder-length dark brown hair. Loose black shirt, light beige pants. Artistic collage wall background with black-and-white cutouts: police car, Pegasus, perfume bottle, newspaper text clippings, abstract paint textures in charcoal and gray.
```

---

## Cinematic Low-Key Portrait in Red Rose Room

Creates a dramatic, low-key cinematic portrait of a woman in a red dress surrounded by red roses.

```text
{
  "generation_request": {
    "meta_data": {
      "task_type": "cinematic_lowkey_valentines_rose_room_red_dress",
      "language": "en",
      "priority": "highest",
      "version": "v1.0_RED_DRESS_ROSE_ROOM_LOWKEY_DRAMA"
    },
    "output": {
      "aspect_ratio": "4:5",
      "resolution": "ultra_high",
      "num_images": 4,
      "sharpness": "high",
      "grain": "fine_film_grain"
    },
    "scene": {
      "concept": "dramatic low-key cinematic portrait of a woman in a room filled with red roses",
      "environment": "dark minimalist interior room, glossy white floor, multiple large glass vases filled with dense red rose bouquets arranged around the subject in a circle",
      "composition": "top-down or slightly elevated angle, subject centered, surrounded by roses, strong negative space in shadows, deep vignette edges",
      "mood": "luxury, moody, intimate, dramatic"
    },
    "subject": {
      "person": "adult woman",
      "pose": "sitting on the floor with legs folded to the side, holding or resting arms on a bouquet, head slightly bowed, gaze downward",
      "expression": "soft, introspective, calm",
      "hair": "very long straight black hair, sleek and glossy, center part",
      "makeup": "full glam: defined lashes, soft contour, nude-pink lips or subtle rose tone",
      "wardrobe": {
        "dress": "fitted red maxi dress with thin straps, smooth fabric, clean silhouette, realistic folds at seated position"
      },
      "accessories": "minimal jewelry, small necklace"
    },
    "lighting": {
      "setup": "single strong soft spotlight from above-left creating dramatic shadows; minimal fill",
      "look": "low-key, chiaroscuro style, deep blacks",
      "highlights": "controlled highlights on roses and hair; no blown whites on floor"
    }
  }
}
```

---

## Cinematic Portrait of Man on Motorbike

Creates an ultra-realistic cinematic portrait of a man on a modern motorbike during golden hour.

```text
Ultra-realistic cinematic photography. Man with same facial features as reference image. Sitting confidently on a stylish modern motorbike, one foot on the ground, relaxed but powerful posture. Calm confident slightly intense look. Black leather jacket, plain white crew-neck t-shirt, cool black sunglasses. Beautiful open road surrounded by greenery, soft-focus mountains in distance. Golden hour, natural warm sunlight with soft cinematic shadows, rim light. Low-angle slightly front-facing shot, 85mm DSLR lens, shallow depth of field.
```

---

## Clothing items laid out on asphalt

A very short edit-style prompt asking the model to separate and place each piece of a person’s clothing on asphalt, useful for testing object extraction and rearrangement.

```text
Give each piece of his clothing separately on the asphalt
```

---

## Clothing laid out separately on a bed

A short English prompt for generating an image where each piece of a girl’s clothing is placed separately on a bed.

```text
Give each piece of her clothing separately on the bed
```

---

## Clothing separated on the bed

An edit-style prompt that takes a reference person and lays out each piece of her clothing separately on a bed.

```text
Give each piece of her clothing separately on the bed
```

---

## Collectible Toyline Forge Engine System Prompt

A complex system prompt designed for an AI model acting as a 'Collectible Toyline Forge Engine.' It instructs the AI to interpret an object's form into a stylized character/figure, infer articulation,

```text
Do this for {argument name="subject" default="Nikola Tesla"}<analysis> You are the Collectible Toyline Forge Engine. An AI toy designer and packaging stylist. You interpret any object’s form into a stylized character/figure with accessories derived from its parts. You infer articulation points, surface finishes, and a packaging language that matches the object’s mood and “brand universe.” </analysis>

[DESIGNER FIGURE TYPE] inspired by [OBJECT] Materials: [Toy/packaging materials inferred from source + finish logic] Key Features: [3 to 5 bullets: silhouette gimmick, accessories, articulation, micro-details] Colorway: [Palette derived from object] Edition: [Toyline name + drop/series tag]
```

---

## Conceptual High-End Product Design Prompt

A very brief, high-level prompt instructing the AI to generate a conceptual high-end product design. The full details are likely in the linked image (not provided), but the core instruction is extract

```text
Conceptual high-end product design
```

---

## Conceptual Luxury Fashion Portrait with Shadow Sculpting

A prompt for generating a conceptual luxury fashion portrait where the subject's black couture gown is sculpted and defined by architectural shadows created by dramatic directional studio lighting, em

```text
{
  "render_goal": "Conceptual luxury fashion portrait",
  "subject": {
    "pose": "female standing confidently under strong directional light",
    "expression": "subtle confident smile"
  },
  "wardrobe": "minimal black couture gown with cutout layers formed by {argument name="sculpting element" default="shadows"}",
  "environment": {
    "location": "studio with dramatic lighting",
    "props": "architectural shadows shaping the dress silhouette"
  }
}
```

---

## Coquette Aesthetic 'Get Ready With Me' Selfie

A structured prompt for generating a 'Get Ready With Me' style image with a coquette aesthetic, featuring a young woman applying lip gloss in front of a Hollywood-style vanity mirror, emphasizing a mo

```text
{
  "image_details": {
    "subject": {
      "person": "Young woman",
      "pose": "Leaning forward slightly towards a vanity mirror, applying lip gloss with right hand, left hand resting on the table surface",
      "expression": "Soft gaze, lips slightly parted",
      "hair": "Dark, slicked back into a low bun with a middle part",
      "makeup": "Dewy skin, rosy blush, glossy pink lips, groomed eyebrows, light mascara",
      "clothing": {
        "top": "Light pink satin crop top with spaghetti straps",
        "bottom": "Matching light pink satin mini skirt",
        "outerwear": "Fuzzy, textured pink cardigan worn off the shoulders",
        "jewelry": "Layered silver necklaces (one pearl-like choker, one chain, one with a heart pendant), small heart hoop earrings"
      }
    },
    "setting": {
      "room": "Bedroom or dressing room with pink walls",
      "lighting": "Bright vanity mirror lights (Hollywood style bulbs) visible on the left frame and top, natural light from a window in the background",
      "furniture": {
        "vanity": "White vanity table with a large mirror",
        "drawers": "White 9-drawer unit (tall chest) in the background reflection",
        "seating": "Pink plush chair or sofa visible in the background"
      },
      "background_elements": {
        "window": "Large window with sheer white curtains",
        "decor": "Hello Kitty plush toys (one large pink one on the seating, smaller ones on shelves), a gold-framed floor mirror in the background"
      }
    },
    "foreground_objects": {
      "vanity_surface": {
        "perfume": "Square glass perfume bottle with pink liquid and crystal-like cap",
        "makeup_tools": "Jar of makeup brushes (brown and rose gold handles)",
        "cosmetics": "Various makeup palettes, tubes, and a Glossier lip gloss tube standing upright",
        "action_item": "Lip gloss wand being held near lips"
      }
    },
    "composition": {
      "perspective": "Selfie-style or shot through a mirror reflection",
      "color_palette": "Monochromatic pink theme (various shades of pink), white accents, warm lighting",
      "style": "Coquette aesthetic, 'Get Ready With Me' vibe, soft and feminine"
    }
  }
}
```

---

## Coquette Aesthetic Vanity Selfie Prompt

A detailed JSON prompt for generating an image of a young woman applying lip gloss in a coquette-style bedroom setting, featuring a monochromatic dark cherry red theme, Hollywood vanity lights, and He

```text
{
  "image_details": {
    "subject": {
      "person": "Young woman",
      "pose": "Leaning forward slightly towards a vanity mirror, applying lip gloss with right hand, left hand resting on the table surface",
      "expression": "Soft gaze, lips slightly parted",
      "hair": "Dark, slicked back into a low bun with a middle part",
      "makeup": "Dewy skin, rosy blush, glossy pink lips, groomed eyebrows, light mascara",
      "clothing": {
        "top": "{argument name=\"top color and style\" default=\"dark cherry red satin crop top with spaghetti straps\"}",
        "bottom": "Matching dark cherry red satin mini skirt",
        "outerwear": "Fuzzy, textured dark cherry red cardigan worn off the shoulders",
        "jewelry": "Layered silver necklaces (one pearl-like choker, one chain, one with a heart pendant), small heart hoop earrings"
      }
    },
    "setting": {
      "room": "Bedroom or dressing room with {argument name=\"room color\" default=\"pink\"} walls",
      "lighting": "Bright vanity mirror lights (Hollywood style bulbs) visible on the left frame and top, natural light from a window in the background",
      "furniture": {
        "vanity": "White vanity table with a large mirror",
        "drawers": "White 9-drawer unit (tall chest) in the background reflection",
        "seating": "Pink plush chair or sofa visible in the background"
      },
      "background_elements": {
        "window": "Large window with sheer white curtains",
        "decor": "Hello Kitty plush toys (one large pink one on the seating, smaller ones on shelves), a gold-framed floor mirror in the background"
      }
    },
    "foreground_objects": {
      "vanity_surface": {
        "perfume": "Square glass perfume bottle with pink liquid and crystal-like cap",
        "makeup_tools": "Jar of makeup brushes (brown and rose gold handles)",
        "cosmetics": "Various makeup palettes, tubes, and a Glossier lip gloss tube standing upright",
        "action_item": "Lip gloss wand being held near lips"
      }
    },
    "composition": {
      "perspective": "Selfie-style or shot through a mirror reflection",
      "color_palette": "Monochromatic dark cherry red theme (various shades of pink), white accents, warm lighting",
      "style": "{argument name=\"aesthetic style\" default=\"Coquette aesthetic\"}, 'Get Ready With Me' vibe, soft and feminine"
    }
  }
}
```

---

## Coquette Pink Fashion Editorial

A structured prompt for generating a romantic editorial photograph in the 'Coquette Pink' style. It describes a young woman in a pastel pink mini dress, twirling in a European villa garden, emphasizin

```text
{
 "subject": "{argument name="subject description" default="Young woman, soft curls, doe eyes, blush makeup"}", "outfit": "Pastel pink coquette mini dress, bow details, pearl accessories", "pose": "Twirling in garden courtyard, joyful laugh", "environment": "European villa garden, roses, fountain", "style": "Romantic editorial photography, soft focus bokeh, dreamy pastel palette"
}
```

---

## Cozy-Sweet Editorial Portrait with Cotton Candy

A prompt for generating a whimsical, cozy-sweet editorial portrait with playful, soft realism. It focuses on a subject interacting with pastel cotton candy at a fair, specifying high-key lighting, sof

```text
• Concept: Cozy-sweet editorial, face preserved, playful-soft realism.

• Story: Blowing bubbles or eating a giant pastel {argument name="cotton candy color" default="pastel"} cotton candy at a fair.

• Clothing: Oversized pastel knit sweater, pleated baggy.

• Accessories: Glitter on the cheekbones, colorful hair clips.

• Pose: Peering through the cotton candy, eyes wide and bright, slight playful pout.

• Lighting: Bright, soft "candy" colors, high-key lighting with no harsh shadows.

• Background: Blurred carnival lights, pastel-colored booths.

• Camera: 35mm, vibrant saturation, soft focus on the edges.

• Style: Whimsical, youthful, soft-focused skin and bright eyes.
```

---

## Crystal Hologram Product Photography

Creates ultra-high-fidelity product photography with crystal hologram effect.

```text
Ultra_high_fidelity_request: {argument name="product" default="[PRODUCT]"}. Strictly centered and levitating, full product visibility, zero cropping, isolated in 3D space. Solid pure black void background #000000. Extremely brilliant spectral iridescence, vivid neon oil-slick gradients. Internal volumetric lighting, ethereal inner glow. High-index caustic light refraction, prismatic color splitting at edges. Super-saturated holographic highlights, intense electric blues and deep magentas. Ultra-glossy liquid-smooth finish, deep translucent obsidian glass with infinite depth.
```

---

## Curvy Woman on Luxury Yacht Prompt

A highly detailed, structured prompt for Nano Banana Pro describing a scene with a young, curvy woman posing seductively at the helm of a luxury yacht. It meticulously defines her facial features, hai

```text
{ "scene": "A young woman sitting at the helm of a luxury yacht on the open ocean under a bright, partly cloudy sky.",

"subject": { "character": "Young woman with a curvy physique and tanned complexion, posing while steering a boat.",

"face": {
  "structure": "Soft oval face with rounded cheeks and a defined jawline.",
  "skin": "Sun-kissed tanned skin with a natural glow and subtle texture.",
  "eyes": {
    "shape": "Almond-shaped",
    "color": "Dark brown",
    "expression": "Alluring, direct gaze over the shoulder toward the lens."
  },
  "mouth": {
    "lips": "Full, naturally pigmented lips with a slight pouty, neutral expression."
  },
  "makeup": "Minimal, natural 'no-makeup' look with groomed eyebrows and a hint of lip balm."
},

"hair": {
  "color": "Deep espresso brown, appearing almost black in shadows.",
  "length": "Medium length, approximately shoulder-blade level when down.",
  "texture": "Type 3C curly texture; dense, coiled, and naturally voluminous.",
  "style": "High messy bun updo with loose tendrils and natural flyaways around the hairline.",
  "visible": "Secured on top of the head, revealing the neck and back."
},

"accessories": {
  "hat": {
    "type": "none",
    "color": "n/a",
    "detail": "n/a",
    "fit": "n/a"
  }
}
},

"pose": { "overall": "Seated, twisting torso back toward the camera in a dynamic, over-the-shoulder pose.",

"position": {
  "base": "Seated on a blue cushioned bench at the boat's helm.",
  "orientation": "Body angled toward the steering wheel, head turned 90 degrees back."
},

"torso": {
  "direction": "Facing the helm station.",
  "position": "Twisted rightward to face the viewer, arching the back slightly."
},

"hips": {
  "position": "Seated firmly on the cushion.",
  "emphasis": "Highly emphasized curvature, angled to showcase the profile."
},

"legs": {
  "position": "Left leg bent at the hip and knee, foot resting on the deck; right leg tucked.",
  "visible": "Lower left thigh and knee visible in the foreground."
},

"arms": {
  "position": "Left arm extended forward with the hand gripping the steering wheel; right arm tucked close to the side."
},

"head": {
  "turn": "Sharp turn over the left shoulder.",
  "expression": "Sultry and confident."
}
},

"outfit": { "swimwear": { "type": "Two-piece bikini", "color": "Brown and white gingham (checkered) pattern.",

  "top": {
    "style": "Halter-neck triangle top with white ruffled lace trim.",
    "ties": "Thin brown string ties at the neck and back.",
    "coverage": "Minimal to moderate."
  },

  "bottom": {
    "style": "High-cut, cheeky thong-style bottoms with matching white ruffle edges.",
    "cut": "High-leg/Y-cut over the hips.",
    "ties": "Side-tie strings visible on the right hip.",
    "coverage": "Minimal, cheeky coverage."
  }
}
},

"body": { "type": "Curvy, athletic 'slim-thick' build.", "skin": "Even tan with natural skin variations; slight visible stretch marks on the outer hip and glute area.", "back": "
```

---

## Cutout Pop Product Photography Prompt

A prompt designed for generating high-impact, editorial-advert style product photography, featuring the product suspended in front of a die-cut shape with bold complementary colors and dramatic hard s

```text
{argument name="product" default="[PRODUCT]"} suspended in front of a die-cut shape ({argument name="shape" default="circle/triangle"}), bold complementary color pair, hard side light to create a crisp silhouette, shallow DOF, editorial-advert style.
```

---

## Decadent, Surreal Glamour Portrait of Ana de Armas in Luxury Bathroom

A detailed prompt for generating a high-fashion, surreal portrait of Ana de Armas in a luxury bathroom setting at 3:00 AM. It specifies a pose on a marble vanity, a reflective sequin mini-dress, and a

```text
{
  "version": "1.0",
  "aspect_ratio": "3:4",
  "subject": {
    "identity": "Ana de Armas",
    "fidelity": "Exact facial preservation, high-detail skin texture",
    "expression": {
      "eyes": "Heavy-lidded, tired but piercing",
      "mouth": "Slightly parted lips, subtly smudged red lipstick",
      "gaze": "Lazy, confident, post-party fatigue",
      "mood": "Decadent, surreal glamour, beautiful discomfort"
    },
    "pose": {
      "position": "Half-seated on white marble bathroom vanity",
      "body_language": "Elegantly arched back, chest pushed forward, one arm bracing behind with flat palm on marble",
      "legs": "One leg raised with knee bent and foot on vanity edge; one leg hanging with toes grazing the floor",
      "hands": "Free hand resting loosely on the raised knee"
    }
  },
  "wardrobe_accessories": {
    "clothing": "Form-fitting golden metallic mini-dress, iridescent purple accents, sweetheart neckline, reflective sequin texture, hem ridden up to reveal upper thigh",
    "jewelry": [
      "Long dangling gold earrings",
      "Stacked beaded bracelets",
      "Elegant luxury wristwatch"
    ],
    "footwear": "Barefoot"
  },
  "environment": {
    "setting": "Luxury bathroom at 3:00 AM",
    "materials": "White marble countertops, gold-finished fixtures",
    "key_elements": "Large floor-to-ceiling mirror behind subject, multiplying reflections of back and profile",
    "props": "Scattered champagne glass, decadent party debris"
  },
  "lighting_style": {
    "aesthetic": "Guy Bourdin surrealism mixed with Y2K millennium flash",
    "key_light": "Direct on-camera flash (high-intensity, Y2K style)",
    "accent_lights": {
      "camera_left": "Hot pink and magenta wash",
      "camera_right": "Electric cyan and blue rim lighting"
    },
    "effects": "High saturation light play on marble, mirror reflections creating voyeuristic tension, subtle halation on sequin highlights"
  },
  "technical_specs": {
    "camera": "35mm film aesthetic",
    "lens": "35mm wide-angle at f/2.8",
    "angle": "Slightly low angle to emphasize height and dominance",
    "focus": "Sharp focus on eyes and dress texture",
    "film_stock_simulation": {
      "contrast": "High",
      "grain": "Fine film grain",
      "color_grading": "Punchy, saturated, high-fashion editorial"
    }
  }
}
```

---

## Detailed Image Generation Prompt for Athletic Woman in Outdoor Adventure Setting

This is an extremely detailed, structured prompt designed for image generation (via the Degaus app and Nano Banana Pro) to create a photorealistic image of an athletic woman in an outdoor adventure se

```text
{
  "subject": {
    "type": "adult woman",
    "age": "mid-20s",
    "overall_vibe": "outdoor adventure, confident sporty energy, natural candid",
    "face": {
      "angle": "back-facing body with head turned over shoulder (three-quarter side profile)",
      "shape": "soft feminine face with high cheekbones and a defined jawline",
      "eyes": "almond-shaped eyes, calm focused gaze toward the side (not straight at viewer)",
      "brows": "full natural brows with a clean arch (slightly darker than hair)",
      "nose": "straight refined bridge with a soft rounded tip",
      "lips": "natural full lips, muted nude tone, relaxed neutral expression",
      "skin": "real skin texture with visible pores, sun-kissed warmth, natural outdoor realism (no beautify smoothing)"
    },
    "hair": {
      "color": "platinum blonde",
      "style": "long hair gathered into a low ponytail/bun tucked through the cap opening; a few loose strands near the neck/ear",
      "length_rule": "keep hair long even if tied back"
    },
    "headwear": {
      "type": "baseball cap",
      "color": "dark navy/charcoal",
      "logo_rule": "no readable logos/text on the cap (keep it blank/neutral)"
    },
    "body": {
      "build": "athletic, gym-trained silhouette with enhanced curves (toned shoulders, strong legs)",
      "proportions": "larger bust and fuller hips/glutes while staying realistic and proportional (no extreme cartoon curves)",
      "bust_detail": "fuller chest volume visible as a natural rounded silhouette under the life vest (subtle, not exaggerated)",
      "hips_glutes_detail": "noticeably larger, rounder glutes and wider hip line; natural muscle + softness balance",
      "waist": "defined waist with smooth transition into fuller hips (hourglass but realistic)",
      "skin_finish": "natural daylight sheen with realistic highlights and soft shadows; wet lower legs with visible waterline marks"
    },
    "expression": "calm, slightly serious, outdoorsy confidence"
  },
  "wardrobe": {
    "outerwear": {
      "type": "life jacket / flotation vest",
      "color": "dusty pink",
      "details": "black straps and buckles across torso, slightly bulky padded shape, realistic fabric texture",
      "fit": "snugger fit across chest due to fuller bust, straps show mild tension without distortion"
    },
    "swimwear": {
      "bottom": {
        "type": "minimal string bikini bottom (thong/brazilian cut)",
        "color": "white",
        "fabric": "matte swim fabric, clean edges, thin side strings",
        "fit": "high-cut on hips, sits cleanly, subtle stretch tension along the fuller hips/glutes (tasteful, non-explicit)"
      },
      "top": {
        "type": "bikini top mostly hidden under vest",
        "hint": "thin strap ties visible at upper back/neck area"
      }
    },
    "jewelry": [
      "small hoop earrings (subtle, no branding)"
    ]
  },
  "pose_action": {
    "shot_type": "outdoor river por"
}
```

---

## Dior Floating Garden 3D Billboard

A poetic and surreal image generation prompt describing a 3D billboard concept for Dior, featuring a floating couture garden, perfume mist, and butterflies flowing into the street, with an ethereal wo

```text
DIOR  A FLOATING GARDEN POURING INTO THE STREET
A poetic 3D billboard for Dior: a floating couture garden with blooming flowers, perfume mist, and butterflies flowing outside into the real street. The woman is styled in ethereal Dior fashion, adjusting tiny runway models. Her hand holds a real-size perfume bottle dripping luminous petals.
Tagline: “BREATHE BEAUTY.”  Elegantly surreal, dreamlike
```

---

## DIOR High-Fashion Studio Portrait with Bubble Gum

A prompt for generating a high-fashion editorial portrait based on an uploaded photo, featuring the subject with long messy hair, wearing a black oversized blazer and white tube top, blowing a bubble

```text
Using the uploaded photo of me, see the reference photo in a a high-fashion studio same skin in the photo and long messy hair. She wears a black oversized blazer layered over a white tube top. She has a bubble gum that bubbles on his lips. She poses with her head tilted slightly to the side, gazing softly at the camera with a dreamy, calm expression. A loose strand of hair falls across her face, adding elegance. Soft diffused lighting against a plain white background highlights her glossy lips, peach-toned makeup, and minimal yet ethereal editorial style. The lighting is soft and diffused against a plain white background, emphasizing her natural beauty, glossy lips, and peach-toned makeup. The overall aesthetic is elegant, modern, and editorial.Put a one word "{argument name="brand name" default="DIOR"}" at the back. Don't change my face.
```

---

## Ditto-Inspired Outfit Change with Identity Lock

A short prompt for image generation that instructs the AI to use a reference image for identity locking, change the subject's outfit to a coordinated three-piece Ditto (Pokémon)-inspired ensemble, and

```text
reference image + is wearing a coordinated three-piece {argument name="outfit inspiration" default="ditto(pokemon)"}-inspired ensemble. Change the background to one that matches the subject. Pale skin, same expression and makeup as in the reference image
```

---

## Dramatic Portrait on Fire Escape with Angel Wings

A detailed JSON prompt for generating a high-resolution, low-light photograph of an Asian woman sitting on a green metal fire escape at night. The subject is wearing a black suit jacket and a white dr

```text
{
  "prompt": {
    "subject": "亚洲女性，长直黑发，坐在绿色金属消防楼梯上。",
    "attire": {
      "jacket": "黑色定制西装外套",
      "top": "白色上衣，胸前有大型金色太阳刺绣图案",
      "skirt": "白色褶皱长裙",
      "shoes": "棕色系带皮鞋",
      "accessories": "金色太阳吊坠项链"
    },
    "features": {
      "wings": "巨大的白色羽毛天使翅膀，从背部展开"
    },
    "environment": {
      "location": "夜间的绿色金属消防梯",
      "details": "湿润的金属台阶，背景是黑暗的城市街道和灯光",
      "lighting": "戏剧性的低光照明，有背景灯光光晕"
    },
    "style": "真实照片，高分辨率，低光摄影"
  },
  "size": "原始图像比例"
}
```

---

## Dua Lipa Skincare Editorial Collage

A structured prompt for generating a four-image collage of a woman (styled like Dua Lipa) performing a skincare routine in a clean, minimal bathroom, focusing on natural light, product placement, and

```text
{
  "scene": {
    "location": "modern bathroom vanity",
    "environment": "clean white walls, glass shower enclosure, chrome fixtures",
    "lighting": "soft natural indoor lighting with even highlights",
    "time_of_day": "daytime",
    "ambience": "minimal, fresh, skincare-focused"
  },
  "subject": {
    "description": "young woman performing skincare routine at bathroom mirror",
    "hair": "long dark blonde hair, straight, center-parted",
    "makeup": "minimal makeup, natural skin finish",
    "expressions": [
      "focused and calm while applying cream",
      "neutral gaze into mirror",
      "gentle concentration while massaging product",
      "warm smile holding skincare jar"
    ],
    "actions": [
      "holding {argument name="product type" default="skincare jar"}",
      "applying cream to cheek",
      "massaging product into face",
      "presenting product toward mirror"
    ]
  },
  "wardrobe_and_accessories": {
    "outfit": "strapless light-toned top or towel",
    "jewelry": [
      "small hoop earrings",
      "delicate necklace"
    ]
  },
  "props": {
    "skincare_products": [
      "white skincare jar",
      "matching lotion bottle with pump"
    ],
    "mirror": "round tabletop vanity mirror",
    "bathroom_fixtures": [
      "chrome towel ring"
    ]
  },
  "composition": {
    "layout": "four-image collage",
    "framing": [
      "mirror-facing portrait",
      "product application close-up",
      "hands-on skincare routine shot",
      "smiling product-hold pose"
    ],
    "camera_angle": "eye level",
    "focus": "sharp subject and product, clean background",
    "aesthetic": "skincare editorial, clean beauty, lifestyle branding"
  },
  "camera": {
    "lens": "35mm",
    "aperture": "f/2.8",
    "iso": 200,
    "shutter_speed": "1/125",
    "white_balance": "neutral daylight"
  },
  "style_keywords": [
    "clean beauty",
    "skincare routine",
    "minimal bathroom",
    "natural glow",
    "lifestyle editorial"
  ]
}
```

---

## Dual Celebrity Photo Shoot Analysis Prompt

A highly structured, JSON-formatted prompt designed for generating a 4-panel collage featuring two celebrities, Sydney Sweeney and Ana de Armas, each shown in two distinct high-fashion looks. It speci

```text
{
  "event_analysis": {
    "location": "Red Carpet ({argument name="event style" default="Cannes Film Festival style"})",
    "lighting": "Bright, outdoor natural light with professional flash",
    "total_subjects": 2,
    "total_looks": 4
  },
  "subjects": [
    {
      "name": "Sydney Sweeney",
      "looks": [
        {
          "outfit": {
            "style": "Elegant/Classic",
            "garment": "Full-length satin gown",
            "color": "{argument name="sydney gown color" default="Deep Red"}",
            "features": ["High neck", "Long sleeves", "Floor-length train"]
          },
          "beauty": {
            "hair": "Blonde, side-parted, loose waves",
            "makeup": "Soft glam, neutral tones"
          }
        },
        {
          "outfit": {
            "style": "Glamorous/Glittery",
            "garment": "Sequin embellished column dress",
            "color": "Metallic Gold",
            "features": ["Short sleeves", "Boat neck", "Form-fitting"]
          },
          "beauty": {
            "hair": "Sleek high ponytail",
            "makeup": "Bold red lipstick, defined eyeliner"
          }
        }
      ]
    },
    {
      "name": "Ana de Armas",
      "looks": [
        {
          "outfit": {
            "style": "Gothic Romance/Couture",
            "garment": "Intricate lace overlay gown",
            "color": "Black",
            "features": ["Spaghetti straps", "Floral lace patterns", "Sheer details"]
          },
          "beauty": {
            "hair": "Brunette, effortless beach waves",
            "makeup": "Smokey eye, nude lip"
          }
        },
        {
          "outfit": {
            "style": "Sophisticated/Modern",
            "garment": "Tailored blazer dress",
            "color": "Black and White",
            "features": ["Sharp lapels", "Button-down white shirt inside", "Mini length"]
          },
          "beauty": {
            "hair": "Sleek center-parted bun",
            "makeup": "Clean skin look, contoured cheeks"
          }
        }
      ]
    }
  ],
  "image_metadata": {
    "format": "4-panel collage",
    "orientation": "Landscape",
    "resolution_context": "High Definition"
  }
}
```

---

## Dual Valentine's Day Fashion and Product Prompts

Two separate prompts for generating Valentine's Day themed images: one for a high-fashion editorial shoot of a woman in a red satin gown, and another for a luxury perfume advertisement featuring a cry

```text
Fashion editorial shoot of a woman in an elegant long red satin gown holding a bouquet of deep burgundy roses, minimal ivory studio background, wind effect in hair and fabric, high-fashion lighting, luxury magazine aesthetic.

High-end Valentine’s Day perfume advertisement, crystal perfume bottle placed on a velvet red pedestal, surrounded by scattered rose petals and golden heart charms, soft pink mist swirling around the bottle, glossy reflective surface, dramatic spotlight, luxury editorial photography, rich red and gold palette, 1080x1080.
```

---

## Ecosystem trophic levels infographic

A prompt for generating a detailed infographic about trophic levels and energy transfer in ecosystems, tailored for college students with a labeled ecological pyramid.

```text
Create a detailed infographic for {argument name="audience" default="college students"} on trophic levels and energy transfer in ecosystems. The infographic should feature an ecological pyramid (energy or biomass), with definitions of producers, primary, secondary, and tertiary consumers, and
```

---

## Editorial Background Visual Prompt for Premium Magazine Layouts

A concise image generation prompt designed to create high-quality, expensive-looking editorial background visuals. It emphasizes soft natural light, neutral tones, and ample negative space, making it

```text
Editorial-style background visual.
Soft natural light with subtle directional shadows,
calm neutral tones,
organic depth with foreground blur,
ample negative space for text,
timeless and understated,
like a premium magazine layout backdrop.
```

---

## Editorial Fashion Campaign Prompt

A simple smart prompt designed for generating editorial fashion campaign images using the Nano Banana tool.

```text
Editorial fashion campaign
```

---

## Editorial Fashion Portrait in Indoor Garden

A concise prompt structure for generating an editorial fashion portrait of a confident woman in an indoor garden setting, featuring a tailored outfit integrated with natural, leaf-inspired elements an

```text
{
  "render_goal": "Editorial fashion portrait",
  "subject": {
    "pose": "female standing confidently",
    "expression": "gentle confident smile"
  },
  "wardrobe": "{argument name="wardrobe style" default="tailored outfit integrated with leaf or branch-inspired elements"}",
  "environment": {
    "location": "indoor garden",
    "props": "natural light, soft greenery shadows"
  }
}
```

---

## Editorial Fashion Portrait Series Grid

Generates a multi-frame editorial fashion portrait series grid template.

```text
Editorial fashion portrait series (multi-frame grid style, high virality). Preserve original face structure and proportions exactly from reference. Direct flash or golden hour, high contrast, vintage/cinematic aesthetic, saturated colors, hyper-realistic textures, 8K. {argument name="hair description" default="long dark hair"}, {argument name="skin tone" default="fair skin"}. 16:9 or 1:1 grid layout.
```

---

## Editorial Lifestyle Portrait: Monaco Grand Prix Rooftop

A detailed prompt for generating an editorial lifestyle portrait of a young woman on a private rooftop overlooking the Monaco Grand Prix circuit, focusing on neutral earth tones, soft daylight, and sp

```text
{
  "subject": {
    "person": "Young woman, early 20s, Caucasian",
    "hair": "Soft blonde hair, loose waves with natural shine",
    "pose": "Standing casually with shoulders open, gaze off-camera",
    "expression": "Peaceful, confident, subtle smile"
  },
  "outfit": {
    "top": "Beige off-shoulder knit top",
    "bottoms": "High-rise tailored taupe trousers",
    "accessories": "Small leather bag, minimalist jewelry, nude nails"
  },
  "action": {
    "hands": "One hand resting on railing; other by side"
  },
  "location": {
    "setting": "Private rooftop overlooking Monaco Grand Prix circuit",
    "background": "Street circuit, hillside apartments, cloudy afternoon"
  },
  "typography": {
    "text": "{argument name="brand name" default="Heineken 0.0"} visible on safety walls"
  },
  "lighting": {
    "type": "Natural daylight",
    "quality": "Soft, cloud-diffused"
  },
  "composition": {
    "style": "Editorial lifestyle portrait, medium framing, deep depth, 4:5",
    "color_palette": "Neutral earth tones"
  }
}
```

---

## Editorial Mirror Selfie with Detailed Identity Lock

A highly detailed image generation prompt for an editorial-style mirror selfie of a young athletic woman. It includes an extensive 'identity lock' section specifying facial features, body type, hair,

```text
"ar": "9:16",
  "intent": "rooftop golden hour, city skyline background, editorial feel",
  "subject": {
    "type": "young woman",
    "age": "mid-20s",
    "identity_lock": "young athletic woman in her mid-20s with long platinum-blonde hair, fair skin with a light tan, soft feminine facial features (defined jawline, high cheekbones, natural lips), fit gym-trained body (toned shoulders, visible abs, strong legs and glutes)",
    "face_lock": {
      "face_shape": "oval face with soft features",
      "eyes": "almond-shaped light hazel/green eyes, sharp catchlights, slightly lifted outer corners, natural lashes",
      "brows": "full natural brows with a clean arch",
      "nose": "small button nose",
      "lips": "slightly pouty lips",
      "skin": "real skin texture with visible pores and faint freckles (no smoothing)"
    },
    "hair": {
      "style": "medium-length curls",
      "finish": "perfectly styled with no flyaways"
    },
    "makeup": "minimal: tinted moisturizer, mascara, tinted lip balm",
    "expression": "playful side-glance + soft smirk, relaxed jaw"
  },
  "outfit": {
    "top": {
      "type": "fitted tank top",
      "cut": "off-shoulder",
      "structure": "cropped at waist",
      "fabric": "soft cotton jersey"
    },
    "bottom": {
      "type": "tailored trousers",
      "fit": "A-line silhouette"
    }
  },
  "accessories": {
    "earrings": "statement chandelier earrings",
    "bracelets": "none",
    "rings": "none",
    "other": "dainty pendant necklace"
  },
  "action_pose": {
    "type": "mirror selfie",
    "body_position": "walking mid-stride",
    "upper_body": "arms crossed casually",
    "phone_hand": "phone extended at arm's length",
    "glass_action": "mid-sip with the rim touching lips, white wine visible inside",
    "framing": "full body from head to feet visible; subject centered"
  },
  "scene": {
    "location": "modern bedroom (hotel-like)",
    "table": [
      "bread basket",
      "water glass",
      "silverware set on the right edge of frame"
    ],
    "background": [
      "rows of tables with white tablecloths",
      "glass/window wall on the right with reflections",
      "ceiling with angled panels/awnings",
      "palm trees visible outside through the large windows"
    ],
    "bed": {
      "bedding": "plush velvet comforter",
      "throw_blanket": "none"
    },
    "background_details": {
      "vanity_setup": [
        "makeup vanity/desk with lots of items scattered naturally (brush cup, palettes, bottles, perfume silhouettes)",
        "jewelry box with items spilling out"
      ],
      "mirror_lights": "Hollywood-style bulb lights around mirror",
      "ring_light": "ring light behind the vanity with tripod legs visible (off or dim)",
      "extra_room_details": [
        "a water glass or bottle on a side table edge",
        "small scented candle on the vanity (soft glow)",
        "laptop slightly open on the desk edge or chair (screen dim, no "
  }
```

---

## Editorial Portrait on a Private Jet

A detailed prompt for generating an editorial portrait of a subject (based on an uploaded reference photo) sitting on a luxury private jet, wearing professional attire, holding a champagne glass, and

```text
The main subject is the person in the attached photo (hereinafter referred to as THE_SUBJECT). Carefully and accurately replicate THE_SUBJECT’s facial features, hairstyle, skin tone, proportions, and overall appearance exactly as shown in the photo with the exception of the clothing.

An editorial portrait of a THE_SUBJECT wearing navy blue blazer, professional white shirt with collar, black pencil mini skirt, black sheer pantyhose.

THE_SUBJECT is sitting on beige leather luxury seat inside private jet. THE_SUBJECT has a soft smile and holding champagne glass with legs crossed and extended (stockinged feet, relaxed pose); shoes off, black high heels on the floor in front of the seat. In the midground there are a few rows of empty luxury seats. The main cabin door on the jet is open and an attractive female flight attendant is looking out the door as if speaking with someone not in view. In the distant background, the cockpit door is open and the interior is visible; pilots are sitting in their seats in the cockpit; soft interior cabin lighting mixes with light coming in through the windows; depth of field; professional editorial and fashion photography vibe; ultra-detailed 8k editorial photography
```

---

## Editorial Product Photography Prompt for Levitation Effect

A detailed image generation prompt designed for creating editorial-style product photography featuring a levitation effect. It specifies cinematic lighting, soft shadows, motion blur on trailing eleme

```text
[PRODUCT] and supporting props floating in mid-air, soft shadows anchored below, motion blur on trailing elements, suspended-from-the-moment storytelling, cinematic three-point lighting, editorial fashion-magazine framing.
```

---

## Editorial-Style Marketing Banner for Premium Tech

A concise prompt designed to generate a wide-format marketing banner that looks like a high-end magazine editorial rather than a traditional advertisement. It focuses on composition, soft lighting, an

```text
Wide-format marketing banner for a premium tech brand.
Editorial-style composition,
balanced typography space,
soft natural lighting,
calm, confident tone,
designed to feel like a magazine spread, not an ad.
```

---

## Emerald Green Satin Dress Fashion Editorial

Creates an editorial image of a young woman wearing an elegant emerald green satin midi dress with a high slit, standing outside a modern architectural building.

```text
Young woman with long light brown hair styled in a sleek high ponytail, a few soft strands gently framing her face, wearing an elegant emerald green midi dress crafted from luxurious satin or silk that catches the light with a subtle luminous sheen. The dress features a deep V-neck wrap front that enhances the silhouette, short softly puffed sleeves adding a romantic touch, and a perfectly cinched waist defined by a matching tie belt that creates a flattering hourglass shape. The skirt falls gracefully below the knees in a flowy, gathered design, moving naturally with every step, with an asymmetrical high slit on one side that reveals a glimpse of her leg and adds a refined yet bold edge.
She stands gracefully outside a sleek modern building with clean architectural lines and glass panels reflecting the daylight, giving a sophisticated fashion event atmosphere. She wears delicate gold strappy heeled sandals that complement the rich emerald tone of the dress, along with minimal elegant jewelry for a polished finish. Her makeup is natural and glowing—soft foundation, subtle contour, lightly flushed cheeks, neutral eyeshadow, defined lashes, and a muted rose lip color. Her expression is soft yet confident, poised and effortlessly stylish.
Photorealistic, ultra-detailed, sharp focus, realistic skin texture, natural daylight illumination, cinematic depth, editorial fashion photography style, 85mm lens look, shallow depth of field, luxury event vibe, high resolution, crisp fabric texture, subtle fabric folds, natural body proportions, balanced composition.
```

---

## Energy Drink Can with Green Apple Splash and Neon Lightning

A concise prompt for generating a bold, edgy product shot of a slim energy drink can. It features a fizzy green apple splash, neon green lightning strikes in the background, and floating white apple s

```text
A slim green energy drink can ( BRAND NAME)in apple green and matte black, hovering diagonally 45°, bursting with fizzy green apple splash. Neon green lightning strikes the background, and white apple slices float around. Intense sour energy, bold and edgy --ar 3:4
```

---

## Ethereal Fashion Editorial Close-Up Portrait Prompt

A prompt for generating a fashion editorial close-up portrait of an ethereal young woman, focusing on delicate features, light-freckled porcelain skin, and piercing expressive eyes.

```text
Fashion editorial close-up portrait of an ethereal young woman, delicate light-freckled porcelain complexion with natural rosy undertones, piercing expressive eyes with subtle shimmer catching the light, soft full lips gently pursed as she send
```

---

## Ethereal Product Visual with Frosted Glass Hands

Creates a photorealistic product visual with abstract frosted glass hands behind it.

```text
Photorealistic_product_visual. User uploaded image as reference. Preserve product identity, label text, object shape, centered composition. High-key studio, pure white seamless background. Single product object, perfectly centered, floating, ultra-sharp. Two hands positioned behind a frosted glass surface, frosted glass diffusion, milky blur, softened edges. Semi-opaque, intentionally out of focus, slow delicate abstract reach. Soft diffused studio lighting, frontal with gentle top wash. 85mm f/2.0, eye-level camera.
```

---

## Expert Prompt Engineer System Prompt for Nano Banana Pro

A system prompt instructing an AI model (Nano Banana Pro) to act as an expert prompt engineer. The task is to convert a user's video description into a sophisticated, extremely detailed JSON prompt su

```text
You are an expert prompt engineer for Nano Banana Pro and all AI Video models

Your task is to convert the user's description into a sophisticated, EXTREMELY DETAILED JSON prompt to match the video supplied

You must output a single valid JSON object.

### JSON STRUCTURE GUIDELINES:

1. **Dynamic Fields**: You are encouraged to ADD new fields that capture specific details about the subject (e.g., "plating_style" for food, "architecture_era" for buildings, "glitch_patterns" for abstract art).

2. **Remove Irrelevant Fields**: Do NOT include fields that don't apply. If the subject is a stove, do not include "hair", "skin", or "pose". Remove them entirely rather than setting them to "N/A".

3. **Subject Specificity**:

- **For People**: The example structure (subject, face, skin, hair, clothing) is excellent. Keep it.

- **For Non-Humans**: Create a structure that fits the object. For example, a car might have "chassis", "paint_finish", "wheels".

4. **Standard Fields**: Always include "constraints" (with "must_keep" and "avoid" lists) and
```

---

## Exploded View Taco Infographic for Commercial Use

A detailed prompt for generating a clean, commercial-style infographic showing an exploded view of a taco. It specifies the exact ingredients, weights, vertical alignment, and annotation design guidel

```text
Exploded view of the same taco, presented as a clean, commercial recipe-style breakdown.
Exactly five ingredients, matching the first image, separated and arranged vertically from top to bottom, evenly spaced and perfectly aligned.

Ingredient order (top → bottom):

Fresh tomato salsa — 40 g

Shredded cheddar cheese — 30 g

Grilled chicken pieces — 80 g

Crisp lettuce — 25 g

Soft wheat taco tortilla — 60 g (bottom base)

Add clear infographic-style annotations for each ingredient.
Each annotation includes the ingredient name and its exact weight in grams, written exactly as listed above.

Annotation design guidelines:
– Clean sans-serif font, medium weight
– Text placed inside minimal frames or boxes
– Thin, precise connector lines pointing directly to each ingredient
– High readability, no overlap, no decorative excess
– Structured vertical layout, like a modern recipe card

Background is light, neutral, and optimized for text clarity and visual cleanliness.
Overall style is minimal, instructional, and commercial, suitable for marketing, explainer visuals, and product breakdowns.
```

---

## Fantasy Dragon and Warrior Image Prompt

A simple, descriptive prompt used to generate an image featuring a large yellow feathered dragon and a woman in high-fashion yellow armor on a foggy forest floor, demonstrating the initial image creat

```text
"green forest floor, ferns, dew, foggy, day, a large yellow feathered dragon, a woman in high fashion yellow armor"
```

---

## Fashion Catalog Item Extraction from Reference Image

A detailed system prompt for a professional fashion catalog creator AI. It instructs the model to analyze the clothing worn by a man in a reference image and strictly extract the items into four categ

```text
You are a professional fashion catalog creator.
Analyze the clothing worn by the man in the reference image.
Based strictly on the actual designs of the clothes he is wearing, extract and separate them into the following four categories:

① Outerwear / jacket / coat
② Shirt / innerwear / dress shirt
③ Pants / slacks / denim
④ Shoes / sneakers / leather shoes

Each extracted item must accurately reflect the original clothing’s color, material texture, shape, and details.
Do NOT redesign, modify, stylize, or reinterpret the clothing in any way.
Do NOT show the human body. Extract and display the clothing items only.
The output image must be:
・white background
・front-facing view
・no shadows, no noise
・high-quality product photography, apparel e-commerce style
Arrange the four items neatly in either a horizontal row or a 2×2 grid.
Add Japanese labels to each item exactly as follows:

① アウター・ジャケット・コートなど
② シャツ・インナー・ワイシャツなど
③ ズボン・スラックス・デニムなど
④ 靴・スニーカー・革靴など

Create a clean, easy-to-read catalog-style image.
ultra high resolution, photorealistic, studio product lighting, flat lighting, extremely detailed fabric texture, apparel catalog quality

Negative prompt:
anime, illustration, cartoon, stylized, redesigned clothing, fashion sketch, mannequin, human body, model wearing clothes, background, shadow, reflection, blur, low quality, noisy image, dramatic lighting
```

---

## Fashion Editorial Portrait in Venice

A detailed prompt for generating a sophisticated, high-fashion portrait of a woman (specified as Megan Fox) on a stone balcony overlooking historic Venice during golden hour. The prompt emphasizes the

```text
{
  "image_description": {
    "scene": {
      "location": {
        "city": "{argument name="city" default="Venice"}",
        "setting": "Stone balcony overlooking historic venetian architecture",
        "details": "The scene is set on a classic stone balcony, featuring an expansive view of Venice ancient buildings, monuments, and the city skyline near San Marco square. The warm golden light of natural daylight casts soft shadows on the stone, highlighting intricate architectural elements of the city."
      },
      "environment": {
        "elements": [
          "Stone balcony with ornate railings",
          "Ancient venetian buildings in the background",
          "Clear sky with gentle light reflecting off glass windows",
          "Warm, soft glow from the golden hour sunlight"
        ],
        "atmosphere": "Serene, sophisticated, with a sense of timeless luxury and romance, evoking the beauty of luxury travel and refined femininity."
      },
      "lighting": {
        "type": "Natural daylight",
        "effect": "The lighting is soft and crisp, highlighting architectural textures and the subject with a gentle glow. Shadows are softened, creating an inviting and elevated atmosphere."
      }
    },
    "subject": {
      "identity": "{argument name="subject identity" default="Megan Fox"}",
      "pose": {
        "description": "The subject stands confidently near the stone railing, gazing outward towards the venetian skyline. She maintains a poised and elegant posture, embodying grace and sophistication, with a slight smile suggesting confidence and thoughtfulness."
      },
      "outfit": {
        "top": {
          "type": "Structured corset-style top",
          "color": "Dark pink",
          "style": "Fashion editorial, modern yet classic, designed to accentuate the figure. The corset features sharp, defined lines and a clean, structured fit that contrasts beautifully with the natural environment."
        },
        "bottom": {
          "type": "High-waisted short pink skirt",
          "details": "The skirt is high-waisted, with a dramatic thigh-high slit on both sides, giving it an edgy yet refined feel. The fabric flows gracefully, emphasizing the subject's femininity and modern elegance."
        }
      },
      "hair_and_makeup": {
        "hair": {
          "style": "Soft waves",
          "details": "Her hair is styled in natural, soft waves that cascade effortlessly, adding a sense of movement and vitality to the look. The waves are glossy, offering a polished yet relaxed style."
        },
        "makeup": {
          "style": "Refined and natural",
          "details": "The makeup enhances her natural beauty with subtle contouring and a soft highlight. Her eyes are defined with light eyeliner, and her lips sport a neutral shade, contributing to a sophisticated and timeless look."
        }
      }
    },
    "composition": {
      "aspect_ratio": "3:4",
      "ori"
```

---

## Fashion Editorial Portrait with Narrative JSON Prompt

A structured JSON prompt for generating a fashion editorial portrait with a narrative element, depicting a young woman entering an apartment hallway, holding keys in her teeth, and wearing a trench co

```text
{
  "prompt_type": "descriptive_portrait",
  "subject_details": {
    "demographics": "Young female, light skin, tall.",
    "facial_features": {
      "expression": "Holding a set of keys between her teeth, smiling with eyes, looking relieved and mischievous.",
      "eyes": "Grey-blue eyes.",
      "hair": "Straight light brown/dark blonde hair, silky and shiny."
    },
    "apparel": {
      "dress": "A long beige trench coat aimed to be taken off, open wide to reveal a black lace bodysuit/lingerie underneath.",
      "accessories": "A shoulder bag slipping off her arm.",
      "footwear": "One high heel shoe on, the other kicked off on the floor."
    }
  },
  "pose_and_action": {
    "body_position": "Standing in the hallway, leaning back against the closed door.",
    "hands": "One hand struggling with the coat, the other holding the phone high.",
    "camera_angle": "Full body reflection in a tall hallway mirror."
  },
  "background_environment": {
    "location": "Apartment hallway / entryway.",
    "lighting_source": "Warm overhead hallway light.",
    "objects": {
      "entry": "A coat rack, a mail table with letters, the door behind her."
    }
  },
  "technical_specs": {
    "style": "Fashion editorial meets candid life, sharp details, glamorous.",
    "aspect_ratio": "4:5"
  }
}
```

---

## Fashion Editorial Prompt in Lemon Green Studio

A prompt for generating a fashion editorial image of a young man. The image should use an uploaded picture for face reference and feature the subject wearing an oversized white sweatshirt and lemon gr

```text
A young man with a slight smile see the uploaded picture as reference for the face wearing outfit: oversized white sweatshirt, {argument name="pant color" default="lemon green"} oversized combat jean, styled with footwear: lemon green neutral Nike sneakers and white ribbed socks. Environment: futuristic lemon green-tone studio background. Lighting: soft cinematic glow highlighting skin and fabric textures. Style: fashion editorial x futuristic. Model seats on lemon green bench elegantly with a relaxed posture.
```

---

## Flash-Lit Nighttime Portrait of a Woman in a Lace Mini Dress

A highly specific, structured prompt for generating a photorealistic image of a woman seated on a sofa in a high-rise apartment at night. The prompt details her appearance, clothing (chocolate-brown l

```text
{
  "subject_profile": {
    "identity": "Adult woman in her late 20s",
    "appearance": {
      "skin_tone": "Warm, sun-kissed tan with natural tonal variation",
      "hair": "Shoulder-length blonde balayage hair styled in loose, imperfect waves, softly framing the face",
      "face": "Direct eye contact, relaxed mouth, subtle confident expression",
      "skin_texture": "Natural skin with visible pores and slight flash-induced sheen, no smoothing"
    },
    "body_characteristics": {
      "overall_build": "Slim yet curvaceous physique",
      "upper_body": "Full, forward-projecting bust with visible natural weight and volume, creating pronounced cleavage",
      "anatomical_behavior": "Chest mass responds naturally to gravity and posture, no artificial lift or compression"
    }
  },
  "wardrobe_and_styling": {
    "dress": "{argument name="dress color" default="Chocolate-brown"} lace mini dress with a structured corset-inspired bodice, visible boning, and molded cups",
    "design_details": [
      "Floral lace texture",
      "Sweetheart neckline",
      "Off-the-shoulder cap sleeves"
    ],
    "fit_behavior": "Fabric conforms tightly to the torso while allowing natural softness and depth",
    "accessories": [
      "Small gold hoop earrings",
      "White quilted leather handbag with chain strap resting beside the subject on the sofa"
    ]
  },
  "pose_and_body_language": {
    "position": "Seated in a semi-reclined posture on a sofa",
    "support": "Right arm extended downward, palm pressing into the cushion for balance",
    "left_arm": "Bent comfortably with the hand resting over the midsection",
    "legs": "Together and angled toward the lower corner of the frame",
    "spine_and_shou
```

---

## Four-Panel Streetwear Advertisement Grid

A prompt for generating a four-panel grid advertisement for a premium streetwear brand, featuring a model in monochrome sportswear in a concrete studio, with each panel showing a different pose and fr

```text
Four-panel grid advertisement for a premium streetwear brand. The {argument name="model description" default="model"} wears a monochrome technical sportswear set in a minimalist concrete studio.

Top Left: Relaxed standing pose.
Top Right: Close-up portrait with confident expression.
Bottom Left: Mid-stride walking pose.
Bottom Right: Low-angle seated pose highlighting footwear.
High-contrast lighting, crisp shadows, clean negative space for branding, modern commercial styling.
```

---

## Free Christmas Promotional Prompt

This tweet offers a free 'Christmas Prompt' for Nano Banana Pro to create fun holiday advertisements featuring products. The prompt itself is linked externally and not provided in the text.

```text
El Prompt Navideño, crea divertidos anuncios con Nano Banano y tus productos en 1 minuto o menos solo copia el prompt y listo.
```

---

## General Luxury Product Hero Shot Prompt

A simple, general instruction to create a luxury product hero shot, implying the user should provide the product details.

```text
Create a luxury product hero shot using this prompt 👇
```

---

## Gilded Delftware Product Signature Prompt

A short, descriptive prompt aiming to generate a signature product image in the style of Gilded Delftware, likely for a brand presentation.

```text
Signature brand product to Gilded Delftware
```

---

## Glamorous Nighttime Balcony Portrait with Fireworks

An image generation prompt for a glamorous, celebratory portrait of a woman in a deep red sequined halter-neck dress, leaning against a stone balustrade at night. The scene includes a newspaper and ch

```text
{
  "subject": {
    "person": "Woman",
    "appearance": {
      "hair": "Blonde, sleek ponytail",
      "makeup": "Glamorous, defined brows, nude lips",
      "skin": "Tanned",
      "expression": "Looking at camera with a slight smile"
    },
    "pose": "Leaning against a stone balustrade, holding a newspaper and a champagne glass"
  },
  "attire": {
    "dress": {
      "color": "Deep red",
      "style": "Halter-neck, sequined, form-fitting",
      "length": "Full length"
    },
    "accessories": {
      "stole": "Black, faux fur, draped over arms",
      "jewelry": "Gold hoop earrings"
    }
  },
  "objects": {
    "newspaper": {
      "title": "2026",
      "headline": "Stockholm International..." (partially visible),
      "content": "Text and images",
      "held_in": "Both hands"
    },
    "drink": {
      "type": "Champagne glass",
      "contents": "Liquid champagne",
      "held_in": "Right hand"
    }
  },
  "setting": {
    "location": "Stone balcony or terrace",
    "time": "Night",
    "background": {
      "cityscape": "European architecture, illuminated buildings",
      "sky": "Dark, with fireworks exploding",
      "fireworks": "Red and gold bursts"
    }
  },
  "atmosphere": "Glamorous, celebratory, luxurious"
}
```

---

## Gorpcore Fashion Campaign Image

Creates a high-end streetwear fashion campaign image with a male model next to a Mercedes G Wagon.

```text
Low Angle Shot Blur, Fashion Campaign Image For A High-end Streetwear Brand, Male In Their 20s Sat Next To A Mercedes G Wagon Car. He Is Wearing Gorpcore Styled Clothing, Nike Air Max Trainers. Shot With An Ultra-wide Lens Creating Strong Barrel Distortion And Curved Perspective. Harsh Handheld Flash Casts Raw Shadows And Emphasizes Texture. Background Fades Into Deep Blue Twilight With Scattered Field Lighting. The Entire Scene Feels Candid And Cinematic Grainy Film Texture, Slight Motion Blur, Imperfect Lighting, Warm Analog Tone Shifts. Inspired By Experimental Gorpcore Fashion. Shot On Kodak Portra 800, Handheld, F/2.0
```

---

## Grounded Realism Street Portrait Prompt

A detailed prompt for Nano Banana Pro focused on generating a photorealistic, observational street portrait with grounded realism. It specifies a female subject in lived-in fashion (black leather jack

```text
{
  "scene": "Urban street portrait on a quiet city sidewalk",
  "subject": {
    "gender": "female",
    "age_range": "late 20s to early 30s",
    "expression": "neutral, introspective, calm confidence",
    "pose": "standing casually, leaning slightly against a brick wall, weight shifted to one leg, arms relaxed",
    "gaze": "looking directly at camera, unfazed, understated presence"
  },
  "wardrobe": {
    "outerwear": "black leather jacket with natural wear and soft creases",
    "top": "dark charcoal ribbed tank top",
    "bottom": "high-waisted tailored wool trousers in muted grey",
    "accessories": "small dark leather crossbody bag, minimal jewelry",
    "styling_notes": "effortless, functional, lived-in fashion, no trend exaggeration"
  },
  "hair_and_makeup": {
    "hair": "natural medium-length hair, loose and slightly wind-touched, no styling product shine",
    "makeup": "minimal or none, natural skin texture visible, subtle under-eye shadows, real pores"
  },
  "environment": {
    "location": "narrow city street with brick wall and storefronts",
    "background": "softly out-of-focus bicycles and pedestrians in the distance",
    "era_feel": "timeless contemporary, everyday realism"
  },
  "lighting": {
    "type": "natural overcast daylight",
    "direction": "soft frontal with gentle side falloff",
    "contrast": "low to medium contrast",
    "notes": "no harsh highlights, no dramatic rim light"
  },
  "camera": {
    "lens": "50mm full-frame look",
    "framing": "full-body portrait, eye-level perspective",
    "depth_of_field": "moderately shallow, subject separated subtly from background",
    "movement": "static, documentary stillness"
  },
  "color_and_texture": {
    "color_palette": "muted earth tones, soft greys, natural skin tones",
    "texture": "visible fabric weave, brick texture, light film grain",
    "grading": "neutral, slightly cool, filmic, no teal-orange"
  },
  "aesthetic_constraints": [
    "no plastic skin",
    "no beauty retouching",
    "no cinematic exaggeration",
    "no fashion editorial posing",
    "no artificial glow",
    "avoid AI symmetry"
  ],
  "overall_vibe": "quiet confidence, observational, grounded realism, modern street portrait"
}
```

---

## Gucci x Balenciaga Hacker Project Mirror Selfie

A high-fashion, ultra-detailed prompt for generating an 8K image of a model taking a mirror selfie in a luxury hotel elevator, showcasing a mashup of Gucci and Balenciaga 'Hacker Project' apparel and

```text
{
  "title": "Gucci x Balenciaga The Hacker Project – Logo Mashup",
  "subject": "{argument name=\"model description\" default=\"23-year-old Russian-Italian model, porcelain skin with golden undertone, sleek straight platinum-blonde hair to mid-back, icy blue-green eyes, razor-sharp bone structure, 32-22-34 slim hourglass, 5'11\"\}",
  "pose": "mirror selfie in elevator, one hand in pocket, other holding phone, hip cocked, direct intense stare",
  "outfit": "oversized beige GG monogram trench coat with Balenciaga Hourglass cut and printed Gucci x Balenciaga logo tape on sleeves, worn open over black leather bralette and high-waisted black denim with repeated fake Gucci logo print",
  "accessories": "black Balenciaga Knife boots with silver BB, large Gucci x Balenciaga Hacker Jackie bag in GG supreme",
  "setting": "luxury hotel mirrored elevator, dramatic overhead lighting and reflections",
  "quality": "high-fashion 8K, every printed logo and mirror reflection perfectly sharp"
}
```

---

## Gym Selfie of Sadie Sink and Millie Bobby Brown

A highly detailed, structured JSON prompt for generating a photorealistic image of two subjects (Sadie Sink and Millie Bobby Brown likeness implied) taking a mirror selfie in a modern gym. The prompt

```text
{
  "scene_description": {
    "location": "Modern indoor gym",
    "background_elements": [
      "Full-wall mirrors reflecting the room depth",
      "Rows of black dumbbells on racks",
      "Cable weight machines in the background",
      "Black padded weight bench on the right",
      "Black rubber gym flooring",
      "Linear LED ceiling lights providing bright, cool illumination"
    ],
    "atmosphere": "Energetic, fitness-focused, casual lifestyle"
  },
  "subjects": [
    {
      "id": "subject_1",
      "position": "Left",
      "appearance": {
        "hair": "Reddish-blonde, long, tied back in a ponytail",
        "skin_tone": "Fair",
        "expression": [
          "Beaming smile",
          "Looking at mirror",
          "Looking sideways",
          "Smiling directly at camera"
        ]
      },
      "apparel": {
        "outfit_type": "Matching ribbed workout set",
        "color": "{argument name="subject 1 outfit color" default="Lemon yellow"}",
        "top": "Sports bra with a scoop neck and visible 'alo' logo on the band",
        "bottom": "High-waisted biker shorts (mid-thigh length)",
        "footwear": "White crew socks, white sneakers"
      },
      "poses": [
        "Standing with hands on hips",
        "Standing slightly turned inward",
        "Wide stance squat with hands resting on thighs"
      ]
    },
    {
      "id": "subject_2",
      "position": "Right",
      "appearance": {
        "hair": "Brunette, styled in a messy high bun",
        "skin_tone": "Light-to-medium",
        "expression": [
          "Soft smile",
          "Focused neutral expression",
          "Looking at phone screen in mirror"
        ]
      },
      "apparel": {
        "outfit_type": "Matching ribbed workout set",
        "color": "{argument name="subject 2 outfit color" default="Bright red"}",
        "top": "Deep V-neck sports bra",
        "bottom": "High-waisted mini shorts",
        "footwear": "White crew socks, white sneakers"
      },
      "accessories": [
        "Smartphone with dark case and MagSafe ring",
        "Black dumbbell with silver handle"
      ],
      "poses": [
        "Standing holding phone for mirror selfie",
        "Goblet squat holding a dumbbell at chest height with both hands"
      ]
    }
  ],
  "camera_perspective": {
    "type": "Mirror selfie and low-angle timer shot",
    "framing": "Full body and 3/4 body shots",
    "lighting": "Overhead artificial gym strip lighting",
    "focus": "Sharp focus on subjects, slight depth of field in background reflection"
  },
  "specific_details": {
    "color_contrast": "High contrast between the yellow and red outfits against the grey/black gym background",
    "distinctive_features": "Fitness equipment reflections, 'alo' branding on yellow top"
  }
}
```

---

## Heartwarming Festive Christmas Portrait

A structured prompt for generating a heartwarming festive portrait of a woman placing a star atop a Christmas tree in a cozy living room setting, complete with a fireplace, decorations, and gift boxes

```text
{
  "render_goal": "Heartwarming festive portrait",
  "subject": {
    "pose": "female placing a star atop a Christmas tree",
    "expression": "content and joyful"
  },
  "wardrobe": "soft knit dress, subtle jewelry",
  "environment": {
    "location": "cozy living room with fireplace",
    "props": "decorations, gift boxes, {argument name="prop detail" default="Santa figurine nearby"}"
  }
}
```

---

## High-Contrast Beach Portrait in Neon Bikini

A prompt for generating a high-contrast, low-angle close-up shot of a young woman lying on a beach towel, looking over her shoulder at the camera. The scene is set on a crowded public beach under brig

```text
{
  "subject": {
    "description": "A young woman lying prone on a beach towel, looking directly at the camera over her shoulder.",
    "pose": "Lying on her stomach with her upper body propped up by her elbows, one hand resting against her cheek, and her back arched to highlight her silhouette.",
    "build": "Toned and athletic physique."
  },
  "clothing": {
    "swimwear": "A tie-dye string bikini featuring a vibrant pattern of neon yellow, lime green, and royal blue.",
    "accessories": "Gold hoop earrings, a two-tone (silver and gold) luxury watch on her right wrist, a thin gold bracelet, and long red manicured nails."
  },
  "hair": {
    "style": "Slicked back away from the face in a 'wet look' style, likely gathered in a ponytail or bun behind her head.",
    "color": "Dirty blonde or light brown."
  },
  "face": {
    "expression": "Sultry and composed with a direct gaze.",
    "makeup": "Defined cat-eye winged eyeliner, groomed eyebrows, and neutral-toned matte lipstick.",
    "features": "High cheekbones and sun-kissed skin."
  },
  "environment": {
    "setting": "A crowded public beach during a bright, sunny day.",
    "background": "White sand beach with numerous tan umbrellas, blue and white lounge chairs, and other beachgoers in the distance. A large white building is visible on the far right horizon.",
    "sky": "Clear blue sky with scattered, fluffy white clouds.",
    "foreground": "A plush white beach towel on the sand."
  },
  "style": {
    "lighting": "Bright, direct natural sunlight creating high contrast and sharp details.",
    "color_palette": "Primary tones of blue and white from the sky and sand, contrasted with the neon green and yellow of the bikini.",
    "composition": "Low-angle close-up shot with a shallow depth of field, keeping the subject in sharp focus while the background is softly blurred."
  }
}
```

---

## High-Detail Y2K Aesthetic Bikini Portrait with Peace Sign

A highly specific image generation prompt detailing a young woman in a Y2K aesthetic. It specifies the subject's physique (slim, hourglass), hair (bleached blonde with dark roots, textured waves), mak

```text
{
  "prompt_description": {
    "subject": {
      "demographics": "Young woman, approximately early 20s",
      "body_type": "Slim, toned physique with a visible hourglass waist",
      "skin_tone": "Light/Fair complexion with warm, golden undertones and slight tan lines",
      "pose": {
        "stance": "Standing upright, hips slightly cocked to the right",
        "hands": {
          "right_hand": "Raised to eye level, forming a peace sign (V-sign) with palm facing forward, fingers wearing fingerless gloves",
          "left_hand": "Resting naturally on the upper left thigh/hip"
        }
      }
    },
    "face_and_head": {
      "hair": {
        "color": "Bleached light golden blonde with distinct, dark brown visible roots (grown-out effect)",
        "style": "Long, tousled, and textured loose waves falling over both shoulders",
        "texture": "Piece-y separation in the strands (salt-spray or 'lived-in' texture), slightly dry appearance at the ends rather than silky, with backlit flyaways visible against the dark background",
        "parting": "Imperfect center part"
      },
      "facial_features": {
        "face_shape": "Oval with defined cheekbones and a slightly pointed chin",
        "eyes": "Almond-shaped, light blue/green irises, emphasized with thick black winged eyeliner and heavy upper lashes",
        "brows": "Arched, light brown, defined but not overly thick",
        "nose": "Straight bridge with a refined tip; small silver stud piercing on the right nostril",
        "cheeks": "Softly contoured with a warm, peachy-bronze blush",
        "mouth": "Wide open in a playful expression",
        "tongue": "Sticking straight out and downwards, reaching past the bottom lip",
        "lips": "Natural fullness, glossy pink-nude color"
      }
    },
    "apparel_and_accessories": {
      "bikini": {
        "top": "{argument name="bikini color" default="Red"} satin-effect triangle bikini top with clear, transparent plastic shoulder straps and a clear under-bust connector",
        "bottom": "Matching red satin high-cut bikini bottoms with thin clear plastic side straps",
        "fit": "Snug fit, creating slight natural skin indentation"
      },
      "gloves": " fingerless knit gloves (arm warmers) extending to the wrist; white base with horizontal red and blue stripes",
      "socks": "Thigh-high knit socks (matching the gloves); white base with red and blue horizontal stripes at the top cuff",
      "jewelry": {
        "choker": "Thick black fabric choker with rhinestone capital letters (appearing to read '{argument name="choker text" default="BREEDME"}' or similar text)",
        "necklace": "Delicate gold chain with a tiny pendant",
        "navel_piercing": "Silver belly button ring with a red gemstone"
      }
    },
    "environment_and_background": {
      "setting": "Outdoor balcony or patio area",
      "background_objects": {
        "left": "White frame sliding glass door reflecting the outdoor daylight",
        "right": "Solid, dark grey/black stucco wall "
      }
    }
  }
}
```

---

## High-End Fashion Magazine Cover Prompt

This is a prompt designed to generate an ultra-realistic, high-end fashion magazine cover featuring a male model. It specifies the setting, attire, lighting, and aesthetic for a refined, premium edito

```text
Create a high end fashion magazine cover featuring a male model sitting on a wooden block, dressed exactly as shown in the reference image. Maintain clean, refined editorial styling. Use a warm brown studio background, soft diffused studio lighting, luxury color grading, and a minimalist premium aesthetic, image size 4 5.
```

---

## High-End Skincare Advertising Prompt

A prompt designed for Nano Banana Pro to create high-end advertising visuals for skincare products.

```text
Create high-end skincare advertising using this prompt
```

---

## High-Fashion Boho Editorial Prompt

A detailed prompt for generating a high-fashion editorial photograph of a young man in a stylish white boho outfit and clean sneakers, set in a garden with artistic framing, aiming for a Vogue-inspire

```text
A high-fashion editorial shot of a young man posing confidently in a stylish {argument name="outfit color" default="white"} boho outfit paired with clean white sneakers. Slightly tousled chic hair, full body pose captured in a garden with artistic framing. High resolution beauty, refined lighting, soft muted palette, glossy magazine aesthetic, elegant posture, and detailed textures. {argument name="magazine style" default="Vogue"} inspired outdoor editorial.
```

---

## High-Fashion Candid Portrait of Zhao Lusi

Creates a full-length, high-fashion, candid-style professional photograph of Zhao Lusi in a white lace gown.

```text
{
  "subject": {
    "name": "Zhao Lusi",
    "also_known_as": "Rosy Zhao",
    "profession": "Chinese actress",
    "recognition": [
      "Hidden Love",
      "The Long Ballad",
      "Love Like the Galaxy"
    ]
  },
  "scene_type": "High-fashion event appearance",
  "composition": {
    "shot_type": "Candid-style professional photograph",
    "orientation": "vertical",
    "width": 504,
    "height": 1002,
    "framing": "Full-length portrait",
    "focus": "Subject sharply in focus with blurred background"
  },
  "attire": {
    "dress": {
      "style": "Strapless gown",
      "color": "White",
      "details": [
        "Intricate lace bodice",
        "Voluminous textured skirt",
        "Ruffled or floral-patterned fabric"
      ],
      "aesthetic": "Bridal-inspired, classic, elegant"
    },
    "jewelry": {
      "necklace": "Diamond statement necklace",
      "earrings": "Matching diamond drop earrings",
      "style": "Luxury, high-end"
    }
  },
  "hair_and_makeup": {
    "hair": {
      "length": "Long",
      "texture": "Straight",
      "color": "Brunette",
      "parting": "Middle part",
      "styling": "Minimal, face-framing"
    },
    "makeup": {
      "style": "Douyin / glass-skin",
      "features": [
        "Luminous dewy skin",
        "Subtle shimmering eyeshadow",
        "Natural pink lips"
      ]
    }
  },
  "skin_finish": {
    "texture": "Smooth and hyper-reflective",
    "effect": [
      "Glass skin",
      "Wet-look glow",
      "Luminous facial contours"
    ],
    "tone": "Warm enhanced skin tone"
  },
  "lighting": {
    "type": "Bright, soft, diffused",
    "effect": "Enhances fabric texture and facial glow"
  },
  "background": {
    "environment": "Urban setting",
    "elements": [
      "People",
      "Vehicles"
    ],
    "depth_of_field": "Strong background blur (bokeh)",
    "mood": "Busy environment contrasting a calm main character presence"
  },
  "overall_mood": [
    "Ethereal",
    "Elegant",
    "Main character energy",
    "Luxury fashion moment"
  ]
}
```

---

## High-Fashion Editorial Portrait

Creates a high-fashion editorial portrait resembling Ana de armas.

```text
Young woman with features resembling Ana de armas. Almond-shaped hazel-green eyes, focused gaze. Light brown hair with honey-blonde highlights, slicked back away from forehead, damp/wet-look texture, flowing straight down the back. Fair smooth skin with soft matte finish. Oval face, soft jawline, straight nose, naturally full lips slightly parted. Bold black winged eyeliner, nude satin-finish lipstick. Sheer black long-sleeved mesh top with fine vertical pleated texture, black spaghetti-strap camisole underneath. Soft diffused studio lighting, high-key setup, solid clean off-white/minimalist grey backdrop. Shot on 85mm lens, f/2.8.
```

---

## High-Fashion Editorial: The Dip

A detailed prompt for generating a high-fashion editorial image of a business professional seated gracefully on the floor next to an elevator, looking exhausted but composed, with financial projection

```text
The subject is wearing a blue-grey sleeveless business dress with black stiletto heels, a red lanyard loosely around her neck with an ID badge attached, and the same accessories as the uploaded person. The subject is seated gracefully on the floor, leaning slightly against a wall next to an elevator. Both legs are bent, wearing nude stockings, creating an elegant yet relaxed posture. Her expression is calm and composed but slightly exhausted, looking up toward the ceiling with a subtle air of exasperation. The minimalist background features a sleek, modern hallway with an elevator, emphasizing clean lines and smooth surfaces. Nearby, a beige handbag, smartphone, glasses, and an open laptop are placed on the floor. The laptop screen displays the UI of a professional investment app with downward projections, contributing to the modern corporate aesthetic. The lighting is soft and natural, illuminating the subject and creating a serene, high-fashion editorial atmosphere.
```

---

## High-Fashion Illusion Lace Corset Gown Editorial

A prompt for generating a high-fashion editorial image of a woman wearing a strapless illusion lace corset gown, focusing on the intricate details of the nude base, black lace embroidery, visible boni

```text
Create a high-fashion editorial look featuring a woman wearing a strapless sheer corset gown, also known as an illusion lace evening gown. The dress has a nude skin-tone base with intricate {argument name="lace color" default="black"} lace embroidery layered over transparent fabric. The corset-style bodice includes visible boning that cinches and shapes the waist, while the strapless neckline highlights the shoulders and collarbone. A dramatic {argument name="train color" default="black"} tulle train or skirt is attached at the back, adding volume, movement, and elegance to the silhouette. The overall aesthetic is luxurious, refined, and couture-focused, emphasizing structure, transparency, and contrast between nude fabric and black detailing.
```

---

## High-Fashion Magic Carpet Editorial Shot

A prompt for generating a high-fashion editorial image featuring a model (man or woman) on a flying magic carpet. It emphasizes luxury brand styling, cinematic warm lighting, elegant billowing fabrics

```text
{
  "options": {
    "gender": ["man", "woman"]
  },
  "prompt": "A high-fashion editorial shot of a {argument name="gender" default="woman"} model sitting or standing on a flying magic carpet during takeoff. The model is wearing a sophisticated, layered outfit featuring the structured silhouettes and premium textures typical of luxury brands like Celine, Balenciaga, Ralph Lauren, Givenchy, and Zegna. The clothes billow elegantly in the wind. The carpet is ornate and detailed, kicking up a subtle dust cloud as it ascends from a sun-drenched, minimalist architectural terrace. The lighting is cinematic and warm, highlighting the motion and the luxurious fabrics. Low angle perspective focusing entirely on the subject and the scene."
}
```

---

## High-Fashion Motion Capture Image Prompt

A structured prompt for generating a high-fashion, motion-capture style image featuring a female subject in a flowing silk dress walking through an empty luxury hotel hallway.

```text
{
  "render_goal": "High-fashion motion capture",
  "subject": {
    "pose": "female walking forward slowly, fabric trailing behind",
    "expression": "serene, inward-focused smile"
  },
  "wardrobe": "flowing silk dress in soft sage green, lightweight layers",
  "environment": {
    "location": "empty luxury hotel hallway",
    "props": "warm ceiling lights, gentle motion blur"
  }
}
```

---

## High-Fashion Streetwear Editorial Grid Collage

A complex, structured JSON prompt designed for Nano Banana Pro to generate a high-fashion streetwear editorial collage in a 2x2 grid format. It focuses heavily on identity locking (using a reference p

```text
{
  "meta_control": {
    "generation_mode": "multi_panel_consistent",
    "priority_stack": ["identity_lock", "perspective_physics", "material_fidelity", "environmental_coherence"],
    "quality_target": "editorial_print_ready"
  },
  "intent": {
    "primary": "High-fashion streetwear editorial with extreme wide-angle perspective study",
    "secondary": "Technical demonstration of foreshortening and forced perspective",
    "publication_context": "Double-page spread, fashion magazine collage layout"
  },
  "frame": {
    "aspect_ratio": "3:4",
    "layout": {
      "type": "2x2 grid collage",
      "gutter_width": "2px white or seamless",
      "panel_uniformity": "identical dimensions per panel"
      }
  },
  "subject": {
    "type": "Human male model",
    "identity_lock": {
      "enforcement_level": "strict",
      "anchor_features": ["face_geometry", "skin_tone", "body_proportions", "hair_style"]
    },
    "biometrics": {
      "age_presentation": "{argument name="age presentation" default="22-30"}",
      "height_cm": {argument name="height cm" default="178"},
      "build": "Athletic, masculine proportions",
      "ethnicity_presentation": "Your real appearance from reference image"
    },
    "facial_signature": {
      "structure": "As in reference image (identity locked)",
      "eyes": "Match reference image",
      "nose": "Match reference image",
      "lips": "Match reference image",
      "skin": "Match reference — natural texture preserved",
      "expression_default": "Neutral confidence, direct eye contact"
    },
    "hair": {
      "style": "Match reference image",
      "texture": "Match reference",
      "behavior": "Natural movement responding to pose changes"
    },
    "wardrobe": {
      "jacket": {
        "item": "Oversized bomber jacket",
        "material": "Ripstop nylon, high gloss",
        "color": "Neon orange (vivid, saturated)",
        "state": "Unzipped, hanging open",
        "light_behavior": "Sharp specular highlights, visible weave texture"
      },
      "top": {
        "item": "Fitted black crew-neck T-shirt",
        "material": "Thick cotton jersey",
        "fit": "Slightly tight, masculine silhouette",
        "details": "Minimal, no logos, subtle ribbed collar"
      },
      "pants": {
        "item": "Tactical cargo pants",
        "material": "Heavy cotton twill, matte",
        "color": "Charcoal grey",
        "details": "Multiple pockets, silver buckles, black nylon straps, baggy fit"
      },
      "footwear": {
        "item": "Platform sneakers",
        "color": "White, chunky sole",
        "condition": "Clean but worn, realistic sole texture"
      }
    },
    "accessories": {
      "neck": "Layered heavy silver Cuban link chains",
      "hands": "Silver rings on index and middle fingers both hands"
    }
  },
  "panels": [
    {
      "id": 1,
      "position": "top-left",
      "concept": "Extreme low-angle sneaker perspective",
    }
```

---

## High-Fashion Streetwear Editorial with Forced Perspective

A highly technical and structured JSON prompt for generating a multi-panel, high-fashion streetwear editorial image. It focuses on technical execution, including multi-panel consistency, identity lock

```text
{
  "meta_control": {
    "generation_mode": "multi_panel_consistent",
    "priority_stack": ["identity_lock", "perspective_physics", "material_fidelity", "environmental_coherence"],
    "quality_target": "editorial_print_ready"
  },
  "intent": {
    "primary": "High-fashion streetwear editorial with extreme wide-angle perspective study",
    "secondary": "Technical demonstration of foreshortening and forced perspective",
    "publication_context": "Double-page spread, fashion magazine collage layout"
  },
  "frame": {
    "aspect_ratio": "3:4",
    "layout": {
      "type": "2x2 grid collage",
      "gutter_width": "2px white or seamless",
      "panel_uniformity": "identical dimensions per panel"
    }
  },
  "subject": {
    "type": "Human female fashion model",
    "identity_lock": {
      "enforcement_level": "strict",
      "anchor_features": ["face_geometry", "skin_tone", "body_proportions", "hair_style"]
    },
    "biometrics": {
      "age_presentation": "22-26",
      "height_cm": 175,
      "build": "Slender athletic, model proportions",
      "ethnicity_presentation": "Northern European features"
    },
    "facial_signature": {
      "structure": "Angular diamond face, high cheekbones, defined jawline",
      "eyes": "Sharp almond, steel grey, graphic black winged liner extending 8mm",
      "nose": "Refined, straight, small silver hoop piercing on left nostril",
      "lips": "Natural shape, matte nude-pink",
      "skin": "Fair, visible pores and natural texture, subtle peach fuzz, tiny freckle cluster left cheekbone",
      "expression_default": "Cool confidence, intense direct eye contact, composed"
    },
    "hair": {
      "style": "Platinum blonde straight bob, blunt bangs ending at eyebrows",
      "texture": "Silky, light-catching, individual strand definition",
      "behavior": "Natural movement responding to pose changes"
    },
    "wardrobe": {
      "jacket": {
        "item": "Oversized bomber jacket",
        "material": "Ripstop nylon, high gloss",
        "color": "Neon orange (vivid, saturated)",
        "state": "Unzipped, hanging open",
        "light_behavior": "Sharp specular highlights, visible weave texture"
      },
      "top": {
        "item": "Crop top",
        "material": "Black synthetic mesh, diamond pattern",
        "fit": "Tight, stretched across torso",
        "transparency": "Semi-sheer, skin visible through weave"
      },
      "pants": {
        "item": "Tactical cargo pants",
        "material": "Heavy cotton twill, matte",
        "color": "Charcoal grey",
        "details": "Multiple pockets, silver buckles, black nylon straps, baggy fit"
      },
      "footwear": {
        "item": "Platform sneakers",
        "color": "W"
      }
    }
  }
}
```

---

## High-Fashion Summer Outfit Infographic with Exploded Composition

A prompt for generating a high-fashion summer outfit infographic using an elegant exploded circular composition. It specifies the clothing items (straw hat, organic cotton top, pleated skirt, leather

```text
High-fashion summer outfit infographic with color-coordinated floating elements arranged in an elegant exploded circular composition, featuring a breathable straw hat, sleeveless organic cotton top, fluid pleated skirt, artisan leather sandals, and a woven palm-leaf bag; refined callouts highlight fabric breathability, crisp texture, moisture-wicking, and seasonal comfort, with warm neutral tones of {argument name="color palette" default="ivory, terracotta, sand, and soft tan"}; subtle motion trails and airy fabric swirls suggest a gentle summer breeze, bright natural sunlight creates soft shadows and a sun-kissed glow, Mediterranean gemini lifestyle mood, premium editorial aesthetic, ultra-sharp details, minimal typography, luxury fashion magazine infographic style, Instagram-ready
```

---

## High-Resolution Beach Lifestyle Editorial

Creates a high-resolution lifestyle and swimwear photograph with an editorial feel on a sandy beach with rocky cliffs.

```text
{
  "type": "image_prompt",
  "description": {
    "subject": "A young woman with long, wavy blonde hair sits on a beach towel, looking calmly toward the camera with a relaxed, confident expression.",
    "clothing": "She wears a light lavender ribbed bikini with thin straps and tie-side bottoms.",
    "pose": "Seated with one leg bent and the other extended, supporting herself with one arm placed behind her.",
    "setting": "A sandy beach backed by low rocky cliffs covered with green coastal plants.",
    "props": [
      "A woven straw beach tote with pink accents",
      "An open book placed on the towel",
      "Pink-toned beauty items including a compact, brush, and pouch"
    ],
    "lighting": "Natural daylight with soft, warm sunlight creating gentle shadows.",
    "mood": "Calm, summery, effortless, lifestyle-focused.",
    "color_palette": [
      "lavender",
      "sand beige",
      "soft pink",
      "green",
      "natural skin tones"
    ],
    "style": "High-resolution lifestyle and swimwear photography with a clean, editorial feel",
    "camera": {
      "framing": "medium full-body shot",
      "angle": "eye-level",
      "focus": "sharp subject focus with softly detailed background"
    },
    "details": "Beach picnic arrangement emphasizing a relaxed, aesthetic summer atmosphere"
  }
}
```

---

## Historical romantic editorial of a couple dancing in 1920s Istanbul

A concise JSON prompt for generating a historical romantic editorial image of a couple dancing in 1920s Istanbul. It focuses on the mood of freedom, early modern fashion, and a scene set in a hall wit

```text
{
  "generation_request":{
    "meta_data":{"tool":"NanoBanana Pro","task_type":"historical_romantic_editorial","version":"L11_DANCE"},
    "references":{"female":"UPLOAD_REF","male":"UPLOAD_REF"},
    "creative_prompt":{
      "scene_summary":"{argument name=\"location\" default=\"1920s Istanbul hall\"}.",
      "foreground_story":"They dance slowly, smiling.",
      "background_story":"Other couples dance, jazz band plays.",
      "wardrobe":"{argument name=\"fashion era\" default=\"Early modern fashion\"}.",
      "mood":"freedom"
    }
  }
}
```

---

## Industrial Packaging Design Sheet Prompt

A prompt for generating an industrial packaging design sheet, although the actual prompt text is not provided in the tweet or visible in the image link.

```text
Create industrial packaging design sheet using Nano Banana 2.
```

---

## iPhone Mirror Selfie with Old Money Corporate Elegance Vibe

A prompt used to compare different AI models, requesting an iPhone mirror selfie taken in a luxury elevator. The image should convey an 'old money, corporate elegance' aesthetic, detailing the subject

```text
iPhone mirror selfie in luxury elevator. Woman's face hidden by phone while shooting. Outfit: {argument name="outfit details" default="white shirt (slightly unbuttoned), black trousers, blazer casually on shoulders"}. Accessories: black designer bag, coffee cup, minimal gold jewelry. Sleek straight hair. Stainless steel elevator, soft lighting, reflective surfaces. Vibe: old money, corporate elegance, effortless chic. Shot on iPhone, natural lighting, sharp focus, Instagram aesthetic. No branding visible.
```

---

## Isometric Kawaii Hero Generator

A prompt template, named 'Isometric Kawaii Hero,' designed to generate an insanely detailed, full-body isometric humanoid figure in the style of a premium collectible. The user is instructed to swap t

```text
Swap “{argument name="主体" default="SUBJECT"}” and get a scroll-stopping full-body isometric humanoid, insanely detailed like a premium collectible figure.

Works for mascots, brands, and characters.
```

---

## Jennie Kim Athleisure Editorial

A structured JSON prompt to generate an ultra-detailed, photorealistic fashion editorial image of Jennie Kim (BLACKPINK) in sporty chic Adidas athleisure wear. The setting is a minimalist industrial g

```text
{
  "subject": {
    "name": "{argument name="celebrity name" default="Jennie Kim"}",
    "profession": "South Korean singer and rapper, BLACKPINK member",
    "gender": "female",
    "pose": {
      "position": "seated on a white geometric block",
      "body_language": "one knee tucked toward chest, other leg slightly extended",
      "hand_placement": {
        "right_hand": "touching hair",
        "left_hand": "resting on block for balance"
      }
    },
    "expression": "soft-glam, confident, calm intensity, direct piercing gaze"
  },
  "face_and_skin": {
    "skin_finish": "dewy, hyper-reflective glass skin",
    "glow": "wet-look luminous highlights",
    "contours": "smooth, softly sculpted facial contours",
    "skin_tone": "warm enhanced complexion",
    "makeup": {
      "base": "natural matte base with glow",
      "eyes": "warm neutral tones",
      "lips": "soft nude tones"
    },
    "hair": {
      "style": "long, dark, straight",
      "detail": "slightly tucked behind ear"
    }
  },
  "wardrobe": {
    "brand": "Adidas Originals",
    "style": "sporty chic, athleisure, high-fashion streetwear",
    "top": {
      "type": "cropped t-shirt",
      "color": "sand beige",
      "detail": "subtle logo patch"
    },
    "bottoms": {
      "type": "athletic shorts",
      "color": "black",
      "details": "three white stripes, Trefoil logo"
    },
    "footwear": {
      "socks": "white high-top socks with Trefoil logo",
      "shoes": {
        "type": "chunky Adidas sneakers",
        "colors": ["light blue", "mint green", "iridescent silver"]
      }
    }
  },
  "environment": {
    "setting": "minimalist industrial urban gym",
    "background": {
      "walls": "cool-toned blue and grey",
      "floor": "dark tiled floor"
    }
  },
  "lighting": {
    "type": "bright clean studio lighting",
    "effect": "highlight facial contours and fabric texture",
    "accent": "soft futuristic glow from white block"
  },
  "composition": {
    "framing": "centered subject",
    "orientation": "vertical",
    "width": 504,
    "height": 1002
  },
  "color_palette": {
    "primary": ["beige", "black", "white"],
    "contrast": ["cool blue", "grey"]
  },
  "aesthetic": {
    "theme": "high-fashion athletic editorial",
    "trend": "athleisure as luxury streetwear",
    "vibe": "cool, confident, modern, premium"
  },
  "quality_tags": [
    "ultra-detailed",
    "photorealistic",
    "editorial fashion photography",
    "4k",
    "sharp focus",
    "clean textures"
  ]
}
```

---

## Liquid Gloss Logo Generation

A prompt template for generating a logo formed from thick, flowing liquid gloss, emphasizing high-shine, viscous texture, and a luxury cosmetic-brand aesthetic against a minimal background.

```text
Create a {argument name="brand name" default="Brand Name"} logo formed from thick, flowing liquid gloss. High-shine surface, smooth curves, reflective highlights. Viscous, slightly dripping appearance frozen in motion. Minimal background, luxury cosmetic-brand aesthetic, studio lighting.
```

---

## LLM Prompt for Social Media Feed Generation

A simple text prompt used to instruct an AI (Gamma/Nano Banana Pro) to generate a complete social media feed, including hyper-realistic product shots and typography, for a small-batch olive oil brand.

```text
Create a social media feed for this small-batch olive oil brand.
```

---

## Louis Vuitton Sneaker Editorial Grid

Creates a 9-panel grid concept for a Louis Vuitton sneaker editorial campaign.

```text
Louis Vuitton Malletier, Luxury Leather Sneaker / Trainer, 3:4 aspect ratio, High-Fashion Editorial | Avant-Garde Luxury. Full-grain calf leather, Monogram Embossed Canvas, Polished Gold Hardware. Cognac Brown, Deep Obsidian, Champagne Gold. 9-panel grid: Row 1 Heritage: Hero profile on vintage LV trunk, extreme macro gold lace aglets, gold dust particles. Row 2 Innovation: Abstract floating glass V sculpture, deconstructed view, gloved hand adjusting tongue. Row 3 Surrealism: Monochromatic Havane brown, geometric desert landscape, mirror-still lake reflecting Parisian sunset.
```

---

## Louis Vuitton Sneaker Editorial Grid (9-Panel Concept)

A complex JSON prompt outlining a 9-panel grid concept for a Louis Vuitton sneaker editorial campaign. It details three themes (Heritage, Innovation, Surrealism) and specifies the visual content for e

```text
{
  "campaign_metadata": {
    "brand_identity": "Louis Vuitton Malletier",
    "product_focus": "Luxury Leather Sneaker / Trainer",
    "aspect_ratio": "3:4",
    "aesthetic": "High-Fashion Editorial | Avant-Garde Luxury"
  },
  "visual_dna": {
    "materials": ["Full-grain calf leather", "Monogram Embossed Canvas", "Polished Gold Hardware"],
    "color_scheme": ["Cognac Brown", "Deep Obsidian", "Champagne Gold"],
    "lighting": "High-contrast Chiaroscuro | Soft-box Key Lighting"
  },
  "grid_layout_execution": {
    "row_1_heritage": {
      "cell_1_1": "Hero profile: Shoe resting on a vintage LV trunk, side-lit to show leather grain.",
      "cell_1_2": "Extreme macro: Focus on the gold-tone 'LV' lace aglets and precision stitching.",
      "cell_1_3": "Dynamic: Gold dust/particles swirling around the sole as it 'steps' into frame."
    },
    "row_2_innovation": {
      "cell_2_1": "Minimalist: The shoe balanced atop an abstract, floating glass 'V' sculpture.",
      "cell_2_2": "Floating: Deconstructed view showing the sole and upper suspended in a void.",
      "cell_2_3": "Sensory: A gloved hand adjusting the tongue, emphasizing soft leather suppleness."
    },
    "row_3_surrealism": {
      "cell_3_1": "Color Palette: Monochromatic scene in LV 'Havane' brown with liquid silk drapes.",
      "cell_2_3": "Abstraction: Symbolic representation of the rubber sole pattern as a geometric desert landscape.",
      "cell_3_3": "Fusion: The shoe walking on a mirror-still lake reflecting a Parisian sunset skyline."
    }
  }
```

---

## Louis Vuitton Sneaker Editorial Grid Prompt

A highly structured JSON prompt designed for generating a 3x3 grid layout of high-fashion editorial images for a Louis Vuitton luxury sneaker, covering themes of heritage, innovation, and surrealism w

```text
{
  "campaign_metadata": {
    "brand_identity": "{argument name="brand" default="Louis Vuitton Malletier"}",
    "product_focus": "Luxury Leather Sneaker / Trainer",
    "aspect_ratio": "3:4",
    "aesthetic": "High-Fashion Editorial | Avant-Garde Luxury"
  },
  "visual_dna": {
    "materials": ["Full-grain calf leather", "Monogram Embossed Canvas", "Polished Gold Hardware"],
    "color_scheme": ["Cognac Brown", "Deep Obsidian", "Champagne Gold"],
    "lighting": "High-contrast Chiaroscuro | Soft-box Key Lighting"
  },
  "grid_layout_execution": {
    "row_1_heritage": {
      "cell_1_1": "Hero profile: Shoe resting on a vintage LV trunk, side-lit to show leather grain.",
      "cell_1_2": "Extreme macro: Focus on the gold-tone 'LV' lace aglets and precision stitching.",
      "cell_1_3": "Dynamic: Gold dust/particles swirling around the sole as it 'steps' into frame."
    },
    "row_2_innovation": {
      "cell_2_1": "Minimalist: The shoe balanced atop an abstract, floating glass 'V' sculpture.",
      "cell_2_2": "Floating: Deconstructed view showing the sole and upper suspended in a void.",
      "cell_2_3": "Sensory: A gloved hand adjusting the tongue, emphasizing soft leather suppleness."
    },
    "row_3_surrealism": {
      "cell_3_1": "Color Palette: Monochromatic scene in LV 'Havane' brown with liquid silk drapes.",
      "cell_3_2": "Abstraction: Symbolic representation of the rubber sole pattern as a geometric desert landscape.",
      "cell_3_3": "Fusion: The shoe walking on a mirror-still lake reflecting a Parisian sunset skyline."
    }
  }
}
```

---

## Low-Angle High-Fashion Portrait with Fur Coat

Creates a high-fashion editorial photograph of a woman in a voluminous golden-orange shaggy fur coat with bare legs.

```text
A high-fashion editorial photograph, captured from a low angle, showing a woman with the likeness of the person in the reference image. She is crouching elegantly, wearing a voluminous, textured golden-orange shaggy fur coat that billows around her. The main focus is on her bare legs and beautifully detailed feet in white strappy sandals, positioned prominently in the foreground. Her toenails have a clean pedicure. The lighting is soft studio light in a minimalist, off-white concrete room. The woman gazes confidently at the camera.
```

---

## Luxurious Perfume Campaign Editorial Prompt

A detailed image generation prompt for a luxurious perfume campaign editorial, designed as a dynamic 4-panel grid. It specifies cinematic glamour styling, deep burgundy and rose gold color palettes, a

```text
Luxurious perfume campaign editorial, dynamic 4-panel grid composition, 9:16 aspect ratio.

BACKGROUND: Deep burgundy foundation - rich wine ({argument name="background color" default="#3F0D19"}) as dominant canvas, alternating with ruby panels (#672232), strategic blocks of velvet plum (#2C0911) creating subtle tonal depth.
LAYOUT: Asymmetric editorial grid - full-bleed hero shot commanding 60% of canvas, detail images in varying sizes, intentional contrast between negative space and illuminated product details.
FASHION IMAGES: Cinematic glamour styling - a {argument name="subject ethnicity" default="Korean"} woman emerging from shadow, butterfly lighting revealing curves and product details - Hourglass figure with luminous skin, crimson silk gown with lace details, dewy skin, glossy lips, seductive gaze, shot on Canon EOS R5 with 85mm f/1.2 lens, Rembrandt lighting, dramatic shadows.
TYPOGRAPHY: Elegant contrast - collection title "{argument name="collection title" default="SCARLET NIGHT"}" in refined rose gold (#B76E79) serif with subtle metallic sheen (Bodoni style), product names in warm ivory (#F8F0E3).
COLOR STORY: Strictly burgundy and rose gold - burgundy absorbs, rose gold illuminates.
Style: Gucci glamour, Dior drama, cinematic luxury, mystery as sophistication, rose gold as accent.
FOOTER: Refined rose gold line above, "ROUGE & OR COLLECTION" in small elegant rose gold capitals on dark background.

Style keywords: premium fragrance, Korean beauty, cinematic editorial, sensual, opulent. A stylish handwritten signature Willy is elegantly and small letters placed at the Bottom Right corner.
```

---

## Luxury Ad Style Prompt

A prompt template for Nano Banana Pro, designed to generate images in a high-end luxury advertisement style, suitable for product or fashion visuals.

```text
Create a luxury ad style using this prompt 👇
```

---

## Luxury Black and Gold Korean Brand Identity Collage

A detailed prompt for generating a luxury brand identity presentation collage, focusing on a black and gold aesthetic with traditional Korean elements. The central hero is a Korean woman in a moderniz

```text
Luxury brand identity presentation, premium product branding collage, central hero with orbital panels arrangement, black and gold aesthetic, brand touchpoints showcase. Center: A Korean woman in a modernized black silk hanbok, gold embroidery, jeweled norigae. Orbital panels: Close-ups of hanbok details (silk texture, embroidery), gold jewelry (hairpins, rings), packaging (black lacquer box, gold foil lettering), cosmetics (cushion compact, lipstick), lifestyle shots (woman in hanbok at a traditional Korean tea ceremony, calligraphy demonstration), brand logo (stylized Korean script), pattern detail (geometric bojagi). Black background, gold accents, traditional Korean patterns. High-end commercial product photography, studio lighting, Hasselblad X2D, 85mm f/1.2. Style: heritage meets modern, sophisticated, black and gold aesthetic.. A stylish handwritten signature {argument name="signature name" default="Willy"} is elegantly and small letters placed at the Bottom Right corner.
```

---

## Luxury Bucket Hat Product Editorial

Generates a luxury editorial photograph of a fictional bucket hat.

```text
Premium fictional bucket hat with a softly structured crown.
Balanced crown height, neither too tall nor too shallow.
Brim has a gentle downward slope with a rounded edge.
Fabric is premium brushed cotton in deep espresso brown.
Front embroidery is a small star symbol stitched in warm amber thread.
No other branding.

Cinematic portrait lighting with a single soft side light.
Deep shadows and warm highlights.
Background is an amber-to-dark-brown gradient.
Analog film grain, luxury editorial photography.
```

---

## Luxury Editorial Paparazzi Style Image Editing Prompt for Nano Banana Pro

A highly specific image editing prompt for Nano Banana Pro, intended to transform an existing image into a luxury editorial, paparazzi-style photograph. The prompt requires strict preservation of the

```text
{
  "type": "image_editing_prompt",
  "language": "English",
  "style": "luxury editorial, paparazzi-style street photography",
  "aspect_ratio": "4:5",
  "identity_preservation": {
    "use_reference_image": true,
    "strict_identity_lock": true,
    "notes": "Preserve 100% of the original facial identity, structure, proportions, skin texture, and expression from the uploaded reference image. No facial alterations."
  },
  "subject": {
    "gender": "female",
    "expression": "confident, serious, mysterious",
    "appearance": {
      "eyewear": "dark, thick-rimmed sunglasses concealing the eyes",
      "hair": "unchanged from reference image"
    },
    "clothing": {
      "suit": {
        "color": "light gray / silver",
        "pattern": "fine vertical pinstripes",
        "jacket": "double-breasted with two rows of dark buttons",
        "trousers": "matching gray pinstriped fabric"
      },
      "shirt": "white dress shirt",
      "tie": "dark red tie",
      "pocket_square": "dark red, neatly folded"
    },
    "accessories": [
      "oversized luxury wristwatch with gold bezel on left wrist",
      "wide heavy gold chain bracelet on left wrist",
      "ring on the ring finger of the right hand"
    ],
    "props": {
      "right_hand": "holding a thick cigar between the fingers",
      "left_hand": "holding a small white object (possibly a lighter)"
    },
    "pose": {
      "position": "seated on a woven rattan/wicker café chair",
      "body_language": "leaning slightly forward",
      "elbow_position": "right elbow resting on a small round table"
    }
  },
  "shot": {
    "type": "close-up to medium close-up",
    "framing": "chest level and above",
    "focus": "subject is the absolute focal point"
  },
  "environment": {
    "setting": "sophisticated outdoor café or restaurant terrace"
```

---

## Luxury editorial portrait of a woman on a glass staircase

An image generation prompt designed for Google Gemini Nano Banana Pro to create a high-end, editorial-style portrait. It specifies a female subject walking up a reflective glass staircase with an eleg

```text
{
  "render_goal": "Luxury editorial portrait with architectural chic",
  "subject": {
    "pose": "{argument name="pose" default="female walking up a glass staircase, elegant posture"}",
    "expression": "{argument name="expression" default="soft composed smile, sophisticated charm"}"
  },
  "wardrobe": "{argument name="wardrobe" default="structured blazer dress or gown in neutral tones"}",
  "environment": {
    "location": "modern building with reflective glass stairs",
    "props": "natural light highlights, minimalist shadows"
  }
}
```

---

## Luxury Editorial Portrait with Architectural Chic

A concise JSON prompt for generating a luxury editorial portrait. It specifies the goal (architectural chic), the subject's pose (walking up a glass staircase), expression, and wardrobe (structured ne

```text
{
  "render_goal": "Luxury editorial portrait with architectural chic",
  "subject": {
    "pose": "female walking up a glass staircase, elegant posture",
    "expression": "soft composed smile, sophisticated charm"
  },
  "wardrobe": "structured blazer dress or gown in {argument name="wardrobe color" default="neutral tones"}",
  "environment": {
    "location": "modern building with reflective glass stairs",
    "props": "natural light highlights, minimalist shadows"
  }
}
```

---

## Luxury Fashion Editorial Collage on Modern Staircase

A structured prompt for generating a four-image collage (2x2 layout) of a fashion model (Sydney Sweeney style) posing on a modern marble staircase. The aesthetic is luxury fashion editorial, using dir

```text
{
  "scene": {
    "location": "modern indoor staircase",
    "environment": "light marble steps, white walls, stainless steel handrails",
    "lighting": "direct on-camera flash with soft ambient fill, clean shadows",
    "time_of_day": "evening",
    "set_style": "minimal, upscale residential interior"
  },
  "subject": {
    "description": "fashion model posing on staircase",
    "hair": "long brown hair in loose waves, center part",
    "makeup": "glam evening makeup, bronzed complexion, defined eyes, glossy lips",
    "expression": "confident, composed, editorial gaze",
    "poses": [
      "seated on steps with legs crossed, chin resting on hand",
      "standing sideways on stairs looking back at camera",
      "seated upright with relaxed smile",
      "standing with one hand in hair, body angled"
    ]
  },
  "wardrobe_and_accessories": {
    "outfit": "fitted {argument name=\"dress color\" default=\"brown\"} mini dress",
    "shoes": "black open-toe heels",
    "bag": "black designer shoulder bag",
    "jewelry": [
      "gold wristwatch",
      "bracelet",
      "rings"
    ]
  },
  "composition": {
    "layout": "four-image collage",
    "framing": [
      "three-quarter body shot",
      "full-body shot",
      "seated portrait",
      "standing portrait"
    ],
    "camera_angle": "eye level to slightly above",
    "focus": "sharp subject, neutral background",
    "aesthetic": "luxury fashion editorial, Instagram-ready"
  },
  "camera": {
    "lens": "35mm",
    "aperture": "f/2.8",
    "iso": 400,
    "shutter_speed": "1/60",
    "flash": "on-camera flash"
  },
  "style_keywords": [
    "modern luxury",
    "evening fashion",
    "editorial photoshoot",
    "minimal interior",
    "high-end lifestyle"
  ]
}
```

---

## Luxury Fashion Editorial Collage on Modern Staircase (Duplicate)

A structured prompt for generating a four-image collage (2x2 layout) of a fashion model (Sydney Sweeney style) posing on a modern marble staircase. The aesthetic is luxury fashion editorial, using dir

```text
{
  "scene": {
    "location": "modern indoor staircase",
    "environment": "light marble steps, white walls, stainless steel handrails",
    "lighting": "direct on-camera flash with soft ambient fill, clean shadows",
    "time_of_day": "evening",
    "set_style": "minimal, upscale residential interior"
  },
  "subject": {
    "description": "fashion model posing on staircase",
    "hair": "long brown hair in loose waves, center part",
    "makeup": "glam evening makeup, bronzed complexion, defined eyes, glossy lips",
    "expression": "confident, composed, editorial gaze",
    "poses": [
      "seated on steps with legs crossed, chin resting on hand",
      "standing sideways on stairs looking back at camera",
      "seated upright with relaxed smile",
      "standing with one hand in hair, body angled"
    ]
  },
  "wardrobe_and_accessories": {
    "outfit": "fitted {argument name=\"dress color\" default=\"brown\"} mini dress",
    "shoes": "black open-toe heels",
    "bag": "black designer shoulder bag",
    "jewelry": [
      "gold wristwatch",
      "bracelet",
      "rings"
    ]
  },
  "composition": {
    "layout": "four-image collage",
    "framing": [
      "three-quarter body shot",
      "full-body shot",
      "seated portrait",
      "standing portrait"
    ],
    "camera_angle": "eye level to slightly above",
    "focus": "sharp subject, neutral background",
    "aesthetic": "luxury fashion editorial, Instagram-ready"
  },
  "camera": {
    "lens": "35mm",
    "aperture": "f/2.8",
    "iso": 400,
    "shutter_speed": "1/60",
    "flash": "on-camera flash"
  },
  "style_keywords": [
    "modern luxury",
    "evening fashion",
    "editorial photoshoot",
    "minimal interior",
    "high-end lifestyle"
  ]
}
```

---

## Luxury Fashion Editorial on a Balcony

A JSON-structured prompt for generating a modern luxury fashion editorial image of a woman standing on a contemporary outdoor balcony. The prompt strictly locks the identity and body proportions to a

```text
{
  "image_request": {
    "identity_lock": {
      "face_reference": "Use the uploaded reference image",
      "constraints": [
        "Preserve exact facial features",
        "Preserve exact body proportions",
        "No face reshaping",
        "No body alteration",
        "Maintain natural anatomy and asymmetry"
      ]
    },
    "subject": {
      "type": "Adult woman",
      "confidence_level": "High",
      "style": "Modern luxury fashion editorial"
    },
    "pose_and_body": {
      "stance": "Standing near glass railing",
      "legs": {
        "position": "One leg bent and lifted slightly forward through high slit",
        "weight_distribution": "Weight on back leg"
      },
      "arms": {
        "one_arm": "Extended outward, hand resting gently on dark vertical pillar",
        "other_arm": "Relaxed near waist"
      },
      "posture": "Relaxed yet seductive, editorial elegance"
    },
    "camera_and_framing": {
      "angle": "Eye-level with slight downward tilt",
      "framing": "Medium-full body (head to feet)",
      "lens": "Natural perspective with subtle background compression",
      "depth_of_field": "Shallow, subject sharply focused"
    },
    "wardrobe": {
      "top": {
        "type": "White sleeveless knit top",
        "fit": "Fitted",
        "texture": "Visible knit pattern",
        "detail": "Small red flower accent at chest center"
      },
      "skirt": {
        "type": "Flowing white skirt",
        "design": "High thigh slit",
        "movement": "Soft, elegant fabric flow"
      },
      "footwear": {
        "type": "Platform high-heel sandals",
        "color": "Nude / beige",
        "details": "Ankle straps"
      }
    },
    "makeup": {
      "style": "Soft glam",
      "skin": "Smooth, natural texture",
      "contour": "Subtle",
      "brows": "Defined but natural",
      "eyes": "Light eyeliner",
      "lips": "Natural pink tone"
    },
    "accessories": {
      "jewelry": "Minimal",
      "details": [
        "Delicate bracelet",
        "Subtle accessories only"
      ]
    },
    "lighting": {
      "type": "Natural daylight",
      "quality": "Bright, soft, evenly diffused",
      "direction": "Open outdoor light",
      "shadows": "Minimal, no harsh contrast",
      "highlights": "Gentle highlights on legs, shoulders, collarbones"
    },
    "environment": {
      "location": "Modern outdoor balcony",
      "elements": [
        "Floor-to-ceiling glass railing",
        "Outdoor dining table and chair set",
        "Soft yellow table lamp",
        "Greenery below balcony"
      ],
      "background": {
        "view": "Contemporary apartment buildings, balconies, trees, blue sky",
        "focus": "Slightly blurred for depth"
      }
    },
    "color_and_processing": {
      "grading": "Clean warm-neutral",
      "aesthetic": "Modern lifestyle editorial",
      "contrast": "Bal
```

---

## Luxury Fashion Editorial Staircase Collage Prompt

A detailed JSON prompt for generating a four-image collage (triptych) featuring a fashion model (Sadie Sink likeness) posing in a fitted brown mini dress on a modern, minimalist indoor staircase, emph

```text
{
  "scene": {
    "location": "modern indoor staircase",
    "environment": "light marble steps, white walls, stainless steel handrails",
    "lighting": "direct on-camera flash with soft ambient fill, clean shadows",
    "time_of_day": "evening",
    "set_style": "minimal, upscale residential interior"
  },
  "subject": {
    "description": "fashion model posing on staircase",
    "hair": "long brown hair in loose waves, center part",
    "makeup": "glam evening makeup, bronzed complexion, defined eyes, glossy lips",
    "expression": "confident, composed, editorial gaze",
    "poses": [
      "seated on steps with legs crossed, chin resting on hand",
      "standing sideways on stairs looking back at camera",
      "seated upright with relaxed smile",
      "standing with one hand in hair, body angled"
    ]
  },
  "wardrobe_and_accessories": {
    "outfit": "fitted {argument name="dress color" default="brown"} mini dress",
    "shoes": "black open-toe heels",
    "bag": "black designer shoulder bag",
    "jewelry": [
      "gold wristwatch",
      "bracelet",
      "rings"
    ]
  },
  "composition": {
    "layout": "four-image collage",
    "framing": [
      "three-quarter body shot",
      "full-body shot",
      "seated portrait",
      "standing portrait"
    ],
    "camera_angle": "eye level to slightly above",
    "focus": "sharp subject, neutral background",
    "aesthetic": "luxury fashion editorial, Instagram-ready"
  },
  "camera": {
    "lens": "35mm",
    "aperture": "f/2.8",
    "iso": 400,
    "shutter_speed": "1/60",
    "flash": "on-camera flash"
  },
  "style_keywords": [
    "modern luxury",
    "evening fashion",
    "editorial photoshoot",
    "minimal interior",
    "high-end lifestyle"
  ]
}
```

---

## Luxury Korean Skincare Advertisement Prompt

A highly structured prompt for generating a luxury Korean skincare advertisement layout suitable for an SNS feed. It specifies a radial arrangement of products (hero product centered, complementary pr

```text
Luxury Korean skincare advertisement, SNS feed, 4:5 ratio.

LAYOUT: Centered (main product as hero) + Orbital (supporting elements surrounding)
DIRECTION: Radial arrangement - complementary products orbiting the hero product at varying distances

BACKGROUND: Dark marble surface with veining, black lacquer tray, traditional Korean silk fabric accent, subtle silver leaf scattered

PRODUCT:
- Overhead shot
- Sleek glass containers
- Silver applicator

DYNAMIC: Vapor rising from the main product (subtle), silver sparkle accents
TONE: Luxury dark - black/charcoal base with cool silver and traditional white porcelain contrast
STYLE: Luxury + Modern hybrid, traditional Korean beauty

TEXTURE DETAILS:
- Visible marble veins
- Smooth lacquer patina
- Glass reflection variations
- Woven silk texture

TYPOGRAPHY: Brand name in elegant calligraphy style, silver foil effect, Korean + English

CAMERA: Hasselblad X2D, 90mm Macro f/3.5, overhead shot, cool tungsten + soft fill lighting

SIGNATURE: A stylish handwritten signature "{argument name="signature name" default="Willy"}" elegantly placed at bottom right corner (small letters)

Style keywords: Korean beauty, serum arrangement, traditional luxury, heritage skincare.
A stylish handwritten signature Willy is elegantly and small letters placed at the Bottom Right corner.
```

---

## Luxury Mirror Selfie Prompt (Influencer Aesthetic)

A highly detailed JSON prompt for generating an image in the style of an influencer mirror selfie. It specifies the subject's appearance (blonde hair, glowy makeup), attire (bralette, high-waisted ski

```text
{
  "prompt_details": {
    "subject": {
      "type": "Woman",
      "appearance": {
        "hair": "{argument name="hair style" default="Long, blonde, highlighted, straight with slight wave, parted in the middle"}",
        "skin_tone": "Tan, bronzed",
        "expression": "{argument name="expression" default="Smiling warmly, white teeth visible, looking at phone screen"}",
        "makeup": "Glowy natural glam, defined brows, glossy lips, soft contour"
      }
    },
    "attire": {
      "top": "Nude/beige structured bralette or bikini top with underwire and thin straps",
      "bottom": "Dark chocolate brown high-waisted pencil skirt",
      "outerwear": "Oversized, fluffy faux fur coat in light beige/taupe, worn open and draped over arms",
      "accessories": [
        "Small gold hoop earrings",
        "Gold ring on left ring finger",
        "Nude/light pink manicure"
      ]
    },
    "action": {
      "pose": "Standing mirror selfie",
      "hands": "Right hand resting on hip, left hand holding phone",
      "device": "iPhone Pro model (likely gold or silver) with three camera lenses"
    },
    "environment": {
      "setting": "Luxury bathroom or dressing room",
      "architecture": "Beige stone/travertine tiled walls, arched alcove with built-in wooden shelving",
      "furniture": "Large rectangular mirror with bevel, wooden vanity counter",
      "decor": "Skincare bottles and products on shelves, wall-mounted sconce lights with warm shades",
      "background_reflection": "Reflection shows depth of room and another mirror/doorway"
    },
    "technical_specs": {
      "lighting": "Soft warm indoor lighting mixed with natural light from the left, golden hour vibes",
      "color_palette": [
        "Beige",
        "Cream",
        "Chocolate Brown",
        "Tan",
        "Gold"
      ],
      "style": "Influencer aesthetic, lifestyle photography, high resolution, soft focus background",
      "angle": "Front-facing reflection shot"
    }
  }
}
```

---

## Luxury Nightlife Photo Collage (4-Image Grid)

A JSON prompt template for creating a four-image (2x2) cinematic nightlife lifestyle collage, maintaining continuity of the subject, outfit, and location across all frames. The setting is an upscale o

```text
{ "scene\_type": "nightlife\_lifestyle", "setting": { "location": "outdoor restaurant or lounge patio", "time": "night", "environment": "urban, intimate, upscale", "lighting": "warm ambient lighting from patio heaters and string lights" }, "composition": { "format": "four-image collage", "layout": "2x2 grid", "continuity": "same subject, outfit, and location across all frames" }, "subject": { "type": "person in the reference image", "appearance": { "hair": { "color": "blonde", "length": "long", "style": "loose, softly waved" } }, "clothing": { "outerwear": "black leather jacket", "top": "black cut-out crop top", "bottom": "black fitted mini skirt" }, "expressions": [ "confident", "relaxed", "contemplative", "posed" ], "poses": [ "standing with wine glass", "seated holding wine glass", "leaning with hands near waist", "resting chin on hand" ] }, "objects": [ { "type": "wine\_glass", "content": "{argument name="drink color" default="red wine"}", "held": true }, { "type": "patio\_heater", "description": "tall outdoor gas heater emitting warm light" }, { "type": "met"

First, define the scene as a nighttime outdoor restaurant or lounge patio. The environment should feel urban, intimate, and premium. Use warm ambient lighting such as patio heaters and string lights to create a cozy yet luxurious night atmosphere.

Next, make sure visual continuity is locked. Use the same subject, outfit, and location in all images. This consistency is what gives the final collage a professional, editorial feel.

Style the subject in a full black nightlife outfit. A black leather jacket paired with a black cut-out crop top and a fitted black mini skirt works perfectly for a confident and modern look. The hair should be long, blonde, loose, and softly waved to maintain an effortless nightlife vibe.

Across the four frames, vary the subject’s expressions and poses. One image can show the subject standing confidently while holding a glass of red wine. Another can be seated and relaxed with the wine glass in hand. A third pose can involve leaning slightly with hands near the waist for a composed look. The final frame can be more contemplative, with the subject resting their chin on their hand.

When generated correctly, Nano Banana Pro will produce a high-end nightlife photo collage that feels cinematic, stylish, and social-media ready, suitable for fashion editorials, lifestyle branding, and premium AI visuals. Share your nightlife photo collages below!
```

---

## Luxury Packaging Reveal Prompt for Leonardo AI

This is a prompt for Leonardo AI, shared by a Nano Banana Pro user, designed to create a visually appealing luxury packaging reveal image.

```text
Create a luxury packaging reveal using this prompt 👇
```

---

## Luxury Paparazzi Street Photography Prompt

A highly detailed, JSON-structured prompt for image editing, requiring strict preservation of facial identity from a reference image. It generates a luxury editorial, paparazzi-style street photo of a

```text
{
  "type": "image_editing_prompt",
  "language": "English",
  "style": "luxury editorial, paparazzi-style street photography",
  "aspect_ratio": "4:5",
  "identity_preservation": {
    "use_reference_image": true,
    "strict_identity_lock": true,
    "notes": "Preserve 100% of the original facial identity, structure, proportions, skin texture, and expression from the uploaded reference image. No facial alterations."
  },
  "subject": {
    "gender": "female",
    "expression": "confident, serious, mysterious",
    "appearance": {
      "eyewear": "dark, thick-rimmed sunglasses concealing the eyes",
      "hair": "unchanged from reference image"
    },
    "clothing": {
      "suit": {
        "color": "{argument name="suit color" default="light gray / silver"}",
        "pattern": "fine vertical pinstripes",
        "jacket": "double-breasted with two rows of dark buttons",
        "trousers": "matching gray pinstriped fabric"
      },
      "shirt": "white dress shirt",
      "tie": "dark red tie",
      "pocket_square": "dark red, neatly folded"
    },
    "accessories": [
      "oversized luxury wristwatch with gold bezel on left wrist",
      "wide heavy gold chain bracelet on left wrist",
      "ring on the ring finger of the right hand"
    ],
    "props": {
      "right_hand": "holding a thick cigar between the fingers",
      "left_hand": "holding a small white object (possibly a lighter)"
    },
    "pose": {
      "position": "seated on a woven rattan/wicker café chair",
      "body_language": "leaning slightly forward",
      "elbow_position": "right elbow resting on a small round table"
    }
  },
  "shot": {
    "type": "close-up to medium close-up",
    "framing": "chest level and above",
    "focus": "subject is the absolute focal point"
  },
  "environment": {
    "setting": "sophisticated outdoor café or restaurant terrace
```

---

## Luxury Product Photography Black Oudh Diffuser

Creates ultra-realistic luxury product photography of a black glass reed diffuser bottle.

```text
Ultra-realistic luxury product photography of a black glass reed diffuser bottle labeled "{argument name="product name" default="BLACK OUDH – Private Collection – RITUALS"}" in elegant gold serif typography. Bottle has curved rectangular shape with soft edges, glossy reflective surface, gold wax-seal style emblem. Thin black diffuser reeds extend upward. Covered in realistic water droplets and condensation. Placed among deep black roses and dark burgundy petals with visible water droplets, rich green leaves. Moody dramatic with dark botanical background, softly blurred. Cinematic low-key lighting, cool-toned. Vertical portrait 4:5 ratio, centered product.
```

---

## Luxury Product Photography for Artisanal Vanilla Coffee

A detailed prompt for generating luxury product photography for artisanal vanilla ground coffee. The scene features the coffee packaged in a soft, ivory sculpted pouch resting on an oak tabletop, acco

```text
Luxury product photography of artisanal vanilla ground coffee packaged in a soft sculpted ivory pouch with gentle wave contours, minimal branding embossed into fabric. The pouch rests on a rustic oak tabletop dusted with coffee grounds, accompanied by a hand-carved wooden scoop spilling aromatic powder.
Natural Madagascar vanilla pods curve organically around the base, blending into drifting coffee granules that form a subtle flowing aroma path instead of a spiral.
On the pouch front, a modern sensory chart: thin matte gold lines showing flavor balance — low acidity, rich sweetness, full-bodied depth.
Warm morning sunlight enters from the left at a low angle, creating soft shadows and tactile fabric highlights. Background fades into a cozy café interior with creamy bokeh lights, evoking calm morning rituals.
Ultra-sharp macro texture on vanilla pods and coffee grains, cinematic depth of field, premium lifestyle aesthetic, inviting, warm, handcrafted, high-end brand feel.
```

---

## Luxury Skincare Diorama in a Perfume Bottle

A highly detailed, couture-style prompt for generating a macro photograph of a luxury skincare serum diorama, featuring miniature Korean women musicians and a conductor performing in a serum pool insi

```text
Luxury skincare serum diorama
LAYOUT: Single hero, miniature concert hall within a perfume bottle
DIRECTION: Vertical, rising elegance, intricate details
BACKGROUND: Opulent miniature concert hall, velvet textures, soft bokeh
PRODUCT: Voluptuous Korean woman conductors and musicians in shimmering couture performing in a serum pool within the perfume bottle, porcelain skin, long silky hair, sultry gazes, graceful poses, jeweled instruments
DYNAMIC: Cascading serum droplets, floating musical notes, subtle mist
TONE: Tone-on-tone, blush rose and champagne gold palette
STYLE: Soft, luxurious, K-beauty aesthetic, macro photography, couture fashion editorial
MAIN ELEMENT:
A scaled-down world inside a Chanel No. 5 perfume bottle, crystal-clear serum forming a pool, miniature rose bushes and glowing flora, miniature musicians playing harps, violins, and cellos, and a woman conductor standing poised.
DYNAMIC ELEMENTS:
Droplets of serum cascading like waterfalls, musical notes gently floating, subtle golden mist adding a magical touch, fabric flow from the silk gowns.
CAMERA: Shot on Hasselblad X2D, 85mm f/1.2, Rembrandt lighting, shallow depth of field.
Style keywords: enchanting, voluptuous, luxurious, K-beauty, miniature, diorama, couture.
```

---

## Luxury Street Style Portrait in Porsche Interior

Creates a photorealistic image of a young, stylish woman in the driver's seat of a luxury Porsche car.

```text
{
  "image_generation_prompt": {
    "subject": {
      "description": "Young stylish woman with long blonde wavy hair.",
      "pose": "Sitting in the driver's seat of a luxury car, side profile view. She is sitting with her knees pulled up close to her chest, feet resting on the seat, holding the steering wheel with both hands.",
      "expression": "Calm, focused, model-like demeanor."
    },
    "attire": {
      "headwear": "Black baseball cap with white text embroidery on the side.",
      "eyewear": "Black rectangular designer sunglasses with a gold logo on the temple (resembling Celine style).",
      "jewelry": "Chunky gold hoop earrings.",
      "outerwear": "Oversized black wool blazer or coat.",
      "bottoms": "Dark grey or faded black denim jeans.",
      "footwear": "Classic chestnut brown sheepskin mini boots (Ugg style)."
    },
    "environment": {
      "location": "Interior of a high-end luxury car (Porsche).",
      "details": "Black leather seats with white stitching, Porsche crest embossed on the headrest and visible on the steering wheel.",
      "background": "Blurred city street view visible through the car window, daytime natural lighting."
    },
    "style": {
      "aesthetic": "Old money aesthetic, luxury street style, influencer lifestyle, candid photography.",
      "lighting": "Soft natural daylight coming through the window.",
      "camera_angle": "Eye-level, side profile shot captured from the passenger side."
    },
    "technical_specs": {
      "aspect_ratio": "4:5",
      "quality": "High resolution, photorealistic, sharp focus, 8k."
    }
  }
}
```

---

## Luxury Streetwear Instagram Feed Composite

A detailed, structured prompt for creating a high-fashion Instagram feed composite (4:5 ratio) featuring a stunning Eurasian model in a luxury/streetwear fusion outfit (silk slip dress and high-top sn

```text
Stunning Eurasian (Chinese/French) model, Instagram feed, 4:5 ratio.

LAYOUT: Irregular Grid (main image 60% of space, details filling remaining) + Layered (images overlapping for depth).

DIRECTION: Diagonal flow guiding eye from top left to bottom right.

BACKGROUND: Urban rooftop at sunset with blurred city lights, graffiti art accents, high-fashion editorial vibe.

PRODUCT: Worn shot – model showcasing silver high-top sneakers with pink accents, close-up detail shots of sneaker texture and design layered over main image.

DYNAMIC: Gold dust particles swirling around sneakers and model, fabric of dress floating dramatically, light rays catching the gold dust.

TONE: Color contrast – cool silver sneakers against warm sunset backdrop, pink accents popping against the urban gray.

STYLE: Luxury + Streetwear fusion. Model in {argument name="dress type" default="silk slip dress with lace trim"}, diamond jewelry, and messy high ponytail. Raw urban setting juxtaposed with high-end fashion elements.

UI ELEMENTS: None.

CAMERA: Hasselblad H6D, 85mm f/1.2, dramatic rim lighting with soft fill, composite shot.

Style keywords: streetwear meets luxury, unexpected elegance, golden hour glow, urban fairytale.. A stylish handwritten signature Willy is elegantly and small letters placed at the Bottom Right corner
```

---

## Luxury Travel Lifestyle Portrait in Monaco

A structured prompt for generating a luxury travel lifestyle photograph of a young woman in Monaco. The prompt details the subject's appearance, chic outfit (cream off-shoulder top, white trousers), p

```text
{
  "subject": {
    "person": "Young woman, early 20s, Caucasian",
    "hair": "Golden blonde hair with loose curls and subtle flyaways",
    "pose": "Seated on ledge, legs crossed at ankles, shoulders relaxed",
    "expression": "Gentle, composed, understated smile"
  },
  "outfit": {
    "top": "{argument name=\"top style\" default=\"Cream off-shoulder fitted top\"}",
    "bottoms": "High-waisted white trousers",
    "accessories": "Mini handbag, pearl studs, thin chain necklace"
  },
  "action": {
    "hands": "Hands resting loosely on knees"
  },
  "location": {
    "setting": "Terrace overlooking Monaco circuit near Casino Square",
    "background": "Luxury hotels, racetrack walls, cloudy sky"
  },
  "typography": {
    "text": "{argument name=\"branding text\" default=\"MONTE-CARLO, UBS branding\"}"
  },
  "lighting": {
    "type": "Natural ambient daylight",
    "quality": "Soft, evenly diffused"
  },
  "composition": {
    "style": "Luxury travel lifestyle photograph, medium portrait, 4:5",
    "color_palette": "Warm creams and muted greys"
  }
}
```

---

## Luxury Yacht Lifestyle Photo Collage Prompt

A highly detailed JSON prompt for generating a three-frame vertical photo collage depicting a glamorous female subject enjoying a luxury summer lifestyle on a yacht. The prompt specifies the setting,

```text
{
  "image_type": "photo collage",
  "number_of_frames": 3,
  "overall_theme": "luxury summer lifestyle, yacht leisure, coastal glamour",
  "setting": {
    "location": "onboard a luxury yacht",
    "environment": {
      "water": "deep blue sea with visible wake and splashes",
      "background": "rocky coastal cliffs with greenery and a few distant white buildings",
      "weather": "clear, sunny day",
      "lighting": "natural bright sunlight, high contrast, sharp shadows"
    }
  },
  "subject": {
    "count": 1,
    "gender_presentation": "female",
    "approximate_age_range": "young adult",
    "appearance": {
      "skin_tone": "light to lightly tanned",
      "body_type": "slim, athletic, toned",
      "hair": {
        "color": "blonde",
        "length": "long",
        "style": "loose, slightly wavy"
      }
    },
    "clothing": {
      "outfit": "black bikini",
      "style": "minimal, modern",
      "fit": "form-fitting"
    },
    "accessories": "none visible",
    "footwear": "barefoot"
  },
  "poses_by_frame": {
    "frame_1": {
      "pose": "reclining sideways",
      "details": "one arm bent behind the head, body stretched along the yacht cushion",
      "expression": "relaxed, eyes closed or softly focused",
      "camera_angle": "side view, slightly elevated"
    },
    "frame_2": {
      "pose": "lying on back",
      "details": "arms stretched overhead, legs bent slightly",
      "expression": "calm, eyes closed, serene",
      "camera_angle": "top-down to slightly angled"
    },
    "frame_3": {
      "pose": "lying on stomach",
      "details": "elbows resting on cushion, feet lifted and crossed",
      "expression": "smiling, playful, direct engagement with camera",
      "camera_angle": "rear three-quarter angle"
    }
  },
  "surface_and_objects": {
    "yacht_details": {
      "material": "white leather or vinyl cushions",
      "design": "clean, modern, luxury finish",
      "color_palette": "white upholstery contrasting with blue sea"
    }
  },
  "color_palette": {
    "dominant_colors": [
      "white",
      "deep blue",
      "black",
      "sand beige"
    ],
    "accent_colors": [
      "turquoise highlights in water",
      "green from coastal vegetation"
    ]
  },
  "mood_and_aesthetic": {
    "mood": "relaxed, confident, glamorous",
    "aesthetic": "luxury travel, summer sensuality, high-end lifestyle",
    "energy": "calm yet playful"
  },
  "composition": {
    "layout": "vertical collage with three horizontal frames",
    "focus": "subject centered in each frame",
    "depth": "foreground subject with scenic coastal background",
    "sharpness": "high clarity and detail"
  },
  "photography_style": {
    "style": "editorial lifestyle photography",
    "lighting_type": "natural daylight",
    "post_processing": "light color enhancement, crisp contrast, clean tones"
  },
  "intended_use": [
    "fashion or swimwear editorial",
    "luxury travel promotion",
    "so"
```

---

## Margaret Qualley Close-Up Portrait Prompt

A highly detailed JSON prompt for generating a close-up, high-fashion portrait of Margaret Qualley. It meticulously defines her facial features, hair (slicked-back low ponytail), makeup (natural glam,

```text
{
  "prompt_elements": {
    "subject": {
      "name": "Margaret Qualley",
      "face_style": "High-fashion actress look with delicate bone structure and expressive eyes",
      "age_range": "Late 20s to early 30s",
      "skin_tone": "Fair with cool undertones",
      "face_shape": "Soft oval with gently tapered jawline",
      "facial_features": {
        "eyes": "Large almond-shaped blue-gray eyes with wide spacing and soft outer corners",
        "eyebrows": "Naturally full, straight brows with subtle arch and feathered texture",
        "nose": "Narrow straight bridge with softly rounded tip and petite nostrils",
        "lips": "Medium-full lips with defined cupid’s bow and slightly fuller lower lip",
        "cheekbones": "High-set, softly sculpted cheekbones with smooth transitions",
        "jawline": "Slim, feminine jaw with gentle curve",
        "chin": "Softly pointed, delicate chin",
        "complexion": "Smooth luminous skin with visible natural texture and reflective cheekbone highlights"
      },
      "hair": {
        "color": "Dark brown",
        "style": "Slicked-back low ponytail",
        "texture": "Smooth, glossy",
        "part": "No visible part, brushed straight back"
      },
      "expression": "Neutral, composed, confident",
      "pose": {
        "head_position": "Turned slightly to the left",
        "gaze_direction": "Looking directly at camera",
        "shoulders": "Angled slightly away from camera",
        "framing": "Close-up portrait from chest to top of head"
      }
    },
    "clothing_and_accessories": {
      "outfit": {
        "type": "Formal evening dress",
        "color": "Black",
        "material": "Sequined fabric",
        "neckline": "Deep scoop",
        "fit": "Fitted bodice",
        "style": "Elegant, red carpet fashion"
      },
      "earrings": {
        "type": "Statement drop earrings",
        "design": "Black circular stud with gold connector and long white ceramic teardrop shape with black speckled pattern",
        "length": "Long, dangling"
      },
      "makeup": {
        "eyes": "Soft neutral eyeshadow, mascara-enhanced lashes ‘clean girl’ finish",
        "cheeks": "Rosy blush with glossy highlight",
        "lips": "Muted rose nude satin finish",
        "overall_style": "Natural glam, editorial red carpet look"
      }
    },
    "environment": {
      "location_type": "Outdoor balcony or terrace",
      "background": "Light stone classical building facade with windows and architectural molding",
      "foreground_elements": "Dark metal railing partially visible",
      "setting": "Urban, upscale, elegant exterior venue"
    },
    "lighting_and_color": {
      "lighting_type": "Direct on-camera flash mixed with daylight",
      "light_direction": "Front-facing, slightly above eye level",
      "shadows": "Minimal shadowing, hard-edged highlights",
      "highlights": "Strong specular highlights on skin and sequins",
```

---

## Marketing Mastermind for Product Promotion

Optimizes product and e-commerce strategies for marketing mastermind for product promotion.

```text
Act as a Marketing Mastermind. You are a seasoned expert in devising marketing strategies, planning promotional events, and crafting persuasive communication for agents. Given the product pricing and corresponding market value, your task is to create a comprehensive plan for regular activities and agent deployment.

Your responsibilities include:
- Analyze product pricing and market value
- Develop a schedule of promotional activities
- Design strategic initiatives for agent collaboration
- Create persuasive communication to motivate agents for enhanced performance
- Ensure alignment with market trends and consumer behavior

Constraints:
- Adhere to budget limits
- Maintain brand consistency
- Optimize for target audience engagement

Variables:
- ${productPrice} - the price of the product
- ${marketValue} - the assessed market value of the product
- ${budget} - available budget for activities
- ${targetAudience} - the intended audience for marketing efforts
```

---

## Master Prompt for Premium Minimalist Product Photography

A reusable master prompt template designed for generating premium, minimalist product photography (UGC statics). It guides the user to specify the brand, product, surface, and relevant props, ensuring

```text
Premium minimalist product photography. A {argument name="brand name" default="BRAND"} {argument name="product name" default="PRODUCT"} featuring {argument name="packaging details" default="PACKAGING/LOGO DETAILS"} placed at the center of the frame. The product rests on {argument name="surface type" default="SURFACE"} surrounded by {argument name="relevant props" default="RELEVANT PROPS"}. Clean matte {argument name="background color" default="COLOR"} background with subtle gradient. Soft diffused lighting with gentle rim light creates a luminous glow highlighting {argument name="key features" default="KEY FEATURES"}. Sharp focus, high clarity, realistic textures, luxury advertising style, modern branding, ultra-realistic, 8K detail, high dynamic range.

Negative Prompt: hands, people, faces, clutter, harsh reflections, label distortion, unreadable text, warped product, hard shadows, grain, noise, low resolution, CGI look, cartoon style, messy spills, uneven lighting, watermark
```

---

## Mediterranean Sunbathing Scene with Red Bikini and NY Cap

A detailed JSON prompt for generating a photorealistic image of a woman relaxing in a vibrant red bikini and a baseball cap on a lounge chair in a sunny Mediterranean garden, focusing on realistic ski

```text
{
  "scene": "Sunny outdoor garden setting with a Mediterranean aesthetic, featuring a woman relaxing on a lounge chair in a calm, sun-drenched environment.",
  "subject": {
    "character": "Young woman with a sun-kissed complexion and a fit, athletic build.",
    "face": {
      "structure": "Oval face with a defined jawline and soft, balanced features.",
      "skin": "Naturally tanned skin with realistic texture visible under direct sunlight.",
      "eyes": {
        "shape": "Almond-shaped",
        "color": "Light brown",
        "expression": "Focused, confident gaze directed toward the camera with a composed, calm expression."
      },
      "mouth": {
        "lips": "Full lips with a natural shape, gently closed in a neutral expression."
      },
      "makeup": "Minimal, natural makeup look with warm-toned eyeshadow, softly groomed eyebrows, and matte nude lipstick."
    },
    "hair": {
      "color": "Light brown with sun-bleached golden blonde highlights.",
      "length": "Long hair reaching mid-back.",
      "texture": "Naturally wavy with visible flyaways and slight frizz from outdoor humidity.",
      "style": "Loose and unstyled, flowing naturally.",
      "visible": "Falling over the left shoulder and cascading down the back."
    },
    "accessories": {
      "hat": {
        "type": "Baseball cap",
        "color": "Cream crown with a navy blue brim.",
        "detail": "Red embroidered '{argument name=\"cap logo\" default=\"NY\"}' logo on the front.",
        "fit": "Standard fit, worn low over the forehead."
      }
    }
  },
  "pose": {
    "overall": "Prone position on a lounge chair, body angled away from the camera while the head is turned back.",
    "position": {
      "base": "Lying on the stomach on a wooden deck lounge chair.",
      "orientation": "Profile view of the body with the head turned three-quarters toward the camera."
    },
    "torso": {
      "direction": "Facing downward and away from the camera.",
      "position": "Slightly supported by the arms, creating a natural arch in the back."
    },
    "hips": {
      "position": "Elevated and subtly angled toward the camera.",
      "emphasis": "Natural emphasis on posture and body lines created by the pose."
    },
    "legs": {
      "position": "Extended straight along the length of the lounge chair.",
      "visible": "Upper thighs and partial lower legs visible before leaving the frame."
    },
    "arms": {
      "position": "Right arm folded beneath the upper torso; left arm extended forward, resting along the chair frame."
    },
    "head": {
      "turn": "Turned clearly over the left shoulder.",
      "expression": "Calm, steady expression with direct eye contact."
    }
  },
  "outfit": {
    "swimwear": {
      "type": "Two-piece string bikini",
      "color": "Vibrant {argument name=\"bikini color\" default=\"red\"}",
      "top": {
        "style": "Triangle bikini top",
        "ties": "Thin straps tied around the neck and back.",
        "coverage": "Tasteful, fashion-forward coverage."
      },
```

---

## Messy Closet Selfie Portrait Prompt

A structured prompt for Nano Banana Pro to generate a fashion editorial style portrait of a young woman lying on a messy closet floor, taking a top-down selfie in a mismatched outfit, capturing the ae

```text
{
  "prompt_type": "descriptive_portrait",
  "subject_details": {
    "demographics": "Young female, pale skin with cool undertones, slender frame.",
    "facial_features": {
      "expression": "Looking up at the phone with a playful frown/pout ('tired but cute'), blowing a strand of hair out of her face.",
      "eyes": "Grey eyes with winged eyeliner.",
      "hair": "Platinum blonde bob cut, messy and tousled."
    },
    "apparel": {
      "dress": "A mismatched set: a leopard print bikini top and high-waisted black sequined shorts.",
      "accessories": "Multiple rings on fingers and large hoop earrings.",
      "footwear": "One black combat boot on, the other foot bare with painted toenails."
    }
  },
  "pose_and_action": {
    "body_position": "Lying on her back on a plush carpeted floor, surrounded by piles of clothes. Legs kicked up in the air, crossed at the ankles.",
    "hands": "Holding the smartphone directly above her face with both hands for a top-down selfie.",
    "camera_angle": "High-angle, top-down reflection from a ceiling mirror or looking down into a large floor mirror."
  },
  "background_environment": {
    "location": "Messy walk-in closet floor.",
    "lighting_source": "Even, bright overhead track lighting.",
    "objects": {
      "clutter": "Piles of discarded jeans, tops, shoes, hangers, and bags spread all over the floor around her."
    }
  },
  "technical_specs": {
    "style": "Fashion editorial aesthetic, organized chaos, high detail, sharp focus.",
    "aspect_ratio": "4:5"
  }
}
```

---

## Miniature Brand Building Prompt (Placeholder)

A general prompt template instructing the creation of a miniature brand building, suggesting a use case for architectural or product visualization, but the detailed JSON prompt is linked externally.

```text
Create miniature brand building using this JSON prompt 👇
```

---

## Miniature Construction Site Ad for a Product

A creative image generation prompt designed to create a playful yet hyper-realistic miniature scene of a construction crew assembling a product, making it look like a skyscraper. This style is suitabl

```text
A miniature construction crew assembling {argument name="product" default="[PRODUCT]"} like a skyscraper. Cranes, scaffolding, sparks flying. Playful but hyper-real, brand-campaign ready.
```

---

## Miniature Construction Site Product Ad

A playful but hyper-realistic prompt for a brand campaign, depicting a miniature construction crew assembling a specified product as if it were a skyscraper, complete with cranes, scaffolding, and spa

```text
A miniature construction crew assembling {argument name="product name" default="[PRODUCT]"} like a skyscraper. Cranes, scaffolding, sparks flying. Playful but hyper-real, brand-campaign ready.
```

---

## Minimalist Fashion Ad Studio Photograph Prompt

A prompt for generating a minimalist, stark white studio photograph for a fashion advertisement. It details the composition, subject (man in a black suit), props (modern chair, glasses), and the place

```text
A minimalist studio photograph fashion ad. At the top center, the bold sans-serif text "{argument name="bold text" default="[TEXT]"}" is positioned above the smaller sans-serif text "{argument name="smaller text" default="[TEXT]"}", which is above the italic script text "{argument name="italic text" default="[TEXT]"}". Below the text, a man in a black suit, black t-shirt, and polished black dress shoes sits in profile, facing left. He is seated in a modern chair with a black leather seat and backrest suspended on a tubular black metal frame. His right leg is extended, and he holds a pair of glasses in his right hand near his mouth. The background and floor are a seamless, stark white studio space with soft, diffused lighting that casts grounded shadows beneath the man and chair.
```

---

## Minimalist Skincare Product Photography with Bubbles

A prompt for generating premium, minimalist product photography of a translucent pink liquid cleanser bottle, featuring soft pink foamy bubbles and specific lighting to create a luxury beauty advertis

```text
Premium minimalist skincare product photography. A translucent pink liquid cleanser bottle with a white pump dispenser placed vertically at the center of the frame. The bottle rests inside an organic pool of soft pink foamy bubbles, with airy soap lather spreading outward in smooth, rounded shapes. Small transparent bubbles float around the foam surface. Clean matte pastel pink background with subtle gradient. Soft diffused top lighting with gentle rim light creates a luminous glow through the liquid, highlighting the pump tube inside the bottle. Sharp focus, high clarity, realistic liquid refraction, smooth plastic and glass textures, luxury beauty advertising style, modern cosmetic branding, ultra-realistic, 8K detail, high dynamic range.

Negative Prompt:

hands, people, faces, clutter, harsh reflections, label distortion, unreadable text, warped pump, hard shadows, grain, noise, low resolution, CGI look, cartoon style, messy foam, uneven lighting, watermark
```

---

## Minimalist Startup Presentation Cover Visual Prompt

A prompt designed for generating a minimalist, high-impact cover visual for a premium startup presentation. The focus is on restraint, strong visual hierarchy, abstract branding, and ample negative sp

```text
Cover visual for a premium startup presentation.
Minimal layout,
strong visual hierarchy,
abstract brand motif,
ample negative space,
designed to set tone without overwhelming content.
```

---

## Minimalistic Premium Website Landing Page Prompt

A prompt designed for generating a minimalistic yet premium website landing page screenshot, intended to showcase specific products from a given brand, requiring reference images of the products.

```text
"Create a screenshot of a web site landing page it should be minimalistic but premium, showing these products by {argument name="brand name" default="(brand name)"}. add any details needed"
```

---

## Mirror Selfie in Neon Yellow Swimsuit

A detailed prompt for generating a mirror selfie of a young woman in a neon yellow one-piece swimsuit and high pigtails. The scene includes specific foreground props like a glass bong and vase on a dr

```text
{
  "prompt": {
    "subject": {
      "description": "Young woman taking a mirror selfie",
      "hair": "Blonde, styled in high pigtails secured with yellow scrunchies, loose tendrils framing her face",
      "face": {
        "expression": "Neutral, slightly serious, gaze looking towards the side away from the phone",
        "skin_tone": "Fair",
        "eyes": "Light-colored, defined with makeup",
        "nose": "Small, defined",
        "lips": "Pink, full",
        "cheeks": "Lightly blushed, defined cheekbones"
      },
      "body": "Slender build, fair skin"
    },
    "attire": {
      "swimsuit": {
        "color": "{argument name="swimsuit color" default="Neon yellow"}",
        "style": "One-piece, high-cut leg, zip-front neckline"
      },
      "accessories": {
        "fanny_pack": {
          "colors": "Pink, white, teal, yellow strap",
          "text": "White 'polpi' logo on the pink section",
          "placement": "Worn crossbody over the swimsuit"
        },
        "jewelry": {
          "neck": "Layered delicate gold necklaces",
          "wrist": "Gold bracelet, black scrunchie",
          "fingers": "Multiple gold rings"
        },
        "phone": "Silver smartphone in a clear case, held in her right hand"
      }
    },
    "setting": {
      "location": "Bedroom",
      "background": {
        "bed": "Unmade white bedding, white pillows, light-colored upholstered headboard with vertical channels",
        "furniture": "White bedside table, white wall",
        "lighting": "Gold lamp with two globe shades on the bedside table"
      },
      "foreground": {
        "surface": "Reflective white dresser top",
        "objects": [
          "Clear glass vase",
          "Tall clear glass bong",
          "Smaller glass jar with a lid",
          "Small white tube"
        ]
      }
    },
    "photography": {
      "style": "Mirror selfie",
      "lighting": "Bright natural daylight",
      "aspect_ratio": "Vertical (portrait)"
    }
  }
}
```

---

## Mirror Selfie Prompt with Detailed Subject and Object Specifications

A highly detailed prompt specifying the subject's appearance (hair, tattoo, clothing) and the objects in the scene (phone, Stanley-style tumbler, keys) for generating a realistic mirror selfie image i

```text
{
  "subject": {
    "gender": "female",
    "hair": {
      "color": "brunette",
      "style": "wavy",
      "length": "long",
      "bangs": "curtain bangs",
      "highlights": "light brown"
    },
    "tattoo": {
      "location": "left forearm",
      "design": "floral",
      "style": "black and grey line work"
    },
    "accessories": [
      {
        "type": "bracelet",
        "style": "gold chain",
        "charm": "green clover/quatrefoil",
        "quantity": 2
      }
    ],
    "pose": {
      "orientation": "side profile/turned away from camera",
      "action": "taking mirror selfie",
      "hand_position": "holding phone up to mirror with left hand"
    },
    "clothing": {
      "top": {
        "color": "{argument name="top color" default="pink"}",
        "style": "t-shirt",
        "fit": "loose/casual"
      },
      "bottom": {
        "color": "purple",
        "style": "biker shorts/athletic shorts",
        "fit": "tight"
      }
    }
  },
  "objects": {
    "phone": {
      "case_pattern": "white marble",
      "camera_lens_count": 3
    },
    "cup": {
      "type": "tumbler with handle and straw",
      "color": "pink",
      "brand_style": "Stanley-style"
    },
    "keys": {
      "location": "countertop",
      "type": "car key fob and house keys"
    }
  },
  "setting": {
    "location": "bathroom or dressing room",
    "background_wall": {
      "texture": "beige textured wallpaper/fabric"
    },
    "countertop": {
      "material": "dark granite/marble"
    },
    "flooring": {
      "type": "light beige tile"
    }
  }
}
```

---

## Mirror Selfie with Cat Ears and Gingham Skirt Prompt

A structured JSON prompt for generating a mirror selfie photograph of a young woman in a playful, pink-themed outfit (cat ears, brocade corset, gingham skirt). It specifies the pose (tongue sticking o

```text
{
  "prompt": {
    "subject": {
      "description": "A young woman with long blonde hair and fair skin, wearing white fluffy cat ears headband.",
      "attire": {
        "top": "Pink brocade corset with front lacing and trim.",
        "bottom": "Pink gingham ruffled mini skirt with white lace trim.",
        "accessories": "Pink collar choker with a small silver bell, white thigh socks with pink stripes at the top.",
        "jewelry": "Small stud earrings, delicate gold bracelet."
      },
      "expression": "Playful, looking up and to the left with tongue sticking out, slight smile, light eye makeup with winged liner, pink lip color, rosy cheeks, defined nose.",
      "action": "Taking a mirror selfie with a white iPhone held in her right hand, showing her reflection."
    },
    "background": {
      "setting": "Modern apartment interior.",
      "elements": "Large floor-to-ceiling windows showing a bright daytime cityscape and sky.",
      "flooring": "Grey wood plank flooring.",
      "objects": {
        "left_side": "Large brown teddy bear leaning against a grey tiled wall section.",
        "right_side": "White upholstered armchair, wooden side table, green artificial ivy plant hanging in the foreground, clear glass vase on a shelf.",
        "reflection": "The mirror itself shows the reflection of the subject and the room.",
        "text": "White text '{argument name=\"text overlay\" default=\"HIII\"}' overlaying the background near the chair."
      },
      "lighting": "Bright natural daylight from the windows."
    },
    "style": "Mirror selfie photograph.",
    "aspect_ratio": "2:3"
  }
}
```

---

## Modern Brands in 19th Century Prompt

A simple prompt for generating images that depict modern brand aesthetics transposed into a 19th-century setting or style.

```text
Modern brands in 19th century
```

---

## Modern Urban Editorial Portrait of a Man

An image generation prompt for an ultra-realistic indoor portrait of a stylish man walking confidently in a glass hallway with city views, emphasizing modern fashion details, natural daylight, and a c

```text
Ultra-realistic indoor portrait. Stylish man walking confidently down a bright glass hallway with city views. Clean fade, short beard, pearl beaded necklace. Oversized abstract shirt in {argument name="shirt colors" default="blue/beige/white/black"} with sketch-style figures; loose beige knee-length shorts with hanging strap details. White sneakers with beige/brown accents. Hands in pockets, relaxed posture. Natural daylight, crisp soft shadows on glossy floor, cool urban editorial vibe
```

---

## Monochrome Hypebeast Editorial with Airborne Action

A highly detailed JSON prompt for generating a cinematic, luxury hypebeast editorial image in strict monochrome. The prompt focuses on a single subject frozen in impossible, gravity-defying airborne p

```text
{
  "subject_gender_placeholder": "[CHOOSE: woman]",
  "aesthetic_lodestar": "cinematic luxury hypebeast editorial, strictly monochrome, shadowless stasis, deep rich blacks, single-frame photograph",
  "composition": {
    "frame": "minimalist controlled studio, clinical stark clarity, extremely dynamic camera angles capturing the action from aggressive low or high perspectives. No grid layouts, solitary subject focus.",
    "background": "pure, seamless, blown-out white infinite void, completely free of floor or wall shadows",
    "focus": "razor-sharp deep focus across the entire subject in motion"
  },
  "subject_action": {
    "pose": "impossible, gravity-defying airborne contortions and explosive mid-air leaps, frozen at the absolute peak of movement with extreme bodily tension",
    "energy": "maximum athletic tension meets high-fashion structure, controlled chaos suspended in time, creating sculptural, almost unbelievable silhouettes against the void"
  },
  "wardrobe_styling": {
    "vibe": "creative street fashion x avant-garde tailoring, non-provocative, clean and impactful silhouettes with varied layering",
    "garment_variations": [
      "Open cardigan sweaters layered over premium t-shirts",
      "Oversized knitwear and structured lounger sweaters",
      "Technical bomber jackets or varsity jackets",
      "Japanese minimalist silhouettes (unstructured, flowing, layered)",
      "Premium denim jackets and jeans styles",
      "Japanese Americana wear and styles",
      "Moncler puffer jackets",
      "Statement structured outerwear (as previously defined)"
    ],
    "brands_reference": ["Supreme", "Fear of God", "Maison Margiela", "Martine Rose", "UMBRO", "Aimé Leon Dore", "RHUDE", "Maison Kitsuné", "NikeLab", "Moncler", "Issey Miyake"],
    "accessories": {
      "general": "scarves, neck bandanas, paisley bandanas hanging from pockets (used sparingly when sensible)",
      "womens_specific": "Avant-Garde style bags, Saint Laurent structured totes or crossbodies, designer baseball caps, trucker caps, premium wool beanies (applied only if subject is woman)",
 "details": "only apply head gear objects on the subject's head, nowhere else"
    },
    "key_details": "focus on singular statement outfits without excessive bulk, oversized cuts contrasting with sharp tailoring, prominent branding, varied fabric weights rendered through pure texture without shadow"
  },
  "footwear_focus": {
    "models": ["Nike SB Dunk", "Off-White™ x Nike deconstructed models", "Converse Chuck 70 premium high-top", "Vans Vault Slip-On", “Adidas Samba”, “New Balance 327”, “ASICS Onitsuka Tiger Sneakers”],
    "details": "the only object on the subject's feet, highly visible and pristine, forming the anchor point of the dynamic motion"
  },
  "visual_color_treatment": {
    "base_spectrum": "pure, uncompromising black and white with ultra-deep, rich black tones",
    "blend_mode": "cohesive fusion of extreme textural"
  }
}
```

---

## MRE Package Design Prompt (Big Brands)

A conceptual prompt for generating package design mockups for a Meal, Ready-to-Eat (MRE) product, styled as if created by major consumer brands.

```text
Package design:
Meal, Ready-to-Eat, by big brands
```

---

## Multi-Style Sticker Pack Generator

A prompt for Nano Banana Pro to generate a 3x3 sticker pack based on an uploaded photo. The stickers feature the same person in various clothing and fashion styles (e.g., teacher, traditional, nurse u

```text
一个以上传照片为原型的3*3贴纸包，人物穿着不同服装和时尚风格。边缘干净裁剪，带有粗线条轮廓，姿势富有表现力，整体采用活泼的现代贴纸设计。在每个贴纸旁边采用中英文标注风格，所有贴纸保持相同的面部特征、一致的相似度和比例。
包含{argument name="clothing styles" default="教师装、传统、护士制服、街头潮牌和奇幻灵感"}等多种服装风格。高分辨率成品，带有柔和阴影和光泽贴纸纸张质感，适合社交分享。
```

---

## Multi-Subject Italian Aesthetic Portrait (Urdu/English)

A complex JSON prompt written primarily in Urdu (Romanized) for generating a scene featuring three subjects (Madison Beer, Sydney Sweeney, and Kendall Jenner) in Rome, Italy, near Ponte Sant'Angelo. T

```text
{
    "tasveer_id": 1,
    "shakhsiyat_naam": "{argument name="first subject name" default="Madison Beer"}",
    "pesha": "American Singer aur Songwriter",
    "location_details": {
      "shehar": "Rome",
      "mulk": "Italy",
      "maqam": "Ponte Sant'Angelo (Farishton wala pul)",
      "pas-e-manzar": "Castel Sant'Angelo ki tareekhi imarat aur neela aasman"
    },
    "fashion_details": {
      "dress_type": "Strapless Tiered Ruffle Mini Dress",
      "kapray_ka_rang": "Baby Pink / Pastel Pink",
      "bag_style": "Fendi Baguette (multitonal graphics ke saath)",
      "zaili_ashya": "Moti (pearl) ka haar aur sar par rakhi hui sunglasses"
    }
  },
  {
    "tasveer_id": 2,
    "shakhsiyat_naam": "{argument name="second subject name" default="Sydney Sweeney"}",
    "pesha": "American Actress (Euphoria fame)",
    "location_details": {
      "view": "Bridge ke darmiyan se qila saaf nazar aa raha hai",
      "mausam": "Khush-gawar aur dhoop wala din"
    },
    "fashion_details": {
      "pose": "Reling (balustrade) par hath rakh kar khari hain",
      "sunglasses": "Retro black oval shapes",
      "haath_ke_zewar": "Kayi rangon wale beaded bracelets"
    }
  },
  {
    "tasveer_id": 3,
    "shakhsiyat_naam": "{argument name="third subject name" default="Kendall Jenner"}",
    "pesha": "Fashion Model aur Media Personality",
    "location_details": {
      "angle": "Side view jahan farishte ka mujasma (angel statue) upar wazeh hai",
      "crowd": "Peechay sayahat karne wale log (tourists) nazar aa rahe hain"
    },
    "fashion_details": {
      "style_vibe": "Chic Summer Italian Aesthetic",
      "makeup": "Natural aur glowy look",
      "bag_position": "Neeche ki taraf pakra hua graphic printed mini bag"
    }
  }
```

---

## Multilingual Fashion Editorial Prompt for Ana de Armas

A complex, multi-image prompt written partially in Urdu/Hindi (romanized) and English, detailing three different fashion looks and settings for Ana de Armas in a European heritage site, focusing on ar

```text
"project_metadata": {
    "subject_identity": "Ana de Armas (Synthetic/AI Representation)",
    "setting_context": "European Heritage Site, likely Rome, Italy",
    "time_of_day": "Late Afternoon / Golden Hour",
    "overall_aesthetic": "High-end Fashion Editorial / Travel Blog",
    "total_images": 3
  },
  "detailed_analysis": [
    {
      "image_reference": "20260121_152344.jpg",
      "visual_narrative": "Subject terrace par ek pur-aitamaad (confident) mudra mein khari hain. Libaas ka rang aur material unke skin tone aur background ki historical vibe ke saath contrast paida kar raha hai.",
      "fashion_detailed": {
        "bodice": "Deep burgundy velvet corset, structural boning ke saath jo figure-hugging fit deta hai.",
        "skirt": "A-line black maxi skirt, breathable fabric, featuring dual frontal leg slits for movement.",
        "bag": "Structured brown leather tote, minimalist design, gold-tone hardware details.",
        "hair_and_makeup": "Soft voluminous waves, side-parted. Matte makeup palette with subtle rose-toned lipstick."
      },
      "architectural_background": {
        "structures": "Classical Italian domes (Cupolas), terracotta tiled roofs, stone balustrades with weathered texture.",
        "depth_of_field": "Shallow depth, background ko naram (soft blur) rakha gaya hai taake subject par focus rahe."
      }
    },
    {
      "image_reference": "20260121_150316.jpg",
      "visual_narrative": "Is frame mein tawajjo 'Simplicity and Elegance' par hai. Roshni seedha chehre par par rahi hai jo ek dewy look create kar rahi hai.",
      "fashion_detailed": {
        "dress_type": "Emerald green silk-satin slip dress, floor-length, spaghetti straps, plunging V-neckline.",
        "fabric_dynamics": "Satin fabric roshni ko reflect kar raha hai, jis se dress mein highlights aur shadows numayan ho rahi hain.",
        "accessories": "Wahi brown handbag jo pichli image mein tha, railing par rakha hua hai."
      },
      "environmental_cues": "Skyline mein naram neela aur safaid rang hai, jo purani imaraton ke ochre (yellow-brown) rangon ko balance kar raha hai."
    },
    {
      "image_reference": "20260121_150319.jpg",
      "visual_narrative": "Ek candid moment jahan subject muskurate hue side par dekh rahi hain, jo ek friendly aur approachable vibe deta hai.",
      "fashion_detailed": {
        "outfit": "Full-length floral chiffon gown. Base color cream/beige hai jis par rust-orange aur navy blue floral motifs hain.",
        "details": "Ruffled sleeves aur tiered skirt layerings, jo dress ko volume aur feminine touch dete hain.",
        "footwear": "Simple tan leather flat sandals, travel-friendly aur comfortable."
      },
      "composition_details": {
        "pose": "Seated on a stone balustrade, legs crossed slightly at the ankles.",
        "lighting": "Backlit effect, baalon ke kinaron par ek halki 'halo' roshni hai jo subject ko background"
      }
    }
  ]
```

---

## Nano Banana Character Sheet and Fashion Prompts

This tweet links to a collection of character sheets and fashion prompts specifically designed for use with Nano Banana Pro, suggesting users can freely use the provided prompts for generating images.

```text
Model-02 / Fashion: 004
```

---

## Nano Banana Pro Image Generation Capabilities

This tweet describes the capabilities of the 'Nano Banana Pro' feature within GlobalGPT, which focuses on generating high-quality images with enhanced control. It highlights the ability to create shar

```text
Fotos más nítidas y realistas con mejor iluminación
Ideal para {argument name="tipo de toma" default="retratos"}, {argument name="tipo de toma 2" default="productos"}, {argument name="tipo de toma 3" default="anuncios"} y tomas cinematográficas
```

---

## Nano Banana Pro Tutorial for Product Branding

This tweet announces a tutorial for the 'Nano Banana Pro' tool, focusing on how to brand any product in 10 seconds. The prompt and tutorial link are promised in the thread, but the prompt text itself

```text
Brand any product in 10 seconds
```

---

## Nano Banana Prompt for Minimalist Branded Bag Concept

A simple instruction prompt for Nano Banana to generate a minimalist concept design for a branded bag.

```text
Minimalist branded bag concept
```

---

## Nano Banana Prompt for Sport Jersey Design

A simple, direct prompt for the Nano Banana model, instructing it to generate an image of a sport jersey. The prompt is highly customizable, allowing the user to specify the brand and style of the jer

```text
Sport jersey by {argument name="brand" default="any brand"}
```

---

## Neon X-Ray Photorealistic Scan

Generates a photorealistic image of an object shown as a glowing X-ray scan.

```text
Neon X-Ray Photorealistic {argument name="object" default="[OBJECT]"} shown as glowing X-ray scan against pure black background. Internal structure visible in electric {argument name="color" default="[COLOR]"} neon wireframe, outer shell semi-transparent. Floating holographic labels pointing to key [COMPONENTS]. Cyberpunk medical scan aesthetic, ultra-sharp, dramatic glow effects.
```

---

## Night Sky Brand Canvas Prompt

A prompt designed to turn the night sky into a canvas for brand visualization, although the specific prompt text is mentioned to be in the comments (which are not provided here).

```text
Turn the night sky into the ultimate canvas for brands.
```

---

## Nighttime Street Scene with Two Women in Surprise Poses

A detailed JSON prompt for Nano Banana Pro to generate an image of two women—one blonde and one brunette—at night in a street/parking area setting, both exhibiting expressions of surprise or exclamati

```text
{
  "prompt": {
    "subjects": [
      {
        "name": "blonde_woman",
        "appearance": {
          "hair": "Long, platinum blonde, straight",
          "skin_tone": "Fair, lightly bronzed",
          "eyes": "Dark, wide open, detailed makeup",
          "lips": "Light pink, open wide in surprise or exclamation",
          "nose": "Defined, straight bridge",
          "cheeks": "Slightly flushed, contoured",
          "expression": "Open-mouthed surprise, looking upward and right"
        },
        "clothing": {
          "top": "Red bandeau tube top",
          "bottom": "Light blue denim shorts with white circular details"
        },
        "pose": "Standing behind other woman, hand on her back, leaning forward",
        "position": "Left side of frame"
      },
      {
        "name": "brunette_woman",
        "appearance": {
          "hair": "Long, dark brown, wavy",
          "skin_tone": "Medium olive",
          "eyes": "Dark, looking upwards",
          "lips": "Nude, slightly parted in a smile",
          "nose": "Defined, slight curve",
          "cheeks": "Defined cheekbones, contoured",
          "expression": "Looking upward with a slight smile"
        },
        "clothing": {
          "top": "Red ribbed crop top",
          "bottom": "Black denim shorts",
          "socks": "White socks with blue patterns"
        },
        "pose": "Bent over at the waist, looking up",
        "position": "Right side of frame"
      }
    ],
    "environment": {
      "time": "Night",
      "location": "Street, parking area",
      "lighting": "Artificial street and car lights",
      "background_objects": [
        "White sedan (partial, left)",
        "Grey sedan (right, behind brunette)",
        "Red octagonal 'STOP' sign on post",
        "Green rectangular street sign above STOP sign",
        "Palm trees in background",
        "Asphalt pavement"
      ]
    },
    "aspect_ratio": "4:5"
  }
}
```

---

## Off-White × Balenciaga Hypebeast Editorial

A structured prompt for generating an avant-garde hypebeast editorial image featuring a young woman wearing an exaggerated, intentionally oversized Off-White x Balenciaga collaborative jacket, focusin

```text
{
  "title": "Off-White × Balenciaga — Scale Error",
  "prompt": {
    "subject": {
      "description": "Young woman wearing an Off-White x Balenciaga collaborative jacket with exaggerated proportions for a hypebeast campaign",
      "age": "early 20s",
      "ethnicity": "Eastern European",

      "expression": {
        "overall": "cold, dominant, untouchable"
      },

      "clothing": {
        "jacket": {
          "type": "extreme oversized parka",
          "color": "{argument name="jacket color" default="off-white with black accents"}",
          "fit": "intentionally oversized, sculptural",
          "details": {
            "collab_design_language": [
              "Balenciaga exaggerated silhouette annotated with Off-White measurement text",
              "oversized hardware treated as design elements"
            ],
            "branding": [
              "Balenciaga logo stretched and partially obscured",
              "Off-White arrows wrapping around garment volume"
            ]
          }
        },
        "top": {
          "type": "oversized heavyweight tee",
          "color": "washed charcoal",
          "details": {
            "design": "minimal Balenciaga typography disrupted by Off-White graphics",
            "fit": "boxy, exaggerated street cut"
          }
        }
      }
    },

    "photography": {
      "resolution": "8K",
      "style": "avant-garde hypebeast editorial"
    }
  }
}
```

---

## Off-White × Timberland Industrial Work Alpine Parka Editorial Prompt

A detailed JSON-formatted prompt designed for an image generation model (Gemini Nano Banana Pro) to create a rugged, hypebeast alpine editorial image. The subject is a young woman wearing a conceptual

```text
{
  "title": "Off-White × Timberland — Industrial Work Alpine",
  "prompt": {
    "subject": {
      "description": "Young woman wearing an Off-White x Timberland alpine parka merging workwear and conceptual streetwear",
      "age": "early 20s",
      "ethnicity": "white with olive undertones",

      "expression": {
        "overall": "grounded, intimidating calm"
      },

      "clothing": {
        "jacket": {
          "type": "heavy utility ski parka",
          "color": "{argument name="jacket color" default="off-white"}",
          "fit": "boxy industrial silhouette",
          "details": {
            "collab_design_language": [
              "Timberland-style reinforced work seams exaggerated and labeled",
              "Off-White printed measurement markings along sleeve panels"
            ],
            "branding": [
              "co-branded rubberized chest patch combining Timberland tree + Off-White arrows",
              "industrial Off-White text printed inside hood lining"
            ],
            "material": "thick rugged technical fabric with visible wear texture"
          }
        },
        "base_layer": {
          "type": "minimal bikini top",
          "color": "{argument name="base layer color" default="khaki"}"
        }
      }
    },

    "photography": {
      "resolution": "8K",
      "style": "{argument name="photography style" default="rugged hypebeast alpine editorial"}"
    }
  }
}
```

---

## Old Money Aesthetic: Woman in LBD on Grand Staircase

A detailed prompt for generating a photorealistic image in the 'Old Money' or Parisian chic aesthetic. It features a slender woman in a little black dress, sheer opera gloves, and pearl jewelry, posin

```text
{
  "image_analysis_prompt": {
    "subject": {
      "demographics": "Young woman, slender build, light skin tone",
      "hair": "Dark brunette, styled in a sleek, tight low bun with a middle part",
      "expression": "Neutral, elegant, looking off-camera to her right"
    },
    "apparel": {
      "dress": "Little black dress (LBD), mini length, sleeveless straps, sweetheart neckline, fitted bodice with a flared skater-style skirt",
      "legwear": "Sheer black tights (pantyhose)",
      "footwear": "Black patent pointed-toe heels with gold hardware accents",
      "gloves": "Sheer black opera-length gloves"
    },
    "accessories": {
      "jewelry": [
        "Single-strand pearl choker necklace",
        "Large pearl stud earrings"
      ],
      "handbag": "Small, black quilted leather handbag (reminiscent of Chanel) held in the right hand"
    },
    "pose_and_action": {
      "stance": "Standing on a staircase landing, legs crossed at the ankles",
      "hands": "Right hand resting on the banister holding the bag, left hand gently lifting the edge of the dress skirt",
      "orientation": "Body facing forward, head turned in profile to the left"
    },
    "environment": {
      "location": "Grand interior staircase (possibly a hotel or chateau)",
      "architectural_details": [
        "Curved cream stone walls",
        "Ornate black wrought-iron railing with elaborate gold leaf scrollwork",
        "Polished gold handrail",
        "Red and beige patterned stair runner carpet"
      ],
      "background_decor": [
        "Classic oil painting in a gold frame hanging on the upper wall",
        "Antique wooden chest/commode visible on the upper landing",
        "Brass wall sconce with candle-style bulbs"
      ]
    },
    "lighting_and_style": {
      "lighting": "Warm, soft indoor artificial lighting creating gentle shadows",
      "aesthetic": "Old Money, Parisian chic, luxury, formal, elegant, high-class fashion"
    }
  }
}
```

---

## Olive Oil Social Media Feed Generation Prompt

A simple text prompt used in 'studio mode' to generate a complete social media feed for a small-batch olive oil brand, resulting in hyper-realistic product shots with perfect typography.

```text
Create a social media feed for this small-batch olive oil brand.
```

---

## Olive Oil Social Media Feed Generation Prompt (Duplicate)

A simple text prompt used in 'studio mode' to generate a complete social media feed for a small-batch olive oil brand, resulting in hyper-realistic product shots with perfect typography. This is a dup

```text
Create a social media feed for this small-batch olive oil brand.
```

---

## Optimize E-commerce Listing for High CTR with Holiday Design

Optimizes product and e-commerce strategies for optimize e-commerce listing for high ctr with holiday design.

```text
Act as an E-commerce Listing Optimization Specialist. You are an expert in creating high-conversion product listings with a focus on visual appeal and strategic content placement.

Your task is to optimize the listing for a ${productType:white women's medical suit} with a ${theme:New Year} design to achieve a high ${metric:CTR} (Click-Through Rate).

You will:
- Design an eye-catching main image incorporating ${theme} elements.
- Write compelling product titles and descriptions that highlight unique features and benefits.
- Utilize keywords effectively for improved search visibility.
- Suggest additional images that showcase the product in various settings.
- Provide tips for engaging with potential customers through description and visuals.

Rules:
- Ensure all content is relevant to the ${platform:e-commerce platform}.
- Maintain a professional yet appealing tone throughout the listing.
- Adhere to all platform-specific guidelines for product imagery and descriptions.
```

---

## OS2.0 SAFe Delivery Context (Master)

Optimizes product and e-commerce strategies for os2.0 safe delivery context (master).

```text
I serve as the Chief Solution / Release Train Architect working in a SAFe Agile delivery program.

The program consists of 4 Agile delivery teams, operates on PI Planning, and delivers through Planning Intervals (PIs).

Work items are structured into three hierarchical levels:

Epic: Strategic initiatives delivering significant business or architectural value, which could span multiple PIs, and are broken into Features.

Feature: Cohesive groupings of system functionality aligned to business or functional domains, typically deliverable within a PI.

User Story: Atomic, executable units of work representing the smallest meaningful product transformation. Each user story is either completed or cancelled and has an execution mode: Manual, Interactive, or Automated.

Responses should follow SAFe principles, respect this hierarchy, and maintain clear separation between strategic intent, functional capability, and execution detail.
```

---

## Outfit combinations using Sergey Brin as model

A follow-up prompt requesting the AI to mix and match the previously generated clothing items into outfits, using Sergey Brin as the model.

```text
Now mix and match them to show me combinations of what outfits I can create, use Sergey Brin as the model
```

---

## Outfit Style Edit: Santa-Inspired Dress

A prompt used for editing an existing image, instructing Nano Banana Pro to change a woman's outfit from a blazer/skirt to a longer, pleated Santa-inspired dress with a black belt and a large red bow

```text
"Change her outfit style: replace the blazer and short skirt with a slightly longer Santa-inspired dress that has a pleated bottom, in classic Christmas colors (red with white accents). Add a black belt with a large buckle. Instead of the Santa hat, add a large red bow on top of her head. Keep the same pose and all other elements unchanged."
```

---

## Overhead Romantic Fashion Editorial in Flower Field

Creates an overhead fashion editorial photograph of a woman lying in a dense field of hot-pink flowers.

```text
{
  "generation_request": {
    "meta_data": {
      "task_type": "photoreal_fashion_editorial_flower_field_overhead",
      "language": "en",
      "priority": "highest",
      "version": "v1.0_PINK_DRESS_FLOWER_BED_HEART_BAG"
    },
    "output": {
      "aspect_ratio": "4:5",
      "resolution": "ultra_high",
      "num_images": 4,
      "sharpness": "high",
      "grain": "subtle_analog"
    },
    "scene": {
      "concept": "overhead romantic fashion editorial of a woman lying in a dense flower bed",
      "environment": "lush ground cover packed with small hot-pink blossoms and green leaves, hints of purple flowers in corners, full-frame botanical texture",
      "composition": "top-down overhead shot, full-body diagonal pose, subject centered, floral carpet filling entire background, basket of pink flowers near chest/shoulder",
      "mood": "spring romance, dreamy, joyful, vibrant"
    },
    "subject": {
      "person": "adult woman",
      "expression": "bright joyful smile, relaxed eyes, confident and warm",
      "pose": "lying on her back in the flowers, one leg bent slightly, arms hugging a wicker basket of flowers close to the chest",
      "hair": "dark brown hair, styled neatly with soft volume, swept back from face",
      "makeup": "fresh glam: soft blush, glossy pink lips, subtle highlight, defined lashes",
      "wardrobe": {
        "dress": "light pink off-shoulder mini dress with a large bow detail on the bodice, structured waist, soft skirt folds, crisp fabric texture and highlights"
      },
      "shoes": "light pastel heels or sandals, elegant and minimal",
      "accessories": "delicate ring on finger, minimal jewelry"
    },
    "props": {
      "basket": "wicker basket overflowing with pink flowers (carnations/roses mix), placed near the subject's upper torso",
      "handbag": "transparent pink heart-shaped clutch placed on top of the flowers in the basket, glossy plastic texture with realistic reflections"
    },
    "camera": {
      "shot_type": "overhead fashion editorial",
      "lens": "35mm",
      "aperture": "f/4",
      "focus": "subject face and dress sharp, flowers crisp with slight natural falloff",
      "framing": "4:5 vertical, full-body top-down"
    },
    "lighting": {
      "time_of_day": "golden hour or late afternoon",
      "key_light": "strong warm sunlight with natural leaf shadows across the scene",
      "contrast": "medium-high with crisp sunlit highlights on skin and dress",
      "skin_tone": "realistic, warm glow, visible natural texture"
    },
    "color_grading": {
      "palette": "hot pink flowers + fresh greens + pastel pink dress",
      "look": "bright editorial, clean whites, punchy florals, warm sun tone",
      "contrast": "medium-high",
      "saturation": "vivid but controlled (no neon clipping)"
    },
    "quality_rules": {
      "anatomy_accuracy": "strict",
      "hands": "correct fingers, natural joints, no extra digits"
    }
  }
}
```

---

## Parisian Luxury Fashion Ad at Golden Hour

A natural language prompt for generating a luxury fashion advertisement image. It describes a young Caucasian woman with ethereal beauty sitting at a Parisian cafe, wearing a cream-colored tailored po

```text
Luxury fashion advertisement, blog post, 4:5 ratio.

COMPOSITION:
A young Caucasian woman in her early 20s with slim oval face and V-line jawline, seated elegantly at a Parisian cafe. She has long flowing wavy light brown hair with golden caramel highlights cascading over her shoulders. Large bright blue-green doe eyes with long natural lashes, luminous dewy porcelain skin with healthy glow and glass skin effect, soft rosy blush on cheeks, glossy pink lips with radiant subtle smile, slim straight nose, delicate feminine features, ethereal doll-like beauty.

She wears a {argument name="suit color" default="cream-colored"} tailored power suit with elegant draping, paired with a delicate layered gold necklace. A designer handbag rests on the marble cafe table beside a steaming cup of coffee.

DYNAMIC ELEMENTS:
Subtle motion blur as she turns her head slightly with gentle head tilt, soft dreamy expression, steam rising from the coffee cup creating warmth and atmosphere.

CAMERA: Hasselblad X2D, 85mm f/1.4 lens, soft diffused golden hour lighting, shallow depth of field, beauty retouching with luminous skin detail.

Style keywords: Parisian elegance, power dressing, luxury fashion, ethereal Caucasian beauty, golden hour, warm cream and soft gold tones, high-end fashion editorial.

A stylish handwritten signature "Willy" is elegantly placed in small letters at the Bottom Right corner.
```

---

## Personal Shopper

Acts as my personal shopper to help with personal shopper-related tasks.

```text
I want you to act as my personal shopper. I will tell you my budget and preferences, and you will suggest items for me to purchase. You should only reply with the items you recommend, and nothing else. Do not write explanations. My first request is "I have a budget of $100 and I am looking for a new dress."
```

---

## Photo to Product Packaging Dieline Prompt

A concise prompt for the Nano Banana tool to convert a photo into a product packaging dieline, suggesting a workflow for design and manufacturing preparation.

```text
Photo to product packaging dieline
```

---

## Photorealistic Portrait of Zhao Lusi (Rosy Zhao) with Cottagecore Vibe

A highly structured JSON prompt for generating a vertical, hyper-reflective portrait of actress Zhao Lusi, emphasizing a 'clean girl' makeup look, a vibrant floral dress, and a fresh, approachable 'gi

```text
{
"subject": {
"name": "Zhao Lusi",
"alias": "Rosy Zhao",
"appearance": {
"expression": "smiling warmly, waving toward the camera/fans",
"hairstyle": "loose, romantic side-braid with delicate butterfly clips",
"makeup": {
"style": "clean girl",
"details": {
"skin": "dewy, hyper-reflective, glass-skin finish",
"lips": "soft coral-pink",
"eyes": "natural, light makeup emphasizing features"
}
}
}
},
"fashion": {
"dress": {
"type": "off-the-shoulder mini dress",
"pattern": "vibrant green floral print",
"silhouette": "flowy, babydoll with draped sleeves",
"vibe": "fresh, summery, cottagecore"
},
"accessories": {
"phone_case": "lavender/light pink"
}
},
"setting": {
"location": "stepping out of a dark-colored luxury van",
"lighting": "natural, bright, highlights airy fabric and radiant expression"
},
"overall_vibe": "fresh, elegant, approachable, girl-next-door charm",
"skin_face_glow": {
"finish": "dewy, hyper-reflective",
"highlight": "smooth highlights, luminous facial contours",
"tone": "warm skin tone enhancement"
},
"image_dimensions": {
"width": 504,
"height": 1002,
"orientation": "vertical"
},
"context": {
"notable_roles": ["Hidden Love", "The Love You Give Me"],
"signature_aesthetic": "sweetheart"
}
}
```

---

## Photorealistic Volleyball Player Pose

A highly detailed JSON prompt for generating a photorealistic image of a young female volleyball player in a specific prone pose, propped up on her elbows with a Spalding volleyball balanced between h

```text
{
  "subject_details": {
    "demographics": {
      "age": 19,
      "gender": "female",
      "ethnicity": "Caucasian/White"
    },
    "hair": {
      "color": "light blonde with subtle darker roots",
      "style": "long, loose beach waves",
      "length": "extends past shoulders to mid-back",
      "parting": "center part",
      "texture": "soft, fine strands framing the face"
    },
    "skin": {
      "tone": "fair/light with warm undertones",
      "texture": "smooth, natural",
      "complexion": "slight natural sheen on forehead and nose bridge",
      "blemishes": "very faint, natural freckling across nose and cheeks"
    },
    "facial_features": {
      "face_shape": "oval with soft chin structure",
      "eyes": {
        "color": "dark brown",
        "shape": "almond, slightly downturned",
        "eyelashes": "natural length, lightly mascaraed",
        "eyebrows": "medium thickness, arched, light brown/dark blonde"
      },
      "nose": {
        "shape": "straight bridge, slightly rounded tip (button nose)",
        "width": "average/proportional"
      },
      "lips": {
        "shape": "full, cupid's bow defined",
        "color": "natural pale pink/nude",
        "finish": "matte to satin"
      },
      "cheeks": {
        "prominence": "soft apples",
        "color": "subtle peach/pink flush"
      },
      "expression": {
        "mood": "calm, approachable, confident",
        "mouth": "closed, slight smirk or subtle smile",
        "gaze": "direct contact with camera"
      }
    },
    "body": {
      "pose": "lying prone (on stomach) on floor, upper body propped up on elbows",
      "legs": "knees bent at 90-degree angle, feet raised in the air",
      "hands": "clasped loosely in front on the floor, fingers interlaced",
      "fingernails": "short, manicured, painted white",
      "jewelry": "thin silver ring on left ring finger"
    }
  },
  "attire_and_accessories": {
    "top": {
      "garment": "long-sleeve volleyball jersey",
      "color": "white base",
      "graphics": {
        "chest": "Partial blue letter 'A' visible (likely 'BEAR' or similar team name)",
        "sleeves": "Two horizontal stripes on upper arm (one royal blue, one yellow/gold)",
        "wrist_cuff": "Blue text visible near left wrist cuff (upside down)"
      },
      "fit": "loose athletic fit"
    },
    "bottoms": {
      "garment": "spandex volleyball shorts",
      "color": "royal blue",
      "fit": "skin-tight"
    },
    "footwear": {
      "shoes": "white athletic sneakers (court shoes)",
      "soles": "white with visible grey Under Armour logo on sole",
      "socks": "white crew socks, slightly scrunched"
    },
    "props": {
      "volleyball": {
        "brand": "Spalding",
        "model_text": "TF-VB5",
        "colors": "Navy blue, white, and silver panels",
        "location": "balanced securely between the soles of h"
      }
    }
  }
}
```

---

## Physicist relaxing in a hammock with SPA drink

Generates a scene of a physicist’s legs on a hammock with a drink and spa setting, surrounded only by trees and vegetation, ideal for relaxed conceptual imagery.

```text
Physicist on a hammock, with a glass and an S.P.A. Only legs, without shoes and trees and vegetation are shown.
```

---

## Premium Advertising Photo of Levitation Bottles

A prompt for creating a dynamic, premium advertising image featuring two matte product bottles levitating in a balanced diagonal composition. The bottles are wrapped with a branded satin ribbon, shot

```text
A product photo in a premium advertising style. Two tall matte bottles of Salton Shoe Deodorant levitate in the air in a dynamic, balanced composition.
The bottles are positioned at an angle to each other, creating a striking diagonal composition. One bottle is slightly forward, the other is slightly behind, creating depth and hierarchy. Both bottles are elegantly wrapped with a wide black and brown satin ribbon featuring the repeating "Salton" branding. The lettering is executed in a neat, contrasting font, legible without distortion, and is repeated evenly along the entire length of the ribbon. The ribbon flows smoothly between the bottles, uniting them into a single composition, without obscuring key messages on the packaging or clashing with the main branding on the bottles. Shot from a slightly lower angle, the bottles are slightly tilted, enhancing a sense of confidence, strength, and premium quality. The background is a solid studio color, a deep warm shade (chocolate, dark caramel or soft terracotta), clean and minimalist, without distracting details.
```

---

## Premium Beverage Package Design Prompt

A simple, high-level prompt intended for generating premium packaging designs for beverages, with the full detailed prompt likely available via the external link provided.

```text
Premium beverage package design
```

---

## Premium Dark Horizon Product Reveal Prompt

A high-level prompt suggesting the generation of a product reveal image with a 'Premium Dark Horizon' aesthetic, likely involving sleek design, dark colors, and dramatic lighting.

```text
Premium Dark Horizon Product Reveal
```

---

## Premium Liquid Glass Bento Grid Product Infographic

Creates a premium liquid glass Bento grid product infographic with 8 modules for any product.

```text
Input Variable: [insert product name]
Language: [insert language]

System Instruction:
Create an image of premium liquid glass Bento grid product infographic with 8 modules (card 2 to 8 show text titles only).
1) Product Analysis:
→ Identify product's dominant natural color → "hero color"
→ Identify category: FOOD / MEDICINE / TECH
2) Color Palette (derived from hero):
→ Product + accents: full saturation hero color
→ Icons, borders: muted hero (30-40% saturation, never black)
3) Visual Style:
→ Hero product: real photography (authentic, premium), 3D Glass version [choose one]
→ Cards: Apple liquid glass (85-90% transparent) with Whisper-thin borders and Subtle drop shadow for floating depth and reflecting the background color
→ Background stays behind cards and high blur where cards are [choose one]:
  - Ethereal: product essence, light caustics, abstract glow
  - Macro: product texture close-up, heavily blurred
  - Pattern: product repeated softly at 10-15% opacity
  - Context: relevant environment, blurred + desaturated
→ Add subtle motion effect
→ Asymmetric Bento grid, 16:9 landscape
→ Hero card: 28-30% | Info modules: 70-72%
4) Module Content (8 Cards):
M1 — Hero: Product displayed as real photo / 3D glass / stylized interpretation (choose one)in beautiful form + product name label
M2 — Core Benefits: 4 unique benefits + hero-color icons
M3 — How to Use: 4 usage methods + icons
M4 — Key Metrics: 5 EXACT data points
Format: [icon] [Label] [Bold Value] [Unit]
FOOD: Calories: [X] kcal/100g, Carbs: [X]g (fiber [X]g, sugar [X]g), Protein: [X]g, [Key Vitamin]: [X]mg ([X]% DV), [Key Mineral]: [X]mg ([X]% DV)
MEDICINE:Active: [name], Strength: [X] mg, Onset: [X] min, Duration: [X] hrs, Half-life: [X] hrs 
TECH:Chip: [model], Battery: [X] hrs, Weight: [X]g,[Key spec]: [value], Connectivity: [protocols]
M5 — Who It's For: 4 recommended groups with green checkmark icons | 3 caution groups with amber warning icons
M6 — Important Notes: 4 precautions + warning icons
M7 — Quick Reference:
→ FOOD: Glycemic Index + dietary tags with icons
→ MEDICINE: Side effects + severity with icons
→ TECH: Compatibility + certifications with icons
M8 — Did You Know: 3 facts (origin, science, global stat) + icons
Output: 1 image, 16:9 landscape, ultra-premium liquid glass infographic.
```

---

## Premium Studio Product Photo of Sparkling Water Can

A detailed prompt for generating a premium studio photograph of a red aluminum sparkling water can. The focus is on condensation, crisp typography, and surrounding the product with fresh strawberries,

```text
A premium studio product photograph of a tall, slim red aluminum sparkling water can standing upright and centered against a seamless vivid red background, the can covered in fine condensation droplets with crisp white typography reading “{argument name="text" default="GOOD IDEA"}” and smaller flavor text beneath, positioned on a matte red surface with subtle reflections, surrounded symmetrically by fresh ripe strawberries with glossy seeds and deep red flesh, some resting directly on the surface and others.
```

---

## Premium Studio Shot of Blueberry Mint Iced Drink

Creates ultra-realistic commercial product photograph of a blueberry mint iced drink.

```text
Blueberry Mint Iced Drink – Premium Studio Shot. Tall clear highball glass filled with blue blueberry mint soda. Vibrant gradient blue drink deep blue at bottom fading to clear at top. Large crystal-clear ice cubes. Fresh mint leaves inside and on top, whole blueberries inside the drink. Light wooden straw angled inside the glass. Soft misty vapor rising from top, tiny bubbles in liquid, water droplets on glass. Dark navy to black gradient backdrop, glossy black reflective surface. Professional studio lighting, soft diffused key light from left, cool rim light from right.
```

---

## Product Ingredient Labeling Prompt

A tweet promoting a prompt designed to 'explode any product into labeled ingredients in seconds,' suggesting a utility for quick product analysis or visualization.

```text
One prompt to explode any product into labeled ingredients in seconds
```

---

## Product Manager

Optimizes product and e-commerce strategies for product manager.

```text
Please acknowledge my following request. Please respond to me as a product manager. I will ask for subject, and you will help me writing a PRD for it with these heders: Subject, Introduction, Problem Statement, Goals and Objectives, User Stories, Technical requirements, Benefits, KPIs, Development Risks, Conclusion. Do not write any PRD until I ask for one on a specific subject, feature pr development.
```

---

## Product photo with item placed on a stone

A simple product photography prompt placing the subject neatly on top of a stone for clean, minimalistic 4K product shots.

```text
place the product on top of the stone
```

---

## Product Photography Poster with Liquid Splash and Text Overlays

A prompt designed for generating a vertical poster image for a juice bottle, focusing on high-detail product photography. It requires the exact uploaded bottle image, adds dynamic elements like a liqu

```text
Exact uploaded [BOTTLE_NAME] bottle (label unchanged). Vertical poster. Center bottle w/ condensation. Add {argument name="juice color" default="JUICE_COLOR"} liquid splash wrap + ice cubes + {argument name="ingredients" default="INGREDIENTS"} floating (controlled). Background: {argument name="background color" default="BG_COLOR"} gradient + vignette + grain.
Top-left: “FRESH JUICE” + “[FLAVOR_TAGLINE]”. Right: circular “30% OFF” ring. Lower-right: price circle “[PRICE]”. Bottom-right CTA “[CTA]”. White doodle arrows. Studio key+rim, 85mm, sharp text, no watermark.
```

---

## Product Promotion Expert

Optimizes product and e-commerce strategies for product promotion expert.

```text
Act as a Product Promotion Expert. You are responsible for creating engaging and persuasive product information for marketing purposes.

Your task is to write promotional content for a product based on the following input details:
- Product Name: {{ $json['商品名称'] }}
- Product Reference Image: {{ $json['商品参考图'] }}
- Promotion Scenario: {{ $json['推广场景'] }}

You will:
- Develop a captivating product description.
- Highlight key features and benefits.
- Tailor the content to the specified promotion scenario.

Rules:
- Ensure the content is clear and appealing.
- Use persuasive language to attract the target audience.
```

---

## Prompt for Generating 'Hot White Girl in Prom Dress' (Failure Case)

A prompt mentioned in a discussion about the model's tendency towards 'correctness' and difficulty generating certain types of images, specifically a 'hot white girl in a prom dress.' This is presente

```text
hot white girl in prom dress
```

---

## Prompt for Visual Storyboard Creation

A call to action for users to receive a prompt designed to create a brand visual storyboard for product presentation using Nano Banana Pro, often shared upon request.

```text
Create a brand visual storyboard for presenting your product with Nano Banana Pro:
```

---

## Provocative Villa Pool Pose Portrait

A structured prompt for Gemini Nano Banana Pro to generate a seductive, sunlit portrait of a young woman posing in a yellow striped string bikini at the edge of a luxurious villa pool. The prompt spec

```text
{
  "subject": "A young woman in a bikini posing at the edge of a private villa pool",
  "appearance": {
    "hair": "long straight brown hair in a side braid, partially wet",
    "headwear": "{argument name="cap color" default="yellow"} snapback cap worn backwards",
    "body": "light brown skin, curvy figure with prominent hips and buttocks, small tattoos on forearm and hip",
    "face": "profile view, looking away from camera"
  },
  "clothing": {
    "swimwear": "{argument name="bikini color" default="yellow"} striped string bikini with thin side ties, push-up top details, cheeky bottom cut"
  },
  "pose": "on all fours at pool edge, knees in shallow water, torso leaning forward, one hand on tiled ledge, looking to the side",
  "setting": "outdoor luxurious villa pool with mosaic tiles, exotic flowers, cabanas, bright sunny day",
  "lighting": "bright natural sunlight, clear blue sky",
  "style": "provocative villa pool pose, playful and seductive vibe"
}
```

---

## Quad-Pose Studio Lookbook Grid

Creates a four-panel studio fashion lookbook grid with identity preservation from a reference image.

```text
{
  "generation_request": {
    "meta_data": {
      "task_type": "studio_fashion_editorial_lookbook_quad_pose",
      "language": "en",
      "priority": "highest",
      "version": "v1.1_IVORY_CHIFFON_HALTER_LOOKBOOK_GRID_FACE_MATCH"
    },
    "input": {
      "mode": "image_to_image",
      "reference_image_usage": "high",
      "preserve_identity": true,
      "preserve_facial_features": true,
      "notes": "Use the provided reference image as the facial identity anchor. The model's FACE must closely match the reference (very similar). Keep the overall lookbook grid style and studio setup. Do NOT change the person into someone else."
    },
    "output": {
      "aspect_ratio": "2:3",
      "resolution": "ultra_high",
      "num_images": 1,
      "layout": {
        "type": "grid",
        "rows": 2,
        "cols": 2,
        "gutter": "thin"
      },
      "sharpness": "high",
      "grain": "subtle_analog"
    },
    "scene": {
      "concept": "minimal studio lookbook collage with soft editorial light",
      "environment": "clean off-white studio wall backdrop, seamless floor, neutral studio setting, no clutter",
      "mood": "elegant, airy, understated, high-end boutique lookbook"
    },
    "subject": {
      "person": "adult woman",
      "identity_consistency": "model across all panels",
      "face_match": "very_high lips",
      "expression": "calm, slightly sultry, neutral editorial gaze",
      "hair": "long dark hair, soft waves, center part (similar to reference), tidy and glossy; allow subtle variation but keep overall match",
      "makeup": "soft neutral glam, defined eyeliner, natural nude lips (match reference makeup vibe)",
      "accessories": "small gold hoop earrings, delicate rings/bracelet",
      "wardrobe": {
        "dress": "ivory / champagne chiffon halter mini dress with high neck band, airy layered bubble hem, semi-sheer flowing fabric, open back with long scarf-like tie draping down"
      },
      "shoes": "minimal strappy heels or sandals in nude/ivory"
    },
    "poses_grid": {
      "panel_1_top_left": "front 3/4 pose, one arm bent with hand resting near neck, relaxed posture",
      "panel_2_top_right": "side profile pose, holding a small ivory woven clutch, looking off-camera",
      "panel_3_bottom_left": "back view showcasing open back and long tie drape, head turned slightly to show profile",
      "panel_4_bottom_right": "front pose with one hand behind head, subtle contrapposto, gaze to the side"
    },
    "camera": {
      "shot_type": "lookbook / editorial",
      "lens": "50mm",
      "aperture": "f/3.2",
      "focus": "tack sharp on face and garment texture, consistent exposure across panels",
      "framing": "full-body to 3/4 body depending on panel, consistent scale"
    },
    "lighting": {
      "setup": "soft key light from camera-left, gentle fill from right, minimal shadow hardness",
      "look": "clean studio editorial, no harsh flash"
    }
  }
}
```

---

## Quiet Luxury Editorial Fashion Template

A detailed prompt for creating a luxury editorial fashion image focusing on a Persian female model. The aesthetic emphasizes quiet luxury, soft diffused lighting, neutral color palettes, and a Vogue e

```text
Single hero editorial fashion aesthetic,
3:4 vertical ratio.
LAYOUT: Full-bleed editorial hero
COMPOSITION:
- Subject: Persian female model, luxury designer pieces, polished hair/makeup, confident pose
- Position: Center-right with left text zone
- Style: Confident, relaxed, editorial aesthetic
SUBJECT STYLING:
- Luxury designer pieces, premium fashion
- Polished hair/makeup, confident pose
- Statement jewelry piece
BACKGROUND:
- Type: Subtle gradient
- Color: Neutral tones (cream, warm gray)
- Treatment: Clean, non-distracting
LIGHTING:
- Style: Soft, diffused beauty lighting
- Main: Large softbox, frontal
- Fill: Reflector for shadow detail
- Quality: Premium fashion photography
COLOR PALETTE:
- Quiet luxury aesthetic
- Gold/brass accent elements
- Low saturation, sophisticated
TEXT OVERLAY:
- Brand name: Elegant serif, upper-left corner
- Headline/Collection: Left-side vertical stack
- Tagline: Below headline, bilingual (KR/EN)
- CTA: Bottom-right
MOOD: Sophisticated, aspirational, premium,
quiet luxury, editorial fashion
STYLE: Vogue editorial aesthetic,
Hasselblad medium format, 80mm f/2.8,
natural window light + fill
Keywords: editorial hero, fashion aesthetic campaign,
luxury photography, editorial portrait,
brand lookbook, premium advertising,
quiet luxury, sophisticated style.
```

---

## Quiet Luxury Office Lady Lookbook Prompts (3 Variations)

A set of three highly structured prompts for Nano Banana Pro designed to generate fashion lookbook images for 'Quiet Luxury' or 'Old Money' style office wear. Each prompt specifies the model (young Da

```text
主体 (Subject): 年轻Danmark丹麦女性，金色长卷发，妆容自然清透，气质优雅、知性。

服装 (Outfit): 核心是“静奢风 (Quiet Luxury)”或“老钱风”。

色调: pantone 15-4504TCX/ Nacreous Clouds 低饱和度。

材质: 亚麻或亚麻混纺 (Linen blend)，有自然的褶皱纹理。

款式: 三件套——廓形西装外套 (Blazer) + 同色系吊带内搭 (Camisole) + 裹身半身长裙 (Wrap midi skirt)。

配饰 (Accessories): 棕色手提包 (卡其色/焦糖色)，金色细项链，丝巾（在平铺图中）。

构图与风格 (Composition & Style):

时尚杂志排版 (Magazine Layout / Collage)。

多视角展示：主图是七分身，侧边有全身照、背影细节、局部特写。

背景：干净的摄影棚白底/灰底 (Clean studio background)。

文字：极简主义排版 (Minimalist typography)。

==============================

主体 (Subject): 年轻Danmark丹麦女性，红棕色长卷发，妆容自然清透，气质优雅、知性。

服装 (Outfit): 核心是“静奢风 (Quiet Luxury)”或“老钱风”。

色调: Pantone 18-1018TCX/ Otter 低饱和度。

材质: 亚麻或亚麻混纺 (Linen blend)，有自然的褶皱纹理。

上装: linen blazer, asymmetric closure, tailored fit (亚麻西装，不对称闭合，剪裁合身).

下装: pleated wide-leg pants (褶皱阔腿裤).

配饰: Brown square-toe flats, mini leather top-handle bag (棕色方头平底鞋，迷你手提皮包).

构图与风格 (Composition & Style): 时尚杂志排版 (Magazine Layout / Collage)。

多视角展示：主图是七分身，侧边有全身照、背影细节、局部特写。

背景：干净的摄影棚白底/灰底 (Clean studio background)。

文字：极简主义排版 (Minimalist typography)。

=====================================

这是一个典型的**时尚型录（Lookbook）**或电商详情页排版。

主图： 左侧占据大面积的是模特的半身/七分身展示。

辅图： 右侧垂直排列三张小图，分别、全身远景、背面视角、服装平铺展示。

静物： 右下角有配饰的平铺展示（包、丝巾、耳环）。

文字： 上下留白处有简约的排版文字（品牌名、季节、Slogan）。

主体 (Subject): 年轻Danmark丹麦女性，金色长发，妆容自然清透，气质优雅、知性。

服装 (Outfit): 老钱风（Old Money）、静奢风（Quiet Luxury）、极简主义（Minimalism)

色调: Pantone 15-1116 TCX/ Safari 低饱和度。

材质: 亚麻或亚麻混纺 (Linen blend)，有自然的褶皱纹理。

外套：无领西装外套/开衫，剪裁利落，亚麻质感。

内搭：炭灰色丝绸/缎面 V领衬衫。

下装： 西装裤。
```

---

## Random Strange Product Grid Generator

A simple prompt template designed to generate a 2x2 grid of random, strange products from a specified year and style, with text labels underneath describing what they are.

```text
2 x 2 of random strange {argument name="year" default="Year"} {argument name="style" default="style"} products with what they are underneath in text
```

---

## Realistic Cocoa Plantation Commercial Shot with Motion

A detailed prompt for generating a high-quality, realistic commercial image of a cocoa plantation, focusing on the texture and appearance of a partially split cocoa pod. It also includes a motion comp

```text
High-quality realistic commercial shot of a cocoa plantation in landscape orientation, cocoa tree as background, one cocoa pod partially split open on the branch in the center, fresh cocoa beans clearly visible inside with fibrous natural texture, slight irregular opening, surrounding pods and leaves softly out of focus, rich earthy brown and green tones, warm natural daylight with soft directional highlights, shallow depth of field, premium agricultural realism, no text, no people, no branding.

Motion:  The cocoa pod beans rapidly fly out and transform into {argument name="motion effect" default="roasted cocoa vortex"}
```

---

## Realistic Gym Selfie Portrait Prompt

A prompt for generating a realistic, documentary-style selfie photograph of a woman in a gym, focusing on preserving her facial features exactly. The scene includes a mirror reflection revealing gym e

```text
Create a realistic selfie-style photograph, preserving the woman’s facial features exactly with no changes. The scene shows a woman standing in front of a large mirror in the free-weights area of a gym. She wears a {argument name="clothing item" default="black long-sleeved zipped jumpsuit"} and light-colored sneakers. Her hair is pulled back into a loose bun, and her makeup is polished and flawless. She holds a water bottle in one hand and a smartphone in the other, with a workout app visible on the phone screen. The mirror reflection reveals gym details including a power rack and a rack of dumbbells. Natural daylight streams in from large gym windows, creating a clean, authentic look. Documentary, realistic, lifestyle photography style, candid and natural, vertical 9:16 aspect ratio.
```

---

## Recontextualized Glass Espresso Machine Product Shot

A detailed prompt for generating a high-end product editorial image, recontextualizing an everyday coffee machine as a luxury technological artifact. The prompt specifies that the machine must be made

```text
BAGEL LABS.
Act as a creative director curating a wide-ranging, eclectic collection of “recontextualized everyday objects.”

DIVERSE OBJECT SELECTION (MANDATORY VARIETY):
Randomly select ONE object from these distinct categories to ensure diversity:
Analog Office & Desk:
Sport & Leisure:
Barware & Kitchen:
Utility & Tools:
Grooming:
Travel:

SELECTED CATEGORY:
Barware & Kitchen

CHOSEN OBJECT:
A coffee machine and coffee cup — instantly recognizable, reimagined as a luxury technological artifact.

THE CONCEPT:
Recontextualize the everyday coffee machine as a transparent, high-precision object of engineered beauty.
A fully glass espresso machine reveals its internal systems: hot water circulation, pressure chambers, coffee bean hopper, grinding mechanism, and extraction pathway. Integrated computer circuitry runs through the machine like a nervous system, visually linking ritual, data, and energy.

Fresh coffee is actively pouring from the machine into a matching glass cup, captured mid-flow. The moment feels frozen, precise, and intentional—ritual meets technology.

MATERIALS & FINISH:
- COFFEE MACHINE BODY:
  Precision-molded optical glass with subtle green-tinted transparency. Internal structure is fully visible and meticulously organized.
- INTERNAL COMPONENTS:
  - Hot water tubes and pressure lines clearly visible, rendered in brushed titanium and warm grey.
  - Coffee bean chamber visible at the top with realistic roasted beans.
  - Grinding and extraction mechanisms exposed, engineered and clean.
- CIRCUITRY:
  Integrated PC-style circuitry embedded within the machine’s internal architecture.
  - Circuit paths in muted industrial orange.
  - Supporting components in graphite and titanium tones.
  Circuits are physical and structural, not glowing or decorative.
- COFFEE CUP:
  Matching optical glass cup with weighted base and refined silhouette.
  Subtle BAGEL LABS logomark engraved near the base.
- BRAND INTEGRATION:
  BAGEL LABS logomark engraved into the glass body of the machine (side or rear plane), and subtly etched on the cup.
  No stickers. No printed logos.

ACTION / MOMENT:
Coffee is visibly flowing from the machine into the glass cup.
Liquid motion is realistic and smooth.
Crema and color gradient are visible through the glass, emphasizing transparency and material depth.

PRESENTATION (NO BOXES):
The coffee machine and cup stand fully exposed on a minimal pedestal or surface.
No packaging, no housing, no covers.
All components are visible by design.

PHOTOGRAPHY & LIGHTING:
Style: High-end product editorial (Wallpaper* / Dezeen).
Lighting: Soft, studio high-key lighting with carefully controlled reflections to highlight glass thickness, liquid motion, and internal depth. No harsh shadows.
Background: Clean, seamless light grey or white cyclorama.

COLOR & GRADING:
Primary tones: transparent glass with subtle green tint, warm greys, titanium neutrals.
Accent: restrained
```

---

## Red Satin Slip Dress Bathroom Flash Photo Prompt

A prompt for generating a high-fidelity, influencer-style snapshot of a woman in a vibrant red satin slip dress leaning against a luxury bathroom vanity. The prompt specifies dark brunette hair, direc

```text
{
  "prompt_structure": {
    "subject": {
      "description": "Young woman with light skin tone",
      "hair": "Long, voluminous dark brunette hair, styled in loose waves, center part, reaching past shoulders",
      "face": "Oval face shape, light-colored eyes (appearing green or grey), soft makeup with defined eyeliner and neutral glossy lips",
      "expression": "Neutral, alluring gaze, direct eye contact with the camera"
    },
    "clothing": {
      "type": "Slip dress / Chemise",
      "color": "{argument name="dress color" default="Vibrant red"}",
      "material": "Satin or silk finish with a glossy sheen",
      "details": "Spaghetti straps, V-neckline with scalloped lace trim, lace detailing near the hem, mini length",
      "accessories": "Small silver pendant necklace, ring on ring finger of left hand"
    },
    "pose": {
      "stance": "Leaning backward against a bathroom vanity counter",
      "arms": "Arms extended downward, hands gripping or resting on the edge of the marble countertop",
      "orientation": "Front-facing"
    },
    "environment": {
      "setting": "Modern luxury bathroom",
      "elements": [
        "White marble countertop",
        "Dark wood vanity cabinetry",
        "Large wall mirror behind subject",
        "Circular magnifying mirror on a gold/brass stand",
        "Glass shower door/enclosure in background"
      ],
      "reflections": "Subject's back and hair visible in the large mirror behind her"
    },
    "lighting_and_style": {
      "lighting": "Direct flash photography, bright front illumination with slight shadows behind the subject",
      "aesthetic": "Influencer lifestyle, candid snapshot, high-fidelity, 'night out' preparation vibe",
      "color_palette": "Red, warm skin tones, cool whites and dark browns in background"
    }
  }
}
```

---

## Resort Portrait with Red Wet Hair

Generates an ultra-realistic, high-quality candid photograph of a mid-20s woman with a fit physique, red wet hair, and a deep tan, posed thoughtfully in a resort setting.

```text
{
  "ar": "4:5",
  "subject": {
    "type": "adult woman",
    "age": "mid-20s",
    "character_outline": "fit physique with prominent, athletically sculpted curves; deep bronzed tan with defined muscle tone; hair is long, wet, and red, falling loose around her shoulders",
    "expression": "thoughtful, pensive expression with a slight frown, hand resting on her cheek",
    "gaze": "looking slightly off-camera to the side"
  },
  "wardrobe": {
    "bikini": {
      "type": "string bikini set",
      "color": "{argument name="bikini color" default="red up and black down"}",
      "top_detail": "triangle cups with thin straps, designed for a fuller bust",
      "bottom_detail": "matching bottoms with side ties, accentuating the hips"
    },
    "bag": "sea shoulder bag tucked under her arm"
  },
  "accessories": {
    "jewelry": "layered gold pendant necklaces, a watch, and a bracelet on her left wrist",
    "other": "holding a small cup of gelato with a spoon in her left hand"
  },
  "pose_action": {
    "shot_type": "standing medium shot",
    "stance": "standing casually with her weight on one leg, emphasizing her silhouette",
    "arms_hands": "right hand touching her cheek in a pensive gesture; left hand holding the ice tea",
    "framing": "centered composition capturing her from the mid-thigh up"
  },
  "scene": {
    "location": "covered patio or open-air hallway of a resort or villa",
    "background": "large dark wood door behind her; a large potted plant with green and purple leaves on the left; light beige stucco walls; a glimpse of a bright outdoor area through a doorway on the left",
    "atmosphere": "warm, tropical vacation setting"
  },
  "lighting": {
    "type": "natural shaded daylight",
    "look": "soft, diffused light filtering into the covered area, creating gentle shadows and highlighting the skin's tanned texture and the wet hair"
  },
  "camera": {
    "device_vibe": "high-quality candid photograph",
    "focus": "sharp focus on the subject",
    "style": "ultra-realistic, detailed image capturing the natural textures of skin, hair, fabric, and the environment"
  }
}
```

---

## Retro-Modern Disco-Pop Portrait of Sadie Sink

Creates a high-saturation, monochromatic, retro-modern disco-pop portrait of Sadie Sink with a high-cut spandex bodysuit.

```text
{
  "style_summary": "Retro-modern disco-pop aesthetic with high-saturation monochromatic tones.",
  "pose": {
    "orientation": "Over-the-shoulder look",
    "description": "Sadie Sink is positioned with front to the camera with open legs sitting on a reversed red glossy chair creating a focal point in the upper half of the frame.",
    "stance": "High-cut silhouette emphasizing the chest, legs and red glossy high heels."
  },
  "colors": {
    "primary_palette": ["Bubblegum Pink", "Fuchsia", "Hot Pink"],
    "accent_colors": ["Metallic Silver", "White"],
    "skin_tones": "Warm, natural tan with highlights",
    "vibe": "Monochromatic and high-energy."
  },
  "composition": {
    "framing": "Vertical, medium-full shot",
    "subject_placement": "Centered silhouette",
    "background": "Minimalist, solid-colored flat wall",
    "depth": "Shallow, with a sharp drop-off shadow on the background to create a 3D pop effect."
  },
  "outfits_and_props": {
    "clothing": "High-leg pink spandex bodysuit with white piping/trim",
    "accessories": "Rose-tinted transparent aviator-style sunglasses",
    "key_prop": "A large, multi-faceted metallic silver disco ball",
    "hair": "High ponytail, sleek and brunette."
  },
  "lighting": {
    "type": "Hard studio lighting",
    "direction": "Side-lit from the left",
    "shadows": "Sharp, defined shadows on the wall and body contours",
    "highlights": "Specular highlights on the bodysuit and disco ball facets",
    "special_lighting": "Caustic light reflections (small squares of light) projected onto the subject's skin from the disco ball."
  },
  "effects_and_texture": {
    "finish": "Glossy and high-contrast",
    "texture": "Reflective surfaces (disco ball), matte background, and smooth spandex sheen",
    "saturation": "High",
    "grain": "Clean, digital finish with minimal noise."
  }
}
```

---

## Rooftop Skyline Mirror Selfie

A highly detailed, structured prompt for generating a seductive, high-rise rooftop mirror selfie of a young woman, emphasizing specific pose details, platinum blonde hair blowing in the wind, and cold

```text
{
  "scene_type": "rooftop skyline mirror selfie, glass-walled terrace, cold night wind, seductive calm energy",
  "aspect_ratio": "9:16",

  "subject": {
    "demographics": "young woman, pale skin, Eurasian features",
    "hair": {
      "color": "platinum blonde",
      "style": "long and windswept, strands moving with the rooftop breeze"
    },
    "facial_features": {
      "expression": "over-shoulder half-smirk, eyes slightly narrowed with city-light reflection",
      "makeup": "soft glam, glossy lips, shimmering highlighter"
    }
  },

  "pose_and_body": {
    "orientation": "back fully turned to the mirror, shoulder twist revealing clean sideboob",
    "upper_body": {
      "posture": "slight arch in lower back, relaxed confident stance"
    },
    "arms": {
      "right_arm": "raised holding iPhone at ear-level",
      "left_arm": "hand resting at lower back, thumb hooked into waistband"
    },
    "legs": {
      "pose": "one knee bent inward, subtle hip pop"
    }
  },

  "outfit": {
    "top": {
      "type": "oversized cream knit sweater falling dramatically off one shoulder",
      "underneath": "no bra, loose slip reveals natural sideboob"
    },
    "bottom": {
      "type": "ultra mini lounge shorts",
      "color": "light grey",
      "fit": "thin fabric riding up from twist + wind"
    },
    "accessories": {
      "headwear": "pink fuzzy cat ear headband"
    }
  },

  "environment": {
    "setting": "high-rise rooftop terrace overlooking city skyline",
    "lighting": "cold white city lights mixed with warm rooftop lamps"
  }
```

---

## Rooftop Skyline Mirror Selfie Prompt

A detailed JSON prompt for generating a seductive mirror selfie on a high-rise rooftop overlooking a city skyline at night. The prompt specifies the subject's features, outfit (oversized knit sweater,

```text
{
  "scene_type": "rooftop skyline mirror selfie, glass-walled terrace, cold night wind, seductive calm energy",
  "aspect_ratio": "9:16",

  "subject": {
    "demographics": "young woman, pale skin, Eurasian features",
    "hair": {
      "color": "platinum blonde",
      "style": "long and windswept, strands moving with the rooftop breeze"
    },
    "facial_features": {
      "expression": "over-shoulder half-smirk, eyes slightly narrowed with city-light reflection",
      "makeup": "soft glam, glossy lips, shimmering highlighter"
    }
  },

  "pose_and_body": {
    "orientation": "back fully turned to the mirror, shoulder twist revealing clean sideboob",
    "upper_body": {
      "posture": "slight arch in lower back, relaxed confident stance"
    },
    "arms": {
      "right_arm": "raised holding iPhone at ear-level",
      "left_arm": "hand resting at lower back, thumb hooked into waistband"
    },
    "legs": {
      "pose": "one knee bent inward, subtle hip pop"
    }
  },

  "outfit": {
    "top": {
      "type": "oversized cream knit sweater falling dramatically off one shoulder",
      "underneath": "no bra, loose slip reveals natural sideboob"
    },
    "bottom": {
      "type": "ultra mini lounge shorts",
      "color": "light grey",
      "fit": "thin fabric riding up from twist + wind"
    },
    "accessories": {
      "headwear": "pink fuzzy cat ear headband"
    }
  },

  "environment": {
    "setting": "high-rise rooftop terrace overlooking city skyline",
    "lighting": "cold white city lights mixed with warm rooftop lamps"
```

---

## ROSÉ and Bruno Mars Diptych Hero Image

A prompt for generating a premium personal branding hero image in a seamless diptych style featuring ROSÉ (BLACKPINK) and Bruno Mars. It specifies a 16:9 aspect ratio, a continuous gradient background

```text
Premium personal branding hero image in diptych style with 16:9 aspect ratio. Single seamless canvas with two poses side by side, no frames, no borders, no panels. Single continuous gradient background flowing from {argument name="left color" default="deep burgundy"} on the left to {argument name="right color" default="soft cream ivory"} on the right, no separation, no frames, full-bleed. Soft diffused light consistent across entire canvas. Editorial beauty campaign aesthetic, seamless tone-on-tone. Magazine cover quality. Intimate mood with mirrored symmetry.
The subjects are {argument name="subject 1" default="ROSÉ, BLACKPINK member"}, and {argument name="subject 2" default="Bruno Mars, singer"}. Both have oval face, high cheekbones, flawless porcelain skin with glass-skin finish. ROSÉ has blonde soft waves framing face, Bruno Mars has curly black hair. Minimal dewy makeup with nude pink glossy lips. ROSÉ wears cream ivory chunky knit sweater, Bruno Mars wears deep burgundy velvet blazer, black shirt, and black fedora hat.
ROSÉ and Bruno Mars face toward the center, looking at each other. ROSÉ is touching her cheek with her hand, with "ROSÉ" text in elegant serif typeface similar to Didot or Times New Roman, light weight, small size, at bottom left. Bruno Mars is holding his fedora hat with his hand, with "Bruno Mars" text in elegant serif typeface similar to Didot or Times New Roman, light weight, small size, at bottom right.
Negative prompt: vertical line, center line, dividing line, split screen, separated panels, border between subjects.
```

---

## SaaS Payment Plan Options

Optimizes product and e-commerce strategies for saas payment plan options.

```text
Act as a website designer. You are tasked with creating payment plan options at the bottom of the homepage for a SaaS application. There will be three cards displayed horizontally:

- The most expensive card will be placed in the center to draw attention.
- Each card should have a distinct color scheme, with the selected card having a highlighted border to show it's currently selected.
- Ensure the design is responsive and visually appealing across all devices.

Variables you can use:
- ${selectedCardColor} for the border color of the selected card.
- ${centerCard} to indicate which plan is the most expensive.

Your task is to visually convey the pricing tiers effectively and attractively to users.
```

---

## Sadie Sink at Venice Film Festival

A structured JSON prompt to generate a high-contrast, photorealistic image of actress Sadie Sink at the Venice Film Festival, detailing her Alexander McQueen gown, makeup, and the specific red carpet

```text
{
  "subject": {
    "name": "Sadie Sink",
    "occupation": "actress",
    "known_for": "Max Mayfield in Stranger Things",
    "event": "79th Venice International Film Festival",
    "pose": "confident and poised expression",
    "hair": {
      "color": "copper-red",
      "style": "loose, voluminous waves",
      "length": "just past shoulders"
    },
    "makeup": {
      "lipstick": {
        "color": "bold red",
        "finish": "matte"
      },
      "eye_makeup": "subtle, emphasizing blue eyes",
      "skin": {
        "finish": "dewy, hyper-reflective",
        "style": "wet look / glass-skin",
        "highlights": "smooth, luminous facial contours",
        "tone": "warm"
      }
    },
    "attire": {
      "designer": "Alexander McQueen",
      "type": "custom gown",
      "style": "strapless, floor-length, black velvet",
      "features": [
        "dramatic deep V-neckline",
        "structured architectural cutouts on bodice"
      ]
    }
  },
  "composition": {
    "orientation": "vertical",
    "width": 504,
    "height": 1002,
    "background": {
      "color": "vibrant red",
      "elements": [
        "Venice International Film Festival logo",
        "Armani Beauty branding"
      ]
    },
    "lighting": "bright, even, eliminating harsh shadows"
  },
  "style": {
    "theme": ["Gothic elegance", "modern Hollywood glamour"],
    "contrast": "high, subject is focal point"
  }
}
```

---

## Sadie Sink Champagne Silk Slip Dress Portrait

A detailed JSON prompt, written primarily in Hindi/Urdu (Romanized), for generating three portraits of Sadie Sink in a luxury room setting. The prompt specifies a champagne silk slip dress, beachy wav

```text
{
  "shaksiyat_ki_maloomat": {
    "naam": "Sadie Sink",
    "pehchaan": "Hollywood adakaara (Stranger Things, The Whale)",
    "andaz": "Pur-waqar aur haseen (Elegant and Graceful)"
  },
  "libas_ki_tafseelat": {
    "libas_ka_naam": "Champagne Silk Slip Dress",
    "fabric": "Silk Satin (Chamakdar aur naram kapda)",
    "neckline": "Cowl neck (Gale par thoda sa jhol wala design)",
    "straps": "Thin Spaghetti straps (Bareek doriyaan)",
    "length": "Knee-length (Ghutno tak ka dress)",
    "color_palette": "Champagne, Beige, Nude tones"
  },
  "zair_o_jawahar_aur_accessories": {
    "gulluband": "Chandi ki bareek zanjeer jisme ek chota sa heere ka pendant hai",
    "baaliyan": "Drop earrings jo chehre ki rangat ke sath match kar rahi hain",
    "anguthi": "Hath ki ungliyon mein koi bhari jewellery nahi hai, jo look ko simple rakhti hai"
  },
  "makeup_aur_baal": {
    "baal_ka_rang": "Strawberry Blonde (Sunehri-surkh)",
    "baal_ka_style": "Kandhon tak lambe, beachy waves (halki lehrein)",
    "makeup_style": "No-makeup makeup look",
    "lips": "Mauve-pink lipstick",
    "eyes": "Halka mascara aur brown eyeshadow"
  },
  "tasvir_ka_mahaul": {
    "location": "Luxury Room ya Studio setting",
    "furniture": "Cream rang ka textured sofa (Armchair)",
    "parde": "Vertical pleats wale cream/beige parde",
    "roshni": "Naram aur qudrati roshni (Soft indoor lighting)"
  },
  "mukhtalif_poses": {
    "tasvir_1": "Sofe par baith kar camera ki taraf dekhte hue ek masoom muskurahat",
    "tasvir_2": "Sofe ke sath khadi hui, ek hath sofe par aur ek hath neeche, pura qad (full length) dikh raha hai",
    "tasvir_3": "Sofe par baith kar side ki taraf dekhte hue, sanjeeda aur gehri soch wala expression"
  }
}
```

---

## Sadie Sink in Grecian Dress in Ancient Ruins

A detailed JSON prompt for generating an image of Sadie Sink in a Grecian-inspired dusty rose dress, sitting or wading in water within ancient architectural ruins (like a Roman thermal bath). The prom

```text
{
  "subject": {
    "identity": "{argument name="subject name" default="Sadie Sink"}",
    "appearance": {
      "hair": "wet, shoulder-length, strawberry blonde/light red, slightly wavy strands falling around the face",
      "face": "natural look, minimal to no visible makeup, fair skin with freckles, serious and contemplative expression, gaze directed slightly upward or straight ahead",
      "body": "slender figure, skin wet from the surroundings"
    },
    "clothing": {
      "dress": {
        "color": "dusty rose or muted pink",
        "style": "sleeveless, deep V-neckline, gathered waist, flowing Grecian-inspired drapes",
        "fabric": "lightweight, wet and clinging to the body due to water immersion"
      },
      "accessories": [
        {
          "item": "arm cuff",
          "description": "gold, coiled snake design",
          "placement": "upper right arm"
        },
        {
          "item": "necklaces",
          "description": "layered gold chains, one shorter chain and one longer with a round pendant",
          "placement": "neck"
        },
        {
          "item": "bracelet",
          "description": "simple gold bangle",
          "placement": "right wrist"
        }
      ]
    },
    "poses": [
      "sitting in the water, leaning back on hands, looking upwards",
      "wading through water, body turned slightly, reaching down to touch the water surface",
      "sitting upright in water, looking directly at the camera, profile slightly visible"
    ]
  },
  "environment": {
    "location": "ancient architectural ruins, resembling a Roman or Greek thermal bath (e.g., Cleopatra's Pool in Hierapolis)",
    "elements": [
      "tall, weathered stone columns with ornate Corinthian capitals",
      "submerged ancient stone blocks",
      "stone arch structures in the background"
    ],
    "water": "clear, calm with gentle ripples, waist-deep to knee-deep, reflecting the sky and ruins"
  }
```

---

## Seductive Nighttime Balcony Portrait of Two Women

A complex JSON prompt for generating a cinematic portrait of two women on a luxury hotel balcony overlooking a city skyline at night. The prompt meticulously defines the appearance, clothing, and pose

```text
{
  "prompt": {
    "subjects": [
      {
        "name": "brunette_woman",
        "appearance": {
          "hair": "Long dark chocolate brown, silky straight with center part",
          "skin_tone": "Smooth olive",
          "eyes": "Dark, heavy lashes, sultry gaze",
          "lips": "Plum matte, softly parted",
          "nose": "Defined bridge",
          "cheeks": "Subtle bronzed glow",
          "expression": "Seductive half-lidded eyes looking over shoulder"
        },
        "clothing": {
          "top": "Black sheer chiffon blouse, unbuttoned just enough",
          "bottom": "Tailored cream trousers, low on hips"
        },
        "pose": "Standing behind, hands resting lightly on the balcony rail beside the other woman, body close",
        "position": "Left side of frame"
      },
      {
        "name": "honey_blonde_woman",
        "appearance": {
          "hair": "Long honey blonde waves, wind-tousled",
          "skin_tone": "Sun-kissed fair",
          "eyes": "Blue-green, looking up at city lights",
          "lips": "Nude gloss, slight smile",
          "nose": "Delicate",
          "cheeks": "Soft rosy flush",
          "expression": "Dreamy upward gaze with subtle invitation"
        },
        "clothing": {
          "top": "Champagne silk slip dress, thin straps slipping slightly",
          "accessories": "Diamond stud earrings"
        },
        "pose": "Leaning forward on balcony railing, back gently arched, looking up at the skyline",
        "position": "Right side of frame"
      }
    ],
    "environment": {
      "time": "Night",
      "location": "Luxury hotel balcony overlooking city",
      "lighting": "Soft city glow, warm balcony lights",
      "background_objects": [
        "Sparkling city skyline",
        "Glass of champagne on railing",
        "Plush outdoor lounge cushions",
        "Distant traffic lights",
        "Night sky with faint stars"
      ]
    },
    "aspect_ratio": "4:5"
  }
}
```

---

## Showa Retro-Pop Girl with Japanese Text

A prompt originally used with Niji 7 but mentioned in the context of Nano Banana Pro's capabilities, describing a girl embodying the Showa retro-pop aesthetic with bright, quirky attire, lively pop-ar

```text
a girl embodying the Showa retro-pop vibe. She dons attire filled with bright hues and quirky designs, with her hairstyle, makeup, and accessories all radiating a lively and nostalgic pop-art charm. she said "{argument name="Japanese phrase" default="おはよう！元気？"}"
```

---

## Single Prompt Product Shot Generation for Olive Oil Brand

A prompt used to generate a social media feed for a small-batch olive oil brand, resulting in hyper-realistic product shots with perfect label text and typography, demonstrating the efficiency of Nano

```text
Create a social media feed for this small-batch olive oil brand.
```

---

## Skeletal Product Design Prompt

A very brief, high-level prompt instructing the AI to generate a skeletal product design. The full details are likely in the linked image (not provided), but the core instruction is extracted.

```text
Skeletal Product Design
```

---

## Skincare Editorial Photography Collage Prompt

A highly structured prompt designed to generate a photography collage for a beauty/skincare product, focusing on a serene, spa-like atmosphere. It specifies a sequence of shots (wide, medium, close-up

```text
{
  "subject": {
    "person": "Woman, appears to be in her 20s or 30s",
    "pose_and_expression": [
      "Standing by window, looking out, relaxed",
      "Reaching for bottle on counter, hand focus",
      "Looking in mirror, slight smile",
      "Hand dispensing serum from bottle, close-up",
      "Serum drop on fingertip, macro shot",
      "Applying serum to face, eyes closed, serene",
      "Face close-up, eyes closed, content",
      "Bottle and orchid on counter, still life",
      "Walking away from camera, standing by window"
    ]
  },
  "clothing": {
    "items": "White robe, white pajamas/loungewear",
    "material": "Soft, flowing fabric",
    "style": "Casual, luxurious"
  },
  "hair": {
    "color": "Dark brown",
    "style": "Pulled back, neat bun or ponytail"
  },
  "face": {
    "makeup": "Natural, minimal",
    "skin": "Clear, glowing",
    "expression": "Calm, serene, content"
  },
  "accessories": {
    "jewelry": "Simple ring on ring finger",
    "props": [
      "Glass skincare bottle with gold pump dispenser",
      "Product label: '{argument name="product name" default="Promptopia"}'",
      "White orchid in a small white vase"
    ]
  },
  "environment": {
    "location": "Modern, luxurious bathroom",
    "elements": [
      "Large floor-to-ceiling windows",
      "Marble countertop and walls",
      "Round mirror",
      "View of trees/garden outside",
      "Fog or mist outside window"
    ],
    "atmosphere": "Serene, spa-like, tranquil"
  },
  "lighting": {
    "source": "Natural daylight",
    "quality": "Warm, golden, soft, diffused",
    "time_of_day": "Sunrise or golden hour"
  },
  "camera": {
    "type": "Photography collage",
    "shots": [
      "Wide shot",
      "Medium shot",
      "Close-up",
      "Macro shot"
    ],
    "focus": "Sharp on subject and product, soft background blur (bokeh)"
  },
  "style": {
    "aesthetic": "Cinematic, editorial, beauty, wellness, clean, minimalist",
    "color_palette": "Warm neutrals, white, gold, natural greens"
  }
}
```

---

## Skincare Product Key Visual Generator

A customizable prompt template for generating ultra-realistic premium skincare product key visuals. It uses placeholders for the product, background colors, and key ingredients, focusing on clean stud

```text
centered {argument name="product type" default="FACEWASH_PACKAGING"} on a bold {argument name="background color 1" default="BG_COLOR_1"}→{argument name="background color 2" default="BG_COLOR_2"} gradient, modern studio lighting, crisp reflections + soft grounded shadow. Label text perfectly readable: "{argument name="brand name" default="BRAND"} {argument name="product name" default="PRODUCT_NAME"}" only.Surround with floating KEY_INGREDIENT_1, KEY_INGREDIENT_2, BOTANICAL in a balanced ring layout, plus glossy gel/foam ribbon swirls (smooth loops), micro water droplets + light mist. Ultra-sharp focus, shallow DOF, 85mm, HDR, ISO100, clean negative space, no clutter, no watermark.Output {ASPECT} (1:1/4:5/9:16).
```

---

## Social Feed Creation for Olive Oil Brand

A prompt used with Gamma's Nano Banana Pro to generate a complete social media feed, including hyper-realistic product shots and design elements, for a small-batch olive oil brand.

```text
Create a social feed for a small-batch olive oil brand.
```

---

## Social Media Feed for Olive Oil Brand

A simple, high-level prompt for Gamma/Nano Banana Pro to generate a complete social media feed for a small-batch olive oil brand, resulting in hyper-realistic product shots with perfect typography.

```text
Create a social media feed for this small-batch olive oil brand.
```

---

## Social Media Feed Generation for Olive Oil Brand

A text generation prompt used with GammaApp and Nano Banana Pro to create a social media feed for a small-batch olive oil brand, emphasizing the model's ability to generate hyper-realistic product sho

```text
Create a social media feed for this small-batch olive oil brand.
```

---

## Social Media Feed Generation Prompt

A text prompt instructing an AI model (Gamma/Nano Banana Pro) to generate a complete social media feed for a specific product, focusing on hyper-realistic product shots with accurate typography and br

```text
Create a social media feed for this {argument name="product type" default="small-batch olive oil brand"}.
```

---

## Social Media Feed Generation Prompt for Olive Oil Brand

A simple text prompt used to test the Nano Banana Pro's capability to generate a complete social media feed, including hyper-realistic product shots and appropriate typography, for a small-batch olive

```text
Create a social media feed for a small-batch olive oil brand.
```

---

## Sophisticated Dining Scene with Burgundy Gown (Urdu/Hindi)

A highly detailed, structured image generation prompt written in Urdu/Hindi, describing a sophisticated, high-end dining and fashion scene. It focuses on a woman in a burgundy gown, luxurious interior

```text
{
  "tasvir_ki_base": {
    "mozu": "High-end dining aur fashion",
    "vibe": "Sophisticated, khamosh aur pur-ashayish",
    "climax_point": "Khatoon ka pur-waqar andaz aur burgundy gown"
  },
  "pash-e-manzar_details": {
    "deewarain": "Safaid rang ki panelled deewarain jin par sunehri (gilded) moldings hain",
    "lighting_fixtures": {
      "wall_sconces": "Deewar par lage do shandar fanus (chandeliers)",
      "table_lamps": "Chote classic lamps jo har table par naram roshni phela rahe hain"
    },
    "aaine": "Piche ki taraf bade aur sunehri frame wale aaine jo kamre ki gehrai (depth) ko barha rahe hain"
  },
  "markazi_shakhsiyat": {
    "chehra": "Haseen features, halka makeup, aur pursukoon tasur",
    "baal": "Silk ki tarah narm, blonde baal jo kaandhon par bikhre hue hain",
    "libas_ki_banawat": {
      "bodice": "Corset ki tarah fit, jo jism ki sakht ko numaya kar raha hai",
      "fabric": "Gown ka kapra makhmali (velvet) ya gehra satin maloom hota hai",
      "shawl": "Ek hi rang ki shawl ya kapra jo baazuon par narmat se gira hua hai"
    },
    "clutch": "Chota, rectangular sunehri (gold) clutch jo sofa par hath ke niche rakha hai"
  },
  "dining_set_up": {
    "table_setting": {
      "linens": "Bilkul saaf aur istri shuda safaid mez-posh (tablecloth)",
      "crockery": "Safaid ceramic ki plates aur crystal ke glass",
      "cutlery": "Chandi (silver) ke chammach aur kaante jo nizam ke sath rakhe hain",
      "glassware": "Wine glass jis mein halkay sunehri rang ka mashroob hai"
    },
    "furniture": "Tan/Peach rang ka makhraati sofa jis par vertical stitching hui hai"
  },
  "technical_aspects": {
    "focus": "Khatoon par sharp focus hai jabke piche ka manzar halka sa dundhla (bokeh effect) hai",
    "color_palette": {
      "primary": "Deep Burgundy, Champagne Gold",
      "secondary": "Creamy White, Warm Amber"
    }
  }
}
```

---

## Sora video prompt for Macho Meal McDonald’s commercial

A short Sora prompt for generating an authentic-looking 1980s-style McDonald’s commercial featuring Macho Man Randy Savage promoting a Macho Meal happy meal.

```text
Authentic vintage 1980s commercial for the {argument name="product name" default="Macho Meal happy meal"} at {argument name="brand" default="McDonalds"} featuring {argument name="celebrity" default="Macho Man Randy Savage"}.
```

---

## Stranger Things Cast as DC Superheroes Cosplay

A structured prompt defining a scenario where four actresses from Stranger Things (Millie Bobby Brown, Natalia Dyer, Sadie Sink, and Maya Hawke) are depicted cosplaying as specific DC Comics character

```text
[
  {
    "actress_info": {
      "name": "Millie Bobby Brown",
      "famous_for": "Eleven in Stranger Things",
      "nationality": "British"
    },
    "character_cosplay": {
      "character_name": "Wonder Woman",
      "alter_ego": "Diana Prince",
      "universe": "DC Comics",
      "costume_description": "Blue and gold metallic Amazonian armor with a signature star tiara and leather straps.",
      "vibe": "Strong and Heroic"
    }
  },
  {
    "actress_info": {
      "name": "Natalia Dyer",
      "famous_for": "Nancy Wheeler in Stranger Things",
      "nationality": "American"
    },
    "character_cosplay": {
      "character_name": "Raven",
      "alter_ego": "Rachel Roth",
      "universe": "DC Comics Teen Titans",
      "costume_description": "Dark blue glossy bodysuit with a purple hooded cape and matching wrist guards.",
      "vibe": "Mysterious and Dark"
    }
  },
  {
    "actress_info": {
      "name": "Sadie Sink",
      "famous_for": "Max Mayfield in Stranger Things",
      "nationality": "American"
    },
    "character_cosplay": {
      "character_name": "Starfire",
      "alter_ego": "Koriand'r",
      "universe": "DC Comics Teen Titans",
      "costume_description": "Shiny green two-piece outfit with silver trim and emerald gemstones.",
      "vibe": "Energetic and Powerful"
    }
  },
  {
    "actress_info": {
      "name": "Maya Hawke",
      "famous_for": "Robin Buckley in Stranger Things",
      "nationality": "American"
    },
    "character_cosplay": {
      "character_name": "Harley Quinn",
      "alter_ego": "Dr. Harleen Quinzel",
      "universe": "DC Comics Suicide Squad",
      "costume_description": "White 'Daddy's Lil Monster' shirt with purple sequined shorts and fishnet stockings.",
      "vibe": "Playful and Chaotic"
    }
  }
]
```

---

## Stranger Things Cast as Toy Story's Jessie Cosplay

A structured prompt detailing four separate images, each featuring a different actress (Maya Hawke, Natalia Dyer, Millie Bobby Brown, Sadie Sink) cosplaying as Jessie from Toy Story. It specifies uniq

```text
[
  {
    "actress_name": "Maya Hawke",
    "cosplay_theme": "Jessie from Toy Story",
    "outfit_description": {
      "headwear": "Bright red cowgirl hat with white decorative stitching along the brim",
      "clothing": "Green and white bandeau crop top paired with denim shorts and white chaps",
      "accessories": "Yellow wristbands accented with red ribbons and a brown western belt",
      "hair_style": "Light blonde hair styled in two long, symmetrical braids"
    },
    "visual_elements": "Holding a glass of red wine against a neutral studio backdrop"
  },
  {
    "actress_name": "Natalia Dyer",
    "cosplay_theme": "Jessie from Toy Story",
    "outfit_description": {
      "headwear": "Classic red western-style felt hat",
      "clothing": "Green and white tube top with a silver ring detail and frayed denim chaps",
      "accessories": "Contrasting black wrist cuffs with red ribbon ties and a gold belt buckle",
      "hair_style": "Dark brunette hair tied into loose, stylish side braids"
    },
    "visual_elements": "Posing with a glass of white wine and a confident expression"
  },
  {
    "actress_name": "Millie Bobby Brown",
    "cosplay_theme": "Jessie from Toy Story",
    "outfit_description": {
      "headwear": "Red cowgirl hat featuring white lacing around the edges",
      "clothing": "Green bandeau top with buckle detailing and classic blue denim shorts",
      "accessories": "Yellow fabric armbands with small red bows and a vintage leather belt",
      "hair_style": "Natural brown hair braided into two thick, wavy pigtails"
    },
    "visual_elements": "Standing centered while holding a glass of red wine"
  },
  {
    "actress_name": "Sadie Sink",
    "cosplay_theme": "Jessie from Toy Story",
    "outfit_description": {
      "headwear": "Deep red cowgirl hat in a traditional felt finish",
      "clothing": "Tri-color green, white, and red bandeau top with white leg overlays",
      "accessories": "Bright yellow wrist sleeves tied with red ribbons and an embossed belt",
      "hair_style": "Vibrant red hair styled into two neat, tight braids"
    },
    "visual_elements": "Capturing a candid facial expression while holding a red wine glass"
  }
]
```

---

## Streetwear Man on Lamborghini at Sunset

A prompt for generating an image of a stylish man in modern streetwear (orange jacket, black t-shirt with red logo, grey cargo pants) sitting on the hood of an orange Lamborghini sports car. The scene

```text
A-STYLISH MAN WEARING MODERN STREETWEAR-{argument name="jacket color" default="ORANGE"} LONG JACKET, BLACK T-SHIRT WITH RED HIDDEN LEAF LOGO, GREY CARGO PANTS, AND STYLISH ADIDAS SNEAKERS; SITTING CASUALLY ON THE HOOD OF AN ORANGE LAMBORGHINI SPORTS CAR WITH A CONFIDENT POSE AT SUNSET IN A CITYSCAPE BACKGROUND. THE CAR AND OUTFIT HAVE MATCHING ORANGE-BLACK ACCENTS, GLOWING WARM SUNSET LIGHTING, DRAMATIC CLOUDS, AND REALISTIC REFLECTIONS ON THE CAR SURFACE.
```

---

## Structured Prompt for Fashion Editorial with Oversized Product

A structured JSON prompt for Gemini Nano Banana 3.0 Pro to create a fashion editorial image. The scene features a slim model leaning against a monolithic, oversized Fenty Beauty Gloss Bomb Lip Luminiz

```text
{
  "subject": "fashion model leaning against a massively oversized beauty product",
  "character": {
    "gender": "female",
    "age_range": "early 20s",
    "body_type": "slim, athletic",
    "skin_tone": "light natural skin tone",
    "hair": "dark brown hair in a high ponytail with loose front strands",
    "face_structure": "soft jawline, refined nose, expressive eyes",
    "expression": "confident, cool, detached editorial gaze",
    "pose": "full body standing, legs crossed casually at ankles, leaning side against product, one hand touching face/jawline"
  },
  "wardrobe": {
    "top": "black cropped zip-up hoodie",
    "bottom": "minimal white briefs",
    "socks": "white crew socks (scrunched)",
    "shoes": "chunky black leather loafers",
    "style": "clean fashion editorial, sporty minimal, gen-z luxury"
  },
  "hero_product": {
    "brand": "{argument name="product brand" default="Fenty Beauty"}",
    "product_name": "{argument name="product name" default="Gloss Bomb Lip Luminizer"}",
    "product_state": "closed, cap attached",
    "scale": "monolithic, taller than the model",
    "design": {
      "form": "classic rectangular lip gloss tube",
      "cap": "signature metallic rose-gold Fenty cap",
      "material": "clear acrylic tube with visible gloss volume",
      "finish": "high-gloss reflection",
      "color": "deep cherry-red gloss"
```

---

## Submerged Product Effect Prompt

A simple prompt title indicating the generation of a product image featuring a 'Submerged Product Effect,' suggesting a visual style where a product is partially or fully underwater with associated ef

```text
Submerged Product Effect
```

---

## Summer Skincare Product Photography on Beach

Creates AI-edited photorealistic product photograph of a cosmetic serum dropper bottle on sandy beach.

```text
8K UHD, AI-edited photorealistic product photography, portrait approximately 3:4. Sandy beach shoreline, fine golden-brown sand, wet compacted sand with small water-filled depressions. Sea water shallow moving, white sea foam. Cosmetic serum dropper bottle lying flat on sand, slightly diagonal. Transparent glass with deep translucent red liquid, matte white plastic dropper cap. Multiple visible water droplets on glass, light reflections. Multiple visible water droplets on glass, light reflections. Label with RED GLOW text in gold, rectangular with thin gold outline.
```

---

## Sun-Drenched POV Selfie on a Tropical Beach (Lifestyle Aesthetic)

A high-resolution prompt for a sun-drenched POV selfie/medium shot of a stylish blonde woman (Millie Bobby Brown likeness) on a white sand beach. The prompt specifies a lifestyle influencer aesthetic,

```text
"A high-resolution, sun-drenched POV selfie and a medium-shot of a stylish blonde woman sitting on a white sand beach. She is wearing a {argument name="bikini color" default="red leopard-print"} bik!ni with cherry accents and thin red straps. She has a playful, confident expression, posing with a golden bottle of tanning oil or body mist near her face.
Fashion & Accessories:

Eyewear: Oversized, square-framed silver aviator sunglasses with a slight blue/pink gradient tint.

Jewelry: Statement floral-shaped white pearl earrings.

Hair: Blonde hair styled in a casual, textured updo with a red bow accessory.

Details: Long, manicured almond-shaped nails with silver glitter/metallic tips. Small, minimalist tattoos visible on the wrist and ribcage.
Environment & Lighting:

Setting: A pristine tropical beach with bright white sand and scattered patches of dark sea kelp.

Lighting: Harsh, direct overhead midday sunlight creating sharp, high-contrast shadows. The skin has a bronzed, dewy, and shimmering glow.

Color Palette: Dominant reds, golden ambers from the product bottle, and the neutral tones of the sand.
Technical Style:
Shot on a modern smartphone, sharp focus on the subject, vibrant saturation, high contrast, lifestyle influencer aesthetic, summer vacation vibes."
```

---

## Surreal Editorial: Miniature Makeup Artists

A detailed prompt for a surreal editorial fashion/beauty concept featuring an extreme close-up of a giant female face being attended to by multiple miniature human figures dressed as lab technicians,

```text
{
  "image_type": "surreal editorial fashion / beauty concept",
  "composition": {
    "framing": "extreme close-up portrait filling almost entire frame",
    "orientation": "vertical",
    "scale_contrast": "giant female face contrasted with multiple miniature human figures",
    "focus": "sharp focus on facial features and miniature figures simultaneously",
    "depth_of_field": "moderate depth, background softly blurred but still readable"
  },
  "primary_subject": {
    "gender_presentation": "female",
    "face_position": "head tilted slightly, face angled diagonally across frame",
    "skin_texture": "smooth, natural skin with visible pores, soft glow",
    "skin_tone": "light warm beige",
    "facial_details": {
      "eyes": {
        "color": "green",
        "eyelashes": "long, dark, curled",
        "eyeliner": "black eyeliner visible along upper lash line",
        "gaze_direction": "eyes partially open, relaxed gaze slightly downward"
      },
      "eyebrows": {
        "shape": "thick, natural, softly arched",
        "color": "dark brown"
      },
      "lips": {
        "shape": "full lips",
        "finish": "glossy, natural sheen",
        "color": "muted rose / nude pink",
        "mouth_position": "slightly open, relaxed expression"
      },
      "nose": {
        "shape": "straight bridge, soft tip",
        "lighting": "subtle highlight along bridge"
      }
    },
    "hair": {
      "color": "dark brown",
      "texture": "soft, voluminous, slightly tousled",
      "placement": "hair spread across background and around face"
    }
  },
  "miniature_figures": {
    "count": 4,
    "appearance": {
      "scale": "miniature human scale compared to face",
      "clothing": {
        "upper": "white lab coats",
        "lower": "dark pants",
        "footwear": "dark shoes, one figure standing on a small ladder"
      },
      "accessories": {
        "gloves": "pink latex gloves",
        "masks": "light blue surgical masks"
      }
    },
    "actions": [
      {
        "tool": "hair dryer",
        "interaction": "blowing air onto hair near forehead"
      },
      {
        "tool": "spray bottle",
        "interaction": "spraying mist near eyebrow/eye area"
      },
      {
        "tool": "eyeliner brush",
        "interaction": "applying eyeliner to upper eyelid"
      },
      {
        "tool": "lip gloss applicator",
        "interaction": "applying gloss to lower lip"
      }
    ],
    "pose_and_positioning": {
      "one_figure": "standing on a small ladder near hairline",
      "others": "standing directly on hair or face surface"
    }
  },
  "lighting": {
    "type": "soft studio lighting",
    "direction": "even frontal and side lighting",
    "highlights": "gentle highlights on cheekbones, nose, lips",
    "shadows": "soft, minimal shadows maintaining facial contours"
  },
  "color_palette": {
    "dominant_colors": [
      "warm skin tones",
```

---

## Surreal Glamour Portrait in Luxury Bathroom

A highly stylized JSON prompt for generating a photorealistic image in the style of Guy Bourdin surrealism mixed with Y2K flash. It features a subject (Ana de Armas reference) in a golden metallic min

```text
{
  "version": "1.0",
  "aspect_ratio": "3:4",
  "subject": {
    "identity": "Ana de Armas",
    "fidelity": "Exact facial preservation, high-detail skin texture",
    "expression": {
      "eyes": "Heavy-lidded, tired but piercing",
      "mouth": "Slightly parted lips, subtly smudged red lipstick",
      "gaze": "Lazy, confident, post-party fatigue",
      "mood": "Decadent, surreal glamour, beautiful discomfort"
    },
    "pose": {
      "position": "Half-seated on white marble bathroom vanity",
      "body_language": "Elegantly arched back, chest pushed forward, one arm bracing behind with flat palm on marble",
      "legs": "One leg raised with knee bent and foot on vanity edge; one leg hanging with toes grazing the floor",
      "hands": "Free hand resting loosely on the raised knee"
    }
  },
  "wardrobe_accessories": {
    "clothing": "Form-fitting golden metallic mini-dress, iridescent purple accents, sweetheart neckline, reflective sequin texture, hem ridden up to reveal upper thigh",
    "jewelry": [
      "Long dangling gold earrings",
      "Stacked beaded bracelets",
      "Elegant luxury wristwatch"
    ],
    "footwear": "Barefoot"
  },
  "environment": {
    "setting": "Luxury bathroom at 3:00 AM",
    "materials": "White marble countertops, gold-finished fixtures",
    "key_elements": "Large floor-to-ceiling mirror behind subject, multiplying reflections of back and profile",
    "props": "Scattered champagne glass, decadent party debris"
  },
  "lighting_style": {
    "aesthetic": "Guy Bourdin surrealism mixed with Y2K millennium flash",
    "key_light": "Direct on-camera flash (high-intensity, Y2K style)",
    "accent_lights": {
      "camera_left": "{argument name="accent color 1" default="Hot pink and magenta"} wash",
      "camera_right": "{argument name="accent color 2" default="Electric cyan and blue"} rim lighting"
    },
    "effects": "High saturation light play on marble, mirror reflections creating voyeuristic tension, subtle halation on sequin highlights"
  },
  "technical_specs": {
    "camera": "35mm film aesthetic",
    "lens": "35mm wide-angle at f/2.8",
    "angle": "Slightly low angle to emphasize height and dominance",
    "focus": "Sharp focus on eyes and dress texture",
    "film_stock_simulation": {
      "contrast": "High",
      "grain": "Fine film grain",
      "color_grading": "Punchy, saturated, high-fashion editorial"
    }
  }
}
```

---

## Surreal Miniature Potato Chip Commercial Prompt

A prompt for generating a surreal miniature advertisement scene featuring a Lay's chips can on snowy mountains, where golden potato chips are used as snowboards by tiny figures, emphasizing clean ligh

```text
Surreal miniature ad scene: a {argument name="chip brand" default="Lay’s"} chips can on snowy mountains, golden potato chips used as snowboards. Tiny snowboarders ride directly on the chips along an icy blue trail, snow spraying. Clean lighting, high contrast, premium commercial style.
```

---

## Surreal minimal beauty composition with floating gold lips and hands on a peach background

A text prompt for an ultra-realistic, surreal minimal beauty composition. It describes elegant female hands painted nude-beige, framing empty space, with floating sunglasses and glossy metallic gold l

```text
Ultra-Realistic Promotional
Surreal minimal beauty composition on a soft peach background with a pink watercolor texture at the top. Two elegant female hands painted in a matte nude-beige color, forming a symmetrical curved shape framing empty space. Floating above the hands are sunglasses. Below the sunglasses: glossy metallic gold lips, floating without a face. High-fashion editorial style, clean lighting, smooth shadows, aesthetic surrealism, pastel tones, elegant composition, luxury product photography mixed with artistic collage.
```

---

## Swimsuit to bikini pose-edit prompt (reply)

A pose-edit and wardrobe-change prompt from the replies, asking to change a one-piece swimsuit to a bikini and add high heels while keeping style and background.

```text
Change the one-piece swimsuit to a bikini and add high heels while keeping the same style and background.
```

---

## Sydney Sweeney Dual Fashion Looks Prompt

A structured JSON prompt designed to generate two distinct fashion images of Sydney Sweeney: one in a monochromatic denim set with structural details in an urban evening setting, and another in a cout

```text
[
  {
    "image_id": "1000583563.png",
    "subject": {
      "name": "{argument name=\"subject name\" default=\"Sydney Sweeney\"}",
      "action": "Walking out of a building entry",
      "pose": "Mid-stride, full-body side profile"
    },
    "fashion_details": {
      "outfit_type": "Monochromatic Denim Set",
      "jacket": {
        "style": "Structural denim blazer/tunic",
        "features": [
          "Shoulder cut-outs",
          "Corset-style lace-up detailing on the sides and sleeves",
          "Metallic button-down front",
          "Cinching at the waist"
        ]
      },
      "bottom": "Matching dark wash denim micro-shorts",
      "accessories": {
        "eyewear": "Dark cat-eye sunglasses",
        "handbag": "Small white pleated 'Miu Miu' style bag",
        "footwear": "White pointed-toe heels with black tips"
      }
    },
    "setting": "Urban evening, likely a hotel or event entrance with a doorman in the background"
  },
  {
    "image_id": "1000583561.png",
    "subject": {
      "name": "{argument name=\"subject name\" default=\"Sydney Sweeney\"}",
      "action": "Posing for cameras",
      "expression": "Radiant, wide-toothed smile"
    },
    "glam_details": {
      "hair": {
        "style": "Voluminous, honey-blonde bombshell waves",
        "accessory": "Large black sheer tulle bow headband"
      },
      "makeup": {
        "look": "Soft glam with dewy skin",
        "eyes": "Natural lashes and subtle shadow",
        "lips": "Neutral pink gloss"
      },
      "jewelry": "Elegant diamond drop earrings"
    },
    "attire_glimpse": {
      "dress_style": "Couture gown with heavy crystal embellishments",
      "neckline": "Sweetheart neckline with thin jeweled straps"
    },
    "setting": "Formal red carpet event (Met Gala) with warm, blurred background lighting"
  }
]
```

---

## Sydney Sweeney Fashion Portrait on Coastal Beach

Creates a hyper-realistic fashion editorial portrait of Sydney Sweeney on a pebbled beach with metallic pink swimsuit dress.

```text
{
  "prompt_specification": {
    "type": "Ultra-realistic cinematic fashion portrait",
    "subject": {
      "identity": {
        "name": "{argument name="celebrity name" default="Sydney Sweeney"}",
        "constraint_strictness": "100%",
        "directives": [
          "Preserve exact facial identity from reference",
          "Unchanged body proportions from reference",
          "Same facial features only",
          "No face alteration",
          "No body reshaping",
          "No stylization",
          "Natural anatomy must remain accurate"
        ]
      },
      "physical_attributes": {
        "body_type": "Curvy woman with natural proportions",
        "skin": {
          "tone": "Natural, exactly matching the reference",
          "texture": "Natural skin texture with visible pores",
          "highlights": "Realistic highlights",
          "negative_constraint": "No plastic skin"
        },
        "hair": {
          "directive": "Identical to reference",
          "properties": ["color", "length", "texture", "styling"]
        },
        "expression": "Strong confident pout toward the camera"
      },
      "pose_and_action": {
        "stance": "Standing, posture balanced and anatomically correct",
        "limb_placement": {
          "arm_1": "gently on her neck",
          "arm_2": "resting on her thigh"
        },
        "camera_view": "Medium low-angle, three-quarter front view"
      }
    },
    "attire": {
      "garment": {
        "item": "One-piece swimsuit dress",
        "color": "Soft metallic pink",
        "cut": ["high-cut sides", "thigh-high slit"],
        "fabric_physics": ["realistic stretch", "folds", "sheen"]
      },
      "details": {
        "chest_piece": {
          "item": "Gold brooch detail at the bust",
          "note": "color change only, no design alteration"
        },
        "jewelry": {
          "items": ["Gold bangles", "gold hoop earrings"],
          "properties": ["realistic metallic reflections", "realistic scale"]
        }
      }
    },
    "environment": {
      "setting_type": "Clean natural coastal atmosphere",
      "composition_layers": {
        "foreground": "Pebbled beach (subject standing here)",
        "mid_ground": [
          "turquoise sea behind the subject",
          "rocky coastal cliffs catching late afternoon light"
        ],
        "background/horizon": "small distant sailboat on the horizon"
      }
    },
    "photography_style": {
      "aesthetic": [
        "Hyper-detailed photorealism",
        "professional editorial finish",
        "high-end fashion editorial realism"
      ],
      "quality_metric": "8K RAW quality",
      "composition_ratio": "Vertical 9:16",
      "lighting": {
        "source": "Natural daylight",
        "time": "Warm late afternoon",
        "qualities": ["cinematic lighting balance", "controlled highlights and shadows"]
      },
      "optics_and_focus": {
        "lens_emulation": "DSLR 85mm"
      }
    }
  }
}
```

---

## Sydney Sweeney in Las Vegas (Urdu/Hindi Prompt)

A structured image generation prompt written in Urdu/Hindi (Romanized) detailing a scene of Sydney Sweeney in a lemon yellow corset dress on a Las Vegas rooftop, including specific accessories like a

```text
[
  {
    "tasveer_ka_unwan": "Sydney Sweeney in Las Vegas",
    "shaksiyat_ka_naam": "{argument name="celebrity name" default="Sydney Sweeney"}",
    "libas_ki_tafseel": {
      "noiyat": "Corset-style bodycon dress",
      "rang": "{argument name="dress color" default="Lemon Yellow (Halka Peela)"}",
      "khusoosiyat": "Front hook-and-eye details, sleeveless, square neckline",
      "fabric": "Structured cotton blend"
    },
    "makeup_aur_baal": {
      "baalo_ka_style": "Half-up, half-down ponytail jiske aage ki latein (strands) chehre par giri hui hain",
      "baalo_ka_rang": "Golden Blonde",
      "makeup": "Soft glam, nude lip gloss, aur natural eye makeup"
    },
    "zewrat_aur_accessories": {
      "gale_ka_haar": "Chunky silver chain jismein dil (heart) wala pendant hai",
      "kaano_ki_baaliyan": "Chote heere ke studs",
      "anguthiyan": "Dono haathon ki ungliyon mein multiple silver rings",
      "handbag": "Louis Vuitton Neverfull tote bag (Classic Brown Monogram)"
    },
    "location_aur_mahaul": {
      "shehar": "Las Vegas, Nevada",
      "muqam": "Bellagio Hotel ka rooftop terrace (mumkina taur par Spago restaurant)",
      "view": "Bellagio Fountains aur Eiffel Tower (Paris Las Vegas) ka manzar",
      "mausam": "Saaf neela aasman aur dhoop wala din"
    },
    "tasveer_ke_khass_ajza": [
      "Table par rakha hua menu card aur plate",
      "Striped (dhari-daar) sofa cushions (harkat-e-sabz aur safed)",
      "Lip gloss lagane ka amal",
      "Glass railing jo balcony ko cover kar rahi hai"
    ],
    "vibe": "Chic, luxury lifestyle, summer fashion"
  }
]
```

---

## Sydney Sweeney in Pale Pink Corset Dress (Las Vegas)

A structured prompt detailing a high-fashion summer aesthetic image of Sydney Sweeney on a Las Vegas rooftop, wearing a pale pink corset dress and holding a Louis Vuitton tote bag, with the Bellagio F

```text
[ { "image_title": "Sydney Sweeney in Las Vegas", "person_name": "{argument name="person name" default="Sydney Sweeney"}", "clothing_details": { "type": "Corset-style bodycon dress", "color": "{argument name="dress color" default="Pale pink (light pink)"}", "features": "Front hook-and-eye details, sleeveless, square neckline", "fabric": "Structured cotton blend" }, "makeup_and_hair": { "hair_style": "Half-up, half-down ponytail with face-framing strands", "hair_color": "Golden Blonde", "makeup": "Soft glam, nude lip gloss, and natural eye makeup" }, "jewelry_and_accessories": { "necklace": "Chunky silver chain with a heart pendant", "earrings": "Small diamond studs", "rings": "Multiple silver rings on both hands", "handbag": "Louis Vuitton Neverfull tote bag (Classic Brown Monogram)" }, "location_and_setting": { "city": "Las Vegas, Nevada", "location": "Bellagio Hotel rooftop terrace (possibly Spago restaurant)", "view": "View of the Bellagio Fountains and Eiffel Tower (Paris Las Vegas)", "weather": "Clear blue sky and sunny day" }, "key_image_elements": [ "Menu card and plate on the table", "Striped sofa cushions (green and white)", "Applying lip gloss", "Glass railing covering the balcony" ], "vibe": "Chic, luxury lifestyle, summer fashion" } ]
```

---

## Sydney Sweeney Madame Web Premiere Gown Description

A JSON prompt detailing the appearance of Sydney Sweeney at the Madame Web premiere, focusing on her hair, makeup, pose, and the intricate black sequined 'cobweb' pattern on her custom floor-length, s

```text
{
  "subject": {
    "name": "Sydney Sweeney",
    "features": {
      "hair": "Long, voluminous blonde hair styled in soft, classic Hollywood waves with a middle part; warm honey and champagne tones.",
      "eyes": "Pale blue/green eyes with a subtle 'siren eye' makeup look.",
      "makeup": "Dewy, luminous skin finish; soft peach-pink blush; glossy rose-pink lips; winged black eyeliner with shimmering neutral eyeshadow.",
      "pose": "Red carpet stance; mix of front-facing and three-quarter profiles; hands resting naturally at hips."
    }
  },
  "attire": {
    "dress_style": "Custom floor-length, strapless column gown with a sweetheart neckline.",
    "color_palette": "Nude/beige base layered with intricate black detailing.",
    "textural_details": {
      "embroidery": "Intricate black sequined 'cobweb' or 'lattice' pattern sprawling across the bodice and hips.",
      "skirt": "Transitioning into a dense
```

---

## Sydney Sweeney Nightclub Look (Hindi/Urdu JSON)

A structured JSON prompt, written primarily in Hindi/Urdu (using Romanized script), for the Gemini Nano Banana Pro model to generate three different images of Sydney Sweeney in a nightclub setting. It

```text
{
  "album_maloomat": {
    "shakhsiyat": "Sydney Sweeney",
    "paisha": "American Actress",
    "location": "Lounge / Nightclub jaisa mahool",
    "light": "Neon blue aur pink lighting",
    "libas_ki_tafseel": {
      "kism": "Ruched Bodycon Dress",
      "rang": "Tan / Nude",
      "length": "Midi length (ghutno tak)",
      "gala": "Deep V-neck"
    }
  },
  "tasveer_details": [
    {
      "file_name": "20260209_200356.jpg",
      "pose": "Seedha khadi hain, dono haath kamar par (hips) rakhe hue, muskurata hua chehra.",
      "accessories": "Bade sunhairi (gold) hoop earrings.",
      "background": "Lounge ki red velvet kursi aur lakdi ke pillar."
    },
    {
      "file_name": "20260209_200348.jpg",
      "pose": "Ek haath chehre (chin) ke paas hai aur deewar se halka tek lagaya hua hai.",
      "expression": "Narm aur pur-aitmad (confident) muskurahat."
    },
    {
      "file_name": "20260209_200340.jpg",
      "pose": "Side profile pose, jis mein dress ka ruched design aur strap nazar aa rahe hain.",
      "baal": "Sunehri (blonde) wavy baal jo kandhon par gire hue hain."
    }
  ]
}
```

---

## Sydney Sweeney Over-the-Shoulder Smile in Las Vegas

A structured prompt detailing a cheerful, luxurious portrait of Sydney Sweeney on the Bellagio rooftop terrace, captured from the back looking over her shoulder, emphasizing her pale pink corset dress

```text
[
  {
    "image_title": "Sydney Sweeney Over-the-Shoulder Smile in Las Vegas",
    "person_name": "{argument name="person name" default="Sydney Sweeney"}",
    "pose_details": {
      "angle": "Back angle, looking over her shoulder toward the camera",
      "expression": "Big, joyful smile with teeth showing",
      "posture": "Standing, slightly turned"
    },
    "clothing_details": {
      "type": "Corset-style bodycon dress",
      "color": "{argument name="dress color" default="Pale pink"}",
      "features": "Visible back seams, sleeveless with straps, structured fit",
      "fabric": "Structured cotton blend"
    },
    "makeup_and_hair": {
      "hair_style": "High half-up, half-down ponytail with wavy blonde lengths and face-framing strands",
      "hair_color": "Golden Blonde",
      "makeup": "Soft glam, defined lashes, and natural pink lip"
    },
    "jewelry_and_accessories": {
      "necklace": "Chunky silver chain",
      "earrings": "Small silver drop earrings",
      "rings": "Multiple silver bands on her fingers"
    },
    "location_and_setting": {
      "city": "Las Vegas, Nevada",
      "location": "Bellagio rooftop terrace",
      "background_elements": [
        "Eiffel Tower (Paris Las Vegas) in the distance",
        "Bellagio Fountains",
        "Clear blue sunny sky"
      ]
    },
    "key_foreground_elements": [
      "Glass balcony railing",
      "Green and white striped sofa cushions",
      "Louis Vuitton Monogram Neverfull bags sitting on the sofa",
      "White tablecloth in the corner"
    ],
    "vibe": "Cheerful, luxurious, high-fashion summer aesthetic"
  }
]
```

---

## Sydney Sweeney Wardrobe Selection Generator (4 Scenes)

A JSON prompt designed to generate four distinct images of Sydney Sweeney, each showcasing a different outfit and environment: a wetsuit on a lake boat, a cream suit on a luxury yacht at sunset, an em

```text
{
  "subject": "{argument name="subject name" default="Sydney Sweeney"}",
  "images": [
    {
      "id": "image_01",
      "scene": "Boat on Lake",
      "description": "Sydney Sweeney relaxing on a boat with a German Shepherd.",
      "action": "Hugging a large dog",
      "clothing": {
        "item": "Wetsuit  Swimwear",
        "color": "Black",
        "style": "Long sleeve, sleek"
      },
      "environment": {
        "location": "Lake",
        "background": "Pine forest and water",
        "lighting": "Daylight"
      }
    },
    {
      "id": "image_02",
      "scene": "Luxury Yacht",
      "description": "Sydney Sweeney standing on a yacht deck at sunset.",
      "action": "Holding a champagne glass, posing elegantly",
      "clothing": {
        "item": "Suit",
        "color": "Cream / Off-white",
        "style": "Oversized blazer, trousers, silk camisole",
        "accessories": "Layered necklaces"
      },
      "environment": {
        "location": "Coastal sea",
        "background": "Coastline with hills and buildings",
        "lighting": "Golden hour  Sunset"
      }
    },
    {
      "id": "image_03",
      "scene": "Luxury Interior",
      "description": "Sydney Sweeney sitting in an opulent hotel lobby or hall.",
      "action": "Sitting and smiling",
      "clothing": {
        "item": "Evening Gown",
        "color": "Emerald Green",
        "style": "Satin fabric with gold floral embroidery on the bodice",
        "accessories": "Gold clutch bag, drop earrings"
      },
      "environment": {
        "location": "Hotel Lobby / Ballroom",
        "background": "Marble columns, chandeliers",
        "lighting": "Warm indoor lighting"
      }
    },
    {
      "id": "image_04",
      "scene": "Park Bench",
      "description": "Sydney Sweeney sitting on a wooden bench in a park.",
      "action": "Resting with a book",
      "clothing": {
        "item": "Casual Outfit",
        "style": "Floral midi dress with denim jacket",
        "footwear": "Brown sandals",
        "accessories": "Brown leather tote bag"
      },
      "environment": {
        "location": "Public Park",
        "background": "Green trees, garden path",
        "lighting": "Soft daylight"
      }
    }
  ]
}
```

---

## Technical Outerwear Campaign Poster Generation Prompt

A smart prompt designed to generate a technical outerwear campaign poster by automatically selecting a relevant performance fashion label for collaboration with a specified brand.

```text
Technical outerwear campaign poster

This prompt creates a collab between {argument name="your brand" default="[YOUR BRAND]"} and a relevant performance fashion label

(it automatically picks you a good fit)
```

---

## Text Prompt for Boutique Olive Oil Brand Social Media Feed

A simple text prompt used to generate a series of images suitable for a social media feed, specifically for a boutique olive oil brand. This demonstrates the model's ability to handle product photogra

```text
Create a social media feed for a boutique olive oil brand.
```

---

## Travel Editorial Portrait on Railay Beach

Creates an ultra-realistic cinematic half-body portrait suitable for a travel editorial at Railay Beach, Thailand.

```text
Ultra-realistic cinematic half-body portrait (waist-up) of me standing on Railay Beach, Thailand, with dramatic limestone cliffs rising behind and turquoise Andaman Sea waves softly blurred in the background.
I am wearing a coordinated beach outfit: relaxed off-white linen shirt (visible upper portion), classic sunglasses, minimalist wristwatch partially visible, styled naturally for a travel editorial shoot.
Natural but perfectly styled hair suitable for professional photography.
Golden-hour sunlight with warm skin tones, soft sea breeze subtly moving hair and fabric, realistic skin texture, no retouching.
DSLR photo, 85mm lens, f/2.8, shallow depth of field, high dynamic range, travel editorial style, sharp facial focus, cinematic framing.
```

---

## Turn photo into a Lamborghini ad

A very short prompt for transforming an existing image into something that looks like a Lamborghini advertisement.

```text
make this a {argument name="brand" default="lamborghini"} ad
```

---

## Two Women on Luxury Balcony at Night (Image-to-Image Prompt)

A complex, multi-subject prompt designed for image-to-image generation (using two selfie references) to create a scene of two glamorous women on a luxury hotel balcony overlooking a city skyline at ni

```text
{
"prompt": {
"subjects": [
{
"name": "brunette_woman",
"source":"use exact face from first image reference. 100% face fidelity",
"appearance": {
"hair": "Long, voluminous, dark chocolate brown, silky straight with center-part and bangs",
"skin_tone": "Smooth olive",
"lips": "Red matte, softly parted",
"Make-up": "bold glamour",
"expression": "Seductive eyes looking over shoulder"
},
"clothing": {
"top": "Black sheer chiffon blouse, unbuttoned just enough",
"bottom": "Tailored cream trousers, low on hips"
},
"pose": "Standing behind, hands resting lightly on the waist of the second woman, body close almost hugging from behind",
"position": "Left side of frame"
},
{
"name": "honey_blonde_woman",
"source":"use exact face from second image reference. 100% face fidelity",
"appearance": {
"hair": "Long honey-blonde styled in a high ponytail and half-down, half-up",
"eyes": "Looking up at city lights",
"lips": "glossy pink, slight smile",
"make up":"soft glamour",
"expression": "Dreamy upward gaze with subtle invitation"
},
"clothing": {
"top": "Champagne silk slip mini dress, thin straps slipping slightly",
"accessories": "Diamond stud earrings"
},
"pose": "Leaning forward on balcony railing, back gently arched, looking up at the skyline",
"position": "Right side of frame"
}
],
"environment": {
"time": "Night",
"location": "Luxury hotel balcony overlooking city",
"lighting": "Soft city glow, warm balcony lights",
"background_objects": [
"Sparkling city skyline",
"Glass of champagne on railing",
"Plush outdoor lounge cushions",
"Distant traffic lights",
"Night sky with faint stars"
]
},
"aspect_ratio": "4:5"
}
```

---

## UI Designer Role

Optimizes product and e-commerce strategies for ui designer role.

```text
Act as a UI Designer. You are an expert in crafting intuitive and visually appealing user interfaces for digital products. Your task is to design interfaces that enhance user experience and engagement.

You will:
- Collaborate with developers and product managers to define user requirements and specifications.
- Create wireframes, prototypes, and visual designs based on project needs.
- Ensure designs are consistent with brand guidelines and accessibility standards.

Rules:
- Prioritize usability and aesthetic appeal in all designs.
- Stay updated with the latest design trends and tools.
- Incorporate feedback from user testing and iterative design processes.
```

---

## Ultra Close Photos of Celebrities in a Gym Setting

A highly structured JSON prompt for Gemini Nano Banana Pro 10k, detailing ultra-close photos of three celebrities—Ana de Armas, Anya Taylor-Joy, and Sydney Sweeney—each with specific outfits, poses, e

```text
[
  {
    "subject": "Ana de Armas",
    "appearance": {
      "hair_style": "Wavy brunette hair",
      "activity": "Sitting on a light blue yoga mat",
      "pose": "Back-facing mirror selfie"
    },
    "outfit_details": {
      "top": "Two-tone crop t-shirt in azure blue and lime green",
      "bottom": "Athletic shorts featuring a purple and teal color block design with 'SPAIN' text in orange",
      "accessories": "Red smartphone case"
    },
    "environment": "High-end fitness studio with treadmills, large glass windows, and a view of the Eiffel Tower at twilight"
  },
  {
    "subject": "Anya Taylor-Joy",
    "appearance": {
      "hair_color": "Platinum blonde",
      "expression": "Focused and tired after workout",
      "action": "Wiping forehead with a grey towel"
    },
    "outfit_details": {
      "top": "Royal blue crew neck t-shirt knotted at the waist",
      "bottom": "High-waisted neon lime green biker shorts",
      "jewelry": "Delicate silver chain necklace"
    },
    "environment": "Modern gym setting with mirrored walls and professional exercise equipment"
  },
  {
    "subject": "Sydney Sweeney",
    "appearance": {
      "complexion": "Glowy and perspiring from exercise",
      "hair": "Blonde hair tied back in a messy ponytail",
      "shot_type": "Close-up portrait selfie"
    },
    "outfit_details": {
      "clothing": "Black performance t-shirt with a small silver logo on the chest"
    },
    "environment": "Indoor commercial gym with industrial ceiling lights and weight machines"
  }
]
```

---

## Ultra-Macro Cherry in Milk Splash

Creates a hyper-realistic, ultra-macro food photograph of a cherry suspended in creamy milk splash.

```text
A single ripe {argument name="fruit type" default="cherry"} suspended in a creamy milk splash, ultra-macro food photography, glossy red skin with fine texture, soft {argument name="background color" default="pastel pink"} background, liquid frozen mid-motion, smooth flowing curves, shallow depth of field, cinematic studio lighting, hyper-realistic, high detail, luxury advertising style
```

---

## Ultra-photorealistic 8K glamour portrait of Sydney Sweeney in a strawberry-red satin gown

A concise text prompt for an ultra-detailed, 8K glamour portrait of Sydney Sweeney. It specifies her standing in a strawberry-red satin gown with a high slit, posing with intense eye contact, set in a

```text
Sydney Sweeney standing tall in a {argument name="dress color" default="strawberry-red"} satin gown, one hand on hip, other brushing her hair back, leg revealed through slit, intense eye contact, luxury runway hallway, cinematic shallow depth of field, Vogue cover style
```

---

## Ultra-Realistic Beverage Product Photography

A prompt for generating ultra-realistic product photography of a chilled aluminum soda can, featuring a custom 'Lemonate' label, floating in crystal-clear blue water with dynamic ripples and condensat

```text
-Ultra-realistic premium beverage product photography of a chilled aluminum soda can floating upright at the center of the frame, partially submerged in vivid crystal-clear blue water, with dynamic ripples and splashes radiating outward; the can features a clean yellow-and-white label design with condensation droplets across the surface, and the brand name “{argument name="brand name" default="lemonate"}” prominently displayed in bold black typography, replacing all original branding, with smaller minimalist
```

---

## Ultra-Realistic Beverage Product Photography (Lemonate)

A prompt for generating ultra-realistic product photography of a chilled aluminum soda can, featuring a custom 'Lemonate' label, floating in crystal-clear blue water with dynamic ripples and condensat

```text
Ultra-realistic premium beverage product photography of a chilled aluminum soda can floating upright at the center of the frame, partially submerged in vivid crystal-clear blue water, with dynamic ripples and splashes radiating outward; the can features a clean yellow-and-white label design with condensation droplets across the surface, and the brand name “{argument name="brand name" default="lemonate"}” prominently displayed in bold black typography, replacing all original branding, with smaller minimalist.
```

---

## Ultra-Realistic Luxury Perfume Ad

Creates ultra-realistic cinematic product photography of a luxury perfume bottle.

```text
Ultra-realistic cinematic product photography of a luxury perfume bottle filled with deep red liquid, standing upright and centered. Thick glass bottle with sharp edges and a bold sculptural cap, premium minimal label. Surrounded by dark rugged wood textures, bark, and crushed wood chips, creating a rich woody atmosphere. Dramatic red and black background with smoky haze and glowing embers, intense contrast lighting. Strong rim light highlighting the bottle silhouette, glossy reflections on glass, deep shadows for a mysterious mood. High-end fragrance advertising style, moody, sensual, powerful aesthetic, hyper-detailed textures, ultra-sharp focus, photorealistic, 8K quality.
```

---

## Ultra-Realistic Skincare Product on Wet Beach

Creates ultra-realistic product photography of a bronzing drop bottle on wet beach sand.

```text
Ultra-realistic summer skincare product photography of a bronzing drop bottle named "{argument name="product name" default="Golden Glow - Bronzing Elixir"}", rectangular matte bottle in warm sun-kissed bronze tone with a clean white cap, placed diagonally on wet beach sand as a gentle ocean wave washes over it, delicate sea foam and tiny bubbles surrounding the base. Fine sand texture visible beneath shallow clear water, golden sunlight casting natural highlights and soft shadows. Warm golden-hour beach lighting, cinematic top-down flat lay composition. 4.5 aspect ratio.
```

---

## Unexpected High-End Product Concepts Prompt

A brief, high-level prompt used to generate unexpected, high-end visual concepts for products, likely for brainstorming or moodboarding.

```text
Unexpected high-end product concepts
```

---

## Unexpected Products by Favorite Brands Prompt

A prompt template designed to generate concept art for unexpected products designed by a user's favorite brand, visualizing high-end, conceptual ideas.

```text
Unexpected products designed by your fav brands
```

---

## Vector Illustration for Five Gods of Wealth Red Packet Cover

A comprehensive prompt designed to generate a vector illustration suitable for a Lunar New Year Red Packet cover, focusing on the Five Gods of Wealth (五路财神). The style is specified as minimalist vecto

```text
矢量插画，抽象线条与曲面线条，线条画，柔美色块构成，极简主义，线条设计叠加多个不规则弧形色块五路財神轮廓，全身重彩特写，财源滚滚，福禄寿喜，仙气飘飘，自然，纹理，装饰，超现实派，具有先锋艺术、时尚字体主标题极小英文“{argument name="英文点缀" default="fashion china"}”作为点缀、大师构图，极简海报，高清画质，大师作品，获奖海报。纯白色背景，{argument name="色彩搭配" default="多巴胺的色彩搭配"}，电影海报，大片效果，典雅大方，视觉冲击力强
```

---

## Vibrant Cardinal Collage Prompt

A prompt for generating a vibrant collage image of a cardinal bird perched on a branch, emphasizing the use of torn paper pieces to form lush foliage and berries, creating an impression of dynamic ene

```text
A vibrant collage depicts a cardinal bird perched on a branch. The bird's eye is sharp and alert, and its beak is pointed. The background is a riot of color, with torn pieces of paper forming lush green foliage and clusters of red berries. The overall impression is one of dynamic energy and natural beauty.
```

---

## Video Animation Prompt (Sneakers Falling)

A prompt structure for generating a video animation using start/end frames, specifying a handheld smartphone video style. The scene involves a pair of sneakers falling from the sky into a box placed o

```text
Prompt Structure:
Handheld smartphone video style
The video starts with a street level perspective of a box on top of a building. Suddenly, a pair of sneakers falls into the box from the sky
```

---

## Vintage 1950s Detergent Ad Recreation Prompt

A detailed JSON prompt designed to recreate a vintage 1950s print advertisement aesthetic, featuring a confident housewife and her impressed husband, complete with specific branding elements like the

```text
{
  "format": { "aspect_ratio": "9:16" },
  "subject": {
    "description": "A confident housewife proudly holding freshly washed shirts while her husband looks impressed.",
    "pose": "wife holding laundry basket, husband inspecting shirt",
    "clothing": {
      "wife": "short-sleeve dress with apron",
      "husband": "undershirt and slacks"
    }
  },
  "branding": {
    "logo": {
      "brand": "Tide",
      "logo_type": "vintage Tide bullseye logo",
      "color": "orange and blue",
      "placement": "upper third center",
      "size": "large"
    },
    "slogan": {
      "text": "{argument name="slogan text" default="SHE KNOWS WHAT WORKS"}",
      "font_style": "bold condensed sans-serif",
      "letter_spacing": "tight",
      "case": "all caps",
      "color": "blue",
      "placement": "lower third center",
      "text_rules": ["strong contrast", "1950s print look"]
    }
  },
  "background": {
    "setting": "classic laundry room",
    "atmosphere": "confident, reassuring, practical"
  }
}
```

---

## Viral Chrome Pink BMW Selfie Prompt (JSON format)

A highly detailed JSON prompt for generating a 'viral' style selfie image featuring a young woman with 'main character energy' leaning against a chrome pink BMW i8. It specifies the subject's pose, ex

```text
{
  "subject": {
    "description": "Young woman taking selfie next to chrome pink BMW i8, casual main character energy",
    "setting_rules": "street scene, luxury car, urban modern backdrop",
    "age": "early 20s",

    "expression": {
      "eyes": "focused on phone screen, taking selfie, casual confidence",
      "mouth": "relaxed, soft, natural",
      "brows": "relaxed, effortless",
      "overall": "unbothered, 'just casually next to a pink supercar' energy"
    },

    "hair": {
      "color": "platinum blonde",
      "style": "loose, flowing from under cap",
      "details": "messy-pretty, some pieces falling forward, effortless waves",
      "length": "medium-long, past shoulders"
    },

    "body": {
      "frame": "petite, slim, toned",
      "waist": "tiny, fully exposed midriff",
      "legs": "toned, athletic, fully visible",
      "stance": "casual lean against car, weight shifted"
    },

    "pose": {
      "position": "standing next to driver door of car, leaning slightly against it",
      "upper_body": {
        "action": "one arm UP holding phone for selfie",
        "phone_angle": "high, classic selfie position",
        "other_arm": "relaxed at side"
      },
      "lower_body": {
        "stance": "one leg straight, one slightly crossed or bent",
        "weight": "casual lean, hip near car",
        "energy": "relaxed but aware of angles"
      },
      "overall": "the 'caught me with this random supercar' pose that's definitely not random"
    },

    "clothing": {
      "top": {
        "type": "ultra cropped baby tee",
        "color": "bright YELLOW, sunshine yellow",
        "graphic": "small star or cute graphic on chest (or BANANA logo)",
        "fit": {
          "length": "EXTREME crop - ends just below chest, full stomach exposed",
          "tightness": "fitted, hugging curves",
          "sleeves": "short sleeves, casual"
        },
        "effect": "entire midriff visible from just under chest to shorts"
      },
      "bottom": {
        "type": "ultra mini athletic shorts",
        "color": "WHITE, clean bright white",
        "fit": {
          "style": "tight fitted athletic shorts",
          "length": "very short, upper thigh",
          "waist": "high-waisted, sits at natural waist",
          "effect": "shows full leg length, hugs curves"
        },
        "material": "stretchy athletic fabric, smooth"
      },
      "shoes": {
        "type": "white sneakers",
        "style": "clean, casual, athletic vibe",
        "effect": "completes sporty-cute look"
      }
    },

    "face": {
      "features": "pretty, big eyes, small nose, soft lips",
      "makeup": "natural, minimal, fresh-faced",
      "expression": "focused on selfie, casual pretty"
    }
  },

  "accessories": {
    "headwear": {
      "type": "baseball cap",
      "color": "BLACK",
      "style": "worn forward, classic",
      "logo": "small pa"
```

---

## Viral Slideshow Prompt: Pink BMW Selfie

A highly structured JSON prompt detailing the generation of a photorealistic image for a slideshow, featuring a young woman taking a selfie next to a chrome pink BMW i8, emphasizing specific clothing,

```text
{
  "subject": {
    "description": "Young woman taking selfie next to chrome pink BMW i8, casual main character energy",
    "setting_rules": "street scene, luxury car, urban modern backdrop",
    "age": "early 20s",

    "expression": {
      "eyes": "focused on phone screen, taking selfie, casual confidence",
      "mouth": "relaxed, soft, natural",
      "brows": "relaxed, effortless",
      "overall": "unbothered, 'just casually next to a pink supercar' energy"
    },

    "hair": {
      "color": "platinum blonde",
      "style": "loose, flowing from under cap",
      "details": "messy-pretty, some pieces falling forward, effortless waves",
      "length": "medium-long, past shoulders"
    },

    "body": {
      "frame": "petite, slim, toned",
      "waist": "tiny, fully exposed midriff",
      "legs": "toned, athletic, fully visible",
      "stance": "casual lean against car, weight shifted"
    },

    "pose": {
      "position": "standing next to driver door of car, leaning slightly against it",
      "upper_body": {
        "action": "one arm UP holding phone for selfie",
        "phone_angle": "high, classic selfie position",
        "other_arm": "relaxed at side"
      },
      "lower_body": {
        "stance": "one leg straight, one slightly crossed or bent",
        "weight": "casual lean, hip near car",
        "energy": "relaxed but aware of angles"
      },
      "overall": "the 'caught me with this random supercar' pose that's definitely not random"
    },

    "clothing": {
      "top": {
        "type": "ultra cropped baby tee",
        "color": "bright YELLOW, sunshine yellow",
        "graphic": "small star or cute graphic on chest (or BANANA logo)",
        "fit": {
          "length": "EXTREME crop - ends just below chest, full stomach exposed",
          "tightness": "fitted, hugging curves",
          "sleeves": "short sleeves, casual"
        },
        "effect": "entire midriff visible from just under chest to shorts"
      },
      "bottom": {
        "type": "ultra mini athletic shorts",
        "color": "WHITE, clean bright white",
        "fit": {
          "style": "tight fitted athletic shorts",
          "length": "very short, upper thigh",
          "waist": "high-waisted, sits at natural waist",
          "effect": "shows full leg length, hugs curves"
        },
        "material": "stretchy athletic fabric, smooth"
      },
      "shoes": {
        "type": "white sneakers",
        "style": "clean, casual, athletic vibe",
        "effect": "completes sporty-cute look"
      }
    },

    "face": {
      "features": "pretty, big eyes, small nose, soft lips",
      "makeup": "natural, minimal, fresh-faced",
      "expression": "focused on selfie, casual pretty"
    }
  },

  "accessories": {
    "headwear": {
      "type": "baseball cap",
      "color": "BLACK",
      "style": "worn forward, classic",
      "logo": "small pa"
    }
  }
}
```

---

## Y2K Grunge Denim Fashion Collage

A detailed JSON prompt for generating a four-panel asymmetrical collage in the style of high-end fashion photography (American Eagle campaign), featuring a subject (Sydney Sweeney) in baggy, low-rise

```text
{
  "file_metadata": {
    "filename": "sydney_sweeney_ae_campaign_collage.jpg",
    "category": "High-End Fashion Photography",
    "project": "American Eagle Denim Collection 2024",
    "talent": "{argument name="model name" default="Sydney Sweeney"}"
  },
  "visual_composition": {
    "layout_type": "4-Panel Asymmetrical Collage",
    "color_palette": {
      "primary": "Indigo Blue (Denim Wash)",
      "secondary": "Creamy White (Top & Background)",
      "accent": "Dusty Rose / Blush Pink (Butterfly Detail)",
      "vibe": "Warm, Nostalgic, Y2K Grunge"
    },
    "lighting": "Soft diffused studio light with warm highlight tones",
    "aesthetic_tags": ["Vintage Revival", "Baggy Silhouette", "Main Character Energy"]
  },
  "detailed_frame_analysis": {
    "panel_1_left": {
      "focus": "Full Body Silhouette",
      "pose": "Mirror selfie aesthetic with a slight lean",
      "outfit_details": {
        "top": "White ribbed racerback crop tank",
        "bottom": "Extra wide-leg low-rise indigo jeans",
        "footwear": "White pointed-toe stilettos",
        "accessories": "Delicate gold bracelets and a floral-patterned phone case"
      }
    },
    "panel_2_top_right": {
      "focus": "Beauty & Expression",
      "pose": "Reclined, looking directly into the lens",
      "styling": "Oversized denim jacket draped off-the-shoulder",
      "hair": "Center-parted blonde waves with natural volume",
      "makeup": "Minimalist 'Clean Girl' look with dewy skin"
    },
    "panel_3_bottom_center": {
      "focus": "Product Detail & Embroidery",
      "subject": "Denim back pocket",
      "features": [
        "Intricate pink and orange butterfly embroidery",
        "Pink leather brand patch with American Eagle logo",
        "Contrast stitching on heavy-duty denim fabric"
      ]
    },
    "panel_4_bottom_right": {
      "focus": "Style Statement",
      "pose": "Symmetrical crouched pose on a dark background",
      "outfit": "Full denim jumpsuit/set (Double Denim)",
      "mood": "Bold and confident"
    }
  },
  "garment_dna": {
    "fabric": "Non-stretch, premium weight cotton denim",
    "wash": "Medium indigo stone-wash with vintage fading",
    "fit_profile": "Loose, oversized, baggy, and low-slung waist"
  },
  "marketing_tags": {
    "target_audience": "Gen-Z and Millennial Fashion Seekers",
    "trending_hashtags": [
    "alt_text": "A fashion collage of Sydney Sweeney for American Eagle showcasing wide-leg jeans with butterfly embroidery and a white crop top in various professional poses."
  }
}
```

---

## Y2K Kawaii Fashion Editorial Prompt

A highly detailed, structured JSON prompt for generating a multi-panel, consistent Y2K Kawaii-fashion editorial image, focusing on extreme wide-angle perspective, hyper-feminine aesthetic, and specifi

```text
{
  "meta_control": {
    "generation_mode": "multi_panel_consistent",
    "priority_stack": ["identity_lock", "perspective_physics", "material_fidelity", "environmental_coherence"],
    "quality_target": "editorial_print_ready"
  },
  "intent": {
    "primary": "Y2K Kawaii-fashion editorial with extreme wide-angle perspective study",
    "secondary": "Technical demonstration of foreshortening in a hyper-feminine aesthetic",
    "publication_context": "Double-page spread, pop-culture magazine collage layout"
  },
  "frame": {
    "aspect_ratio": "9:16",
    "layout": {
      "type": "2x2 grid collage",
      "gutter_width": "2px pink or seamless",
      "panel_uniformity": "identical dimensions per panel"
    }
  },
  "subject": {
    "type": "Human female fashion model",
    "identity_lock": {
      "enforcement_level": "strict",
      "anchor_features": ["face_geometry", "skin_tone", "body_proportions", "hair_color"]
    },
    "biometrics": {
      "age_presentation": "20-24",
      "height_cm": 170,
      "build": "Slender, petite model frame",
      "ethnicity_presentation": "Caucasian / Northern European features"
    },
    "facial_signature": {
      "structure": "Soft oval face shape, full cheeks, rounded feminine jawline",
      "eyes": "Large, expressive, bright blue, defined lashes with rhinestone accents",
      "nose": "Small, delicate button nose, slightly upturned",
      "lips": "Very full, plush and pillowy, glossy bubblegum pink",
      "skin": "Porcelain fair, smooth texture, heavy blush on nose and cheeks, highlighter glow",
      "expression_default": "Playful cute, duck face, winking, blowing kiss"
    },
    "hair": {
      "style": "Long golden blonde hair, half-up pigtails with fluffy scrunchies",
      "texture": "Silky, voluminous, crimped sections",
      "behavior": "Bouncing, dynamic movement"
    },
    "wardrobe": {
      "jacket": {
        "item": "Cropped faux-fur jacket",
        "material": "High-pile mongolian fur",
        "color": "Pastel baby pink",
        "state": "Slouched off shoulders",
        "light_behavior": "Soft diffusion, halo effect on fur tips"
      },
      "top": {
        "item": "Heart-shaped corset top",
        "material": "Satin with all-over rhinestone coverage",
        "color": "Hot pink",
        "fit": "Structured, push-up",
        "details": "Crystal straps, glitter trim"
      },
      "pants": {
        "item": "Wide-leg parachute pants",
        "material": "Iridescent nylon fabric",
        "color": "Metallic rose gold",
        "details": "Drawstrings, butterfly patches, sequin pockets"
      },
      "footwear": {
        "item": "Mega-platform boots",
        "color": "White patent leather with glitter soles",
        "condition": "Pristine, reflective",
        "details": "Furry leg warmers attached"
      }
    },
    "accessories": {
      "neck": "Choker with large heart-shaped pendant"
    }
  }
```

---

## Y2K Surreal After-Party Glamour

A highly stylized prompt for generating a surreal, high-fashion image of Ana de Armas lying decadently on a red and black marble bathroom vanity at 3:00 AM. The aesthetic is inspired by Guy Bourdin an

```text
{
  "version": "1.0",
  "aspect_ratio": "3:4",
  "subject": {
    "identity": "{argument name="subject identity" default="Ana de Armas"}",
    "fidelity": "Exact facial preservation, high-detail skin texture",
    "expression": {
      "eyes": "Light blue",
      "mouth": "Red lipstick",
      "gaze": "Lazy, confident, post-party fatigue",
      "mood": "Decadent, surreal glamour, beautiful discomfort"
    },
    "pose": {
      "position": "Lying on red and black marble bathroom vanity watching in camera",
      "body_language": "Elegantly lying on marble countertops with head looking in camera",
      "legs": "Both legs raised with knee bent and foot on vanity edge",
      "hands": "One hand resting on belly and the other fall down"
    }
  },
  "wardrobe_accessories": {
    "clothing": "Form-fitting silver metallic mini-dress, iridescent purple accents, sweetheart neckline, reflective sequin texture, hem ridden up to reveal upper thigh",
    "jewelry": [
      "Long dangling diamond earrings",
      "Stacked beaded bracelets",
      "Elegant luxury wristwatch"
    ],
    "footwear": "High heels"
  },
  "environment": {
    "setting": "Luxury bathroom at 3:00 AM",
    "materials": "Red and black marble countertops, gold-finished fixtures",
    "key_elements": "Large floor-to-ceiling mirror behind subject, multiplying reflections of back and profile",
    "props": "Scattered champagne glass, decadent party debris"
  },
  "lighting_style": {
    "aesthetic": "Guy Bourdin surrealism mixed with Y2K millennium flash",
    "key_light": "Direct on-camera flash (high-intensity, Y2K style)",
    "accent_lights": {
      "camera_left": "Hot pink and magenta wash",
      "camera_right": "Electric cyan and blue rim lighting"
    },
    "effects": "High saturation light play on marble, mirror reflections creating voyeuristic tension, subtle halation on sequin highlights"
  },
  "technical_specs": {
    "camera": "35mm film aesthetic",
    "lens": "35mm wide-angle at f/2.8",
    "angle": "Slightly low angle to emphasize height and dominance",
    "focus": "Sharp focus on eyes and dress texture",
    "film_stock_simulation": {
      "contrast": "High",
      "grain": "Fine film grain",
      "color_grading": "Punchy, saturated, high-fashion editorial"
    }
  }
}
```

---

## Y2K Surreal After-Party Glamour (Duplicate)

A highly stylized prompt for generating a surreal, high-fashion image of Josephine Langford (or similar subject) lying decadently on a red and black marble bathroom vanity at 3:00 AM. The aesthetic is

```text
{
  "version": "1.0",
  "aspect_ratio": "3:4",
  "subject": {
    "identity": "{argument name="subject identity" default="Josephine Langford"}",
    "fidelity": "Exact facial preservation, high-detail skin texture",
    "expression": {
      "eyes": "Light blue",
      "mouth": "Red lipstick",
      "gaze": "Lazy, confident, post-party fatigue",
      "mood": "Decadent, surreal glamour, beautiful discomfort"
    },
    "pose": {
      "position": "sitting on red and black marble bathroom vanity watching in camera",
      "body_language": "Elegantly lying on marble countertops with head looking in camera",
      "legs": "Both legs raised with knee bent and foot on vanity edge",
      "hands": "One hand resting on belly and the other fall down"
    }
  },
  "wardrobe_accessories": {
    "clothing": "Form-fitting silver metallic mini-dress, iridescent purple accents, sweetheart neckline, reflective sequin texture, hem ridden up to reveal upper thigh",
    "jewelry": [
      "Long dangling diamond earrings",
      "Stacked beaded bracelets",
      "Elegant luxury wristwatch"
    ],
    "footwear": "High heels"
  },
  "environment": {
    "setting": "Luxury bathroom at 3:00 AM",
    "materials": "Red and black marble countertops, gold-finished fixtures",
    "key_elements": "Large floor-to-ceiling mirror behind subject, multiplying reflections of back and profile",
    "props": "Scattered champagne glass, decadent party debris"
  },
  "lighting_style": {
    "aesthetic": "Guy Bourdin surrealism mixed with Y2K millennium flash",
    "key_light": "Direct on-camera flash (high-intensity, Y2K style)",
    "accent_lights": {
      "camera_left": "Hot pink and magenta wash",
      "camera_right": "Electric cyan and blue rim lighting"
    },
    "effects": "High saturation light play on marble, mirror reflections creating voyeuristic tension, subtle halation on sequin highlights"
  },
  "technical_specs": {
    "camera": "35mm film aesthetic",
    "lens": "35mm wide-angle at f/2.8",
    "angle": "Slightly low angle to emphasize height and dominance",
    "focus": "Sharp focus on eyes and dress texture",
    "film_stock_simulation": {
      "contrast": "High",
      "grain": "Fine film grain",
      "color_grading": "Punchy, saturated, high-fashion editorial"
    }
  }
}
```

---

## Zhao Lusi Casual Editorial Look

A structured prompt designed to generate images of Chinese actress Zhao Lusi in a casual, relaxed at-home setting, focusing on the 'clean girl aesthetic' and youthful playfulness. It specifies her out

```text
{
  "subject": {
    "name": "{argument name=\"subject name\" default=\"Zhao Lusi\"}",
    "also_known_as": "Rosy Zhao",
    "profession": "Chinese actress",
    "known_for": [
      "The Romance of Tiger and Rose",
      "Hidden Love"
    ],
    "appearance": {
      "hair": "Long, wavy dark hair parted in the middle",
      "makeup": "Minimalist glass-skin look with soft coral/peach tones on lips and cheeks",
      "skin": "Natural, dewy, radiant finish",
      "expression_style": "Soft, youthful, charming"
    }
  },
  "outfit": {
    "top": "Oversized pink T-shirt with white cat graphic and blue banner text 'HOLIDAY'",
    "bottom": "Simple grey jersey shorts",
    "style": "Casual lounge set"
  },
  "aesthetic": {
    "theme": "Relaxed at-home vibe",
    "style_keywords": [
      "clean girl aesthetic",
      "youthful playfulness",
      "soft editorial",
      "natural beauty"
    ],
    "lighting": "Soft, diffused lighting enhancing glossy skin texture"
  },
  "scenes": [
    {
      "image": 1,
      "setting": "Domestic interior with light wood furniture and storage bins",
      "pose": "Candid-style",
      "expression": "Soft and contemplative"
    },
    {
      "image": 2,
      "setting": "Neutral wall background",
      "pose": "Leaning against wall with arms crossed",
      "expression": "Bright, direct smile"
    },
    {
      "image": 3,
      "setting": "Reflective watery surface with soft blue/white gradient backdrop",
      "pose": "Full-body crouching pose",
      "vibe": "Casual outfit with high-fashion editorial feel"
    }
  ],
  "image_specs": {
    "width": 504,
    "height": 1002,
    "orientation": "vertical"
  }
}
```

---

## Zhao Lusi Radiant Rosy Collection

A structured JSON prompt defining four different looks for a subject resembling actress Zhao Lusi, emphasizing a 'glistening/dewy' skin texture and hyper-realism. The looks range from casual summer to

```text
{
  "collection_name": "Radiant Rosy",
  "subject": {
    "description": "A young woman with soft, symmetrical features, large expressive eyes, and a radiant smile.",
    "inspiration": "Resembles South Korean actress and model Zhao Lusi (Rosy Zhao)",
    "hair": {
      "color": "Chestnut brown",
      "styles": ["flowing waves", "sophisticated half-updo", "damp textured look"]
    },
    "skin": {
      "texture": "Glistening/dewy, 'honey skin' or 'glass skin', moisture-drenched effect"
    }
  },
  "aesthetic": "Hyper-realistic, wet-look, versatile fashion styles ranging from casual summer to high-fashion elegance",
  "images": [
    {
      "title": "Tropical Summer Look",
      "description": "Profile view, vibrant floral-print tube top and matching skirt. Bright blue base with orange hibiscus patterns. Lighting emphasizes athletic silhouette.",
      "outfit": "Floral tube top & skirt",
      "lighting": "Bright, emphasizing contours",
      "style": "Casual summer"
    },
    {
      "title": "Elegant Mini",
      "description": "Playful 'girl-next-door' vibe. Champagne-colored satin mini dress with intricate white lace collar. Holding a smartphone, confident pose.",
      "outfit": "Champagne satin mini dress with lace collar",
      "props": ["smartphone"],
      "style": "Modern lifestyle with classic fashion"
    },
    {
      "title": "High-Fashion Editorial",
      "description": "Luxury look with sheer, intricately embroidered lace gown in soft cream hue. Accented by high-end jewelry. Moody teal-and-warm studio lighting.",
      "outfit": "Sheer embroidered lace gown",
      "accessories": ["sparkling bracelet", "drop earrings"],
      "lighting": "Teal-and-warm professional studio",
      "style": "High-fashion editorial"
    },
    {
      "title": "Dewy Close-Up",
      "description": "Intimate facial portrait, skin and hair appear drenched, hyper-realistic water droplets. Warm, inviting expression. Perfect dental aesthetics.",
      "accessories": ["pearl drop earrings"],
      "focus": "Face close-up",
      "style": "Hyper-realistic, wet-look portrait"
    }
  ],
  "image_dimensions": {
    "width": 504,
    "height": 1002,
    "orientation": "vertical"
  }
}
```

---

## Zhao Lusi Red Carpet Gothic Chic Portrait

Creates a photorealistic image of Zhao Lusi on a red carpet with gothic chic style and a dramatic black lace gown.

```text
{
  "subject": {
    "name": "{argument name="celebrity name" default="Zhao Lusi"}",
    "aliases": ["Rosy Zhao"],
    "profession": "Chinese actress",
    "pose": "graceful, waving both hands",
    "expression": "gentle, confident smile",
    "style": ["gothic chic", "youthful elegance"]
  },
  "appearance": {
    "hair": {
      "color": "dark",
      "style": "voluminous waves framing face"
    },
    "makeup": {
      "eyes": "defined",
      "lips": "soft color",
      "skin": {
        "tone": "luminous white",
        "details": "realistic sweat sheen, subtle moisture highlights on collarbones, shoulders, and cheekbones, natural skin texture visible, pores and micro-detail intact",
        "lighting": "reacts dynamically to cinematic lighting"
      }
    },
    "jewelry": [
      "chunky diamond-encrusted necklace",
      "matching bracelet"
    ]
  },
  "outfit": {
    "gown": {
      "color": "black",
      "bodice": "corset-style, very thin spaghetti straps, central bow detail, sheer midriff paneling",
      "skirt": "multi-layered ruffled lace, dramatic flowing silhouette"
    },
    "footwear": "high-platform black satin sandals"
  },
  "setting": {
    "event_type": "high-profile red carpet",
    "backdrop": "formal media wall typical of Chinese awards ceremonies or fashion galas",
    "sponsors": ["Weibo", "iQIYI", "Mango TV", "Qeelin", "Volvo"],
    "signatures": "golden scrawls of attending celebrities"
  }
}
```

---

## 电商与社交平台内容创作提示词

Optimizes product and e-commerce strategies for 电商与社交平台内容创作提示词.

```text
Act as a Content Creation Specialist for e-commerce and social media platforms like Douyin and Xiaohongshu. You are an expert in crafting engaging content that can effectively promote products and services on these platforms.

Your task is to:
- Develop creative content ideas tailored to the specific platform's audience
- Utilize platform-specific features to enhance content visibility and engagement
- Create persuasive and informative posts that highlight product benefits and unique selling points
- Adapt content style and tone to match platform trends and user preferences

Rules:
- Always research current platform trends and user behavior
- Ensure content aligns with brand messaging and objectives
- Use visuals effectively to complement text and engage viewers

Variables:
- ${platform:Douyin} - The platform for which content is being created
- ${product} - The product or service being promoted
- ${audience} - Target audience demographic
- ${tone:engaging} - Desired tone for the content
```

---

## 电商选品助手

Optimizes product and e-commerce strategies for 电商选品助手.

```text
Act as an E-commerce Product Selection Assistant. You are an expert in identifying high-potential products for online marketplaces. Your task is to help users optimize their product offerings to enhance market competitiveness.

You will:
- Analyze market trends and consumer demand data.
- Identify products with high growth potential.
- Provide recommendations on product diversification.
- Suggest strategies for competitive pricing.

Rules:
- Focus on emerging product categories.
- Avoid saturated markets unless there's a clear competitive advantage.
- Prioritize products with sustainable demand and supply chains.
```

---

