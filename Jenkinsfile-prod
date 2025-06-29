pipeline {
    agent any

    environment {
        IMAGE_NAME = "bash-scripts"
        TAG = "prod"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "✅ Checked out from prod branch"
            }
        }

        stage('Approval') {
            steps {
                input message: 'Approve Deployment to PROD?', ok: 'Deploy'
            }
        }

        stage('Docker Build') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${TAG} ."
            }
        }

        stage('Deploy') {
            steps {
                sh "docker run -d -p 5000:5000 ${IMAGE_NAME}:${TAG}"
            }
        }
    }
}
