# Sales Data Chart

## Overview

Django project created to display sales data fetched from the PostgreSQL Database and displays in chart using chart.js. The sales data is aggregated monthly and rendered using Chart.js. Redis is used for caching the aggregated data to improve performance, and Celery is used to handle background tasks for data aggregation.


## Features

- **Database**: PostgreSQL is used to store sales data.
- **Data Aggregation**: Monthly sales data is aggregated and displayed.
- **Caching**: Redis is used to cache aggregated monthly sales data.
- **Background Tasks**: Celery is used for background data aggregation tasks.
- **Chart Rendering**: Chart.js is used to render the sales data chart on the HTML page.


## Technologies

- Django 
- PostgreSQL
- Redis
- Celery
- Chart.js


## Setup Instructions

### Prerequisites

Before setting up the project, ensure you have the following installed:

- Python (3.8+ recommended)
- PostgreSQL
- Redis
- Node.js and npm (for installing Chart.js)

### Project Setup

1. **Clone the repository**

    ```sh
    git clone https://github.com/san1sk/sales-chart.git
    cd sales-data-chart
    ```

2. **Create a virtual environment and activate it**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required Python packages**

    ```sh
    pip install -r requirements.txt
    ```

4. **Install Chart.js**

    ```sh
    npm install chart.js
    ```

5. **Setup PostgreSQL**

    - Create a PostgreSQL database and user for the project.
    - Update the `DATABASES` settings in `sales_data_chart/settings.py` with your database credentials.

6. **Run database migrations**

    ```sh
    python manage.py migrate
    ```

7. **Create a superuser**

    ```sh
    python manage.py createsuperuser
    ```


9. **Start Redis server**

  Install redis and start redis server. Redis on windows can be installed through https://github.com/tporadowski/redis/releases.


10. **Start Celery worker**

    ```sh
    celery -A myproject worker --loglevel=info
    ```

11. **Run the Django development server**

    ```sh
    python manage.py runserver
    ```

12. **Open Browser**

    ```sh
    http://127.0.0.1:8000/sales/chart/
    ```

## Snapshots of Implementation


**Chart**
![Screenshot (250)](https://github.com/san1sk/sales-chart/assets/88581704/3fe13b43-f08d-46f7-9644-0477227e95f7)


**PostgreSQL (pgadmin4 Panel)**

![Screenshot (251)](https://github.com/san1sk/sales-chart/assets/88581704/95dbc1bd-e8ed-495a-95d9-4976d2a468f9)

