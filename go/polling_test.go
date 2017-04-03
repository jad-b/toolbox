package golang

import (
	"context"
	"time"
)

func ExampleExpBackoff() {
	ctx, cancel := context.WithTimeout(context.Background(), time.Second*5)
	results := ExpBackoff(MyFunc, ctx)
	for {
		x := <-results
		if _, ok := x.(TypeIWant); ok {
			cancel() // Stop the expBackoff function
		}
	}
}
