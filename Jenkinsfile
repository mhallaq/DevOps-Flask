pipeline{
        agent any
        environment {
            app_version = 'v2'
            rollback = 'false'
        }
        stages{
            stage('Build Image'){
                steps{
                    dir("${env.WORKSPACE}/front-end"){
                           sh "pwd"
                    }    
                    script{
                        if (env.rollback == 'false'){
                            image = docker.build("mhallaq/front-end")
                        }
                    }
                }
            }
            stage('Tag & Push Image'){
                steps{
                    script{
                        if (env.rollback == 'false'){
                            docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials'){
                                image.push(env.app_version)
                            }
                        }
                    }
                }
            }
            stage('Deploy App'){
                steps{
                    sshagent(credentials: ['deploy'], ignoreMissing: true) {
                            sh "ssh -o StrictHostKeyChecking=no malhallaq@10.138.0.2 docker-compose pull"
                            sh "ssh -o StrictHostKeyChecking=no malhallaq@10.138.0.2 docker stack deploy --compose-file docker-compose.yaml weather-app"
                        }
                }
            }
        }
}
