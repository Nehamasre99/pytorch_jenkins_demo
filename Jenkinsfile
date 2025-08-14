pipeline {
    // Define the agent for the entire pipeline
    agent {
        docker {
            image 'python:3.9-slim' 
        }
    }

    stages {
        stage('Checkout') {
            steps {
                // This stage checks out the code from your repository
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                // This command now runs inside the python:3.9-slim container
                sh 'pip install torch'
            }
        }
        stage('Run PyTorch Model') {
            steps {
                // This command also runs inside the python container
                sh 'python app.py'
            }
        }
    }
}

