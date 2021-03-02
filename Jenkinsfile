pipeline{
        agent any
        stages{
            stage('Build Image'){
                steps{
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
                                image.push("v1")
                            }
                        }
                    }
                }
            }
            stage('Deploy App'){
                steps{
                    sshagent(credentials: ['deploy'], ignoreMissing: true) {
                            sh "ssh -o StrictHostKeyChecking=no malhallaq@10.138.0.2 docker stack deploy --compose-file docker-compose.yaml weather-app"
                        }
                }
            }
        }
}
