pipeline {
    agent any

    stages {
        stage('Install') {
            steps {
                sh 'python3 --version || python --version'
                sh 'python3 -m pip install -r requirements.txt || python -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m pytest || python -m pytest'
            }
        }

        stage('Check Docker') {
            steps {
                sh 'docker --version'
            }
        }
    }
}