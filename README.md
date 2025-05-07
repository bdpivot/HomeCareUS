# HomeCareUS

A comprehensive homecare agency management system designed to streamline caregiver management, ensure compliance with state regulations, and maintain HIPAA compliance.

## Features

- Agency profile management with NPI and Tax ID validation
- Caregiver management with status tracking and certifications
- State-specific compliance requirements tracking
- HIPAA compliance monitoring and reporting
- Document expiry tracking and alerts
- Comprehensive reporting system

## Requirements

- Python 3.8+
- Django 5.2+
- PostgreSQL
- Bootstrap 5
- jQuery
- DataTables

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/HomeCareUS.git
cd HomeCareUS
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure the database:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Configuration

1. Copy `.env.example` to `.env` and update the settings:
```bash
cp .env.example .env
```

2. Update the following settings in `.env`:
- `SECRET_KEY`
- `DEBUG`
- `DATABASE_URL`
- `ALLOWED_HOSTS`

## Usage

1. Access the admin interface at `/admin`
2. Create an agency profile
3. Add state licenses
4. Add caregivers
5. Track compliance and certifications

## Development

1. Create a new branch for features:
```bash
git checkout -b feature/your-feature-name
```

2. Run tests:
```bash
python manage.py test
```

3. Submit a pull request

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the GitHub repository or contact the development team.

## Acknowledgments

- Django framework
- Bootstrap team
- jQuery team
- DataTables team