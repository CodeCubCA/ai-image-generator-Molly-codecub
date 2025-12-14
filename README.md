---
title: AI Image Generator
emoji: 🎨
colorFrom: purple
colorTo: pink
sdk: streamlit
sdk_version: "1.31.0"
app_file: app.py
pinned: false
license: mit
---

# AI Image Generator 🎨

A powerful web application that generates stunning AI images from text descriptions using the FLUX.1-schnell model via HuggingFace Inference API. Create beautiful artwork with just a few words!

![AI Image Generator](https://img.shields.io/badge/AI-Image%20Generator-blue)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Features

### Core Functionality
- **Text-to-Image Generation**: Transform your ideas into images using state-of-the-art AI
- **8 Style Presets**: Choose from curated artistic styles for consistent results
  - Anime (Studio Ghibli inspired)
  - Realistic (Photorealistic 8K)
  - Digital Art (ArtStation trending)
  - Watercolor
  - Oil Painting
  - Cyberpunk
  - Fantasy
  - None (Custom prompts)

### Advanced Features
- **Reference Image Support**: Upload images for visual inspiration
- **Negative Prompts**: Specify what to avoid in generated images
- **Multiple Image Sizes**: Square, Portrait, and Landscape formats
- **Random Prompt Generator**: Get creative inspiration instantly
- **Example Prompts**: Quick-start templates for beginners
- **Download Images**: Save your creations as PNG files
- **Session Persistence**: View previously generated images

### User Experience
- Clean, intuitive sidebar navigation
- Real-time prompt enhancement preview
- Responsive design
- Progress indicators
- Error handling with helpful messages

## Technologies Used

- **[Python](https://www.python.org/)** - Core programming language
- **[Streamlit](https://streamlit.io/)** - Web application framework
- **[HuggingFace Inference API](https://huggingface.co/inference-api)** - AI model hosting
- **[FLUX.1-schnell](https://huggingface.co/black-forest-labs/FLUX.1-schnell)** - Fast image generation model
- **[Pillow (PIL)](https://python-pillow.org/)** - Image processing
- **[python-dotenv](https://github.com/theskumar/python-dotenv)** - Environment variable management

## Prerequisites

- Python 3.8 or higher
- HuggingFace account with API token
- Internet connection for API calls

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/CodeCubCA/ai-image-generator-Molly-codecub.git
cd ai-image-generator-Molly-codecub
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

The required packages are:
- streamlit>=1.28.0
- python-dotenv>=1.0.0
- Pillow>=10.0.0
- huggingface_hub>=0.19.0

### 3. Set Up HuggingFace API Token

1. Go to [HuggingFace Settings → Tokens](https://huggingface.co/settings/tokens)
2. Create a new token with **Write** permissions
3. Copy your token

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```bash
HUGGINGFACE_TOKEN=hf_your_token_here
```

Replace `hf_your_token_here` with your actual HuggingFace API token.

## Usage

### Running the Application

```bash
streamlit run app.py
```

The application will open automatically in your default browser at `http://localhost:8501`

### Using the Image Generator

1. **Select a Style** (optional)
   - Choose from the sidebar style presets
   - Preview the style enhancement keywords

2. **Enter Your Prompt**
   - Describe the image you want to create
   - Be specific and descriptive for better results

3. **Configure Settings** (optional)
   - Choose image dimensions
   - Add negative prompts to avoid unwanted elements
   - Upload reference images for inspiration

4. **Generate Image**
   - Click "Generate Image" button
   - Wait 10-30 seconds for processing
   - Download your creation

### Tips for Better Results

- **Be Specific**: Include details about colors, lighting, mood, and composition
- **Use Style Keywords**: Mention art styles like "digital art", "photorealistic", "watercolor"
- **Describe the Scene**: Include atmosphere, time of day, and setting details
- **Experiment**: Try different styles and prompt variations
- **Negative Prompts**: Use to avoid common issues like "blurry, low quality, distorted"

## Project Structure

```
ai-image-generator2/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── .env.example          # Example environment file
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## API Rate Limits

- **Free Tier**: Limited requests per hour
- **Pro Tier**: Higher limits available with HuggingFace Pro subscription
- If you hit the rate limit, wait a few minutes before retrying

## Troubleshooting

### "HuggingFace API token not found"
- Ensure `.env` file exists with `HUGGINGFACE_TOKEN=your_token`
- Verify token has **Write** permissions

### "Model is currently loading"
- Wait 20-30 seconds and try again
- Free tier models may take time to wake up

### "Rate limit exceeded"
- Wait a few minutes before making more requests
- Consider upgrading to HuggingFace Pro

### Image generation fails
- Check your internet connection
- Verify API token is valid
- Try a simpler prompt
- Check HuggingFace status page

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [HuggingFace](https://huggingface.co/) for providing the Inference API
- [Black Forest Labs](https://huggingface.co/black-forest-labs) for the FLUX.1-schnell model
- [Streamlit](https://streamlit.io/) for the amazing web framework
- All contributors and users of this project

## Contact

Project Link: [https://github.com/CodeCubCA/ai-image-generator-Molly-codecub](https://github.com/CodeCubCA/ai-image-generator-Molly-codecub)

---

Made with ❤️ using Python and Streamlit
