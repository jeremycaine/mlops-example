# walkthrough

## Up and Running with IBM Code Engine
Create an IBM Code Engine project

Create a Hello World python app
- code listens on port 3333, Dockerfile
- create app in CE with additional settings of Listening port 3333
- CE generates URL to serve "Hello World!"

## Load Model data into COS
bucket `caine-mnist-dataset`
give public access
`https://s3.eu-gb.cloud-object-storage.appdomain.cloud/caine-mnist-dataset/mnist_test.csv`

## Create buck for model to be written to
create service id
assign service id as Object Writer to bucket `caine-mnist-model`

## Test Load data and write out CSC
Load data from COS


