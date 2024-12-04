## Multi-Container Docker Application with CI/CD: Calculator App Project

-------------------------------------------------------------------------
### Please note that I used port 5001 for backend. Please consider this when running my project.
-------------------------------------------------------------------------

#### Submission by Mahsa Mousavi Diva 
#### BannerID: B00954491

### Project Overview

- **Brief project description:** What is the purpose of your application?

The project focused on working with a calculator app that included a React frontend for the user interface and a Python backend for handling tasks like addition, subtraction, and multiplication. I containerized both the frontend and backend by creating Docker images for each. Then, I set up a system with multiple containers using Docker Compose to allow the components to work together. As part of the process, I added tests for the frontend, backend, and the Docker setup to make sure everything worked correctly and included these tests in an automated CI/CD pipeline.


- **Which files are you implmenting? and why?:**

Docker file for both frontend and backend => because I needed to change the port on the code

Github-actions.yaml => for CI/CD implementation

requirement.txt => to use libraries to build and test a Flask-based web application with Flask. Flask-Cors enables cross-origin requests, requests managing HTTP requests, and pytest facilitating testing.

docker-compose.yaml => to define and manage multi-container Docker applications.


- _**Any other explanations for personal note taking.**_

I used port 5001 for backend. Please consider this when running my project.

### Docker Implementation

**Explain your Dockerfiles:**

- **Backend Dockerfile** (Python API):
    - Here please explain the `Dockerfile` created for the Python Backend API. 
    - This can be a simple explanation which serves as a reference guide, or revision to you when read back the readme in future. 

##### My answer: This Dockerfile is designed to containerize a Python-based backend API. It starts with a lightweight Python 3.9 image as the base, sets `/app` as the working directory, and copies the `requirements.txt` file into the container to install dependencies without caching for efficiency. The contents of the current directory are then copied into the container. The backend is set to run on port 5001, which is exposed for external access, and the environment is configured for production using `FLASK_ENV`. Additionally, the Gunicorn server is installed to run the application with 4 worker processes, ensuring efficient handling of incoming requests. The application is launched with the command `gunicorn -w 4 -b 0.0.0.0:5001 app:app`.

- **Frontend Dockerfile** (React App):
    - Similar to the above section, please explain the Dockerfile created for the React Frontend Web Application.
 
##### My answer: This Dockerfile is used to containerize the frontend of the project, which is a Node.js application. It starts with the official Node.js 16 image, sets `/app` as the working directory, and copies the `package.json` and `package-lock.json` files to the container to install dependencies using `npm install`. The remaining source files are then copied into the container, and the application is built for production using `npm run build`. The container exposes port 3000 to allow external access, and the app is served using the `npx serve -s build` command, which serves the static files from the `build` directory.

**Use this section to document your choices and steps for building the Docker images.**


### Docker Compose YAML Configuration

**Break down your `docker-compose.yml` file:**

- **Services:** List the services defined. What do they represent?
- **Networking:** How do the services communicate with each other?
- **Volumes:** Did you use any volume mounts for persistent data?
- **Environment Variables:** Did you define any environment variables for configuration? 

**Use this section to explain how your services interact and are configured within `docker-compose.yml`.**

#### My answer:

**Services:**
- **frontend**: This service builds the frontend application (likely a React app) from the `./frontend` directory. It exposes port 3000 and depends on the `backend` service. The `command: npm start` runs the development server for the frontend.
- **backend**: This service builds the backend application (likely a Flask API) from the `./backend` directory. It exposes port 5001 and uses `flask run` to start the Flask server. The backend is set to run in the development environment (`FLASK_ENV=development`).

**Networking:**
- The services communicate with each other using Docker's internal networking. The `frontend` service uses `http://backend:5001` (as defined in the environment variable `REACT_APP_API_URL`) to send requests to the `backend` service. This works because Docker Compose automatically sets up a network where services can communicate by service names (e.g., `backend`).

**Volumes:**
- **frontend**: The `frontend` service mounts the local `./frontend` directory to the container’s `/app` directory. This allows live code reloading during development, as changes in the local directory are reflected in the container.
- **backend**: The `backend` service mounts the local `./backend` directory to the container’s `/app` directory. This also allows live code reloading during development.

**Environment Variables:**
- **frontend**: The environment variable `REACT_APP_API_URL=http://backend:5001` is defined to tell the frontend where the backend API is located.
- **backend**: The environment variable `FLASK_ENV=development` is defined to set the Flask app to run in development mode, enabling features like debugging.



### CI/CD Pipeline (YAML Configuration)

**Explain your CI/CD pipeline:**

- What triggers the pipeline (e.g., push to main branch)?
- What are the different stages (build, test, deploy)?
- How are Docker images built and pushed to a registry (if applicable)?

**Use this section to document your automated build and deployment process.**

#### My answer:

**What triggers the pipeline:**
- The pipeline is triggered by a push or pull request event, though the specific trigger is currently commented out (`# push` and `# pull_request`). Once these are defined, the pipeline will automatically run whenever changes are pushed to the repository or a pull request is made. Typically, this would be set for the `main` branch, but other branches can also be defined depending on the workflow requirements.

**Different Stages:**
1. **Frontend:**
   - **Build**: This stage sets up the environment for building the frontend (React app), where Node.js is configured, dependencies are installed, and tests are run.
   - **Test**: The frontend tests are executed to ensure the app is working as expected.
   - **Build the React App**: After testing, the React app is built for production, ready to be deployed or containerized.

2. **Backend:**
   - **Build**: This stage configures the environment for the backend (Python Flask API), where Python is set up and dependencies from `requirements.txt` are installed.
   - **Test**: Backend tests are run to validate the functionality of the API and ensure no issues exist.
   
3. **Docker:**
   - **Build Docker Images**: Once both the frontend and backend stages are successful, this stage builds Docker images for both the frontend and backend.
   - **Push to Docker Hub**: If the pipeline is triggered on the `main` branch, the Docker images are pushed to a Docker registry (e.g., Docker Hub) to make them available for deployment.
   
4. **Deployment (Optional):**
   - After successfully building and pushing the Docker images, the optional **deployment** stage can deploy the app to a production or staging environment, depending on the project’s needs.

**Building and Pushing Docker Images:**
- The pipeline checks out the code for both the frontend and backend.
- It sets up Docker and builds Docker images for both services based on the Dockerfiles.
- If the push happens on the `main` branch (as typically configured in a production environment), the images are pushed to a Docker registry (like Docker Hub) so they can be pulled later for deployment.

This pipeline automates the process of building, testing, and deploying the project, ensuring that any changes to the code are properly validated and packaged for production use.


### Assumptions

- List any assumptions you made while creating the Dockerfiles, `docker-compose.yml`, or CI/CD pipeline. 

#### My answer:

1. **Dockerfiles Assumptions:**
   - **Frontend Dockerfile:** It is assumed that the React app uses `npm` for package management and requires the `npm start` command to run in development. Additionally, it’s assumed that the `package.json` and `package-lock.json` files are present and correctly define all necessary dependencies.
   - **Backend Dockerfile:** It is assumed that the backend is a Flask app running in a development environment and requires the `flask run` command. The Flask app listens on port `5001`, and the Gunicorn server is installed for production deployments.

2. **docker-compose.yml Assumptions:**
   - It is assumed that the frontend and backend services are being developed locally with live code reloading, which is why volumes are mounted to sync local files with the container.
   - The `frontend` service is assumed to depend on the `backend` service, as specified by the `depends_on` directive, meaning the backend must be running for the frontend to work.
   - The backend is assumed to be available at `http://backend:5001`, which is set in the frontend's environment variable `REACT_APP_API_URL`.
   - Port `3000` is assumed for the frontend, and port `5001` for the backend, ensuring there are no conflicts between the services.

3. **CI/CD Pipeline Assumptions (GitHub Actions):**
   - It is assumed that the pipeline is triggered by `push` or `pull_request` events, but the exact triggers need to be configured in the `on` section.
   - The frontend and backend are assumed to be built and tested separately to ensure each component works correctly before proceeding.
   - After building the Docker images for the frontend and backend, the pipeline is assumed to push these images to Docker Hub only when changes are made to the `main` branch.
   - It is assumed that the deployment steps will be added once the Docker images are built and pushed, but the specific deployment process (e.g., cloud hosting, container orchestration) would need to be defined.



### Lessons Learned

- What challenges did you encounter while working with Docker and CI/CD?
#### my answer: my challenge was for the tag of docker images, and the Image ID that I didn't sync it with on the docker compose file. however, after changing the frontend and backend version to latest, and then pushing the latest version to the docker hub, this problem was solved.

  
- What did you learn about containerization and automation?
#### my answer: 
As a beginner to DevOps, I learned that containerization, using tools like Docker, ensures consistency across environments by packaging an application with all its dependencies. This eliminates issues like "it works on my machine." I also discovered that automation, through tools like GitHub Actions, streamlines tasks like building, testing, and deploying, saving time and reducing errors. CI/CD pipelines automate these processes, making development more reliable, efficient, and consistent.



### Future Improvements

- How could you improve your Dockerfiles, `docker-compose.yml`, or CI/CD pipeline?
#### my answer: 
To improve the Dockerfiles, docker-compose.yml, and CI/CD pipeline, I would implement multi-stage builds in the Dockerfiles to reduce the final image size and optimize layer caching by copying only necessary files before installing dependencies. I would also use a non-root user for better security. In the docker-compose.yml, I’d add health checks for the backend to ensure it’s fully ready before the frontend starts, specify a custom network for better isolation, and remove unnecessary volumes in the production environment.

- (Optional-Just for personal reflection) Are there any additional functionalities you would like to consider for the calculator application to crate more stages in the CI/CD pipeline or add additional configuration in the Dockerfiles?

