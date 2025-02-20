pipeline {
    agent {
        docker {
            image 'python:3.9'
            args '-v "C:\\Users\\ychen\\Downloads\\jenkins_home\\workspace\\try_pytest":/workspace'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout your code from version control
                git 'https://github.com/ychen-r/try_pytest.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r /workspace/requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest /workspace/'
            }
        }
    }
}
