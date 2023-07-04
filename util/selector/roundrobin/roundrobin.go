// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     https://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
// Original source: github.com/micro/go-micro/v3/selector/roundrobin/roundrobin.go

package roundrobin

import (
	"math"
	"sort"

	"github.com/micro/micro/v3/util/selector"
)

// NewSelector returns an initalised round robin selector
func NewSelector(opts ...selector.Option) selector.Selector {
	return new(roundrobin)
}

type roundrobin struct {
	i int
}

func (r *roundrobin) Select(routes []string, opts ...selector.SelectOption) (selector.Next, error) {
	if len(routes) == 0 {
		return nil, selector.ErrNoneAvailable
	}

	return func() string {
		sort.Strings(routes)
		route := routes[r.i%len(routes)]
		//fmt.Printf("ggggggg %d %s %+v\n", r.i, route, routes)
		// increment
		r.i++
		if r.i >= math.MaxInt32 {
			r.i = 0
		}
		return route
	}, nil
}

func (r *roundrobin) Record(addr string, err error) error { return nil }

func (r *roundrobin) Reset() error { return nil }

func (r *roundrobin) String() string {
	return "roundrobin"
}
