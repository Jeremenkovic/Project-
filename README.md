# CSV Processor API
CSV Processor API is a Django-based RESTful API that allows you to upload large CSV files, process them asynchronously in the background, and download the processed results. The input CSV files have the format "Song", "Date", "Number of Plays" and the API generates an output CSV file with format "Song", "Date, “Total Number of Plays for Date”.

# Technologies Used
Python: The backend is written in Python, a versatile and powerful language with strong support for integration with other languages and tools.
Django: A high-level Python web framework that enables rapid development of secure and maintainable websites.
Django REST framework: A powerful and flexible toolkit for building Web APIs.
Celery: An asynchronous distributed task queue/job queue based on distributed message passing used for processing tasks asynchronously.
Redis: An open-source in-memory data structure store, used as a database, cache and message broker. In this project, it is used as a broker for Celery.
Pandas: A fast, powerful, flexible, and easy-to-use open-source data analysis and manipulation library for Python. Used in this project for CSV file processing.

# Setup and Running the Project
1. Clone the repository.
2. Setup a Python virtual environment.

 python -m venv env

3. Activate the virtual environment.
On Windows, use: .\env\Scripts\activate
On macOS and Linux, use: source env/bin/activate
4. Install the required Python dependencies from requirements.txt.

 pip install -r requirements.txt

5. Start the Redis server. Follow the Redis Quick Start Guide for detailed instructions on installing and running Redis.
6. In a separate terminal window, start the Celery worker.
celery -A your_project_name worker --loglevel=info
7. Run Django migrations.

 python manage.py migrate
8. Run the Django development server.
 python manage.py runserver


# Testing the API
 Uploading a file
You can use curl or any API client, like Postman, to upload a CSV file.

curl -X POST -F "file=@path_to_your_file.csv" http://127.0.0.1:8000/api/upload/
This will return a JSON response with a task_id. Keep this task_id for downloading the processed file.

Downloading the result
To download the processed file, make a GET request to the download API endpoint with the task_id as a path parameter.

curl http://127.0.0.1:8000/api/download/task_id
If the file is still being processed, you will receive a JSON response with an 'error' message. Once processing is complete, this endpoint will return the processed CSV file.
# ScreenShot
<img width="1165" alt="Screen Shot 2023-06-15 at 5 04 51 PM" src="https://github.com/Jeremenkovic/Project-/assets/102044657/8926798a-475e-497c-87f7-c03c9af2825f">

Contributing
If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.

License
MIT © Nemanja Jeremenkovic
