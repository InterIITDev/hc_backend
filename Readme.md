# HC Backend
This is the backend service for the HC application, built with FastAPI.

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/hc_backend.git
    cd hc_backend
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    Create a `.env` file in the root directory and add the necessary environment variables. Refer to `.env.example` for the required variables.

5. **Run the application:**
    ```sh
    uvicorn main:app --reload
    ```

6. **Run tests:**
    ```sh
    pytest
    ```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.