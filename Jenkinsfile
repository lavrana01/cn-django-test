pipeline {
    agent any
    environment {
        EC2_HOST = 'ec2-user@3.110.142.23'
        DOCKER_CONTAINER_NAME = 'cn-django-test-web-1'
        GIT_REPO = 'git@github.com:lavrana01/cn-django-test'
        SSH_KEY = credentials('ec2-user') // Add the SSH key credentials
    }
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: "${GIT_REPO}"
            }
        }
        stage('Deploy to EC2') {
            steps {
                sshagent (credentials: ['ec2-user']) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no ${EC2_HOST} << EOF
                    # Stop existing Docker container
                    docker stop ${DOCKER_CONTAINER_NAME} || true
                    docker rm ${DOCKER_CONTAINER_NAME} || true

                    # Pull the latest code and build a new Docker image
                    cd /path/to/your/project
                    git pull origin main
                    docker-compose down
                    docker-compose up -d --build
                    EOF
                    '''
                }
            }
        }
    }
}
