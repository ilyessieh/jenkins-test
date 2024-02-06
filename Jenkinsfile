pipeline {
environment { // Declaration of environment variables
DOCKER_ID = "ilyessieh" // replace this with your docker-id
DOCKER_MOVIE_IMAGE = "movieservice"
DOCKER_CAST_IMAGE = "castservice"
DOCKER_NGINX_IMAGE = "nginxservice"
DOCKER_TAG = "v.${BUILD_ID}.0" // we will tag our images with the current build in order to increment the value by 1 with each new build
}
agent any // Jenkins will be able to select all available agents
stages {// CAST
        stage(' Docker Build cast'){ // docker build image stage
            steps {
                script {
                sh '''
                 cd ./cast-service
                 docker rm -f cast
                 docker build -t $DOCKER_ID/$DOCKER_CAST_IMAGE:$DOCKER_TAG .
                 cd ..
                sleep 6
                '''
                }
            }
        }    
        stage('Docker run cast'){ // run container from our builded image
                steps {
                    script {
                    sh '''
                    docker run -d -p 8002:8000 --name cast $DOCKER_ID/$DOCKER_CAST_IMAGE:$DOCKER_TAG
                    sleep 10
                    '''
                    }
                }
            }
        stage('Test Acceptance cast'){ // we launch the curl command to validate that the container responds to the request
            steps {
                    script {
                    sh '''
                    curl localhost
                    '''
                    }
            }

        }
        stage('Docker Push'){ //we pass the built image to our docker hub account
            environment
            {
                DOCKER_PASS = credentials("DOCKER_HUB_PASS") // we retrieve  docker password from secret text called docker_hub_pass saved on jenkins
            }

            steps {

                script {
                sh '''
                docker login -u $DOCKER_ID -p $DOCKER_PASS
                docker push $DOCKER_ID/$DOCKER_CAST_IMAGE:$DOCKER_TAG
                '''
                }
            }

        }
        // MOVIE
        stage(' Docker Build movie'){ // docker build image stage
            steps {
                script {
                sh '''
                 cd ./movie-service
                 docker rm -f movie
                 docker build -t $DOCKER_ID/$DOCKER_MOVIE_IMAGE:$DOCKER_TAG .
                 cd ..
                sleep 6
                '''
                }
            }
        }    
        stage('Docker run movie'){ // run container from our builded image
                steps {
                    script {
                    sh '''
                    docker run -d -p 8001:8000 --name movie $DOCKER_ID/$DOCKER_MOVIE_IMAGE:$DOCKER_TAG
                    sleep 10
                    '''
                    }
                }
            }
        stage('Test Acceptance movie'){ // we launch the curl command to validate that the container responds to the request
            steps {
                    script {
                    sh '''
                    curl localhost
                    '''
                    }
            }

        }
        stage('Docker Push movie'){ //we pass the built image to our docker hub account
            environment
            {
                DOCKER_PASS = credentials("DOCKER_HUB_PASS") // we retrieve  docker password from secret text called docker_hub_pass saved on jenkins
            }

            steps {

                script {
                sh '''
                docker login -u $DOCKER_ID -p $DOCKER_PASS
                docker push $DOCKER_ID/$DOCKER_CAST_IMAGE:$DOCKER_TAG
                '''
                }
            }

        }
        // NGINX
        stage(' Docker Build nginx'){ // docker build image stage
            steps {
                script {
                sh '''
                 cd ./nginx-service
                 docker rm -f nginx
                 docker build -t $DOCKER_ID/$DOCKER_NGINX_IMAGE:$DOCKER_TAG .
                 cd ..
                sleep 6
                '''
                }
            }
        }    
        stage('Docker run cast'){ // run container from our builded image
                steps {
                    script {
                    sh '''
                    docker run -d -p 8080:8080 --name nginx $DOCKER_ID/$DOCKER_NGINX_IMAGE:$DOCKER_TAG
                    sleep 10
                    '''
                    }
                }
            }
        stage('Test Acceptance cast'){ // we launch the curl command to validate that the container responds to the request
            steps {
                    script {
                    sh '''
                    curl localhost
                    '''
                    }
            }

        }
        stage('Docker Push'){ //we pass the built image to our docker hub account
            environment
            {
                DOCKER_PASS = credentials("DOCKER_HUB_PASS") // we retrieve  docker password from secret text called docker_hub_pass saved on jenkins
            }

            steps {

                script {
                sh '''
                docker login -u $DOCKER_ID -p $DOCKER_PASS
                docker push $DOCKER_ID/$DOCKER_CAST_IMAGE:$DOCKER_TAG
                '''
                }
            }

        }
        

// deploiement CAST-DB
stage('Deploiement en dev '){
        environment
        {
        KUBECONFIG = credentials("config") // we retrieve  kubeconfig from secret file called config saved on jenkins
        }
            steps {
                script {
                sh '''
                rm -Rf .kube
                mkdir .kube
                ls
                cat $KUBECONFIG > .kube/config
                cp cast-db/values.yaml values.yml
                helm upgrade --install cast-db cast-db --values=values.yml --namespace dev
                '''
                }
            }

        }
stage('Deploiement en qa '){
        environment
        {
        KUBECONFIG = credentials("config") // we retrieve  kubeconfig from secret file called config saved on jenkins
        }
            steps {
                script {
                sh '''
                rm -Rf .kube
                mkdir .kube
                ls
                cat $KUBECONFIG > .kube/config
                cp cast-db/values.yaml values.yml
                helm upgrade --install cast-db cast-db --values=values.yml --namespace qa
                '''
                }
            }

        }
stage('Deploiement en staging'){
        environment
        {
        KUBECONFIG = credentials("config") // we retrieve  kubeconfig from secret file called config saved on jenkins
        }
            steps {
                script {
                sh '''
                rm -Rf .kube
                mkdir .kube
                ls
                cat $KUBECONFIG > .kube/config
                cp cast-db/values.yaml values.yml
                helm upgrade --install cast-db cast-db --values=values.yml --namespace staging
                '''
                }
            }

        }
  stage('Deploiement en prod'){
        environment
        {
        KUBECONFIG = credentials("config") // we retrieve  kubeconfig from secret file called config saved on jenkins
        }
            steps {
            // Create an Approval Button with a timeout of 15minutes.
            // this require a manuel validation in order to deploy on production environment
                    timeout(time: 15, unit: "MINUTES") {
                        input message: 'Do you want to deploy in production ?', ok: 'Yes'
                    }

                script {
                sh '''
                rm -Rf .kube
                mkdir .kube
                ls
                cat $KUBECONFIG > .kube/config
                cp cast-db/values.yaml values.yml
                helm upgrade --install cast-db cast-db --values=values.yml --namespace prod
                '''
                }
            }

        }
// deploiement MOVIE-DB
stage('Deploiement en dev '){
        environment
        {
        KUBECONFIG = credentials("config") // we retrieve  kubeconfig from secret file called config saved on jenkins
        }
            steps {
                script {
                sh '''
                rm -Rf .kube
                mkdir .kube
                ls
                cat $KUBECONFIG > .kube/config
                cp movie-db/values.yaml values.yml
                helm upgrade --install movie-db movie-db --values=values.yml --namespace dev
                '''
                }
            }

        }
stage('Deploiement en qa '){
        environment
        {
        KUBECONFIG = credentials("config") // we retrieve  kubeconfig from secret file called config saved on jenkins
        }
            steps {
                script {
                sh '''
                rm -Rf .kube
                mkdir .kube
                ls
                cat $KUBECONFIG > .kube/config
                cp movie-db/values.yaml values.yml
                helm upgrade --install movie-db movie-db --values=values.yml --namespace qa
                '''
                }
            }

        }
stage('Deploiement en staging'){
        environment
        {
        KUBECONFIG = credentials("config") // we retrieve  kubeconfig from secret file called config saved on jenkins
        }
            steps {
                script {
                sh '''
                rm -Rf .kube
                mkdir .kube
                ls
                cat $KUBECONFIG > .kube/config
                cp movie-db/values.yaml values.yml
                helm upgrade --install movie-db movie-db --values=values.yml --namespace staging
                '''
                }
            }

        }
  stage('Deploiement en prod'){
        environment
        {
        KUBECONFIG = credentials("config") // we retrieve  kubeconfig from secret file called config saved on jenkins
        }
            steps {
            // Create an Approval Button with a timeout of 15minutes.
            // this require a manuel validation in order to deploy on production environment
                    timeout(time: 15, unit: "MINUTES") {
                        input message: 'Do you want to deploy in production ?', ok: 'Yes'
                    }

                script {
                sh '''
                rm -Rf .kube
                mkdir .kube
                ls
                cat $KUBECONFIG > .kube/config
                cp movie-db/values.yaml values.yml
                helm upgrade --install movie-db movie-db --values=values.yml --namespace prod
                '''
                }
            }

        }
//deploiement CAST-SERVICE
stage('Deploiement en dev'){
        environment
        {
        KUBECONFIG = credentials("config") // we retrieve  kubeconfig from secret file called config saved on jenkins
        }
            steps {
                script {
                sh '''
                rm -Rf .kube
                mkdir .kube
                ls
                cat $KUBECONFIG > .kube/config
                cp fastapi-cast/values.yaml values.yml
                cat values.yml
                sed -i "s+tag.*+tag: ${DOCKER_TAG}+g" values.yml
                helm upgrade --install fastapi-cast fastapi-cast --values=values.yml --namespace dev
                '''
                }
            }

        }
stage('Deploiement en qa'){
        environment
        {
        KUBECONFIG = credentials("config") // we retrieve  kubeconfig from secret file called config saved on jenkins
        }
            steps {
                script {
                sh '''
                rm -Rf .kube
                mkdir .kube
                ls
                cat $KUBECONFIG > .kube/config
                cp fastapi-cast/values.yaml values.yml
                cat values.yml
                sed -i "s+tag.*+tag: ${DOCKER_TAG}+g" values.yml
                helm upgrade --install fastapi-cast fastapi-cast --values=values.yml --namespace qa
                '''
                }
            }

        }
stage('Deploiement en staging'){
        environment
        {
        KUBECONFIG = credentials("config") // we retrieve  kubeconfig from secret file called config saved on jenkins
        }
            steps {
                script {
                sh '''
                rm -Rf .kube
                mkdir .kube
                ls
                cat $KUBECONFIG > .kube/config
                cp fastapi-cast/values.yaml values.yml
                cat values.yml
                sed -i "s+tag.*+tag: ${DOCKER_TAG}+g" values.yml
                helm upgrade --install fastapi-cast fastapi-cast --values=values.yml --namespace staging
                '''
                }
            }

        }
  stage('Deploiement en prod'){
        environment
        {
        KUBECONFIG = credentials("config") // we retrieve  kubeconfig from secret file called config saved on jenkins
        }
            steps {
            // Create an Approval Button with a timeout of 15minutes.
            // this require a manuel validation in order to deploy on production environment
                    timeout(time: 15, unit: "MINUTES") {
                        input message: 'Do you want to deploy in production ?', ok: 'Yes'
                    }

                script {
                sh '''
                rm -Rf .kube
                mkdir .kube
                ls
                cat $KUBECONFIG > .kube/config
                cp fastapi-cast/values.yaml values.yml
                cat values.yml
                sed -i "s+tag.*+tag: ${DOCKER_TAG}+g" values.yml
                helm upgrade --install fastapi-cast fastapi-cast --values=values.yml --namespace prod
                '''
                }
            }

        }

//deploiement MOVIE-SERVICE
stage('Deploiement en dev'){
        environment
        {
        KUBECONFIG = credentials("config") // we retrieve  kubeconfig from secret file called config saved on jenkins
        }
            steps {
                script {
                sh '''
                rm -Rf .kube
                mkdir .kube
                ls
                cat $KUBECONFIG > .kube/config
                cp fastapi-movie/values.yaml values.yml
                cat values.yml
                sed -i "s+tag.*+tag: ${DOCKER_TAG}+g" values.yml
                helm upgrade --install fastapi-movie fastapi-movie --values=values.yml --namespace dev
                '''
                }
            }

        }
stage('Deploiement en qa'){
        environment
        {
        KUBECONFIG = credentials("config") // we retrieve  kubeconfig from secret file called config saved on jenkins
        }
            steps {
                script {
                sh '''
                rm -Rf .kube
                mkdir .kube
                ls
                cat $KUBECONFIG > .kube/config
                cp fastapi-movie/values.yaml values.yml
                cat values.yml
                sed -i "s+tag.*+tag: ${DOCKER_TAG}+g" values.yml
                helm upgrade --install fastapi-movie fastapi-movie --values=values.yml --namespace qa
                '''
                }
            }

        }
stage('Deploiement en staging'){
        environment
        {
        KUBECONFIG = credentials("config") // we retrieve  kubeconfig from secret file called config saved on jenkins
        }
            steps {
                script {
                sh '''
                rm -Rf .kube
                mkdir .kube
                ls
                cat $KUBECONFIG > .kube/config
                cp fastapi-movie/values.yaml values.yml
                cat values.yml
                sed -i "s+tag.*+tag: ${DOCKER_TAG}+g" values.yml
                helm upgrade --install fastapi-movie fastapi-movie --values=values.yml --namespace staging
                '''
                }
            }

        }
  stage('Deploiement en prod'){
        environment
        {
        KUBECONFIG = credentials("config") // we retrieve  kubeconfig from secret file called config saved on jenkins
        }
            steps {
            // Create an Approval Button with a timeout of 15minutes.
            // this require a manuel validation in order to deploy on production environment
                    timeout(time: 15, unit: "MINUTES") {
                        input message: 'Do you want to deploy in production ?', ok: 'Yes'
                    }

                script {
                sh '''
                rm -Rf .kube
                mkdir .kube
                ls
                cat $KUBECONFIG > .kube/config
                cp fastapi-movie/values.yaml values.yml
                cat values.yml
                sed -i "s+tag.*+tag: ${DOCKER_TAG}+g" values.yml
                helm upgrade --install fastapi-movie fastapi-movie --values=values.yml --namespace prod
                '''
                }
            }

        }

//deploiement NGINX
stage('Deploiement en dev'){
        environment
        {
        KUBECONFIG = credentials("config") // we retrieve  kubeconfig from secret file called config saved on jenkins
        }
            steps {
                script {
                sh '''
                rm -Rf .kube
                mkdir .kube
                ls
                cat $KUBECONFIG > .kube/config
                cp fastapi-nginx/values.yaml values.yml
                cat values.yml
                sed -i "s+tag.*+tag: ${DOCKER_TAG}+g" values.yml
                helm upgrade --install fastapi-nginx fastapi-nginx --values=values.yml --namespace dev
                '''
                }
            }

        }
stage('Deploiement en qa'){
        environment
        {
        KUBECONFIG = credentials("config") // we retrieve  kubeconfig from secret file called config saved on jenkins
        }
            steps {
                script {
                sh '''
                rm -Rf .kube
                mkdir .kube
                ls
                cat $KUBECONFIG > .kube/config
                cp fastapi-nginx/values.yaml values.yml
                cat values.yml
                sed -i "s+tag.*+tag: ${DOCKER_TAG}+g" values.yml
                helm upgrade --install fastapi-nginx fastapi-nginx --values=values.yml --namespace qa
                '''
                }
            }

        }
stage('Deploiement en staging'){
        environment
        {
        KUBECONFIG = credentials("config") // we retrieve  kubeconfig from secret file called config saved on jenkins
        }
            steps {
                script {
                sh '''
                rm -Rf .kube
                mkdir .kube
                ls
                cat $KUBECONFIG > .kube/config
                cp fastapi-nginx/values.yaml values.yml
                cat values.yml
                sed -i "s+tag.*+tag: ${DOCKER_TAG}+g" values.yml
                helm upgrade --install fastapi-nginx fastapi-nginx --values=values.yml --namespace staging
                '''
                }
            }

        }
  stage('Deploiement en prod'){
        environment
        {
        KUBECONFIG = credentials("config") // we retrieve  kubeconfig from secret file called config saved on jenkins
        }
            steps {
            // Create an Approval Button with a timeout of 15minutes.
            // this require a manuel validation in order to deploy on production environment
                    timeout(time: 15, unit: "MINUTES") {
                        input message: 'Do you want to deploy in production ?', ok: 'Yes'
                    }

                script {
                sh '''
                rm -Rf .kube
                mkdir .kube
                ls
                cat $KUBECONFIG > .kube/config
                cp fastapi-nginx/values.yaml values.yml
                cat values.yml
                sed -i "s+tag.*+tag: ${DOCKER_TAG}+g" values.yml
                helm upgrade --install fastapi-nginx fastapi-nginx --values=values.yml --namespace prod
                '''
                }
            }

        }

}
}