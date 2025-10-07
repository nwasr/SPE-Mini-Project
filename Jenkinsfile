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

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
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
                    sh '''
                        echo $PASS | docker login -u $USER --password-stdin
                        docker push $IMAGE
                    '''
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                sh '''
                    echo "Running Ansible Playbook manually..."
                    ansible-playbook -i inventory deploy.yml
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully — application deployed via Ansible.'
        }
        failure {
            echo 'Pipeline failed. Check Jenkins console for details.'
        }
    }
}
