Deployment
==========

Deployement Pipeline Overview (CI/CD)
-------------------------------------

The deployment process for **Orange County Lettings** is fully automated using GitHub Actions.

This pipeline ensures that the application is tested, built, and deployed with minimal manual intervention.

Each of these steps is automated and triggered when code is pushed to the `main` branch.

For detailed instructions on configuring individual components like **Sentry**, **SonarCloud**, **Render**, or **GitHub Actions**, refer to the next chapter.

Below is a summary of the key steps:

1. **Linting and Testing**:

  - Checks the code for style issues using `flake8`.

  - Executes unit and integration tests with `pytest`

  - Check tests coverage with `coverage`. Ensure code coverage is > 80%

2. **SonarCloud Analysis**:

  - Analyzes the codebase for quality and security issues using SonarCloud.

3. **Documentation Generation**:

  - Builds the project documentation with Sphinx.

4. **Docker Image Creation**:

  - Builds a Docker image for the application and pushes it to Docker Hub.

5. **Deployment to Render**:

  - Deploys the application to Render via a webhook.

6. **Health Check**:

  - Verifies that the deployed application is operational by checking the `/health/` endpoint.


Deployment Components
---------------------

This chapter provides detailed instructions for configuring each component involved in the deployment process.

GitHub Actions
^^^^^^^^^^^^^^

GitHub Actions automates the CI/CD process for the project. To set it up:

1. **Enable GitHub Actions**:

  - Navigate to the project repository on GitHub.
  - Go to the "Actions" tab and enable workflows.

2. **Secrets Configuration**:

  - Add the following secrets to the repository settings:

    - `DJANGO_SECRET_KEY`: Django's secret key.

3. **Workflow File**:

  - The workflow is defined in `.github/workflows/ci-cd-pipeline.yml`. Ensure it is properly configured for the project's requirements.

Sentry
^^^^^^

Sentry tracks application errors and performance issues. To configure:

1. **Create a Sentry Project**:

  - Log in to https://sentry.io/ and create a new project.

2. **Retrieve the DSN**:

  - Copy the DSN provided for the project.

3. **Update `.env` File**:

  - Add the following variables to your `.env` file:

   ```
   SENTRY_DSN=<your-dsn>
   SENTRY_DEBUG=False
   ```

SonarCloud
^^^^^^^^^^

SonarCloud analyzes the code for quality issues. To configure:

1. **Create a SonarCloud Account**:

  - Log in to SonarCloud.io and link it to your GitHub account.

2. **Create a Project**:

  - Set up a new project and retrieve the `SONAR_TOKEN`.

3. **Update GitHub Secrets**:

  - Add the following secrets to your GitHub repository:

    - `SONAR_TOKEN`

    - `SONAR_ORGANIZATION`

    - `SONAR_PROJECT_KEY`

Render
^^^^^^

Render hosts the deployed application. To configure:

1. **Create a Render Account**:

  - Log in to https://render.com/ and create an account.

2. **Set Up the Web Service**:

  - Create a new web service and link it to your GitHub repository.

3. **Add Environment Variables**:

  - Configure the following environment variables in Render:
    - `DJANGO_SECRET_KEY`

    - `ENV`:value *production*

    - `RENDER_URL`

    - `SENTRY_DEBUG`: value *false*

    - `SENTRY_DSN`

  - Add the following secrets to your GitHub repository:

    - `RENDER_DEPLOY_HOOK_URL`

4. **Trigger Deployment**:

  - Use the webhook URL provided by Render for automatic deployments.


Docker Hub
^^^^^^^^^^

Docker Hub stores the application's container images. To configure:

1. **Create a Docker Hub Account**:

  - Sign up on Docker Hub : https://hub.docker.com/

2. **Create a Repository and Token**:

  - Log in to Docker Hub at `https://hub.docker.com/`.
  - Navigate to the "Repositories" tab and click on the **"Create Repository"** button.
  - Fill out the repository details:
    - **Name**: Enter a name for your repository (e.g., `oc-lettings-site`).
    - **Visibility**: Choose between **Public** or **Private** based on your needs.
    - **Description**: Optionally, provide a description for the repository.
  - Click **Create** to finalize the creation of your repository.

3. **Generate a Personal Access Token**:
    - Go to your Docker Hub account settings.
    - Select **Security** from the menu.
    - Under **Access Tokens**, click **New Access Token**.
    - Provide a descriptive name for the token (e.g., `CI/CD Token`).
    - Set the token's permissions (e.g., `Read/Write` for CI/CD purposes).
    - Click **Generate** and securely store the token, as it won't be displayed again.

4. **Authenticate GitHub Actions**:

  - Add `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` as secrets in your GitHub repository.

5. **Push Docker Images**:

  - The workflow pushes images with two tags: `latest` and the commit hash.

*This page was partially generated with the assistance of AI.*
