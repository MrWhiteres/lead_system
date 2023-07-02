# Lead_system

Lead_system is a project aimed at creating a lead management system. It provides a set of API endpoints for managing leads and their associated information. This README file serves as a guide for setting up and running the project.

## Getting Started

To get started with the project, follow these instructions:

### Prerequisites

Make sure you have the following installed on your system:

- Python 3.11.4
- Docker

### Installation

1. Clone the project repository from GitHub:

   ```
   git clone https://github.com/MrWhiteres/lead_system.git
   ```

2. Navigate to the project directory:

   ```
   cd lead_system
   ```

3. Create a `.env` file in the project root directory and add the following variables:

   ```
   DJANGO_KEY='django-insecure-h8l&o0))##-8i)qk#srzbqgf2hhd@x1#u)6v#redza@p^@*h+u'
   DEBUG_TRUE=True
   DEBUG_FALSE=False
   DATABASE='crm_system'
   DATABASE_USER='base_user'
   DATABASE_PASSWORD='base_password'
   ```

4. Build and run the project using Docker Compose:

   ```
   docker-compose up --build
   ```

   Alternatively, you can use the `make` command:

   ```
   make up
   ```

   This will build the necessary Docker containers and start the project.

### Usage

Once the project is up and running, you can access the following endpoints:

- Swagger UI: [http://localhost:8000/swagger](http://localhost:8000/swagger)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

You can use these interfaces to explore and interact with the API endpoints.

### Testing

To run the project's tests, you can use the following commands:

```
make test
```

or

```
docker exec -it django_api sh -c "python manage.py test"
```

These commands will run the test suite and provide feedback on the project's functionality.

## Contributing

If you would like to contribute to the project, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix.
3. Make the necessary changes in your branch.
4. Commit your changes and push the branch to your forked repository.
5. Submit a pull request, describing your changes and the motivation behind them.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code according to your needs.