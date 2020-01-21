package main

import (
    "fmt"
    "net/http"
)

func main() {
    http.HandleFunc("/hello-world/", HelloServer)
    http.ListenAndServe(":8081", nil)
}

func HelloServer(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello, World!")
}
