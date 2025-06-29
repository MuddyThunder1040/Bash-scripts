pipeline {
    agent any

    environment {
        IMAGE_NAME = "bash-scripts"
        TAG = "dev"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "✅ Checked out code from dev branch"
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install pytest
                pytest
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${TAG} ."
            }
        }
    }

    post {
        success { echo "✅ DEV pipeline successful" }
        failure { echo "❌ DEV pipeline failed" }
    }
}
