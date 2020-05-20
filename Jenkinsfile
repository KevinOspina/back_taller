pipeline {
    agent { 
        dockerfile true
    }
    stages {
        stage('migrations') {
            steps {
                sh 'python manage.py migrate'
            }
        }
        stage('test') {
            steps {
                sh 'ip a'
            }
        }
        stage('run') {
            steps {
                sh 'python manage.py runserver 0.0.0.0:9090'
            }
        }
    }
}