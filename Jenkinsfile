#!groovy

node {
    stage 'Checkout'
        checkout scm

    stage 'Test'
        sh './manage.py test'

}
