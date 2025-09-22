# Skill Verse - Pixel-Perfect Django Blog

A retro-styled, pixel-perfect blog platform built with Django, designed for sharing coding tutorials, tech insights, and development experiences.

## Features

- **Retro Design**: Pixel-perfect UI with retro gaming aesthetics
- **User Authentication**: Secure login, registration, and logout system
- **Blog Management**: Create, read, update, and delete blog posts
- **User Profiles**: Personal dashboard showing user's posts and statistics
- **Responsive Design**: Mobile-friendly interface
- **Category System**: Organize posts by topics
- **Image Support**: Featured images for blog posts
- **View Counter**: Track post popularity
  

## Tech Stack

- **Backend**: Django 4.x
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (default)
- **Styling**: Custom CSS with pixel-art aesthetic
- **Fonts**: Google Fonts (Press Start 2P, Orbitron)
- **Authentication**: Django's built-in auth system

## Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/skillverse.git
   cd skillverse
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django pillow
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start development server**
   ```bash
   python manage.py runserver
   ```

7. **Visit the application**
   ```
   http://127.0.0.1:8000/
   ```

## Project Structure

```
skillverse/
├── home/                   # Main app directory
│   ├── templates/home/     # HTML templates
│   │   ├── base.html       # Base template
│   │   ├── index.html      # Homepage
│   │   ├── about.html      # About page
│   │   ├── explore.html    # All posts page
│   │   ├── read_post.html  # Individual post view
│   │   ├── create_post.html # Create new post
│   │   ├── edit_post.html  # Edit existing post
│   │   ├── delete_post.html # Delete confirmation
│   │   ├── profile.html    # User profile
│   │   ├── login.html      # Login page
│   │   └── signup.html     # Registration page
│   ├── models.py           # Database models
│   ├── views.py            # View functions
│   ├── forms.py            # Django forms
│   ├── urls.py             # URL patterns
│   └── admin.py            # Admin configuration
├── media/                  # User uploaded files
│   ├── blog_images/        # Blog post images
│   └── profile_images/     # User profile images
├── skillverse/             # Project settings
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py             # WSGI configuration
├── manage.py               # Django management script
└── requirements.txt        # Python dependencies
```

## Models

### BlogPost
- **title**: Post title
- **category**: Post category (e.g., Python, Web Dev)
- **author**: Foreign key to User model
- **content**: Main blog content
- **excerpt**: Brief description
- **featured_image**: Optional post image
- **views**: View count
- **created_at**: Creation timestamp
- **updated_at**: Last modified timestamp

### UserProfile
- **user**: One-to-one relationship with User
- **bio**: User biography
- **profile_image**: Profile picture
- **website**: Personal website
- **github**: GitHub username
- **linkedin**: LinkedIn profile

## Usage

### For Users
1. **Registration**: Create account via signup page
2. **Login**: Access your dashboard
3. **Create Posts**: Share your knowledge
4. **Explore**: Read posts from other users
5. **Profile**: Manage your posts and profile

### For Developers
1. **Extend Models**: Add new fields to existing models
2. **Custom Views**: Create new functionality
3. **Template Customization**: Modify the pixel-art design
4. **Admin Panel**: Manage content via Django admin

## Configuration

### Settings
Key settings in `settings.py`:
- `MEDIA_URL`: URL for serving media files
- `MEDIA_ROOT`: Directory for uploaded files
- `DEBUG`: Development/production mode
- `ALLOWED_HOSTS`: Allowed domain names

### URL Configuration
- `/` - Homepage
- `/explore/` - All blog posts
- `/about/` - About page
- `/login/` - User login
- `/signup/` - User registration
- `/create/` - Create new post
- `/post/<id>/` - View specific post
- `/profile/` - User profile

## Deployment

### Production Setup
1. **Environment Variables**
   ```bash
   export DEBUG=False
   export SECRET_KEY='your-secret-key'
   export ALLOWED_HOSTS='your-domain.com'
   ```

2. **Static Files**
   ```bash
   python manage.py collectstatic
   ```

3. **Database**
   - Configure PostgreSQL for production
   - Update `DATABASES` setting

4. **Web Server**
   - Use Gunicorn/uWSGI
   - Configure Nginx for static files

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## Future Enhancements

- [ ] Comment system for blog posts
- [ ] Advanced search with filters
- [ ] Email notifications
- [ ] Social media integration
- [ ] Rich text editor
- [ ] Tag system
- [ ] RSS feed
- [ ] API endpoints
- [ ] Dark/Light theme toggle

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Chitransh Ludhiyani**
- Email: chitranshludhiyani103@gmail.com
- GitHub: [@ChitranshLudhiyani1](https://github.com/ChitranshLudhiyani1)
- LinkedIn: [chitranshludhiyani](https://www.linkedin.com/in/chitranshludhiyani)

## Acknowledgments

- Django documentation and community
- Pixel art inspiration from retro gaming
- Google Fonts for typography
- Open source community for tools and resources

---

Built with ❤️ and Django
