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
                sh 'python manage.py showmigrations'
            }
        }
    }
}