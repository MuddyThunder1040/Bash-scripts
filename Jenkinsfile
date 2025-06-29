pipeline {
    agent any

    environment {
        IMAGE_NAME = "bash-scripts"
        TAG = "test"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "✅ Checked out from test branch"
            }
        }

        stage('Unit Tests + Coverage') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install pytest pytest-cov
                pytest --cov=.
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${TAG} ."
            }
        }

        stage('Run Container') {
            steps {
                sh "docker run --rm ${IMAGE_NAME}:${TAG}"
            }
        }
    }
}
