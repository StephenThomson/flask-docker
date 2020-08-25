pipeline {
    agent any

    stages {
        stage('Debug Info') {
            steps {
                sh 'whoami'
                sh 'docker -v'
            }
        }

        stage('Build') {
            steps {
                // sh './build.sh'
                sh 'docker build -t flask-docker .'
            }
        }

        stage('Test') {
            steps {
                echo './dockertest.sh'
            }
        }

        // If the branch is master...
        stage('Deploy') {
            steps {
                echo 'ToDo: Deploy the app'
                echo 'ToDo: Post deployment alert (e.g. in Slack)'
            }
        }

        stage('Smoke Tests') {
            steps {
                echo 'ToDo: Run some smoke tests on the deployed app'
                echo 'ToDo: Post smoke test failure alert (e.g. in Slack)'
            }
        }

        stage('Rollback on Smoke Test Failure') {
            steps {
                echo 'ToDo: Run some smoke tests on the deployed app'
                echo 'ToDo: Post rollback alert (e.g. in Slack)'
            }
        }
    }
}
