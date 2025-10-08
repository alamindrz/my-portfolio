🚀 Django Portfolio Project

A modern, responsive portfolio website built with Django, featuring a blog, project showcase, and admin panel. Designed with Tailwind CSS and deployed on PythonAnywhere.

✨ Features

· 🎨 Modern UI - Clean, responsive design with Tailwind CSS
· 📱 Mobile-First - Optimized for all devices
· 📝 Blog System - Rich text editor with CKEditor
· 💼 Project Portfolio - Showcase your work with image optimization
· ⚡ Fast Performance - Image compression and optimization
· 🔧 Admin Panel - Modern Django Unfold admin interface
· 🎬 Media Ready - YouTube embedding and image handling

🛠️ Tech Stack

· Backend: Django 4.2+
· Frontend: Tailwind CSS, Vanilla JavaScript
· Database: SQLite (Development), MySQL (Production)
· Editor: CKEditor with code snippets
· Admin: Django Unfold
· Deployment: PythonAnywhere
· Image Processing: Pillow

📁 Project Structure

```
my-portfolio/
├── projects/                 # Portfolio app
│   ├── models.py            # Project and Post models
│   ├── views.py             # Project list and blog views
│   ├── admin.py             # Unfold admin configuration
│   └── templates/           # Project templates
├── pages/                   # Static pages app
│   └── views.py            # Homepage and about views
├── utils/                   # Utility functions
│   └── image_utils.py      # Image compression utilities
├── templates/               # Base templates
│   ├── base.html           # Main template with Tailwind
│   ├── pages/home.html     # Landing page
│   └── projects/           # Project templates
├── static/                  # Static files
├── media/                   # Uploaded media files
└── portfolio_project/       # Project settings
```

🚀 Quick Start

Prerequisites

· Python 3.8+
· Django 4.2+
· Pillow
· Termux (for mobile development)

Installation

1. Clone the repository
   ```bash
   git clone https://github.com/alamindrz/my-portfolio.git
   cd my-portfolio
   ```
2. Set up virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate    # Windows
   ```
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations
   ```bash
   python manage.py migrate
   ```
5. Create superuser
   ```bash
   python manage.py createsuperuser
   ```
6. Collect static files
   ```bash
   python manage.py collectstatic
   ```
7. Run development server
   ```bash
   python manage.py runserver
   ```

Visit http://localhost:8000 to see your portfolio!

📸 Admin Features

Modern Admin Interface

· Django Unfold - Beautiful, modern admin panel
· Image Previews - Visual project management
· Rich Text Editing - CKEditor for blog posts
· Media Management - Easy image uploads and organization

Access Admin Panel

1. Go to /admin
2. Login with your superuser credentials
3. Manage projects, blog posts, and categories

🎨 Customization

Adding Projects

1. Go to Admin → Projects
2. Click "Add Project"
3. Fill in:
   · Title and description
   · Upload project image (auto-compressed)
   · Project URL (optional)
   · Category (Web, Mobile, Design, Other)

Writing Blog Posts

1. Go to Admin → Posts
2. Use CKEditor for rich content:
   · Bold, Italic, formatting
   · Code snippets with syntax highlighting
   · Image uploads
   · YouTube embedding
   · Lists and tables

Styling

· Tailwind CSS via CDN
· Custom animations in base.html
· Responsive design patterns
· Color schemes for categories

🖼️ Image Handling

Automatic Optimization

· Compression: Images optimized on upload
· Thumbnails: Auto-generated smaller versions
· Formats: JPEG optimization with quality control
· Sizing: Responsive image delivery

Supported Features

· Project images with compression
· Blog header images
· Category-based styling
· Responsive image display

📝 Blog System

Features

· Rich text editing with CKEditor
· Category organization
· Published/Draft status
· SEO-friendly URLs
· Meta descriptions
· Author management

YouTube Integration

Embed videos directly in blog posts:

```html
<!-- In CKEditor Source view -->
<div class="youtube-embed">
<iframe src="https://www.youtube.com/embed/VIDEO_ID"></iframe>
</div>
```

🚀 Deployment

PythonAnywhere Setup

1. Upload to GitHub
   ```bash
   git add .
   git commit -m "Deploy ready"
   git push origin main
   ```
2. PythonAnywhere Console
   ```bash
   git clone https://github.com/alamindrz/my-portfolio.git
   cd my-portfolio
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Web App Configuration
   · WSGI file: portfolio_project/wsgi_pa.py
   · Static URL: /static/
   · Static path: /home/yourusername/my-portfolio/staticfiles
4. Database Setup
   ```bash
   python manage.py migrate
   python manage.py collectstatic
   python manage.py createsuperuser
   ```

🔧 Configuration

Environment Settings

Update settings.py for production:

```python
DEBUG = False
ALLOWED_HOSTS = ['alamindrz.pythonanywhere.com']
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

CKEditor Configuration

Rich text editor with:

· Code snippet support
· Image uploads
· YouTube embedding
· Custom toolbar

📱 Mobile Development

This project was fully developed on Android using:

· Termux - Linux environment
· Acode Editor - Code editing
· Mobile GitHub - Version control

🤝 Contributing

1. Fork the project
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

📄 License

This project is licensed under the MIT License - see the LICENSE.md file for details.

🙏 Acknowledgments

· Django - The web framework for perfectionists with deadlines
· Tailwind CSS - Rapid UI development
· CKEditor - Rich text editing
· Django Unfold - Modern admin interface
· PythonAnywhere - Django hosting platform

📞 Support

If you have any questions or run into issues:

1. Check the Issues page
2. Create a new issue with details
3. Include your environment and error logs

---

Built with ❤️ using Django and Tailwind CSS

Perfect for developers, designers, and creators to showcase their work!