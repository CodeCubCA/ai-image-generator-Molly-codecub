"""
AI Image Generator using Streamlit and HuggingFace Inference API
"""

import os
import io
import random
from datetime import datetime
import streamlit as st
from PIL import Image
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load environment variables
load_dotenv()

# Configuration
MODEL_NAME = "black-forest-labs/FLUX.1-schnell"
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

# Alternative models (uncomment to use):
# MODEL_NAME = "stabilityai/stable-diffusion-xl-base-1.0"
# MODEL_NAME = "runwayml/stable-diffusion-v1-5"

# Image size options
IMAGE_SIZES = {
    "Square (512x512)": (512, 512),
    "Portrait (512x768)": (512, 768),
    "Landscape (768x512)": (768, 512),
}

# Style presets
STYLE_PRESETS = {
    "None": "",
    "Anime": ", anime style, vibrant colors, Studio Ghibli inspired, detailed illustration, hand-drawn aesthetic",
    "Realistic": ", photorealistic, highly detailed, 8K resolution, professional photography, sharp focus, natural lighting",
    "Digital Art": ", digital painting, artstation trending, concept art, smooth illustration, professional digital art",
    "Watercolor": ", watercolor painting, soft colors, artistic, gentle brushstrokes, traditional art style",
    "Oil Painting": ", oil painting, classical art style, textured brushwork, rich colors, fine art",
    "Cyberpunk": ", cyberpunk style, neon lights, futuristic, sci-fi, dystopian, high contrast, dark atmosphere",
    "Fantasy": ", fantasy art, magical, enchanted, epic, mystical atmosphere, otherworldly, detailed fantasy illustration",
}

# Random creative prompts for inspiration
RANDOM_PROMPTS = [
    "A cyberpunk city at sunset with neon lights reflecting on wet streets",
    "A magical forest with glowing mushrooms and floating fireflies, fantasy art",
    "A cute robot reading a book in a cozy library, digital art",
    "An astronaut riding a horse on Mars, cinematic lighting",
    "A steampunk airship flying over snowy mountains at dawn",
    "A cat wearing a wizard hat casting sparkly spells, whimsical art",
    "A futuristic sports car racing through a neon tunnel, cyberpunk style",
    "A cozy treehouse in autumn with warm golden lighting, studio ghibli style",
    "A friendly dragon sleeping on a pile of ancient books, fantasy illustration",
    "An underwater city with bioluminescent plants and glass domes",
    "A phoenix rising from flames against a starry night sky, epic art",
    "A samurai standing in a field of cherry blossoms, dramatic lighting",
    "A floating island with waterfalls and ancient ruins, fantasy landscape",
    "A friendly ghost serving tea in a haunted Victorian mansion",
    "A cosmic whale swimming through a nebula filled with stars",
]


def init_client():
    """Initialize the HuggingFace Inference Client."""
    if not HUGGINGFACE_TOKEN:
        return None
    return InferenceClient(token=HUGGINGFACE_TOKEN)


def set_random_prompt():
    """Callback to set a random prompt."""
    st.session_state.prompt_input = random.choice(RANDOM_PROMPTS)


def set_example_prompt(example):
    """Callback to set an example prompt."""
    st.session_state.prompt_input = example


def image_to_bytes(image):
    """Convert PIL Image to bytes for download."""
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer.getvalue()


def generate_image(client, prompt, negative_prompt=None, width=512, height=512):
    """Generate an image from the given prompt."""
    try:
        # Build parameters
        params = {
            "model": MODEL_NAME,
            "width": width,
            "height": height,
        }
        if negative_prompt and negative_prompt.strip():
            params["negative_prompt"] = negative_prompt.strip()

        image = client.text_to_image(prompt, **params)
        return image, None
    except Exception as e:
        return None, _handle_error(e)


def _handle_error(e):
    """Handle common API errors with user-friendly messages."""
    error_message = str(e)

    if "401" in error_message or "unauthorized" in error_message.lower():
        return "Authentication failed. Please check your HuggingFace token and ensure it has 'Write' permissions."
    elif "429" in error_message or "rate limit" in error_message.lower():
        return "Rate limit exceeded. Please wait a moment and try again. Free tier has limited requests."
    elif "503" in error_message or "service unavailable" in error_message.lower():
        return "Model is currently loading. Please wait 20-30 seconds and try again."
    elif "timeout" in error_message.lower():
        return "Request timed out. The model might be busy. Please try again."
    else:
        return f"Error generating image: {error_message}"


def main():
    # Page configuration
    st.set_page_config(
        page_title="AI Image Generator",
        page_icon="🎨",
        layout="centered"
    )

    # Custom CSS for cleaner UI
    st.markdown("""
        <style>
        .stButton > button {
            width: 100%;
            background-color: #FF6B6B;
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 0.5rem;
            font-weight: bold;
        }
        .stButton > button:hover {
            background-color: #FF5252;
        }
        .main-header {
            text-align: center;
            padding: 1rem 0;
        }
        .info-box {
            background-color: #f0f2f6;
            padding: 1rem;
            border-radius: 0.5rem;
            margin: 1rem 0;
        }
        </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown("<h1 class='main-header'>🎨 AI Image Generator</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>Generate stunning images from text descriptions using FLUX.1-schnell</p>", unsafe_allow_html=True)

    st.divider()

    # Check for API token
    if not HUGGINGFACE_TOKEN:
        st.error("⚠️ HuggingFace API token not found!")
        st.markdown("""
        **Setup Instructions:**
        1. Go to [HuggingFace Settings → Tokens](https://huggingface.co/settings/tokens)
        2. Create a new token with **Write** permissions
        3. Create a `.env` file in the project root
        4. Add: `HUGGINGFACE_TOKEN=hf_your_token_here`
        5. Restart the application
        """)
        return

    # Initialize client
    client = init_client()

    # Sidebar for style selection
    with st.sidebar:
        st.header("🎨 Style Presets")
        selected_style = st.selectbox(
            "Choose an art style:",
            options=list(STYLE_PRESETS.keys()),
            index=0,
            help="Select a style to automatically enhance your prompt"
        )

        if selected_style != "None":
            st.info(f"**Style enhancement:**\n{STYLE_PRESETS[selected_style]}")

        st.divider()
        st.markdown("### 📐 Image Settings")

        # Image size selector in sidebar
        size_option = st.selectbox(
            "Choose image dimensions:",
            options=list(IMAGE_SIZES.keys()),
            index=0
        )
        width, height = IMAGE_SIZES[size_option]

    # Main input section
    st.subheader("📝 Enter Your Prompt")

    # Initialize prompt in session state if not exists
    if "prompt_input" not in st.session_state:
        st.session_state.prompt_input = ""

    prompt = st.text_area(
        "Describe the image you want to generate:",
        placeholder="Example: A serene mountain landscape at sunset with a crystal clear lake reflecting the orange and purple sky, digital art style",
        height=100,
        label_visibility="collapsed",
        key="prompt_input"
    )

    # Reference image section
    with st.expander("📷 Use Reference Image (Optional)"):
        st.caption("Upload an image for visual reference and describe it to combine with your prompt")

        uploaded_file = st.file_uploader(
            "Choose an image...",
            type=["png", "jpg", "jpeg", "webp"],
            label_visibility="collapsed"
        )

        if uploaded_file is not None:
            uploaded_image = Image.open(uploaded_file)
            st.image(uploaded_image, caption="Your reference image", use_column_width=True)

            reference_description = st.text_input(
                "Describe your reference image:",
                placeholder="Example: a golden retriever dog sitting on grass",
                key="reference_description"
            )

            st.markdown(
                "<small style='color: #888;'>💡 <b>How to use:</b><br>"
                "1. Upload your reference image<br>"
                "2. Describe what's in your image (e.g., 'a cat with orange fur')<br>"
                "3. In the main prompt, add your style/modifications (e.g., 'in anime style, colorful background')<br>"
                "4. The AI will combine both to generate a new image</small>",
                unsafe_allow_html=True
            )
        else:
            reference_description = ""

    # Negative prompt section
    with st.expander("🚫 Negative Prompt (Optional)"):
        st.caption("Tell the AI what to avoid in the image")
        negative_prompt = st.text_input(
            "Negative prompt:",
            placeholder="What you DON'T want in the image...",
            label_visibility="collapsed",
            key="negative_prompt_input"
        )
        st.markdown(
            "<small style='color: #888;'>Examples: <code>blurry, low quality, distorted</code> · "
            "<code>dark, gloomy, scary</code> · <code>text, watermark, signature</code></small>",
            unsafe_allow_html=True
        )

    # Example prompts
    with st.expander("💡 Need inspiration? Click for example prompts"):
        examples = [
            "A futuristic city skyline at night with neon lights and flying cars",
            "A cozy coffee shop interior with warm lighting and plants, watercolor style",
            "An astronaut riding a horse on Mars, photorealistic",
            "A magical forest with glowing mushrooms and fireflies, fantasy art",
            "A steampunk mechanical owl with brass gears and emerald eyes"
        ]
        for example in examples:
            st.button(example, key=example, on_click=set_example_prompt, args=(example,))

    # Generate and Random buttons
    col1, col2 = st.columns([1, 1])
    with col1:
        st.button("🎲 Random Prompt", on_click=set_random_prompt)
    with col2:
        generate_button = st.button("🚀 Generate Image", type="primary")

    st.divider()

    # Image generation
    if generate_button:
        if not prompt or prompt.strip() == "":
            st.warning("Please enter a prompt to generate an image.")
        else:
            # Combine reference description with prompt if provided
            if reference_description and reference_description.strip():
                final_prompt = f"{reference_description.strip()}, {prompt.strip()}"
            else:
                final_prompt = prompt.strip()

            # Apply style preset
            style_suffix = STYLE_PRESETS[selected_style]
            if style_suffix:
                final_prompt = final_prompt + style_suffix

            # Show the enhanced prompt
            if style_suffix or (reference_description and reference_description.strip()):
                st.info(f"📝 **Enhanced prompt:** *{final_prompt}*")

            with st.spinner("🎨 Creating your masterpiece... This may take 10-30 seconds."):
                image, error = generate_image(client, final_prompt, negative_prompt, width, height)

            if error:
                st.error(error)
            elif image:
                st.success("✨ Image generated successfully!")
                st.image(image, caption=final_prompt, use_column_width=True)

                # Store in session state for persistence
                st.session_state.last_image = image
                st.session_state.last_prompt = final_prompt

                # Download button
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"ai_generated_{timestamp}.png"
                st.download_button(
                    label="📥 Download Image",
                    data=image_to_bytes(image),
                    file_name=filename,
                    mime="image/png"
                )

    # Display last generated image if available
    elif "last_image" in st.session_state:
        st.image(
            st.session_state.last_image,
            caption=st.session_state.last_prompt,
            use_column_width=True
        )

        # Download button for previously generated image
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"ai_generated_{timestamp}.png"
        st.download_button(
            label="📥 Download Image",
            data=image_to_bytes(st.session_state.last_image),
            file_name=filename,
            mime="image/png"
        )

    # Footer with info
    st.divider()
    with st.expander("ℹ️ About this app"):
        st.markdown(f"""
        **Model:** `{MODEL_NAME}`

        **Tips for better results:**
        - Be specific and descriptive in your prompts
        - Include style keywords (e.g., "digital art", "photorealistic", "watercolor")
        - Mention lighting, mood, and atmosphere
        - Add details about colors and composition

        **Rate Limits:**
        - Free tier has limited requests per hour
        - If you hit the limit, wait a few minutes and try again

        **Built with:** Streamlit, HuggingFace Inference API
        """)


if __name__ == "__main__":
    main()
