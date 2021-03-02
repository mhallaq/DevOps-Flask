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
                                image.push("latest")
                            }
                        }
                    }
                }
            }
            stage('Deploy App'){
                steps{
                    def dockerRun='docker stack deploy --compose-file docker-compose.yaml weather-app'
                    sshagent(credentials: ['swarm-deployment'], ignoreMissing: true) {
                    sh "ss -o StrictHostKeyChecking=no malhallaq@10.138.0.2 ${dockerRun}" 
                        }
                }
            }
        }
}
