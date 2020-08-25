pipeline {
    agent any

    stages {
        stage('Debug Info') {
            steps {
                sh 'ls -al'
                sh 'whoami'
                sh 'docker -v'
            }
        }

        stage('Build') {
            steps {
                echo 'ToDo'
            }
        }

        stage('Test') {
            steps {
                echo 'ToDo'
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
