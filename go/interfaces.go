package golang

import "net/http"

// RoundTripperFunc converts a function into a Transport.
type RoundTripperFunc func(*http.Request) (*http.Response, error)

// RoundTrip calls the underlying function
func (rt RoundTripperFunc) RoundTrip(req *http.Request) (*http.Response, error) {
	return rt(req)
}
