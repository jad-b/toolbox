package golang

import (
	"fmt"
	"math"
	"math/rand"
	"net"
	"time"

	"github.com/drone/routes/exp/context"
)

// ExpBackoff repeats a command until successful, introducing a growing delay
// between attempts.
//
// The output of the command can be listened for on the first returned channel.
func ExpBackoff(fn genericFunc, ctx context.Context) <-chan interface{} {
	// Channel for sending the output of fn
	result := make(chan interface{})
	// Our default time between retries
	const base = time.Second
	// The longest we'll wait between retries
	const cap = time.Second * 30

	go func() {
		attempt := 0
		for {
			select {
			case <-ctx.Done():
				fmt.Println(ctx.Err())
			case result <- fn():
				// Use the lower of our max sleep and our current attempt's backoff
				max := math.Min(float64(cap), float64(base)*math.Exp2(float64(attempt)))
				// Add some randomness to our calls
				jittered := rand.Float64() * max
				time.Sleep(time.Duration(jittered))
				attempt++
			}
		}
	}()
	return result, done
}

// Ping tests connectivity to a URL over TCP.
func Ping(addr string, timeout time.Duration) bool {
	// Attempt to resolve the address with exponential backoff
	result, done := ExpBackoff(func() interface{} {
		return Resolve(time.Millisecond*250, "tcp", addr)
	})
	tick := time.NewTimer(timeout)
	for {
		select {
		case <-tick.C: // Ran out of time
			done <- struct{}{} // Tell ExpBackoff to stop working
			return false
		case res := <-result:
			if _, ok := res.(error); ok {
				// Unable to connect, keep trying
			} else { // Success
				done <- struct{}{} // Tell ExpBackoff to stop working
				return true
			}
		}
	}
}

// Resolve checks for connectivity. It returns on the first error.
// Useful for testing if a service is running.
//
// Usage:
//   Resolve(time.Second, "tcp", "127.0.0.1:8125" )
func Resolve(duration time.Duration, network string, addrs ...string) error {
	for _, addr := range addrs {
		conn, err := net.DialTimeout(network, addr, duration)
		if err != nil {
			return fmt.Errorf("failed to connect to %s://%s", network, addr)
		}
		conn.Close()
	}
	return nil
}
