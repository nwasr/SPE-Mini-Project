pipeline {
    agent any
    environment {
        IMAGE = 'pep34/calculator:latest'
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/nwasr/SPE-Mini-Project.git'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest discover'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'DockerHubCred', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                    sh 'docker push $IMAGE'
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                ansiblePlaybook credentialsId: 'AnsibleLocal', playbook: 'deploy.yml', inventory: 'inventory'
            }
        }
    }
}
