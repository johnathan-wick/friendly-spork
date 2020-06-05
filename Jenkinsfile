pipeline {
    agent any
    environment {
        IMAGE_NAME="flask-demo"
        VERSION_ID="latest"
    }
    stages {
        stage('Build') {
            
            steps {
                sh '''
                    container_id=`docker ps|grep ${IMAGE_ADDR}:${VERSION_ID}|awk '{print $1}'`
                    if [ -n "${container_id}" ]; then
                        docker stop "${container_id}"
                        docker rm -f "${container_id}"
                    fi
                    ole_image_id=`docker images|grep ${IMAGE_NAME}|grep ${VERSION_ID}|awk '{print $3}'`
                    if [[ -n "${ole_image_id}" ]]; then
                        docker rmi -f ${ole_image_id}
                    fi
                    
                    docker build --pull --rm -t ${IMAGE_NAME}:${VERSION_ID} .
                '''
            }
        }
        stage('DeployToQA') {

            steps {
                withEnv(['JENKINS_NODE_COOKIE=dontKillMe']) {
                    sh '''
                        docker run -dt -P --name "flaskdv-dev" --entrypoint "python" "flask-demo:latest" -m flask run --no-debugger --no-reload --host 0.0.0.0 --port 5000
                    '''
                }
            }
        }
        stage('Test') {
            
            steps {
                sh '''
                
                docker container exec -i flaskdv-dev bash|py.test|exit
                exit
                '''
            }

        }
    }
}
