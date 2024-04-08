# Backend Development with Django and Django Rest Framework

This project focuses on building the backend using Django and Django Rest Framework with a PostgreSQL database. The backend is structured with Generic Views for efficient handling of CRUD operations.

## Installation

To install dependencies for this project, ensure you have `pipenv` installed and execute the following command:

1. pipenv install


This command will set up a virtual environment and install all necessary dependencies listed in the `Pipfile`.

## Dependencies

- Django
- Django Rest Framework
- PostgreSQL

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository: `git clone <repository_url>`
2. Navigate to the project directory: `cd <project_directory>`
3. Install dependencies: `pipenv install`
4. Set up PostgreSQL database configuration in `settings.py`.
5. Run migrations: `pipenv run python manage.py migrate`
6. Start the development server: `pipenv run python manage.py runserver`

## Usage

Once the development server is running, you can access the API endpoints using tools like Postman or curl. The API endpoints will be available at `http://localhost:8000/`.

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify this project for your own purposes.
