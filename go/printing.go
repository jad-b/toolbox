package golang

import (
	"encoding/json"
	"log"
)

// PrettyJSON pretty-prints JSON. If an error occurs, you'll get back an empty,
// but valid, JSON structure.
func PrettyJSON(v interface{}) string {
	s, err := json.MarshalIndent(v, "", "\t")
	if err != nil {
		log.Print(err)
		return "{}"
	}
	return string(s)
}
