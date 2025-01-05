# Proxy Site

A simple and user-friendly proxy site built with Flask that allows users to access blocked websites. This project provides a clean and responsive interface for entering URLs and fetching their content securely.

## Features
- **Web Proxy**: Access blocked websites via a simple proxy server.
- **User-Friendly Interface**: Clean, modern design with a responsive layout.
- **Secure Requests**: Handles both HTTP and HTTPS requests.
- **Error Handling**: Displays user-friendly error messages for inaccessible URLs.

## Technologies Used
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS (Custom Styling)
- **Dependencies**: Requests library for handling HTTP requests

## Prerequisites
- Python 3.6+
- pip (Python package manager)

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/proxy-site.git
   cd proxy-site
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
1. **Start the Flask Server**:
   ```bash
   python proxy_site.py
   ```

2. **Open in Browser**:
   Navigate to `http://127.0.0.1:5000/` in your web browser.

## Deployment
This project is ready for deployment on platforms like [Vercel](https://vercel.com/) or any Python-compatible hosting service.

### Deploy on Vercel
1. Ensure you have a `vercel.json` file in the root directory (included in this repository).
2. Install the [Vercel CLI](https://vercel.com/docs/cli):
   ```bash
   npm install -g vercel
   ```
3. Deploy the project:
   ```bash
   vercel
   ```

## File Structure
```
proxy-site/
├── proxy_site.py       # Main Flask application
├── requirements.txt    # Python dependencies
├── vercel.json         # Vercel configuration
├── README.md           # Project documentation
```

## Screenshots
### Home Page
![Home Page](https://via.placeholder.com/800x400.png?text=Proxy+Site+Home)

### Proxy Page
![Proxy Page](https://via.placeholder.com/800x400.png?text=Accessing+a+Blocked+Website)

## Disclaimer
This project is intended for educational and ethical purposes only. Bypassing restrictions may violate local laws or terms of service. Use responsibly.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For questions or suggestions, feel free to reach out:
- **Email**: [satyajena911@gmail.com](mailto:satyajena911@gmail.com)
- **GitHub**: [https://github.com/Satyasuranjeet](https://github.com/Satyasuranjeet)
