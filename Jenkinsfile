pipeline {
    agent any

    environment {
        IMAGE_NAME = "bash-scripts"
        TAG = "latest"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/MuddyThunder1040/Bash-scripts.git'
                echo "✅ Code checked out from main branch"
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install pytest pytest-cov
                pytest --cov=.
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                docker build -t ${IMAGE_NAME}:${TAG} .
                """
            }
        }

        stage('Run Docker Container') {
            steps {
                sh """
                docker run --rm ${IMAGE_NAME}:${TAG}
                """
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished'
        }
        success {
            echo '✅ Build, Test, and Docker Run Successful'
        }
        failure {
            echo '❌ Pipeline failed'
        }
    }
}
