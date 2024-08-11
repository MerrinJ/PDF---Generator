# PDF-Generator
A FastAPI web service that generates a PDF report from JSON input data. The service will accept JSON via an API endpoint, process it, and produce a formatted PDF saved in a specified directory. The entire application is containerized using Docker for easier deployment and scalability.
**Inclusions:** 
* Development of a FastAPI web service with an endpoint to accept JSON input. 
* Implementation of functionality to process the JSON data and generate a PDF report. 
* Saving the generated PDF to a specified output directory. 
* Basic error handling for invalid input data. 
* Dockerizing the application to ensure it can be easily deployed and run in any environment.
* Unit Testing.

**Exclusions:** 
* Detailed front-end interface for the API (a simple endpoint is sufficient). 
* Advanced error handling and logging (basic error handling is sufficient). 
* Extensive PDF formatting and styling (basic formatting to ensure readability is sufficient). 
* Handling complex JSON schemas that require extensive validation or transformation. 

**Objectives:** <br>
The main objective of this project is to create a FastAPI-based web service that can: 
* Receiving JSON input data through an API endpoint (POST request). 
* Generating a PDF report based on the received JSON data. 
* Saving the generated PDF report in a specified output directory. 
* Running seamlessly within a Docker container to ensure portability and ease of deployment.

*The JSON input consists of a heading, subheading and a table. The schema is defined using Pydantic.*
<br>
*Unit Testing is done using Pytest*
<br>
*PDF is generated using ReportLab*
