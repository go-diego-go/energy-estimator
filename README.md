# Energy Estimator

## Assumptions

I'm making the following initial assumptions as part of the exercise:

* We're always going to get one `TurnOff` command at the beginning and one at the end of the sequence.
* Whenever we find duplicate entries (i.e. same timestamp) we will only leave the last one (sorted by insertion order)
* For all other purposes, entries will be sorted by timestamp
* I'm currently not enforcing that the dimmer value doesn't go over 1.0 (per one of the examples)
* I'm currently not doing any rounding or trimming of decimals
* EOF will be triggered by Ctrl + D or some other equivalent command.

## Command Validation

I'm assuming the following structure:  

```
<timestamp> <command>
```

where  
`timestamp` is any positive integer number  
`command` is one of:  
  - `Delta <value>`
    - `value` in turn is composed of:
      - `Sign`: either `+` or `-`
      - `Number`: an unsigned (because the sign is already included) float number
  - `TurnOff`
    - This takes no parameters and is implicitly equivalent to: `Delta 0` 

Having said all of this, any input that doesn't follow this structure will be rejected as invalid.

## Estimation Formula

I'm assuming that the formula for calculating the total energy used will be:

```
Consumption per period = <period_length> * <consumption_rate>
Total = <period1_consumption> + <period2_consumption> +... + <periodn_consumption>
```
where  
`period_length` is a float expressed in hours, calculated as:
  - `period_end_timestamp` - `period_start_timestamp`  
  
`consumption_rate` is a float expressed in watts

## Example usage

```
$ energy-estimator
> 1544206562 TurnOff
> 1544206563 Delta +0.5
> 1544210163 TurnOff
> EOF
Estimated energy used: 2.5 Wh
```
 
```
$ energy-estimator
> 1544206562 TurnOff
> 1544206563 Delta +0.5
> 1544210163 Delta -0.25
> 1544211963 Delta +0.75
> 1544211963 Delta +0.75
> 1544213763 TurnOff
> EOF
Estimated energy used: 5.625 Wh
```

## Installation

* `brew install pipenv`  (if not already installed)
* `make install`

## Execution

* `energy-estimator`

This is not a true, standalone executable (it needs to run within the context of the python env), but is simple enough for now.  
We could also use `py-installer` to package an actual independent executable file. (We'll see if we have time for that)

## Development

* Install dev dependencies with `make dev`
* Run test scripts with `make qa`
