pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clones the repository
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                // Installs PyTorch using pip
                sh 'pip install torch'
            }
        }
        stage('Run PyTorch Model') {
            steps {
                // Executes the Python script
                sh 'python app.py'
            }
        }
    }
}

