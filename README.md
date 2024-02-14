# Indicium Tech Code Challenge

Written by Jânio César Martins Ferreira

Synopsis of Solution: Building a Data Pipeline for Software Developer Challenge

Challenge Overview:
The challenge entails constructing a pipeline to extract data from two sources daily and write the data to both local disk and a database. The data sources comprise a PostgreSQL database and a CSV file containing order details from an e-commerce system.

Solution Highlights:
To fulfill the challenge requirements, Airflow, a workflow management platform, was chosen for its capability to describe, execute, and monitor workflows efficiently. Airflow organizes tasks into Directed Acyclic Graphs (DAGs) for easy management.

Task Breakdown:
1. **Extract and Write Postgres Data to Local Disk (Task 1):**
   - Connects to the PostgreSQL database, retrieves table names, and exports data to local CSV files.
   - Each table's data is stored in a separate CSV file within a directory structure organized by source, table, and execution date.

2. Copy CSV File to Local Disk (Task 2):
   - Copies the provided CSV file containing order details to the local disk.
   - The file is saved in a directory structure based on the execution date.

3. Extract, Transform, and Load Data to MongoDB (Task 3):
   - Extracts data from local CSV files representing orders, products, customers, and order details.
   - Transforms the data by joining tables and organizing it into JSON format suitable for MongoDB.
   - Loads the transformed data into a MongoDB database, facilitating easy retrieval and analysis.

Pipeline Configuration:
- The tasks are organized into a DAG named "DAG" scheduled to run daily.
- Task 3 depends on the successful completion of tasks 1 and 2, ensuring data availability before transformation and loading.
- The DAG configuration includes default arguments such as the owner, start date, and retry policy.

Setup and Testing:
- The solution is containerized using Docker for easy deployment and management.
- Docker Compose is utilized to set up the environment, providing a straightforward installation process.
- After setup, the pipeline can be tested by accessing the Airflow container and executing individual tasks or the entire pipeline, even retroactively.

Conclusion:
By leveraging Airflow and Docker, a robust data pipeline solution was developed to meet the challenge requirements effectively. The solution demonstrates the ability to handle data extraction, transformation, and loading tasks seamlessly, paving the way for scalable and reliable data processing in real-world scenarios.
