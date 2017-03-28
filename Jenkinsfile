#!groovy

node {
    stage 'Checkout'
        checkout scm

    stage 'Test'
        sh 'python3.5 manage.py test'

}
