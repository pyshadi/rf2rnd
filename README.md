# RF2RND: RF Noise to Random Number Generator
Random number generators (RNGs) are software algorithms that produce sequences of random numbers. There are two types of RNGs: true random number generators (TRNGs) and pseudorandom number generators (PRNGs).
TRNGs use physical processes, such as atmospheric noise or radioactive decay, to generate truly random numbers. These processes are unpredictable, and their outputs are difficult to reproduce, making TRNGs highly secure.
PRNGs, on the other hand, use mathematical algorithms to generate random numbers. PRNGs are deterministic, meaning that they produce the same sequence of numbers each time they are started with the same seed value. However, PRNGs can produce sequences of numbers that appear to be random, and they are often used in applications where true randomness is not required but a reasonable degree of unpredictability is sufficient.

Atmospheric noise, also known as radio noise or static, is a type of electromagnetic interference that is caused by natural atmospheric phenomena, such as lightning, thunderstorms, and the sun's radiation. It is present in the radio frequency spectrum and can be received by radio receivers (RTL-SDR receiver).
To sample atmospheric noise using an RTL-SDR receiver, you would need to tune the receiver to a frequency where atmospheric noise is present, which typically falls within the frequency range of 0.5 MHz to 30 MHz. 
##### One could also terminate the antenna port to capture more thermal noise from the SDR receiver amplifiers. 

# Usage
First clone the repository to your machine by running the following command: <br>
```
git clone https://github.com/pyshadi/rf2rnd.git
```
## Collecting RF Noise

### collect_rf_data <br>
To collect RF noise data using an SDR receiver, you can use the collect_rf_data function from collector.py. Here's an example:
```
from rf2rnd.collector import collect_rf_data
# Collect RF noise data using default parameters
data = collect_rf_data()
# Collect RF noise data using custom parameters
 data = collect_rf_data(center_freq=2.4e6, sample_rate=1.2e6, gain=10, num_samples=4096)
```

## Extracting Random Bits
To extract random bits from the collected data using one of several available extractor functions, you can use the extract_random_bits function from extractor.py. The available extractor functions are:

* von_neumann_extractor: <br>
Implements the Von Neumann extractor, which generates random bits by selecting pairs of consecutive bits and outputting one of them based on the outcome of a coin flip. If the two bits are the same, they are discarded, and the process is repeated with the next pair of bits. This function returns an array of random bits.<br>
* xor_extractor: XOR-based extractor<br>
Implements an XOR-based extractor, which generates random bits by computing the XOR of consecutive bits in the sequence. This function returns an array of random bits.<br>
* majority_vote_extractor: Majority-vote extractor<br>
 Implements a majority-vote extractor, which divides the binary sequence into groups of three consecutive bits and selects the most common bit in each group. This function returns an array of random bits.<br>
* bit_shift_extractor: Bit-shift extractor<br>
Implements a bit-shift extractor, which generates random bits by computing the difference between consecutive bits in the sequence. This function returns an array of random bits.<br>

Here's an example:
```
from rf2rnd import extract_random_bits
# Extract random bits using the default Von Neumann extractor
bits = extract_random_bits(data)
# Extract random bits using a custom extractor function
bits = extract_random_bits(data, extractor_name='majority_vote_extractor')
```
## Generating Random Numbers
To generate a stream of random numbers from the extracted random bits, you can use the randint or randflo function from generator.py. The function uses a Linear Congruential Generator (LCG) to generate the numbers. Here's an example:

```
from rf2rnd.generator import randint
from rf2rnd import extract_random_bits

# Extract random bits from samples
bits = extract_random_bits(samples)

# Generate 100 random integers between 0 and 1000
numbers = randint(bits, num_numbers=100, low=0, high=1000)

# Generate 10 random integers between -10 and 10
numbers = randint(bits, num_numbers=10, low=-10, high=10)
```

```
from rf2rnd.generator import randflo
from rf2rnd import extract_random_bits

# Extract random bits from samples
bits = extract_random_bits(samples)

# Generate 100 random floats between 0 and 1
numbers = randflo(bits, num_numbers=100, low=0, high=1)

# Generate 10 random floats between -10 and 10
numbers = randflo(bits, num_numbers=10, low=-10, high=10)
```


For more information, please refer to the docstrings and the examples in the code.

### Source Files
The package includes the following files:

- collector.py: the module to collect RF noise from a hardware source.
- extractor.py: the module to extract and preprocess the collected data.
- generator.py: the module to generate a stream of random numbers.

### EXAMPLES 
The example file 'test_entropy.py' calculates entropy and compares it to numpy. It also generates a plot.

### Tests
The package includes the following statistical tests:
To run the tests use: <code>pytest -s test_monobit.py </code>

- test_monobit.py: perform a monobit test on the generated random numbers.
- test_cum_sum.py: perform a cumulative sum test on the generated random numbers.
- test_rand_excursion.py: perform a random excursion test on the generated random numbers.
- test_o.py: How to use.


### License
...
