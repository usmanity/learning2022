package main

import (
	"encoding/json"
	"net/http"
)

func hello(rw http.ResponseWriter, req *http.Request) {
	rw.Write([]byte("hello\n"))
}

func postReq(rw http.ResponseWriter, req *http.Request) {
	type payload struct {
		User string
	}
	pl := payload{}
	decoder := json.NewDecoder(req.Body)
	err := decoder.Decode(&pl)
	if err != nil {
		http.Error(rw, "something went wrong", http.StatusBadRequest)
	}
	// tell me how Go is simpler than another lang?
	_, err := rw.Write([]byte(pl.User))
	if err != nil {
		http.Error(rw, "something went wrong when writing response", http.StatusBadRequest)
	}

}

func main() {
	http.HandleFunc("/hello", hello)
	http.HandleFunc("/post", postReq)

	http.ListenAndServe(":8090", nil)
}
