pipeline {
    agent any
    environment {
        EC2_HOST = 'ec2-user@3.110.142.23'
        DOCKER_CONTAINER_NAME = 'cn-django-test-web-1'
        GIT_REPO = 'https://github.com/lavrana01/cn-django-test'
    }
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: "${GIT_REPO}"
            }
        }
        stage('Deploy to EC2') {
            steps {
                sshagent (credentials: ['0080f981-fc6f-4af0-b7fd-a28f67c64220']) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no ${EC2_HOST} << EOF
                    # Stop existing Docker container
                    sudo docker stop ${DOCKER_CONTAINER_NAME} || true
                    sudo docker rm ${DOCKER_CONTAINER_NAME} || true

                    # Pull the latest code and build a new Docker image
                    cd /home/ec2-user/cn-django-test
                    sudo git pull origin main
                    sudo docker-compose down
                    sudo docker-compose up -d --build
                    EOF
                    '''
                }
            }
        }
    }
}
