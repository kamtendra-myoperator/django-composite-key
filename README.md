# Django Project with Composite Primary Key Example

This project is a Django application that demonstrates how to work with composite primary keys using the `viewflow.fields.CompositeKey` field. The project includes a model named `Temp` with a composite primary key composed of `id` and `company_id`.

## Table of Contents

- [Django Project with Composite Primary Key Example](#django-project-with-composite-primary-key-example)
  - [Table of Contents](#table-of-contents)
  - [Theory](#theory)
  - [Prerequisites](#prerequisites)
  - [Project Setup](#project-setup)
  - [Configuration](#configuration)
    - [`settings.py`](#settingspy)
  - [Create Database Table](#create-database-table)
  - [Database Model](#database-model)
    - [`Temp` Model](#temp-model)
  - [Django Shell](#django-shell)
  - [CRUD Operations](#crud-operations)
    - [Create](#create)
    - [Read](#read)
    - [Update](#update)
    - [Delete](#delete)


## Theory
Do Django models support multiple-column primary keys? <br>
No. Only single-column primary keys are supported.

However, you can create a composite primary key using the `viewflow.fields.CompositeKey` field. This field is a subclass of `models.Field` and can be used to define a composite primary key in Django models.

The `CompositeKey` field is used to define a composite primary key in Django models. It is a subclass of `models.Field` and can be used to define a composite primary key in Django models.

To use the `CompositeKey` field, you need to install the `django-viewflow` package. You can install it using pip:

```bash
pip install django-viewflow
```


## Prerequisites

Ensure you have the following installed on your local development environment:

- Python 3.x
- Django
- MySQL
- `pip` (Python package installer)

## Project Setup

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a Virtual Environment**:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

    Note: 

4. **Create MySQL Database**:

    Create a database in MySQL for your Django project.

5. **Configure Environment Variables**:

    Create a `.env` file in the root of your project and add the following:

    ```env
    DB_NAME=your_database_name
    DB_USER=your_database_user
    DB_PASSWORD=your_database_password
    DB_HOST=your_database_host
    DB_PORT=your_database_port
    ```

6. **Run Migrations**:

    ```bash
    python manage.py migrate
    ```

## Configuration

### `settings.py`

Ensure your `settings.py` is configured correctly:

```python
# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}
```

## Create Database Table

Before running the Django application, create the `temp` table in your MySQL database. You can do this using MySQL Workbench or any MySQL client.

Execute the following SQL command to create the table:

```sql
CREATE TABLE `temp` (
  `id` int NOT NULL AUTO_INCREMENT,
  `company_id` varchar(50) NOT NULL,
  `company_name` varchar(50),
  `created_at` TIMESTAMP,
  PRIMARY KEY (`id`, `company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16384 DEFAULT CHARSET=latin1;
```

## Database Model

### `Temp` Model

The `Temp` model demonstrates a composite primary key using `viewflow.fields.CompositeKey`.

```python
# apps/models.py

from django.db import models
from viewflow.fields import CompositeKey

class Temp(models.Model):
    id = models.AutoField()
    company_id = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(null=True)

    composite_key = CompositeKey(columns=['id', 'company_id'])

    class Meta:
        db_table = 'temp'
        unique_together = (('id', 'company_id'),)
```

## Django Shell

To interact with your Django project, you can use the Django shell:

1. Navigate to the Project Directory:

   ```bash
   cd path/to/your/project
   ```

2. Enter the Django Shell:

   ```bash
   python manage.py shell
   ```
   

## CRUD Operations

Perform CRUD operations on the Temp model:

### Create

```python
from apps.models import Temp

new_record = Temp.objects.create(id=1, company_id='company_123', company_name='Company ABC')
```

### Read

```python
record = Temp.objects.get(id=1, company_id='company_123')
print(record)
```

### Update

```python
record = Temp.objects.get(id=1, company_id='company_123')
record.company_name = 'Company XYZ'
record.save()
```

### Delete

```python
record = Temp.objects.get(id=1, company_id='company_123')
record.delete()
```
