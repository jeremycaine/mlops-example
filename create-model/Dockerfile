FROM icr.io/codeengine/golang:alpine
COPY create-model.go /
RUN  go build -o /create-model /create-model.go

# Copy exe into a smaller image
FROM icr.io/codeengine/alpine
COPY --from=0 /create-model /create-model
CMD  /create-model