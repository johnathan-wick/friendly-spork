pipeline {
    agent any
    environment {
        IMAGE_NAME="flask-demo"
        VERSION_ID="latest"
    }
    stages {
        stage('Old') {
            
            steps {
                sh '''
                    ole_image_id=`docker images|grep ${IMAGE_NAME}|grep ${VERSION_ID}|awk '{print $3}'`
                    if [[ -n "${ole_image_id}" ]]; then
                        docker rmi -f ${ole_image_id}
                    fi
                '''
            }
        }
        stage('Test') {
            
            steps {
                echo "done"
            }
            post {
                always {
                    echo 'test-reports/results.xml'
                }
            }
        }
    }
}
