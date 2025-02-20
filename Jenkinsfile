// Jenkinsfile
pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/ychen-r/try_pytest.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t pytest-image .'
                }
            }
        }
        stage('Run pytest') {
            steps {
                script {
                    docker.image('pytest-image').inside {
                        sh 'pytest'
                    }
                }
            }
        }
    }
}
