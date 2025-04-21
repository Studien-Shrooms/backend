<div align="center">
    <h1>Backend for Gebärdenspracheanwendung</h1>
   <!-- Letzter Commit -->
    <img src="https://img.shields.io/github/last-commit/Studien-Shrooms/backend">

    <!-- Build Status (anpassen falls dein Workflow anders heißt) -->
    
 <img src="https://img.shields.io/github/actions/workflow/status/Studien-Shrooms/backend/ci.yml?label=build">

    <!-- Release Version -->
<img src="https://img.shields.io/github/v/release/Studien-Shrooms/backend">

    <!-- Lizenz (automatisch erkannt, falls LICENSE-Datei vorhanden) -->
 <img src="https://img.shields.io/github/license/Studien-Shrooms/backend">

    <!-- Hauptsprache -->
<img src="https://img.shields.io/github/languages/top/Studien-Shrooms/backend">

    <!-- Anzahl Sprachen -->
<img src="https://img.shields.io/github/languages/count/Studien-Shrooms/backend">

    <!-- Repo-Größe -->
 <img src="https://img.shields.io/github/repo-size/Studien-Shrooms/backend">

    <!-- Sterne (social style) -->
 <img src="https://img.shields.io/github/stars/Studien-Shrooms/backend?style=social">

    <br>
    <br>
    <b>Backend repository providing the API for the Angular-based Gebärdenspracheanwendung</b>
    <br>
    <br>
</div>

## Table of Contents

1. [Features](#features)
2. [Setup](#setup)
3. [Usage](#usage)
4. [Deployment](#deployment)
5. [Contributing](#contributing)
6. [License](#license)

## Features

- RESTful API for managing application data.
- Integration with MongoDB for data persistence.
- Authentication and authorization using JWT.
- Scalable and modular architecture.
- Docker support for containerized deployment.

## Setup

### Prerequisites

- Node.js (v16 or higher)
- MongoDB
- Docker (optional, for containerized deployment)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Studien-Shrooms/backend.git
   cd backend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Configure environment variables:
   Create a `.env` file in the root directory and add the required variables:
   ```env
   MONGO_URI=mongodb://localhost:27017/your-database
   JWT_SECRET=your-secret-key
   PORT=3000
   ```

## Usage

Start the development server:
```bash
npm run dev
```

The server will run on `http://localhost:3000`.

## Deployment

To push the Docker image to Azure Container Registry, follow the [official guide](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-get-started-docker-cli).

1. Build the Docker image:
   ```bash
   docker build -t your-image-name .
   ```

2. Tag the image:
   ```bash
   docker tag your-image-name your-registry.azurecr.io/your-image-name
   ```

3. Push the image:
   ```bash
   docker push your-registry.azurecr.io/your-image-name
   ```





